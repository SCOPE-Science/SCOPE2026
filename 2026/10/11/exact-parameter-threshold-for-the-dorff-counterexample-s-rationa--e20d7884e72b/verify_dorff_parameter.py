from fractions import Fraction as Q
from math import comb

# Polynomials are coefficient lists in ascending powers.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def padd(p,q):
    n=max(len(p),len(q)); r=[Q(0)]*n
    for i in range(n): r[i]=(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
    return trim(r)
def pneg(p): return [-c for c in p]
def psub(p,q): return padd(p,pneg(q))
def pmul(p,q):
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return trim(r)
def pscale(p,c): return trim([c*x for x in p])
def ppow(p,n):
    r=[Q(1)]
    for _ in range(n): r=pmul(r,p)
    return r
def peval(p,x): return sum(c*x**i for i,c in enumerate(p))
def deriv(p): return trim([Q(i)*p[i] for i in range(1,len(p))] or [Q(0)])

def compose_affine(p,lo,hi):
    h=hi-lo; out=[Q(0)]
    for i,ci in enumerate(p):
        term=[Q(0)]*(i+1)
        for j in range(i+1): term[j]=ci*Q(comb(i,j))*lo**(i-j)*h**j
        out=padd(out,term)
    return trim(out)
def bernstein(p,lo,hi):
    a=compose_affine(p,lo,hi); n=len(a)-1
    return [sum(a[j]*Q(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
def all_pos(xs): return all(x>0 for x in xs)
def all_neg(xs): return all(x<0 for x in xs)

# Rational functions as (numerator polynomial, denominator polynomial).
def R(n,d=[Q(1)]): return (trim(n),trim(d))
def radd(u,v): return R(padd(pmul(u[0],v[1]),pmul(v[0],u[1])),pmul(u[1],v[1]))
def rneg(u): return R(pneg(u[0]),u[1])
def rsub(u,v): return radd(u,rneg(v))
def rmul(u,v): return R(pmul(u[0],v[0]),pmul(u[1],v[1]))
def rscale(u,c): return R(pscale(u[0],c),u[1])
def rdiv(u,v): return R(pmul(u[0],v[1]),pmul(u[1],v[0]))
def rpow(u,n):
    out=R([Q(1)])
    for _ in range(n): out=rmul(out,u)
    return out

def S(r,x):
    one=R([Q(1)])
    rx=rscale(r,x)
    return rdiv(rscale(rsub(R([Q(2)]),rx),x),rpow(rsub(one,rx),2))

# Fixed source parameter and witness.
a=Q(-10,11); x=Q(-99,100); b=R([Q(0),Q(1)])
den10=[Q(11),Q(10)]
c1=R([Q(21),Q(-110),Q(-121)],pscale(den10,Q(11)))
c2=R([Q(-210),Q(-231)],pscale(den10,Q(121)))
cm1=R([Q(0),Q(10),Q(11),Q(-10),Q(-11)],den10)
delta=rsub(rpow(c1,2),rpow(cm1,2))
A=rdiv(rmul(c1,c2),delta)
B=rdiv(rscale(rmul(rpow(cm1,2),b),Q(-1)),delta)
C=rdiv(rmul(rmul(c1,cm1),b),delta)
D=rdiv(rscale(rmul(cm1,c2),Q(-1)),delta)
Sa2=S(R([a*a]),x); Sab=S(rscale(b,a),x); Sb2=S(rpow(b,2),x)
pprime=radd(R([Q(1)]),radd(rmul(rpow(A,2),Sa2),radd(rscale(rmul(rmul(A,B),Sab),Q(2)),rmul(rpow(B,2),Sb2))))
qprime=radd(rmul(rpow(D,2),Sa2),radd(rscale(rmul(rmul(D,C),Sab),Q(2)),rmul(rpow(C,2),Sb2)))
J=rsub(rpow(pprime,2),rpow(qprime,2))

K=[-441000000,17509800000,17157210000,34669404000,-123932051900,-333078645020,-174164414761,1751200000,963160000]
H=[-19448100000000,1010930760000000,-6420414924000000,17388937112400000,-32519528199900000,-207727750712076000,-106176808553072400,429279211367288760,-338035249181596081,-2248981109067364100,-20746361469003038,3981191613894394680,1786614907376070838,-1953607940142274680,-1432813729830625538,-231322373255930660,26384856553020119,200452967192016000,111370457788920000]
E1=[-21,0,0,110,121]
E2=[21,-220,-242,110,121]
D1=[-10,9]; D2=[100,0,99]
claimed_num=pscale(pmul(K,H),Q(-14641))
claimed_den=pscale(pmul(pmul(ppow(D1,2),ppow(D2,4)),pmul(ppow(E1,3),ppow(E2,3))),Q(1600000000))
# Exact equality without relying on cancellation/factorization routines.
assert trim(pmul(J[0],claimed_den)) == trim(pmul(claimed_num,J[1]))

lo,hi=Q(0),Q(1,43)
assert all_neg(bernstein(K,lo,hi))
assert all_pos(bernstein(deriv(H),lo,hi))
assert peval(H,lo)<0 and peval(H,hi)>0
assert all_neg(bernstein(E1,lo,hi))
assert all_pos(bernstein(E2,lo,hi))
assert all_neg(bernstein(D1,lo,hi))
assert all_pos(bernstein(D2,lo,hi))
bl=Q(2218460173517970,10**17); bu=Q(2218460173517971,10**17)
assert lo < bl < bu < hi and peval(H,bl)<0<peval(H,bu)
print('PASS exact rational reconstruction, factorization, and Bernstein/sign certificate')
print('beta bracket:', float(bl), float(bu))
