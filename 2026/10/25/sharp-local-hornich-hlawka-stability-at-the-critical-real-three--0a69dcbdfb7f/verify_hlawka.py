"""Self-contained exact finite matrix certificate and independent finite-difference checks.
Scientific status: the exact characteristic polynomial supports, but does not replace,
the analytic Taylor and implicit-function arguments in the accompanying theorem.
"""
from fractions import Fraction as Q
from math import log, sqrt
from random import Random

n = 9
one = Q(1)
u = [1,1,1]
vs = [[-1,1,1],[1,-1,1],[1,1,-1]]
def projection(a):
    return [[Q(int(i==j))-Q(a[i]*a[j],3) for j in range(3)] for i in range(3)]
pu = projection(u)
pv = [projection(v) for v in vs]
M = [[pu[a%3][b%3]+(pv[a//3][a%3][b%3] if a//3==b//3 else Q(0)) for b in range(n)] for a in range(n)]

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def charpoly_coefficients(A):
    # Fraction-arithmetic Faddeev--LeVerrier characteristic polynomial.
    B = [[Q(int(i==j)) for j in range(n)] for i in range(n)]
    coefficients = [one]
    for k in range(1,n+1):
        C = mul(A,B)
        c = -sum(C[i][i] for i in range(n))/k
        coefficients.append(c)
        B = [[C[i][j]+c*Q(int(i==j)) for j in range(n)] for i in range(n)]
    assert all(B[i][j]==0 for i in range(n) for j in range(n))
    return coefficients

def poly_mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

# Ascending powers for the known factorization.
target=[Q(1)]
for factor in ([Q(0),one],[-one,one],[-one,one],[-one,one],[-one,one],
               [Q(4,3),Q(-4),one],[Q(4,3),Q(-4),one]):
    target=poly_mul(target,factor)
assert list(reversed(charpoly_coefficients(M))) == target
X0=sum(vs,[])
assert all(sum(M[i][j]*Q(X0[j]) for j in range(n))==0 for i in range(n))
assert sum(M[i][i] for i in range(n))==12

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def matvec(x):return [sum(float(M[i][j])*x[j] for j in range(n)) for i in range(n)]
r6=sqrt(6)/3
h=[r6,-r6,-1-r6,r6,-r6,1+r6,-1,1,0]
lam=2-2*r6
assert max(abs(v-lam*a) for v,a in zip(matvec(h),h))<1e-12
assert abs(dot(h,X0))<1e-12

def lp(v,p):return sum(abs(t)**p for t in v)**(1/p)
def F(X,p):
    a,b,c=[X[3*i:3*(i+1)] for i in range(3)]
    add=lambda v,w:[x+y for x,y in zip(v,w)]
    return (lp(a,p)+lp(b,p)+lp(c,p)+lp(add(add(a,b),c),p)
            -lp(add(a,b),p)-lp(add(a,c),p)-lp(add(b,c),p))

p=log(3)/log(1.5)
sharp=(p-1)*lam/4
assert abs(F(X0,p))<1e-12
for t in [0.02,0.01,0.005,0.002,0.001]:
    Y=[x+t*hi for x,hi in zip(X0,h)]
    ratio=F(Y,p)/(t*t*dot(h,h))
    assert abs(ratio-sharp)<0.2*t**0.5, (ratio,sharp)

rng=Random(20261016)
checks=0
for _ in range(1200):
    a=[rng.uniform(-1,1) for _ in range(n)]
    av=dot(a,X0)/dot(X0,X0)
    w=[ai-av*xi for ai,xi in zip(a,X0)]
    if dot(w,w)<1e-10:continue
    rq=dot(w,matvec(w))/dot(w,w)
    assert rq >=lam-1e-10, rq
    t=0.002
    Y=[xi+t*wi for xi,wi in zip(X0,w)]
    observed=F(Y,p)/(t*t*dot(w,w))
    assert observed>0, observed
    checks+=1

# Check the one-sided critical scaling at the symmetric ray, including its sign.
cross=6*log(3)/(p*p)
for delta in (0.005,0.002,0.001):
    val=F(X0,p-delta)
    assert val>0 and abs(val/delta-cross)<0.1

print('PASS: exact degree-9 characteristic polynomial; null ray; two sharp soft modes;')
print('      five independent soft-mode limits; %d generic transverse tests;' % checks)
print('      one-sided parameter sign and first derivative.')
print('p0=%.12f, least spectral eigenvalue=%.12f, sharp coefficient=%.12f' % (p,lam,sharp))
