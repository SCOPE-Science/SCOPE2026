#!/usr/bin/env python3
"""Exact rational certificates for Richardson--Euler cyclic kernel positivity.
Usage: python verify.py  (requires SymPy, no downloaded data)
"""
from fractions import Fraction
import sympy as S

h = S.Symbol('h')
checks = 0

def check(condition, message):
    global checks
    assert bool(condition), message
    checks += 1

def polynum(n, j):
    """Numerator of h^{-j} times cyclic kernel coefficient, after a positive denominator."""
    A = (h+2)**n - h**n
    B = (h+1)**n - h**n
    d = max(0, j+2-n)
    return S.Poly(
        8*(h+2)**max(0,n-j-2)*((j+1)*(h+2)**n+(n-j-1)*h**n)*B
        -(h+1)**(n-j-1)*A*A*(h+2)**d, h)

def variations(arr):
    global checks
    signs = [S.sign(x) for x in arr if x != 0]
    check(all(q in (-1,1) for q in signs), 'non-real sign')
    return sum(a != b for a,b in zip(signs,signs[1:]))

def sturm_counts(P):
    chain = S.sturm(P.as_expr(),h)
    v0 = variations([q.subs(h,0) for q in chain])
    vinf = variations([S.LC(S.Poly(q,h)) for q in chain])
    positive_count = v0-vinf
    # Zero values at h=0 are omitted from the sign variations: count (0,+inf).
    return v0,vinf,positive_count

def coefficient(n,j,t):
    """Exact coefficient on j-step forward cyclic shift in the endpoint map."""
    t=Fraction(t)
    s=t/(t+2);r=t/(t+1)
    return 2*(1-s)**2*s**j * (j+1+(n-j-1)*s**n)/(1-s**n)**2 - (1-r)*r**j/(1-r**n)

# Smallest unconditional positivity dimension: every small-dimension numerator
# has nonnegative coefficients, including the zero constant in n=4,j=3.
for n in range(2,5):
    for j in range(n):
        cs=polynum(n,j).all_coeffs()
        check(all(x >= 0 for x in cs),'unconditional positivity failed')
        check(any(x > 0 for x in cs),'zero numerator')
print('All cyclic kernel coefficients are positive for h>0 in n=2,3,4.')

# Sharp 14-state diagonal threshold: Sturm variations at h=0 and h=+infinity.
print('n  V(0)  V(+infinity)  positive roots for diagonal numerator')
for n in range(2,15):
    P=polynum(n,0)
    v0,vinf,number=sturm_counts(P)
    check(number == (2 if n == 14 else 0),f'diagonal Sturm count n={n}')
    check(P.eval(0)>0,'diagonal starts positive')
    print(n,v0,vinf,number)

# The full positivity set at n=14 has precisely two nontrivial components.
# The only effective offdiagonal threshold is j=13.
for j in range(14):
    P=polynum(14,j)
    v0,vinf,positive=sturm_counts(P)
    required=(2 if j==0 else 1 if j>=4 else 0)
    check(positive==required,f'wrong positive root count: j={j}, value={positive}')
    if j in (1,2): check(P.eval(0)>0,f'j={j} starting value')
    if j==3:
        check(P.eval(0)==0 and P.nth(1)>0,'j=3 removable zero')
        check(all(c>=0 for c in P.all_coeffs()),'j=3 positivity')
    if 4<=j<=12:
        check(P.eval(0)<0 and P.eval(3)>0,f'j={j} root precedes 3')
    if j==13:
        check(P.eval(3)<0 and P.eval(4)>0,'last offdiagonal threshold in (3,4)')
    if j==0:
        check(P.eval(5)>0 and P.eval(6)<0 and P.eval(9)>0,'diagonal roots bracketed')
print('For n=14: unique last offdiagonal root in (3,4), diagonal roots in (5,6),(6,9).')

# Concrete witnesses. Each rational computation is exact, not floating-point.
for n,t,positive in [(14,4,True),(14,6,False),(14,10,True)]:
    cs=[coefficient(n,j,t) for j in range(n)]
    if positive: check(all(c>0 for c in cs),f'n={n}, h={t} not positive')
    else:
        check(cs[0]<0 and all(c>0 for c in cs[1:]),'n=14, h=6 sign pattern')
    print('n=14 h=',t,'smallest index=',min(range(n),key=lambda j:cs[j]),
          'min coefficient=',str(min(cs)))

# Negativity at h=6 for every n>=14: verify n=14,15,16 exactly.
for n in range(14,17):
    check(coefficient(n,0,6)<0,f'n={n} diagonal should be negative')

# For n>=17 set z=(3/4)^n. The signed correction satisfies
# C_0(n,6) <= -1/56 + (n+1) z/[8 (1-z)^2].
# This is <0 if 7(n+1)z < (1-z)^2; it holds at n=17 and is
# preserved since (n+1)(3/4)^n decreases while (1-(3/4)^n)^2 increases.
z=Fraction(3,4)**17
check(7*18*z < (1-z)**2,'infinite-family tail certificate')
check(Fraction(3,4)*Fraction(19,18)<1,'monotone tail premise')

# Independent direct matrix inverse tests, not used in place of the proof.
for n in (2,3,4,5,14):
    P=S.zeros(n)
    for i in range(n):P[i,(i+1)%n]=1
    Q=P-S.eye(n)
    for t in (S.Rational(1,7),S.Rational(4),S.Rational(6)):
        B=(S.eye(n)-t*Q).inv()
        C=(S.eye(n)-t*Q/2).inv()
        R=2*C*C-B
        for j in range(n):
            check(R[0,j]==coefficient(n,j,Fraction(int(t.p),int(t.q))),
                  f'direct matrix mismatch n={n},j={j},t={t}')
        check(all(sum(R[i,j] for j in range(n))==1 for i in range(n)),
              'not row-stochastic')

print('All exact checks passed:',checks)
