"""Exact certificates for the first modal transition of order-k, r=2 waiting times.
Run with Python 3 and SymPy: python verify_modes.py
"""
import sympy as sp
from math import comb
q = sp.Symbol('q')

def coefficients(k, N):
    a = [sp.Integer(1)]
    for n in range(1, N + 1):
        a.append(sp.expand(q * sum((n+j)*((1-q)**(j-1))*a[n-j] for j in range(1, min(k,n)+1))/n))
    return a

def bernstein_coeffs(poly, right):
    """Bernstein coefficients on [0,right], exact finite-dimensional identity."""
    t = sp.Symbol('t')
    P = sp.Poly(sp.expand(poly.subs(q, right*t)), t)
    d = P.degree()
    v = [P.nth(j) for j in range(d+1)]
    return [sp.factor(sum(v[j]*sp.Rational(comb(i,j),comb(d,j)) for j in range(i+1))) for i in range(d+1)]

def rising(poly, right):
    vals = bernstein_coeffs(sp.diff(poly,q), right)
    assert all(v >= 0 for v in vals), (poly, right, vals)
    assert any(v > 0 for v in vals)
    return vals

def AB(k):
    A = sp.expand(q*sum((1-q)**(j-1) for j in range(1,k+1)))
    B = sp.expand(q*sum(j*(1-q)**(j-1) for j in range(1,k+1)))
    return A,B

def tail_bound(k, right, first_tail):
    A,B = AB(k)
    assert sp.simplify(A - (1-(1-q)**k)) == 0
    assert all(v>=0 for v in bernstein_coeffs(sp.diff(A,q),right))
    assert all(v>=0 for v in bernstein_coeffs(sp.diff(B,q),right)), (k,bernstein_coeffs(sp.diff(B,q),right))
    S = sp.factor(A.subs(q,right)+B.subs(q,right)/first_tail)
    assert S < 1, (k,first_tail,S)
    return S

# Two-run order two
c2=coefficients(2,3)
r2=sp.sqrt(2)-1
assert sp.simplify(c2[2].subs(q,r2)-1)==0
assert sp.simplify(c2[1].subs(q,r2))<1
assert all(v>=0 for v in bernstein_coeffs(sp.diff(c2[1],q),r2))
assert all(v>=0 for v in bernstein_coeffs(sp.diff(c2[2],q),r2))
S2=tail_bound(2,r2,3)

# Two-run order three
c3=coefficients(3,5)
r3=(sp.sqrt(3)-1)/2
u3=sp.Rational(3,8)
assert sp.simplify(c3[3].subs(q,r3)-1)==0
assert r3 < u3
for n in range(1,6):
    rising(c3[n],u3)
    if n != 3: assert c3[n].subs(q,u3) < 1, (n,c3[n].subs(q,u3))
S3=tail_bound(3,u3,6)

# Two-run order four
c4=coefficients(4,8)
lo,hi=sp.Rational(3315,10000),sp.Rational(3316,10000)
assert lo < hi < sp.Rational(1,3)
assert c4[7].subs(q,lo) < 1 < c4[7].subs(q,hi)
for n in range(1,9):
    rising(c4[n],sp.Rational(1,3))
    if n != 7: assert c4[n].subs(q,hi) < 1, (n,c4[n].subs(q,hi))
S4=tail_bound(4,sp.Rational(1,3),9)
assert sp.expand(c4[4] - q*(3*q+2)) == 0
assert c4[4].subs(q,sp.Rational(1,3)) == 1
# Strict g4>1 for q>1/3; g7>1 for q in (root, 1/3].
assert all(v>=0 for v in bernstein_coeffs(sp.diff(c4[7],q),sp.Rational(1,3)))

print('order2 first q:',r2,'tail',S2)
print('order3 first q:',r3,'tail',S3)
print('order4 root polynomial:',sp.factor(c4[7]-1),'tail',S4)
print('order4 c7 at brackets:',float(c4[7].subs(q,lo)),float(c4[7].subs(q,hi)))
print('order4 others at hi:',[(n,float(c4[n].subs(q,hi))) for n in range(1,9) if n!=7])
print('VERIFY_OK')
