#!/usr/bin/env python3
"""Exact characteristic-17 Cartier-rank calculations for a genus-four curve family.

Dependencies: Python 3, SymPy.  All polynomial arithmetic is in GF(17).
"""
import sympy as sp

p = 17
x, a, b = sp.symbols('x a b')
F = x**10 + x**7 + a*x**4 + b*x
P = sp.Poly(sp.expand(F**8), x)
coef = lambda j: sp.Poly(P.nth(j), a, b, modulus=p).as_expr()
A, B, C, D, E = coef(14), coef(32), coef(50), coef(47), coef(65)
assert sp.Poly(A - (-6*a*a*b**6 + 8*b**7),a,b,modulus=p).is_zero
assert sp.Poly(E-(-2*a*a+5*a*b+8*a-2*b+5),a,b,modulus=p).is_zero

# Exact necessary elimination identity over the algebraically closed field.
resultant = sp.Poly(sp.resultant(C,D,b),a,modulus=p)
expected = sp.Poly(3*a**3*(a-6)**12*(a+4)*(a+7)*(a-4),a,modulus=p)
assert resultant == expected

# Specialize the simultaneous-vanishing candidates.  gcd detects every
# common b-root, not just prime-field points.
roots = {0:[(0,1)],6:[(12,3)],13:[(12,1)],10:[(7,1)],4:[(12,1)]}
for av, common in roots.items():
    c = sp.Poly(C.subs(a,av),b,modulus=p)
    d = sp.Poly(D.subs(a,av),b,modulus=p)
    gc = sp.gcd(c,d)
    expected_gcd = sp.Poly(1,b,modulus=p)
    for bv,power in common:
        expected_gcd *= sp.Poly((b-bv)**power,b,modulus=p)
    assert gc.monic() == expected_gcd.monic(), (av,gc,expected_gcd)

# Smooth genus-four locus: b != 0 and cubic discriminant !=0.
disc=a**2-4*a**3-4*b-27*b*b+18*a*b
assert sp.Poly(E.subs(b,5*a*a)-8*(a+4)*(a+7)*(a-4),a,modulus=p).is_zero
assert sp.Poly(B.subs(b,5*a*a)+8*(a+3)*(a+4)*a**8,a,modulus=p).is_zero

special = [(13,12,0,4,11),(4,12,1,3,3),(10,7,1,3,4)]
# columns: a, b, Cartier rank, a-number, discriminant
for av,bv,rank,anumber,dlt in special:
    vv={a:av,b:bv}
    terms = [int(T.subs(vv))%p for T in (A,B,C,D,E)]
    cr = (terms[1]!=0) + ((terms[0],terms[4])!=(0,0)) + ((terms[2],terms[3])!=(0,0))
    assert cr==rank and 4-cr==anumber
    assert int(disc.subs(vv))%p==dlt
    print('EXCEPTION',av,bv,'rank',cr,'a-number',4-cr,'Delta',dlt)
assert int(disc.subs({a:6,b:12}))%17==0
assert int(disc.subs({a:0,b:0}))%17==0

# Confirm the open one- and two-defect strata are inhabited.
for av,bv,goal in [(0,1,2),(1,1,1)]:
    vv={a:av,b:bv}
    assert int(disc.subs(vv))%17!=0 and bv!=0
    terms = [int(T.subs(vv))%p for T in (A,B,C,D,E)]
    rank=(terms[1]!=0)+((terms[0],terms[4])!=(0,0))+((terms[2],terms[3])!=(0,0))
    assert 4-rank==goal,(av,bv,rank,terms)

# Exhaustive prime-field sanity check (not the reason for geometric completeness).
counts={1:0,2:0,3:0,4:0}
for av in range(p):
    for bv in range(1,p):
        vv={a:av,b:bv}
        if int(disc.subs(vv))%p == 0: continue
        v=[int(T.subs(vv))%p for T in (A,B,C,D,E)]
        rk=(v[1]!=0)+((v[0],v[4])!=(0,0))+((v[2],v[3])!=(0,0))
        aa=4-rk
        assert 1<=aa<=4
        assert aa == (4 if (av,bv)==(13,12) else 3 if (av,bv) in [(4,12),(10,7)] else 2 if v[1]==0 else 1)
        counts[aa]+=1
print('F17_SMOOTH_COUNTS',counts)
print('VERIFY_OK: five coefficient identities; exact resultant and fiber gcd certificates; full geometric a-number strata')
