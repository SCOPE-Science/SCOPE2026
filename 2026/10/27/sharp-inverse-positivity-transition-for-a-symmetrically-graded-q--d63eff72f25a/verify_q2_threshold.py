#!/usr/bin/env python3
"""Exact symbolic certificate for the sharp three-cell-per-axis Q2 inverse-positivity threshold.

Requires Python 3.10+ and SymPy 1.11+. Run: python verify_q2_threshold.py
All arithmetic used for the mathematical certificate is rational/symbolic.
"""
import sympy as sp

r = sp.symbols('r', positive=True)
K = sp.zeros(5)
M = sp.zeros(5)
k_local = sp.Matrix([[7,-8,1],[-8,16,-8],[1,-8,7]]) / 3
m_local = [sp.Rational(1,6),sp.Rational(2,3),sp.Rational(1,6)]
for cell, h in enumerate([sp.Integer(1),r,sp.Integer(1)]):
    for a in range(3):
        i = 2*cell + a - 1
        if not (0 <= i < 5):
            continue
        M[i,i] += h*m_local[a]
        for b in range(3):
            j = 2*cell + b - 1
            if 0 <= j < 5:
                K[i,j] += k_local[a,b] / h
S = sp.kronecker_product(K,M) + sp.kronecker_product(M,K)
assert S == S.T

# Reflection parity diagonalizes the two-dimensional stiffness into four exact blocks.
E = sp.eye(5)
P = sp.Matrix.hstack(E[:,0]+E[:,4],E[:,1]+E[:,3],E[:,2],
                     E[:,0]-E[:,4],E[:,1]-E[:,3])
T = sp.kronecker_product(P,P)
D = T.T*S*T
groups = {}
for i in range(25):
    a,b = divmod(i,5)
    groups.setdefault((a >= 3,b >= 3),[]).append(i)
assert sorted(map(len,groups.values())) == [4,6,6,9]
for g1,I in groups.items():
    for g2,J in groups.items():
        if g1 != g2:
            assert all(sp.cancel(D[i,j]) == 0 for i in I for j in J)

inverse_blocks = sp.zeros(25)
for indices in groups.values():
    B = D.extract(indices,indices)
    Binv = B.inv(method='DM')
    assert all(sp.cancel((B*Binv-sp.eye(len(indices)))[i,j])==0 for i in range(len(indices)) for j in range(len(indices)))
    for a,i in enumerate(indices):
        for b,j in enumerate(indices):
            inverse_blocks[i,j] = Binv[a,b]
Green = T*inverse_blocks*T.T

# Symmetries of the graded square and Green-matrix symmetry give 55 entry classes.
transforms = [lambda a,b:(a,b),lambda a,b:(b,a),
              lambda a,b:(4-a,b),lambda a,b:(a,4-b),
              lambda a,b:(4-a,4-b),lambda a,b:(4-b,a),
              lambda a,b:(b,4-a),lambda a,b:(4-b,4-a)]
seen = set()
representatives = []
for i in range(25):
    for j in range(25):
        if (i,j) in seen:
            continue
        x,y=divmod(i,5);u,v=divmod(j,5)
        orbit=set()
        for tr in transforms:
            a,b=tr(x,y);c,d=tr(u,v)
            orbit.add((5*a+b,5*c+d))
            orbit.add((5*c+d,5*a+b))
        for a,b in orbit:
            assert sp.cancel(Green[i,j]-Green[a,b])==0
        seen.update(orbit)
        representatives.append((i,j))
assert len(seen)==625 and len(representatives)==55

lower=sp.Rational(41999,10000)
upper=sp.Rational(21,5)
witness=(1,3)
zero_changes=0
one_change=0
for i,j in representatives:
    num,den=sp.fraction(sp.cancel(Green[i,j]))
    numer=sp.Poly(num,r)
    denom=sp.Poly(den,r)
    assert all(c >= 0 for c in denom.all_coeffs()) and denom.LC()>0
    assert numer.eval(0)>0
    signs=[sp.sign(c) for c in numer.all_coeffs() if c]
    changes=sum(signs[k]!=signs[k-1] for k in range(1,len(signs)))
    assert changes<=1
    if changes==0:zero_changes+=1
    else:one_change+=1
    if (i,j)==witness:
        assert numer.eval(lower)>0 and numer.eval(upper)<0 and changes==1
    else:
        assert numer.eval(upper)>0
assert (zero_changes,one_change)==(45,10)

Q=(192*r**13+2576*r**12+13108*r**11+18631*r**10
   -124198*r**9-830730*r**8-2554448*r**7-4960645*r**6
   -6543798*r**5-5928564*r**4-3589936*r**3-1356656*r**2
   -278880*r-22464)
F=(12*r**5+81*r**4+200*r**3+265*r**2+180*r+44)
H=(48*r**7+488*r**6+2003*r**5+4420*r**4+5799*r**3
   +4500*r**2+1792*r+216)
G13=-3*Q/(2*(r+2)**2*(4*r+3)*F*H)
assert sp.cancel(Green[1,3]-G13)==0
assert sp.cancel(Green[1,3].subs(r,sp.Integer(5))+
                 sp.Rational(29159657937,68799433880114))==0
assert Q.subs(r,lower)<0 and Q.subs(r,upper)>0
assert sum(sp.sign(a)!=sp.sign(b) for a,b in zip(
  [sp.sign(c) for c in sp.Poly(Q,r).all_coeffs() if c][:-1],
  [sp.sign(c) for c in sp.Poly(Q,r).all_coeffs() if c][1:]))==1
print('PASS: 25-by-25 exact stiffness inverse, 55 symmetry classes,')
print('45 zero-sign-change polynomials and 10 one-sign-change polynomials.')
print('Unique sharp threshold lies in (41999/10000,21/5).')
print('At r=5 the sharp witness inverse entry is -29159657937/68799433880114.')
