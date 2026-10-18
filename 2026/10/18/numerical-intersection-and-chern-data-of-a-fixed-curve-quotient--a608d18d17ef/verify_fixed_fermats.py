#!/usr/bin/env python3
"""Exact combinatorial cross-checks for diagonal complete-intersection involutions.

Only verifies finite cases. The all-parameter statements require the accompanying proofs.
"""
from math import comb
from itertools import combinations

def diagonal_ci_euler(t, s=0):
    # s=0: t quadrics in P^(2t-1); s>0: fixed t-quadric
    # complete intersection in P^(2t-s-1)
    n = 2*t-s
    d = t-s-1
    if d < 0: return 0
    coeff = sum(comb(n,j)*(-2)**(d-j)*comb(t+d-j-1,d-j) for j in range(d+1))
    return 2**t*coeff

def vandermonde_minor(vals):
    v=1
    for i in range(len(vals)):
        for j in range(i+1,len(vals)):
            v*=vals[j]-vals[i]
    return v

for t in range(3,9):
    cols=list(range(2*t))
    # A_{i,j}=j^i for i=0,...,t-1: all maximal minors nonzero.
    for subset in combinations(cols,t):
        assert vandermonde_minor(subset)!=0
    # Eliminate the column at j=0. Remaining projected columns are
    # (j,j^2,...,j^(t-1)); every t-1 of them are independent.
    for subset in combinations(cols[1:],t-1):
        assert all(x!=0 for x in subset) and vandermonde_minor(subset)!=0
    e0=diagonal_ci_euler(t)
    outputs=[]
    for s in range(1,t+1):
        f=diagonal_ci_euler(t,s)
        assert (e0+f)%2==0
        quot=(e0+f)//2
        outputs.append((s, f, quot))
        if s==t-1: assert f == 2**t
        if s==t: assert f == 0
    if t==3: assert (e0,outputs)==(24,[(1,-8,8),(2,8,16),(3,0,12)])
    if t==4: assert (e0,outputs)==(-128,[(1,80,-24),(2,-32,-80),(3,16,-56),(4,0,-64)])
    print('t=',t,'Y_euler=',e0,'s_fixed_quot_euler=',outputs)
print('VERIFY_OK exact_vandermonde_and_projected_rank_euler_profiles t=3..8')

# The dimension-three, two-coordinate sign involution case.
t=4
C_degree=2**t
C_genus=1+(t*2-(2*t-2))*C_degree//2  # adjunction: K_C=(2t-(2t-2))H=2H
assert C_genus==17
C_euler=2-2*C_genus
assert C_euler==-32
Y_euler=diagonal_ci_euler(t,0)
assert Y_euler==-128
Q_euler=(Y_euler+C_euler)//2
assert Q_euler==-80
# Blow-up smooth Y along a curve C: e(Bl_C Y)=e(Y)+e(C).
Bl_euler=Y_euler+C_euler
E_euler=2*C_euler
# Involution fixes entire exceptional, quotient ramifies on E.
Z_euler=(Bl_euler+E_euler)//2
assert (Bl_euler,E_euler,Z_euler)==(-160,-64,-112)
h11=2
h21=h11-Z_euler//2
assert (h11,h21)==(2,58)
# D=hyperplane descended to the quotient, E=exceptional divisor.
# q: Bl_C(Y)->Z is degree 2 and q^*E=2 E_Y.
H3=2**t
D3=H3//2
D2E=0
DE2=-2*C_degree
# E_Y^3=-deg(c1(N_{C/Y})), N=O_C(1)^2.
E3=-4*(2*C_degree)
assert (D3,D2E,DE2,E3)==(8,0,-32,-128)
# c2(T_Z).E = Euler(E)-E^3 by adjunction and c1(Z)=0.
c2E=E_euler-E3
# Holomorphic sections of D: six invariant linear coordinates.
h0_D=6
c2D=12*h0_D-2*D3
assert (c2D,c2E)==(56,64)
# CY3 Hirzebruch-Riemann-Roch: chi(D)=D^3/6+(c2.D)/12=6.
assert 2*D3+c2D==12*h0_D
print('VERIFY_OK CY3 Hodge=(2,58) cubic=(8,0,-32,-128) c2=(56,64) pi1=needs_proof')
