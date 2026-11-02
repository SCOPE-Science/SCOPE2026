"""Exact finite and symbolic checks for Mallows alternating-subsequence moments.

Python 3 plus SymPy. Run: python VERIFY.py
The infinite-size extremum theorem is proved in RESULT.md, not inferred from this code.
"""
from fractions import Fraction
from itertools import permutations
import sympy as sp

q = sp.symbols('q', positive=True)
checks = 0

def assert_eq(a,b):
    global checks
    assert sp.factor(a-b)==0,(a,b)
    checks+=1

def inversions(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def turn(p,i):
    return (p[i-1]<p[i]>p[i+1]) or (p[i-1]>p[i]<p[i+1])

def z(m):
    return sp.prod(sum(q**j for j in range(k)) for k in range(1,m+1))

def event(m,predicate):
    return sum(q**inversions(p) for p in permutations(range(m)) if predicate(p))/z(m)

T=q/(1+q)
A=2*q/(1+q+q*q)
B=q*(q*q+3*q+1)/((1+q)**2*(1+q+q*q))
C=q*q*(3*q**4+7*q**3+7*q*q+7*q+3)/((1+q)**2*(1+q+q*q)*(1+q+q*q+q**3+q**4))
U=q/(1+q+q*q)
W=q*q*(2*q*q+q+1)/((1+q)*(1+q*q)*(1+q+q*q))
assert_eq(event(2,lambda p:p[0]>p[1]),T)
assert_eq(event(3,lambda p:turn(p,1)),A)
assert_eq(event(4,lambda p:turn(p,1) and turn(p,2)),B)
assert_eq(event(5,lambda p:turn(p,1) and turn(p,3)),C)
assert_eq(event(3,lambda p:p[0]>p[1] and turn(p,1)),U)
assert_eq(event(4,lambda p:p[0]>p[1] and turn(p,2)),W)

V=4*q*(q**6-q**5+2*q**3-q+1)/((1+q+q*q)**2*(1+q+q*q+q**3+q**4))
K=-q*(11*q**10+5*q**9-15*q**8+5*q**7+17*q**6+13*q**4+q**3-19*q*q+q+7)/((1+q)**2*(1+q*q)*(1+q+q*q)**2*(1+q+q*q+q**3+q**4))
P=q**10-3*q**9-6*q**8-q**7-2*q**6-3*q**5-2*q**4-q**3-6*q*q-3*q+1
assert_eq(A*(1-A)+2*(B-A*A)+2*(C-A*A),V)
assert_eq(T*(1-T)-2*A*(1-A)-6*(B-A*A)-8*(C-A*A)+2*(U-T*A)+2*(W-T*A),K)
assert_eq(sp.diff(V,q),-4*(q-1)*(q+1)*P/((1+q+q*q)**3*(1+q+q*q+q**3+q**4)**2))
assert_eq(P,q**10*P.subs(q,1/q))
assert_eq(V,V.subs(q,1/q))
assert_eq(V.subs(q,1),sp.Rational(8,45))
assert_eq(K.subs(q,1),-sp.Rational(13,180))

# Independently compute longest descent-first alternating subsequence by DP.
def longest_downfirst(p):
    n=len(p)
    up=[1]*n
    down=[1]*n
    for i in range(n):
        for j in range(i):
            if p[j]>p[i]:
                down[i]=max(down[i],up[j]+1)
            if p[j]<p[i] and down[j]>=2:
                up[i]=max(up[i],down[j]+1)
    return max(max(up),max(down))

def predicted(n,r):
    conv=lambda x: Fraction(sp.Rational(x.subs(q,sp.Rational(r.numerator,r.denominator))))
    t,a,b,c,u,w=map(conv,(T,A,B,C,U,W))
    mu=1+t+(n-2)*a
    variance=t*(1-t)+(n-2)*a*(1-a)+2*(n-3)*(b-a*a)+2*(n-4)*(c-a*a)+2*(u-t*a)+2*(w-t*a)
    return mu,variance

for n in range(4,9):
    qs=[Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(2),Fraction(3)] if n<=7 else [Fraction(1,2),Fraction(1)]
    for r in qs:
        mass=Fraction(0); first=Fraction(0); second=Fraction(0)
        for p in permutations(range(n)):
            L=longest_downfirst(p)
            independent_formula=1+int(p[0]>p[1])+sum(turn(p,i) for i in range(1,n-1))
            assert L==independent_formula,(n,p,L,independent_formula)
            checks+=1
            w=r**inversions(p)
            mass+=w
            first+=w*L
            second+=w*L*L
        mu=first/mass
        variance=second/mass-mu*mu
        expected_mu,expected_variance=predicted(n,r)
        assert (mu,variance)==(expected_mu,expected_variance),(n,r,mu,variance,expected_mu,expected_variance)
        checks+=1
print(f'PASS: {checks:,} exact assertions; n=4..8, and 13 symbolic identities')
