"""Supplementary finite checks for low-degree Bernstein node classification.
Run: python CHECK.py (Python 3 standard library). Analytical arguments in RESULT.md cover all parameters.
"""
from math import comb, cos, pi, isclose

def coefficients(n, nodes, m):
    samples = [cos(m*x) for x in nodes]
    p = [sum(comb(n,j)*comb(n-j,k-j)*(-1)**(k-j)*samples[j]
             for j in range(k+1)) for k in range(n+1)]
    return p

def fourier_coefficient(p, k):
    n=len(p)-1
    if k==0:
        return 2*sum(p[j]/(j+1) for j in range(n+1))
    first0=p[1]
    first1=sum(j*p[j] for j in range(1,n+1))
    third=6*p[3] if n>=3 else 0.0
    return 2*(((-1)**k)*first1-first0)/(pi*k)**2 - 2*(((-1)**k)*third-third)/(pi*k)**4

def same(a,b):
    return isclose(a,b,rel_tol=1e-8,abs_tol=3e-9)

checks=0
for n in (2,3):
    for a_index in range(13):
        a=(a_index/12)*pi/2
        nodes=([0,pi/2,pi] if n==2 else [0,a,pi-a,pi])
        for m in range(1,26):
            p=coefficients(n,nodes,m)
            c=cos(m*(pi/2 if n==2 else a))
            for k in range(0,27):
                actual=fourier_coefficient(p,k)
                if n==2:
                    if m%2:
                        formula=0.0 if k==0 or k%2==0 else 8/(pi*k)**2
                    else:
                        formula=2*(2+c)/3 if k==0 else (8*(1-c)/(pi*k)**2 if k%2==0 else 0.0)
                elif m%2==0:
                    formula=1+c if k==0 else (12*(1-c)/(pi*k)**2 if k%2==0 else 0.0)
                else:
                    formula=0.0 if k==0 or k%2==0 else 12*(1-c)/(pi*k)**2+48*(3*c-1)/(pi*k)**4
                assert same(actual,formula),(n,a,m,k,actual,formula)
                assert formula>=-1e-9,(n,a,m,k,formula)
                checks+=2
# Necessary condition test for a nonsymmetric pair, and midpoint failure at degree two.
for n,nodes in ((2,[0,pi/3,pi]),(3,[0,pi/5,3*pi/5,pi])):
    p=coefficients(n,nodes,1)
    a0=fourier_coefficient(p,0)
    even_high=fourier_coefficient(p,1000)
    assert a0*even_high < 0,(n,a0,even_high)
    checks+=1
print(f"PASS: {checks} supplementary identities, nonnegativity tests and asymmetry witnesses.")
