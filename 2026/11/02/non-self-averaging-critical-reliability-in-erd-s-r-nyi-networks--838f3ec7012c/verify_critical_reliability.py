"""Standalone finite and asymptotic consistency checks for the reliability result.

No computation here substitutes for the analytic proof.
Run: python3 verify_critical_reliability.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, exp, log

checks=0

def assert_equal(x,y):
    global checks
    assert x==y,(x,y)
    checks+=1

def close(x,y,tol):
    global checks
    assert abs(float(x)-float(y)) <= tol,(x,y,tol)
    checks+=1

def edges(n):
    return list(combinations(range(n),2))

def connected(n,E,mask):
    parent=list(range(n))
    def find(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    for j,(u,v) in enumerate(E):
        if mask>>j & 1:
            a,b=find(u),find(v)
            parent[a]=b
    return all(find(i)==find(0) for i in range(1,n))

def reliability(n,E,base,t):
    active=[e for j,e in enumerate(E) if base>>j&1]
    m=len(active)
    return sum((t**k)*((1-t)**(m-k)) for subset in range(1<<m)
            if connected(n,active,subset) for k in [subset.bit_count()])

def avgrel(n,E,base):
    active=[e for j,e in enumerate(E) if base>>j&1]
    m=len(active)
    return sum(F(1,(m+1)*comb(m,subset.bit_count()))
               for subset in range(1<<m) if connected(n,active,subset))

def mean_annealed_from_polynomial(n,p):
    E=edges(n); N=len(E)
    acc=F(0)
    for mask in range(1<<N):
        if not connected(n,E,mask): continue
        k=mask.bit_count()
        for j in range(N-k+1):
            acc+=F(comb(N-k,j)*(-1)**j,k+j+1)*p**(k+j)
    return acc

def marginal_connectivity(n,p):
    E=edges(n);m=len(E)
    return sum(p**mask.bit_count()*(1-p)**(m-mask.bit_count())
               for mask in range(1<<m) if connected(n,E,mask))

for n in range(2,5):
    E=edges(n);m=len(E)
    for base in range(1<<m):
        a=avgrel(n,E,base)
        assert F(0)<=a<=F(1)
        checks+=1
        # Independent Bernstein/Beta integral reconstructed from polynomial.
        k=base.bit_count()
        poly=F(0)
        for sub in range(1<<k):
            act=[e for j,e in enumerate(E) if base>>j&1]
            if not connected(n,act,sub): continue
            v=sub.bit_count()
            for l in range(k-v+1):
                poly+=F(comb(k-v,l)*(-1)**l,v+l+1)
        assert_equal(a,poly)
    for p in (F(1,3),F(1,2),F(2,3)):
        direct=sum(p**mask.bit_count()*(1-p)**(m-mask.bit_count())*avgrel(n,E,mask)
                   for mask in range(1<<m))
        assert_equal(direct,mean_annealed_from_polynomial(n,p))
        for t in (F(1,4),F(1,2),F(3,4)):
            lhs=sum(p**mask.bit_count()*(1-p)**(m-mask.bit_count())*reliability(n,E,mask,t)
                    for mask in range(1<<m))
            assert_equal(lhs,marginal_connectivity(n,p*t))
        # Mixed two-thinning second moment, independent direct summations.
        t1,t2=F(1,2),F(2,3)
        lhs=sum(p**mask.bit_count()*(1-p)**(m-mask.bit_count())*
                reliability(n,E,mask,t1)*reliability(n,E,mask,t2)
                for mask in range(1<<m))
        probs=(1-p*(t1+t2-t1*t2),p*t1*(1-t2),p*(1-t1)*t2,p*t1*t2)
        rhs=F(0)
        for codes in range(4**m):
            tmp=codes;a=b=0;w=F(1)
            for j in range(m):
                c=tmp%4;tmp//=4;w*=probs[c]
                if c&1:a|=1<<j
                if c&2:b|=1<<j
            if connected(n,E,a) and connected(n,E,b):rhs+=w
        assert_equal(lhs,rhs)

# Exact isolate probability; shared isolated vertices after two independent thinnings.
for n in (1000,10000,100000):
    for x in (-1,0,1):
        p=(log(n)+x)/n
        s1,s2=.6,1.5
        t1,t2=1-s1/log(n),1-s2/log(n)
        mu0=n*(1-p)**(n-1)
        mu1=n*(1-p*t1)**(n-1)
        mu2=n*(1-p*t2)**(n-1)
        mu12=n*(1-p*(t1+t2-t1*t2))**(n-1)
        if n==100000:
            close(mu0,exp(-x),.008)
            # Finite-n corrected asymptotic, with the slow 1/log(n) drift included.
            close(mu1,exp(-x+s1*(1+x/log(n))),.006)
            close(mu2,exp(-x+s2*(1+x/log(n))),.006)
            close(mu12,exp(-x+(log(n)+x)*s1*s2/log(n)**2),.003)
        assert mu12>=mu0
        checks+=1

# Independent quadratures for the two integral representations of the area.
def simpson(f,a,b,N=40000):
    h=(b-a)/N
    z=f(a)+f(b)
    for k in range(1,N):
        z+=(4 if k%2 else 2)*f(a+k*h)
    return h*z/3

for x in (-2,-1,0,1,2):
    z=exp(-x)
    I=simpson(lambda s:exp(-z*(exp(s)-1)),0,8)
    J=exp(z)*simpson(lambda u:exp(-u)/u,z,40)
    close(I,J,2e-7)
    close(exp(-z)*J,simpson(lambda u:exp(-u)/u,z,40),2e-7)

assert_equal(avgrel(3,edges(3),0b111),F(1,2))
assert_equal(avgrel(3,edges(3),0b011),F(1,3))
print('PASS',checks,'exact or numerical checks')
