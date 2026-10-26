#!/usr/bin/env python3
"""Exact arithmetic checks for a characteristic-five genus-four family.
Run with Python 3 and SymPy (requirements.txt). No network or Magma needed.
"""
from sympy import symbols, Poly, Matrix, groebner, resultant, gcd, factor_list

p = 5
x, a, b = symbols('x a b')
f = x**10+a*x**8+b*x**6+b*x**4+a*x**2+1
c = Poly(f**2, x)
M = Matrix([[c.coeff_monomial(x**(5*i-j)) for j in range(1,5)]
            for i in range(1,5)])
u=a*a+2*b
h=2*a
l=2*b*(a+1)
v=b*b+2*a*b+2*a
expect=Matrix([[u,0,h,0],[0,v,0,l],[l,0,v,0],[0,h,0,u]])
assert all(Poly(M[i,j]-expect[i,j],a,b,modulus=p).is_zero
           for i in range(4) for j in range(4))

D=Poly(u*v-h*l,a,b,modulus=p).as_expr()
# Correct column-action Cartier semilinearity: product is M^(p)*M,
# not M*M^(p); rank-one block scalar is u^(p+1)+h^p*l.
N=Poly(u**6+h**5*l,a,b,modulus=p).as_expr()
S=(a+b+1)*(b+2*a)*(a*a+2*a+b)
Q=Poly(a**6+a**5+a**2+a-1,a,modulus=p)
Beta=Poly(-2*a**5-2*a**4+a**3-a**2+2*a-1,a,modulus=p)

# Reconstruct resultant from its defining Sylvester polynomial operation.
R=Poly(resultant(D,N,b),a,modulus=p)
RF=Poly(2*a**18*(a+1)*(a+2)*(a-2)**6*Q.as_expr(),a,modulus=p)
assert R == RF, ('resultant factorization differs',R)

# Irreducibility of Q over F_5 by Rabin's criterion (prime divisors 2,3).
P=Poly(a,a,modulus=p)
def ppow_mod(base, exponent, mod):
    out=Poly(1,a,modulus=p)
    while exponent:
        if exponent & 1: out=(out*base).rem(mod)
        base=(base*base).rem(mod)
        exponent //= 2
    return out
for d in (2,3):
    assert gcd(Q,ppow_mod(P,5**(6//d),Q)-P).degree()==0
assert (ppow_mod(P,5**6,Q)-P).rem(Q).is_zero
assert gcd(Q,Q.diff()).degree()==0

# The reduced F_5[a]/(Q) field supplies exactly six parameters with b=Beta(a).
assert Poly(D.subs(b,Beta.as_expr()),a,modulus=p).rem(Q).is_zero
assert Poly(N.subs(b,Beta.as_expr()),a,modulus=p).rem(Q).is_zero
assert gcd(Q,Poly(S.subs(b,Beta.as_expr()),a,modulus=p)).degree()==0

# Elimination uniqueness: since this Groebner-polynomial has an a^6*b
# coefficient, Q(a)=0 forces b to have the displayed unique value.
G=groebner([D,N],b,a,modulus=p,order='lex')
rel=G.polys[-2].as_expr()  # linear in b, coefficient a^6
assert Poly(rel.coeff(b)-a**6,a,modulus=p).is_zero
assert Poly(rel.subs(b,Beta.as_expr()),a,modulus=p).rem(Q).is_zero

# Inspect every base-field parameter, independent of elimination.
specials=[]
for ai in range(5):
    for bi in range(5):
        subs={a:ai,b:bi}
        smooth=bool(int(S.subs(subs))%5)
        poly=Poly(f.subs(subs),x,modulus=p)
        assert smooth == (gcd(poly,poly.diff()).degree()==0)
        d=int(D.subs(subs))%5
        n=int(N.subs(subs))%5
        if smooth and d==0 and n==0: specials.append((ai,bi))
assert specials==[(3,2)]
for ai,bi in ((0,0),(2,1),(4,2)):
    assert int(D.subs({a:ai,b:bi}))%5==0
    assert int(N.subs({a:ai,b:bi}))%5==0
    assert int(S.subs({a:ai,b:bi}))%5==0

# Show no further b-roots over any algebraic extension at the special a-values.
for ai,expected_b in ((0,0),(2,1),(3,2),(4,2)):
    db=Poly(D.subs(a,ai),b,modulus=p)
    nb=Poly(N.subs(a,ai),b,modulus=p)
    common=gcd(db,nb)
    assert common.degree()>=1
    assert Poly(common.as_expr(),b,modulus=p).eval(expected_b)==0
    assert Poly(common.as_expr(),b,modulus=p).degree()==(3 if ai==0 else 1)

# Cartier block in the sole rational p-rank-zero case is square-zero.
B0=Matrix([[int(t.subs({a:3,b:2}))%5 for t in row] for row in [[u,h],[l,v]]])
assert all(int(t)%5==0 for t in B0*B0)

# Independent point enumeration on its smooth genus-four curve.
count=2  # monic polynomial of degree 10: two F_5-rational infinity points
for xi in range(5):
    rhs=int(f.subs({x:xi,a:3,b:2}))%5
    count += sum((yi*yi)%5==rhs for yi in range(5))
assert count==6
print('VERIFY_OK')
print('F5_rational_p_rank_zero_parameters',specials)
print('nontrivial_field_of_definition_degree',Q.degree())
print('C_3_2_F5_points',count)
