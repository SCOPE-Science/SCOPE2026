"""Reproduce monomial mixed-commutator singular values and radial residues.
Run with Python >=3.9, numpy and scipy: python check.py
"""
import cmath
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad

NUM_CHECKS = 0

def close(a,b,tol=2e-11):
    global NUM_CHECKS
    assert abs(a-b)<=tol*(1+abs(a)+abs(b)), (a,b)
    NUM_CHECKS += 1

def coefficients(m,n,r,a,b,limit):
    """Nonzero column/output triples from exact monomial adjoint rule."""
    d=math.gcd(m,n); p=m//d; q=n//d
    terms=[]
    for l in range(1,limit//p+1):
        if l%d:
            w=(r**(p+q)*b**p*a.conjugate()**q)**l
        else:
            h=l//d
            w=(r**(m+n)*b**m*a.conjugate()**n)**h-(r*r*b*a.conjugate())**h
        terms.append((p*l,q*l,w))
    return terms

def matrix(m,n,r,a,b,N):
    """Direct finite-coordinate computation, independent of residue derivation."""
    A=np.zeros((N,N),complex);B=np.zeros((N,N),complex)
    for k in range(N):
        if m*k<N:A[m*k,k]=(r*a)**k
        if n*k<N:B[n*k,k]=(r*b)**k
    return A.conj().T@B-B@A.conj().T

def hs_formula(m,n,r,xi):
    d=math.gcd(m,n); p=m//d; q=n//d
    def geom(x):return x/(1-x)
    return (geom(r**(2*(p+q)))-geom(r**(2*(m+n)))
            +geom(r**(2*(m+n)))+geom(r**4)
            -2*(r**(m+n+2)*xi/(1-r**(m+n+2)*xi)).real)

def hs_coefficient(m,n,xi):
    d=math.gcd(m,n);s=m+n
    return d/(2*s)+1/4-(2/(s+2) if abs(xi-1)<1e-14 else 0)

def trace_formula(m,n,r,a,b,max_terms=500000):
    d=math.gcd(m,n);p=m//d;q=n//d
    z=b**(m-1)*a.conjugate()**(n-1)
    first=(r**(p+q)/(1-r**(p+q))-r**(m+n)/(1-r**(m+n)))
    h=np.arange(1,max_terms+1,dtype=np.int64)
    return first+np.abs(r**((m+n)*h)*np.power(z,h)-r**(2*h)).sum()

def Aroot(m,n,Q):
    c=m+n-2
    vals=[]
    for j in range(Q):
        z=cmath.exp(2*math.pi*1j*j/Q)
        vals.append(quad(lambda t:math.exp(-2*t)*abs(1-math.exp(-c*t)*z),0,30,epsabs=1e-11)[0])
    return sum(vals)/Q

def Ahaar(m,n):
    c=m+n-2
    def inner(t):
        rr=math.exp(-c*t)
        return quad(lambda phi:abs(1-rr*cmath.exp(1j*phi)),0,2*math.pi,epsabs=1e-10)[0]/(2*math.pi)
    return quad(lambda t:math.exp(-2*t)*inner(t),0,25,epsabs=1e-9)[0]

# Exact finite-column comparison, including common divisors and complex phases.
for m,n in [(2,2),(2,3),(2,4),(3,6),(4,6)]:
    for r,a,b in [(0.68,1+0j,1+0j),(0.73,cmath.exp(.6j),cmath.exp(.4j))]:
        N=480
        K=matrix(m,n,r,a,b,N)
        for col,row,w in coefficients(m,n,r,a,b,limit=80):
            if row<N and col<N:
                close(K[row,col],w)
                close(np.linalg.norm(K[:,col]),abs(w))
        for col in range(1,79):
            if col % (m//math.gcd(m,n)):
                close(np.linalg.norm(K[:,col]),0)

for m,n in [(2,2),(2,3),(2,4),(3,6),(4,6)]:
    for z in [1+0j,-1+0j,cmath.exp(.7j)]:
        for r in [.4,.63,.85]:
            d=math.gcd(m,n);p=m//d;q=n//d
            h=np.arange(1,1000)
            first=r**(2*(p+q)*h)
            first=first[h%d!=0].sum()
            w=np.power(r,m+n)**h*np.power(z,h)-np.power(r,2)**h
            close(first+np.sum(abs(w)**2),hs_formula(m,n,r,z),1e-9)
        # First-order coefficient direct evaluation sufficiently near boundary.
        r=.99993
        a=hs_formula(m,n,r,z)*(1-r)
        close(a,hs_coefficient(m,n,z),3e-4)

# Trace limit for root phase orders; Cesaro phase factors and diagonal residues.
for m,n in [(2,3),(2,4),(3,6)]:
    d=math.gcd(m,n)
    for Q in [1,2,3,5]:
        xi=cmath.exp(2*math.pi*1j/Q)
        # Select a=1 and b with b^(m-1) a primitive Q-th root.
        a=1+0j;b=cmath.exp(2*math.pi*1j/(Q*(m-1)))
        r=.9985
        actual=trace_formula(m,n,r,a,b,40000)*(1-r)
        target=(d-1)/(m+n)+Aroot(m,n,Q)
        close(actual,target,0.006)

# Check the boundary-layer operator-norm coefficient for gcd one/resonance.
for m,n in [(2,3),(3,4),(5,7)]:
    s=m+n;c=s-2
    theoretical=(1-2/s)*(2/s)**(2/c)
    for r in [.998,.9995]:
        h=np.arange(1,int(25/(1-r)))
        empirical=np.max(r**(2*h)-r**(s*h))
        close(empirical,theoretical,1e-4)

# Strict phase dependence: rational roots versus Haar value.
for m,n in [(2,3),(2,5)]:
    val1=Aroot(m,n,1);val2=Aroot(m,n,2);val3=Aroot(m,n,3)
    valinf=Ahaar(m,n)
    assert val1<val2 and val1<val3 and val1<valinf
    NUM_CHECKS+=3

print(f'PASS: {NUM_CHECKS} finite matrix/formula/asymptotic assertions')
print('Example trace residues m=2,n=3: xi=1',Aroot(2,3,1),'xi=-1',Aroot(2,3,2),'xi=exp(2pi i/3)',Aroot(2,3,3),'irrational',Ahaar(2,3))
