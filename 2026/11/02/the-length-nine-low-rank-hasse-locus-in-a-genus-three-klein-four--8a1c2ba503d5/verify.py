"""Exact finite-characteristic proof checks for a genus-three curve family.

Usage: python verify.py
Dependency: sympy >= 1.13, < 2
All symbolic identities are over F_7; integer discriminants are checked over Z.
"""
import sympy as sp

x, a, b, z = sp.symbols('x a b z')
p = 7
f = x**8 + a*x**6 + b*x**4 + a*x**2 + 1
D = (2*a-b-2)*(2*a+b+2)*(a*a-4*b+8)
P = (a-3)*(a*a-a-b)
Q = (a+3)*(a*a+a-b)
R = (b+1)*(b*b-b-a*a)
A = a*(a*a-b+3)
E = 3*(a*a+b)

def mod7(e):
    return sp.Poly(sp.expand(e),a,b,modulus=7).as_expr()

def ev7(e, aa, bb):
    return int(sp.expand(e).subs({a:aa,b:bb})) % 7

# Smoothness and genus criterion: nonzero octic discriminant.
disc = sp.discriminant(f,x)
assert sp.expand(disc-256*(2*a-b-2)**2*(2*a+b+2)**2*(a*a-4*b+8)**4) == 0

# The Hasse-Witt coefficient matrix has (i,j) entry [x^(7i-j)]f^3.
coeffs = sp.Poly(sp.expand(f**3),x)
H = sp.Matrix([[coeffs.nth(7*i-j) for j in (1,2,3)] for i in (1,2,3)]).applyfunc(mod7)
claimed = sp.Matrix([[A,0,E],[0,R,0],[E,0,A]]).applyfunc(mod7)
assert H == claimed
assert mod7(A+E-P)==0 and mod7(A-E-Q)==0

# The nontrivial two-by-two minors of the diagonalized matrix generate the
# rank-at-most-one determinantal ideal J=(PQ,PR,QR).
J = [P*Q,P*R,Q*R]
G = sp.groebner(J+[z*D-1],z,b,a,order='lex',modulus=7)
GB = [sp.Poly(e.as_expr(),b,a,modulus=7) for e in G.polys if not e.as_expr().has(z)]
assert len(GB)==3
expected = [-2*a*a+b*b, 2*a**5+a**3*b+3*a**3-2*a*b, a**6+a**4+a**2]
assert [sp.Poly(mod7(g.as_expr()-e),a,b,modulus=7).is_zero for g,e in zip(GB,expected)]==[True]*3
lm = {g.LM(order='lex').exponents for g in GB}
assert lm == {(2,0),(1,3),(0,6)}
standard = {(u,v) for u in range(2) for v in range(6) if all(not (u>=i and v>=j) for i,j in lm)}
assert len(standard) == 9

# Complete geometric support is certified by the length-nine quotient:
# six distinct transverse ordinary points plus the origin of length three.
points = [(0,0),(3,5),(4,5),(3,2),(4,2),(5,6),(2,6)]
for aa,bb in points:
    values = [ev7(e,aa,bb) for e in (P,Q,R)]
    assert values.count(0)>=2 and ev7(D,aa,bb)!=0
    if (aa,bb)!=(0,0):
        vanishing=[e for e,v in zip((P,Q,R),values) if v==0]
        assert len(vanishing)==2
        J2 = sp.Matrix([[sp.diff(e,a),sp.diff(e,b)] for e in vanishing])
        assert ev7(J2.det(),aa,bb)!=0

# At (0,0), the lowest homogeneous parts of P,Q,R are respectively
# 3(a+b), 3(a-b), -b. Their three pairwise products span m^2/m^3.
linear = [3*(a+b),3*(a-b),-b]
quad = [sp.expand(linear[i]*linear[j]) for i,j in ((0,1),(0,2),(1,2))]
quad_coeff=sp.Matrix([[sp.Poly(e,a,b).coeff_monomial(mon) for mon in (a*a,a*b,b*b)] for e in quad])
assert int(quad_coeff.det())%7 != 0
# Each nonzero point contributes length 1 and the origin contributes
# at least 3, exhausting the total quotient length 9.

# As an independent finite-field check, list all F_7-parameter points
# and their ranks; this is not used to certify completeness over k-bar.
counts = {0:0,1:0,2:0,3:0}
rankone=[]
for aa in range(7):
    for bb in range(7):
        if ev7(D,aa,bb)==0:
            continue
        rank = sum(ev7(q,aa,bb)!=0 for q in (P,Q,R))
        counts[rank]+=1
        if rank==1:rankone.append((aa,bb))
assert sorted(rankone)==sorted(points[1:])
assert counts[0]==1 and counts[1]==6
print('VERIFY_OK: discriminant, exact 3x3 Hasse-Witt, eigenfactors P,Q,R,')
print('          saturated determinantal quotient length 9, six transverse')
print('          rank-one F7 points plus a length-three superspecial origin.')
print('F7 smooth-parameter rank counts:',counts)
