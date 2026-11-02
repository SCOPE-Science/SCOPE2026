#!/usr/bin/env python3
"""Exact finite-field polynomial certificates for a genus-three dihedral pencil.

Requires Python 3 and sympy. All modular identities are exact.
"""
import sympy as sp

a,x=sp.symbols('a x')
p=13

def coeff_mod(expr,variable,degree,p):
    expr=sp.Poly(sp.expand(expr),variable,a)
    ans=0
    for (d,e),c in expr.terms():
        if d==degree: ans+=int(c)*a**e
    return sp.Poly(ans,a,modulus=p)

f=x**7+a*x**4+x
M=[[coeff_mod(f**6,x,p*i-j,p) for j in range(1,4)] for i in range(1,4)]
assert all(M[i][j].is_zero for i in range(3) for j in range(3) if i!=j)
assert M[0][0]==M[2][2]
H1=M[0][0];H0=M[1][1]
assert H1==sp.Poly(2*a**2+6,a,modulus=13)
assert H0==sp.Poly(a**6+4*a**4-a**2-6,a,modulus=13)
assert H0==coeff_mod((x**3+a*x**2+x)**6,x,12,13)
assert H1==coeff_mod((x**3-3*x+a)**6,x,12,13)
assert sp.gcd(H0,H1).degree()==0
assert sp.gcd(H0,H0.diff()).degree()==0
assert sp.gcd(H1,H1.diff()).degree()==0
assert sp.gcd(H0,sp.Poly(a**2-4,a,modulus=p)).degree()==0
assert sp.gcd(H1,sp.Poly(a**2-4,a,modulus=p)).degree()==0
assert H0 == sp.Poly((a*a+5)*(a*a+6*a-2)*(a*a-6*a-2),a,modulus=p)
assert H1 == sp.Poly(2*(a-6)*(a+6),a,modulus=p)
squares={i*i%p for i in range(p)}
assert 5 not in squares and 8 not in squares
smooth={i for i in range(13) if (i*i-4)%13}
rank1={i for i in smooth if H1.eval(i)==0}
rank2={i for i in smooth if H0.eval(i)==0}
assert rank1=={6,7} and rank2==set()
assert len(smooth-rank1-rank2)==9
print('CHAR13_HASSE_WITT_DIAGONAL_H1_H0_H1=OK')
print('H0=',H0.as_expr(),' H1=',H1.as_expr())
print('CHAR13_ROOTS_H1=2_F13; H0=6_F169; DISJOINT=OK')
print('CHAR13_GEOMETRIC_13_RANKS=1,2,3; NEVER_ZERO; A_NUMBERS=2,1,0')
print('CHAR13_F13_SMOOTH=11; RANK1=2_POINTS_6_7; RANK2=0; RANK3=9')
print('CHAR13_F169_SMOOTH=167; RANK1=2; RANK2=6; RANK3=159')
for pp in [5,7,11]:
    m=(pp-1)//2
    h0=coeff_mod((x**3+a*x**2+x)**m,x,pp-1,pp)
    h1=coeff_mod((x**3-3*x+a)**m,x,pp-1,pp)
    g=sp.gcd(h0,h1)
    if pp==5: assert h1.degree()==0 and int(h1.LC())!=0
    if pp in (7,11):
        assert h1==sp.Poly(h1.LC()*a,a,modulus=pp)
        assert g==sp.Poly(a,a,modulus=pp) or g==sp.Poly(-a,a,modulus=pp)
    print('EARLIER_PRIME',pp,'H0=',h0.as_expr(),'H1=',h1.as_expr(),'GCD=',g.as_expr())
print('EARLIEST_TAME_ODD_PRIME_WITH_RANK1=13')
print('VERIFY_OK')
