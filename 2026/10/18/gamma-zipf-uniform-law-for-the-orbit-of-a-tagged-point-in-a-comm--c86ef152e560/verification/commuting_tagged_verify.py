"""Exact finite checks for the pointed-orbit law of commuting permutations.

Run with python3 commuting_tagged_verify.py; no external packages required.
"""
from itertools import permutations
from fractions import Fraction
from math import factorial, isqrt


def coeffs(theta, nmax):
    """[z**n] product_{j>=1}(1-z**j)**(-theta), by logarithmic derivative."""
    sigma = [0] * (nmax + 1)
    for d in range(1, nmax + 1):
        for j in range(d, nmax + 1, d):
            sigma[j] += d
    z = [Fraction(1)]
    for n in range(1, nmax + 1):
        z.append(theta * sum(sigma[j]*z[n-j] for j in range(1,n+1))/n)
    return z


def composed(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def order_and_orbit(p, q):
    n=len(p)
    a=1
    j=p[0]
    while j!=0:
        a+=1
        j=p[j]
    orbit={0}; stack=[0]
    while stack:
        x=stack.pop()
        for y in (p[x],q[x]):
            if y not in orbit:
                orbit.add(y);stack.append(y)
    return a, len(orbit)


def twist(p,q,a,j):
    d=j//a
    y=0
    for _ in range(d): y=q[y]
    x=0
    for b in range(a):
        if x==y: return b
        x=p[x]
    raise AssertionError("non-transitive twist")


def orbit_count(p,q):
    n=len(p); seen=set(); count=0
    for i in range(n):
        if i in seen: continue
        count+=1; stack=[i];seen.add(i)
        while stack:
            x=stack.pop()
            for y in (p[x],q[x]):
                if y not in seen: seen.add(y);stack.append(y)
    return count


def test_exhaustive():
    checks=0
    for n in range(1,6):
        ps=list(permutations(range(n)))
        data={}; allcnt=0; zw=Fraction(0)
        for p in ps:
            for q in ps:
                if composed(p,q)!=composed(q,p): continue
                a,j=order_and_orbit(p,q)
                k=orbit_count(p,q)
                b=twist(p,q,a,j)
                data[(a,j,b,k)]=data.get((a,j,b,k),0)+1
                allcnt+=1;zw+=Fraction(2**k)
        for theta in (1,2):
            z=coeffs(Fraction(theta),n)
            norm=factorial(n)*z[n]
            assert (allcnt if theta==1 else zw)==norm
            checks+=1
            for a in range(1,n+1):
                for d in range(1,n//a+1):
                    j=a*d
                    weighted=sum(cnt*theta**k for (aa,jj,b,k),cnt in data.items() if aa==a and jj==j)
                    pred=Fraction(theta*a*z[n-j],n*z[n])
                    assert Fraction(weighted,norm)==pred,(n,theta,a,d,weighted,pred)
                    checks+=1
                    for b in range(a):
                        wb=sum(cnt*theta**k for (aa,jj,bb,k),cnt in data.items() if aa==a and jj==j and bb==b)
                        assert Fraction(wb,norm)==Fraction(theta*z[n-j],n*z[n]),(n,theta,a,d,b)
                        checks+=1
    return checks


def test_coefficient_normalization():
    checks=0
    for theta in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(5,3)):
        z=coeffs(theta, 35)
        for n in range(1,36):
            total=sum(Fraction(theta*a)*z[n-a*d] for a in range(1,n+1) for d in range(1,n//a+1))
            assert total==n*z[n]
            checks+=1
    return checks


def test_shape():
    """Low-precision diagnostics, not a proof of asymptotic statements."""
    from math import pi, sqrt, exp
    checks=0
    for theta in (1,2):
        n=500
        z=coeffs(Fraction(theta),n)
        beta=pi*sqrt(theta/6)
        # Exact finite CDF at a scaled test point; compare against Gamma(2, beta).
        for x in (0.5,1.5,3.0):
            max_j=int(x*sqrt(n))
            prob=sum(Fraction(theta*a)*z[n-a*d] for a in range(1,n+1) for d in range(1,n//a+1) if a*d<=max_j)/(n*z[n])
            limit=1-(1+beta*x)*exp(-beta*x)
            assert abs(float(prob)-limit)<0.095,(theta,x,prob,limit)
            checks+=1
        # D=1 probability approaches 6/pi^2, slowly.
        p_d1=sum(Fraction(theta*a)*z[n-a] for a in range(1,n+1))/(n*z[n])
        assert abs(float(p_d1)-6/pi**2)<0.07
        checks+=1
    return checks


if __name__=='__main__':
    c1=test_exhaustive()
    c2=test_coefficient_normalization()
    c3=test_shape()
    print(f'PASS: {c1} exhaustive commuting-pair/pointed-orbit assertions; '
          f'{c2} exact normalized-coefficient assertions; {c3} finite asymptotic diagnostics.')
