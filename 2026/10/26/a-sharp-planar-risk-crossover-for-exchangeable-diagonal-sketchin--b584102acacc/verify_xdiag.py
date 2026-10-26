"""Exact-arithmetic checks for a two-probe exchangeable diagonal estimator.

Usage: python3 verify_xdiag.py (standard library only).
All assertions are finite replay checks; the universal proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def eq(x,y):
    global checks
    assert x == y, (x,y)
    checks += 1

def dot(u,v):
    return sum(x*y for x,y in zip(u,v))

def norm2(x):
    return dot(x,x)

def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def projection_from_image(A,w):
    v=matvec(A,w); d=dot(v,v)
    assert d>0
    return [[v[i]*v[j]/d for j in range(len(w))] for i in range(len(w))]

def xdiag_one(A,w_i,w_j):
    P=projection_from_image(A,w_j)
    n=len(w_i)
    PA=[[sum(P[i][k]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    resid=matvec([[A[i][j]-PA[i][j] for j in range(n)] for i in range(n)], w_i)
    return [PA[i][i]+w_i[i]*resid[i] for i in range(n)]

def xdiag(A,w1,w2):
    q1=xdiag_one(A,w1,w2); q2=xdiag_one(A,w2,w1)
    return [(x+y)/2 for x,y in zip(q1,q2)]

def xdiag_risk_enum(A):
    n=len(A); S=list(product((F(-1),F(1)),repeat=n))
    total=F(0)
    for w1 in S:
        for w2 in S:
            d=xdiag(A,w1,w2)
            total += sum((d[i]-A[i][i])**2 for i in range(n))
    return total/F(len(S)**2)

def closed_risk(a,b,c):
    q=a*b; P=a*a+b*b; u=c*c
    denominator=P*P-8*q*u+4*u*u
    assert denominator>0
    return (q-u)**2*(P+u)/denominator

def h(sigma,u):
    return 2*sigma-(sigma*sigma+4*sigma-2)*u+(2*sigma+4)*u*u-2*u*u*u

for a in (F(1),F(2),F(4),F(9)):
    for b in (F(1),F(3),F(5)):
        for frac in (F(0),F(1,5),F(1,2),F(4,5),F(-1,2)):
            # Choose c rational while ensuring the symmetric matrix is positive definite.
            c=frac*min(a,b)
            assert a*b>c*c
            A=[[a,c],[c,b]]
            r=xdiag_risk_enum(A)
            R=closed_risk(a,b,c)
            eq(r,R)
            q=a*b; P=a*a+b*b; u=c*c; sigma=P/q
            diff=R-u/2
            eq(diff, q**3*h(sigma,u/q)/(2*(P*P-8*q*u+4*u*u)))
            # Four independent BKS Rademacher probes, each with the same sign product.
            gh_risk=sum(2*(c*sum(signs)/4)**2 for signs in product((F(-1),F(1)),repeat=4))/16
            eq(gh_risk,u/2)

# Exact reversed risks, including diagonal and nearly rank-one examples.
for a,b,c,expected in (
        (F(1),F(4),F(0),1),
        (F(1),F(4),F(1),1),
        (F(1),F(4),F(3,2),-1),
        (F(1),F(4),F(199,100),-1),
        (F(1),F(1),F(1,2),1),
        (F(1),F(1),F(-9,10),1)):
    X=closed_risk(a,b,c)
    B=c*c/2
    eq((X>B)-(X<B),expected)

# Algebraic derivative sign: for sigma>=2, H'_sigma increases on [0,1];
# H'_sigma(1)=4-sigma^2 and H''_sigma(u)=4sigma+8-12u>0.
for sigma in (F(2),F(13,6),F(17,4),F(10),F(100)):
    for j in range(101):
        u=F(j,100)
        d=-(sigma*sigma+4*sigma-2)+(4*sigma+8)*u-6*u*u
        dd=4*sigma+8-12*u
        assert dd>0
        checks += 1
        eq(d <=0,True)
    eq(h(sigma,F(0)),2*sigma)
    eq(h(sigma,F(1)),4-sigma*sigma)

# Dimension-lifting witness: positive-definite 5x5 diagonal A, equal probes.
# The baseline is exact, while the leave-one-out estimator is not.
A=[[F(1) if i==j else F(0) for j in range(5)] for i in range(5)]
w=[F(1)]*5
est=xdiag(A,w,w)
eq(est,[F(1,5)]*5)
assert norm2([est[i]-1 for i in range(5)])>0
checks += 1

print(f'PASS: {checks} exact-rational assertion families; all pairwise sign cases included')
