from fractions import Fraction
from itertools import permutations

# Elements a+b*zeta in Z[zeta], zeta^2-zeta+1=0.
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c+b*d)
def conj(x):
    a,b=x
    return (a+b,-b)              # conjugate(zeta)=1-zeta
def scale(n,x): return (n*x[0],n*x[1])
def real(x): return Fraction(2*x[0]+x[1],2)
def imag_zero(x): return x[1]==0 # Im(a+b*zeta)=b*sqrt(3)/2
def norm2(x):
    a,b=x
    return a*a+a*b+b*b

zp=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
expn=[0,0,1,3,0,4] # (1,1,zeta,-1,1,-zeta)

H=[[Fraction(0) for _ in range(6)] for _ in range(6)]
G=[(0,0) for _ in range(6)]
ener=0
for k in range(1,6):
    terms=[]
    for j in range(6-k):
        u=zp[(expn[j+k]-expn[j])%6]
        d=[0]*6; d[j+k]=1; d[j]=-1
        terms.append((u,d))
    C=(0,0)
    A=[(0,0) for _ in range(6)]
    B=[[(0,0) for _ in range(6)] for _ in range(6)]
    for u,d in terms:
        C=add(C,u)
        for r in range(6):
            if d[r]: A[r]=add(A[r],scale(d[r],u))
            for s in range(6):
                if d[r] and d[s]: B[r][s]=add(B[r][s],scale(d[r]*d[s],u))
    assert norm2(C)==1
    ener += norm2(C)
    Cb=conj(C)
    for r in range(6):
        # Sum the lag-gradient factors; the total gradient is -2 Im(sum_k A_{k,r} conjugate(C_k)).
        G[r]=add(G[r],mul(A[r],Cb))
        for s in range(6):
            q=add(neg(mul(Cb,B[r][s])), mul(A[r],conj(A[s])))
            H[r][s] += 2*real(q)

assert ener==5 and all(imag_zero(x) for x in G)
expected=[
[4,-6,-1,2,3,-2],
[-6,10,0,-3,-4,3],
[-1,0,4,-2,-3,2],
[2,-3,-2,4,0,-1],
[3,-4,-3,0,10,-6],
[-2,3,2,-1,-6,4],
]
assert H==[[Fraction(x) for x in row] for row in expected]

ones=[1]*6
linear=list(range(6))
for v in (ones,linear):
    assert [sum(expected[i][j]*v[j] for j in range(6)) for i in range(6)]==[0]*6

# Polynomial utilities, low coefficient first.
def padd(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i in range(n): out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def pscale(c,a): return [c*x for x in a]
def parity(p):
    inv=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            inv += p[i]>p[j]
    return -1 if inv%2 else 1

# det(lambda I-H) by exact permutation expansion.
poly=[0]
for p in permutations(range(6)):
    term=[1]
    for i,j in enumerate(p):
        entry=[-expected[i][j], 1] if i==j else [-expected[i][j]]
        term=pmul(term,entry)
    poly=padd(poly,pscale(parity(p),term))

target=[1]
for root in [0,0,1,5,9,21]: target=pmul(target,[-root,1])
assert poly==target
assert poly==[0,0,945,-1284,374,-36,1]
print('VERIFY_OK base_energy=5 charpoly=lambda^2(lambda-1)(lambda-5)(lambda-9)(lambda-21) transverse=1,5,9,21')
