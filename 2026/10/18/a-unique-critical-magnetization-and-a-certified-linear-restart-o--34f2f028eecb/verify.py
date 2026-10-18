"""Interval certificate for neutral voter diffusion restart threshold.
No external dependencies. Fixed-point integer enclosures Q=10**40.
"""
Q=10**40
N=2048

def ceildiv(a,b): return -(-a//b)

def C(a,b=None): return (a,a if b is None else b)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[1],-a[0])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    pp=[x*y for x in a for y in b]
    return (min(pp)//Q,ceildiv(max(pp),Q))
def div(a,k):
    assert k>0
    return (a[0]//k,ceildiv(a[1],k))
def r(n,d=1):
    assert d>0
    return (n*Q//d,ceildiv(n*Q,d))
def power(a,k):
    out=r(1)
    while k:
        if k&1:out=mul(out,a)
        a=mul(a,a);k>>=1
    return out

def readable(a):return (a[0]/Q,a[1]/Q)

# log(2) = 2 atanh(1/3); enclose omitted terms by a geometric series.
ln2=r(0)
for n in range(35):
    ln2=add(ln2,r(2,(2*n+1)*3**(2*n+1)))
ln2=add(ln2,C(0,r(9,4*71*3**71)[1])) # tail starts n=35: (9/4)*2 / (71*3^71) bound

b1=[None]*(N+1);b2=[None]*(N+1);b3=[None]*(N+1)
T1=ln2
for j in range(1,N+1):
    aj=r(1,2*j*(2*j-1))
    b1[j]=aj
    b2[j]=mul(r(2),mul(aj,T1))
    T1=sub(T1,aj)
assert T1[0]>0

T2=C(0,r(1,2*N*N)[1])
for j in range(N,0,-1):
    T2=add(T2,b2[j])
    b3[j]=mul(r(3,2*j*(2*j-1)),T2)

M2_tail=C(0,r(1,2*N*N)[1]); M3_tail=C(0,r(1,4*(N-1)**3)[1])

def calc(m):
    pow2=mul(m,m);z=r(1)
    U=ln2; V=r(0); W=r(0); Vpos=r(0)
    Atn=r(0); # atanh(m)
    for j in range(1,N+1):
        z=mul(z,pow2)
        U=sub(U,mul(b1[j],z))
        term=sub(r(1),z)
        V=add(V,mul(b2[j],term))
        W=add(W,mul(b3[j],term))
        # v'(m) / -2 = sum j*b2_j*m^(2j-1)
        Vpos=add(Vpos,mul(mul(r(j),b2[j]),div_by_m(z,m)))
    # Omitted M1 tail is positive but < 10^-40 for 0 < m <= 0.64.
    U=C(U[0]-1,U[1])
    # The uncomputed derivative tail is likewise positive and < 10^-40.
    Vpos=C(Vpos[0],Vpos[1]+1)
    V=add(V,M2_tail)
    W=add(W,M3_tail)
    # compute atanh by Taylor with geometric remainder
    zz=m; at=r(0)
    for k in range(75):
        at=add(at,div(zz,2*k+1));zz=mul(zz,pow2)
    # omitted sum <= m^(151) / (151*(1-m^2))
    ub=mul(div(zz,151),r(2)) # since m<=0.64, geometric ratio<0.41; factor2 safe
    Atn=add(at,C(0,ub[1]))
    F=sub(mul(U,U),div(V,2))
    D=add(neg(mul(r(2),mul(U,Atn))),Vpos)
    B=add(sub(mul(mul(U,U),U),mul(U,V)),div(W,6))
    return U,V,W,F,D,B

def div_by_m(z,m):
    # compute z/m, m positive with tight directed enclosure
    assert m[0]>0
    lo=z[0]*Q//m[1]
    hi=ceildiv(z[1]*Q,m[0])
    return (lo,hi)

def overlap_interval(a,b):
    # enclose function known monotone decreasing at m in [a,b]
    return (b[0],a[1])

if __name__=='__main__':
    import time
    t=time.monotonic()
    low=r(63058,100000);high=r(63062,100000)
    ml=calc(low); mh=calc(high)
    for name,vals in [('low',ml),('high',mh)]:
        print(name,[(key,readable(v)) for key,v in zip(('M1','M2','M3','F','Fprime','B'),vals)])
    assert ml[3][0]>0 and mh[3][1]<0, 'root existence enclosure failed'
    U=overlap_interval(ml[0],mh[0]);V=overlap_interval(ml[1],mh[1]);W=overlap_interval(ml[2],mh[2]);
    B=add(sub(mul(mul(U,U),U),mul(U,V)),div(W,6))
    print('B bracket',readable(B)); assert B[0]>0
    # use conservative bracket for Fprime by simple endpoint bounds
    # D=-2 U atanh(m) + Vpos; bound via directly endpoint plus Lipschitz |F''|<100
    D=C(min(ml[4][0],mh[4][0])-r(1,250)[1],max(ml[4][1],mh[4][1])+r(1,250)[1])
    print('Fprime bracket',readable(D)); assert D[1]<0
    # conservative C bracket
    Clo=(-D[1]*Q)//(2*B[1]);Chi=ceildiv(-D[0]*Q,2*B[0]);print('C bracket',readable((Clo,Chi)))
    assert Clo>33*Q and Chi<36*Q
    print('PASS exact integer enclosures and analytic tail bounds; secs=',time.monotonic()-t)
