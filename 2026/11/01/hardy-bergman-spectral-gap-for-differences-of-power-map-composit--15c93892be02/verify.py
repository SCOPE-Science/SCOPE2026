"""Finite consistency checks for monomial composition differences.

Run with Python 3 standard library: python verify.py.
Finite checks are not a substitute for the analytic essential-spectrum proof.
"""
from fractions import Fraction
from math import gcd, sqrt, cos, pi, isclose

checks = 0

def check(flag, message):
    global checks
    assert flag, message
    checks += 1

def moment(n, alpha):
    # Exact normalized weighted-Bergman moment for integer alpha >= 0.
    out = Fraction(1)
    for j in range(1, alpha + 2):
        out *= Fraction(j, n + j)
    return out

def action(p, q, j, alpha):
    out = {}
    for k, sign in ((p, 1), (q, -1)):
        t = k * j
        out[t] = out.get(t, 0.) + sign * sqrt(float(moment(t, alpha) / moment(j, alpha)))
    return out

def inner(x, y):
    return sum(v * y.get(k, 0.) for k, v in x.items())

def path(a, b, r, length):
    return [r * a**u * b**(length-u) for u in range(length + 1)]

def shift(a, b, n):
    return None if n % a else (n // a) * b

for p, q in ((1,2), (2,3), (2,4), (3,6), (4,9), (9,4), (2,5), (6,35)):
    a,b = p//gcd(p,q), q//gcd(p,q)
    for alpha in (0,1,2):
        cols = [action(p,q,j,alpha) for j in range(20)]
        for j in range(20):
            for k in range(20):
                h = lambda n: float(moment(n,alpha))
                term = (h(p*j)/h(j)+h(q*j)/h(j)) if j==k else 0.
                if p*j == q*k:
                    term -= sqrt(h(p*j)/h(j)) * sqrt(h(q*k)/h(k))
                if q*j == p*k:
                    term -= sqrt(h(q*j)/h(j)) * sqrt(h(p*k)/h(k))
                check(isclose(inner(cols[j],cols[k]),term,abs_tol=3e-13,rel_tol=2e-13),f'Gram {p,q,j,k,alpha}')
    if a > 1 and b > 1:
        rs = [r for r in range(1,150) if r%a and r%b]
        for r in rs[:30]:
            for L in range(1,8):
                nodes = path(a,b,r,L)
                check(len(nodes)==len(set(nodes)), 'path nodes distinct')
                for i,n in enumerate(nodes):
                    expected = nodes[i-1] if i>0 else None
                    check(shift(a,b,n)==expected,'forward path link')
                    check((shift(b,a,n)==(nodes[i+1] if i<L else None)),'backward path link')
                # adjacency path eigenvalues obey the determinant recurrence
                for j in range(1,L+2):
                    eig = 2*cos(j*pi/(L+2))
                    d0,d1=1.,eig
                    for k in range(2,L+2):
                        d0,d1=d1,eig*d1-d0
                    check(abs(d1)<1e-10,'Chebyshev root')
    else:
        r = max(a,b)
        for seed in range(1,40):
            if seed%r:
                for level in range(1,15):
                    check(shift(1,r,seed*r**level)==seed*r**(level+1),'ray link')

for alpha in (0,1,2):
    for p in (2,3,5,9):
        c = p**(-(alpha+1)/2)
        for n in (1000,10000,100000):
            w = sqrt(float(moment(p*n,alpha)/moment(n,alpha)))
            check(abs(w-c)<0.005,'Bergman tail constant')

print(f'PASS {checks} finite deterministic assertions')
