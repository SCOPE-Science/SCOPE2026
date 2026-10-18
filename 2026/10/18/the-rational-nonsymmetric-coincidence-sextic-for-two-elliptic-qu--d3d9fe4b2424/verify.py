"""Exact coefficient checks for a genus-three elliptic-quotient coincidence locus.
Requires SymPy. All computations use exact rational/algebraic arithmetic.
"""
import sympy as S

a,b,s,p,z,u,v,T,U=S.symbols('a b s p z u v T U')
A=(a-2)*(b-2);B=(a+2)*(b+2);D=(a-b)**2
H=S.expand(D**3-768*D*A*B-4096*A*B*(A+B))
F=5184*p**3+(720*s*s+73728)*p*p+(12*s**4-14336*s*s+344064)*p-s**6-3072*s**4-118784*s*s+524288
assert S.expand(H+F.subs({s:a+b,p:a*b}))==0
assert S.expand(B*(D+16*A)**3-A*(D+16*B)**3-4*(a+b)*H)==0

def quartic_invariants(c4,c3,c2,c1,c0):
    I=S.expand(12*c4*c0-3*c3*c1+c2*c2)
    J=S.expand(72*c4*c2*c0+9*c3*c2*c1-27*c4*c1*c1-27*c3*c3*c0-2*c2**3)
    return I,J

def j_from_coeff(coefs):
    I,J=quartic_invariants(*coefs)
    return S.cancel(1728*4*I**3/(4*I**3-J**2))

j_minus=j_from_coeff((1,0,a+b-4,0,A))
j_plus=j_from_coeff((1,0,a+b+4,0,B))
assert S.cancel(j_minus-16*(D+16*A)**3/(D*D*A))==0
assert S.cancel(j_plus-16*(D+16*B)**3/(D*D*B))==0
j_r=lambda r:16*(r*r+14*r+1)**3/(r*(r-1)**4)
assert S.cancel(j_minus-j_r((a-2)/(b-2)))==0
assert S.cancel(j_plus-j_r((a+2)/(b+2)))==0

G=(T-2)**2*(U-2)**2-768*(T-2)*(U-2)-4096*(T+U-4)
K=S.cancel(u*u*v*v*G.subs({T:u+1/u,U:v+1/v}))
assert S.Poly(K,v).degree()==4
assert S.Poly(K,u).degree()==4
assert S.factor(j_r(u)-j_r(v)-16*(u-v)*(u*v-1)*K/(u*v*(u-1)**4*(v-1)**4))==0
q=(z+S.I)/(z-S.I)
assert S.cancel(j_r(z**4)-j_r(q**4))==0
assert S.cancel(K.subs({u:z**4,v:q**4}))==0
# Four fourth-root preimages of a generic u have distinct v values.
v_at=[S.factor(q.subs(z,w)**4) for w in (2,2*S.I,-2,-2*S.I)]
assert len(set(v_at))==4
# The rational inverse from ratios u,v to the original ordered parameters.
inv_b=2*(u+v-2)/(u-v)
inv_a=S.cancel(u*inv_b+2*(1-u))
assert S.factor((inv_a-2)/(inv_b-2)-u)==0
assert S.factor((inv_a+2)/(inv_b+2)-v)==0
# Explicit smooth nonsymmetric CM coincidence witness.
ps=-S.Rational(92,9);ss=S.Integer(4)
aa=2+8*S.sqrt(2)/3; bb=2-8*S.sqrt(2)/3
assert S.simplify(aa+bb-ss)==S.simplify(aa*bb-ps)==0
assert S.simplify(H.subs({a:aa,b:bb}))==0
assert aa!=bb and all(S.simplify(x-k)!=0 for x in (aa,bb) for k in (-2,2))
assert S.simplify(j_minus.subs({a:aa,b:bb}))==1728
assert S.simplify(j_plus.subs({a:aa,b:bb}))==1728
j_sigma=j_from_coeff((1,a+b,a*b+2,a+b,1))
assert S.simplify(j_sigma.subs({a:aa,b:bb}))==-S.Rational(8000,81)
print('VERIFY_OK: quartic j formulas; complete coincidence factorization; bidegree-(4,4) off-diagonal relation; birational parametrization; smooth nonsymmetric witness')
