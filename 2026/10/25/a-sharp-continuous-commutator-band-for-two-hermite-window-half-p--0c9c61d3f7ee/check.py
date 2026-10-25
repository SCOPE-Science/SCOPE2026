"""Reproducibility checks for a two-window Hermite half-space concentration theorem.

Only the Python standard library is needed. Finite checks support, but do not replace,
the exact operator proof in RESULT.md.
"""
from math import erf, exp, pi, sqrt, isclose
from itertools import product

def phi(t):
    return exp(-t*t)/sqrt(pi)

def h0(t):
    return pi**(-0.25)*exp(-t*t/2)

def h1(t):
    return sqrt(2)*t*h0(t)

def G(t):
    f=(1+erf(t))/2
    p=phi(t)
    return ((f,-p/sqrt(2)),(-p/sqrt(2),f-t*p))

def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def comm(A,B):
    P,Q=mul(A,B),mul(B,A)
    return tuple(tuple(P[i][j]-Q[i][j] for j in range(2)) for i in range(2))

def simpint(f,a,b,n=8000):
    if b<=a: return 0.0
    step=(b-a)/n
    return (step/3)*(f(a)+f(b)+4*sum(f(a+step*k) for k in range(1,n,2))+2*sum(f(a+step*k) for k in range(2,n,2)))

count=0
for fun,target in ((lambda u:h0(u)**2,1.0),(lambda u:h1(u)**2,1.0),(lambda u:h0(u)*h1(u),0.0)):
    assert abs(simpint(fun,-9,9)-target)<3e-12
    count+=1
for t in [-2.1,-1.3,-0.7,0,0.33,1.15,2.4]:
    R=((simpint(lambda u:h0(u)**2,-9,t),simpint(lambda u:h0(u)*h1(u),-9,t)),
       (simpint(lambda u:h0(u)*h1(u),-9,t),simpint(lambda u:h1(u)**2,-9,t)))
    Q=G(t)
    for i,j in product(range(2),repeat=2):
        assert abs(R[i][j]-Q[i][j])<3e-11,(t,i,j,R[i][j],Q[i][j])
        count+=1
for s in [-2.0,-.9,0,.4,1.6,2.8]:
    for t in [-1.7,-0.8,0.5,1.9]:
        for x in [-2.2,-0.3,0.0,.8,1.7]:
            actual=comm(G(s-x),G(t-x))
            k=(s-t)/sqrt(2)*phi(s-x)*phi(t-x)
            predicted=((0.,-k),(k,0.))
            for i,j in product(range(2),repeat=2):
                assert abs(actual[i][j]-predicted[i][j])<2e-15,(s,t,x,i,j)
                count+=1
for delta in [.01,.12,.5,1,1.5,2.7,5]:
    edge=delta*exp(-delta*delta/2)/(sqrt(2)*pi)
    for center in [-1.5,-.25,0.3,1.7]:
        s,t=center+delta/2,center-delta/2
        mid=(s+t)/2
        kk=abs(comm(G(s-mid),G(t-mid))[0][1])
        assert abs(kk-edge)<3e-16
        count+=1
        for y in [-2,-1,-.22,0.22,1,2]:
            val=abs(comm(G(s-(mid+y)),G(t-(mid+y)))[0][1])
            assert abs(val-edge*exp(-2*y*y))<3e-16
            count+=1
for d in [.15,.7,1,1.2,2.4,4]:
    edge=d*exp(-d*d/2)/(sqrt(2)*pi)
    bound=1/(pi*sqrt(2*exp(1)))
    assert edge<=bound+1e-16
    count+=1
assert abs(1/(pi*sqrt(2*exp(1)))-.136517362297204)<1e-14
count+=1
print('PASS',count,'checks: orthonormality, independent Gaussian integrals, commutator identities, exact spectral-edge samples, sharp bound')
