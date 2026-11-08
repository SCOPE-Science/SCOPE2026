"""Exact arithmetic checks for a sharp affine spline projection on symmetric metric double stars.
Run: python verify_double_star_projection.py (requires SymPy >=1.12).
All universal mathematical steps are proved in RESULT.md; this script independently
checks finite assembled matrices and symbolically verifies the polynomial identities.
"""
from fractions import Fraction as F
import sympy as sp

D,T=sp.symbols('d t',positive=True)
H=sp.Rational(3,2)*D+2*T
U=sp.factor(6*H/(H*H-T*T))
V=sp.factor(6*T/(H*H-T*T))
ABS_PAIR=lambda a,b:(a*a+b*b)/(2*(a+b))
LEAF=sp.factor(ABS_PAIR(3+U/4,U/2)+(D-1)*5*U/24+D*5*V/24+T*ABS_PAIR(U/2,V/2))
HUB=sp.factor(D*5*(U+V)/12+T*ABS_PAIR(U,V))

# Explicit positive-coefficient certificate for the strict leaf/hub norm gap.
X=sp.symbols('x',nonnegative=True)
Qx=(9*X**5+81*X**4+288*X**3+504*X**2+432*X+144
    +T*(60*X**4+420*X**3+1080*X**2+1200*X+480)
    +T**2*(162*X**3+842*X**2+1424*X+776)
    +T**3*(216*X**2+752*X+640)
    +T**4*(136*X+240)+32*T**5)
DEN=3*(D+2*T)**2*(3*D+2*T)*(3*D**2+8*D*T+3*D+4*T**2+4*T)
assert sp.cancel((LEAF-HUB)*DEN-2*Qx.subs(X,D-2))==0
assert all(v>0 for v in sp.Poly(Qx,X,T).coeffs())
print('SYMBOLIC_LEAF_DOMINANCE_COEFFICIENT_CERTIFICATE_OK',len(sp.Poly(Qx,X,T).terms()))

# Exact crossover with 7/3 is governed by a quartic.
CROSS=(4*(D-8)*T**4+4*D*(3*D-25)*T**3+D**2*(11*D-109)*T**2
       +3*D**3*(D-17)*T-9*D**4)
assert sp.cancel((LEAF-sp.Rational(7,3))*DEN-4*CROSS)==0
print('SYMBOLIC_SEVEN_THIRDS_CROSSOVER_IDENTITY_OK')

# The derivative has a single positive root exactly in degrees >=9.
COEFF=[
  108*D**6*(D**2+6*D+1),
  288*D**5*(2*D**2+17*D+1),
  24*D**4*(35*D**2+682*D-1),
  -48*D**3*(11*D**2-662*D+15),
  -64*D**2*(42*D**2-601*D+12),
  -128*D*(23*D**2-223*D+2),
  -128*D*(11*D-92),
  -256*(D-8)
]
POLY=sum(c*T**j for j,c in enumerate(COEFF))
DER_DEN=3*(D+2*T)**3*(3*D+2*T)**2*(3*D**2+8*D*T+3*D+4*T**2+4*T)**2
assert sp.cancel(sp.diff(LEAF,T)*DER_DEN-POLY)==0
for d in range(2,201):
    signs=[sp.sign(c.subs(D,d)) for c in COEFF]
    nonzero=[v for v in signs[::-1] if v]
    transitions=sum(a!=b for a,b in zip(nonzero,nonzero[1:]))
    assert transitions==(0 if d<=8 else 1)
    assert signs[0]>0
    assert (all(v>=0 for v in signs) if d<=8 else signs[-1]<0)
print('SYMBOLIC_DERIVATIVE_IDENTITY_AND_DEGREE_SIGN_PATTERN_OK',199)

# The independently assembled 2d+2 by 2d+2 Gram matrix tests every vertex.
def int_abs(a,b):
    a,b=F(a),F(b)
    if a*b>=0:return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))

def direct(d,t):
    n=2*d+2
    edges=[(0,j,F(1)) for j in range(2,d+2)]+[(1,j,F(1)) for j in range(d+2,2*d+2)]+[(0,1,t)]
    M=sp.zeros(n)
    for v,w,l in edges:
        M[v,v]+=l/sp.Integer(3);M[w,w]+=l/sp.Integer(3)
        M[v,w]+=l/sp.Integer(6);M[w,v]+=l/sp.Integer(6)
    MI=M.inv()
    norms=[]
    for k in range(n):
        norms.append(sum(l*int_abs(MI[k,v],MI[k,w]) for v,w,l in edges))
    return norms

count=0
for degree in [2,3,4,5,7,9,10]:
 for bridge in [F(1,20),F(2,5),F(1),F(3),F(17,2)]:
    norms=direct(degree,bridge)
    expected_leaf=F(LEAF.subs({D:degree,T:sp.Rational(bridge.numerator,bridge.denominator)}))
    expected_hub=F(HUB.subs({D:degree,T:sp.Rational(bridge.numerator,bridge.denominator)}))
    assert norms[0]==norms[1]==expected_hub
    assert all(x==expected_leaf for x in norms[2:])
    assert expected_leaf>expected_hub
    count+=1
print('INDEPENDENT_EXACT_GRAM_INVERSION_AND_EDGE_KERNELS_OK',count)
print('ALL_SYMMETRIC_DOUBLE_STAR_PROJECTION_CHECKS_OK')
