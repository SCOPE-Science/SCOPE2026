#!/usr/bin/env python3
"""Exact integral and equivariant homology of the ordinary matching complex of the three-cube.
Requires Python 3.10+ and SymPy 1.10+. No files or network are read.
"""
from itertools import combinations, permutations
from sympy import Matrix, zeros, eye

V = range(8)
EDGES = sorted((v, v ^ (1 << j)) for v in V for j in range(3) if v < (v ^ (1 << j)))
F = {d: [c for c in combinations(range(12), d + 1)
         if len({v for i in c for v in EDGES[i]}) == 2 * (d + 1)]
     for d in range(4)}
I = {d: {s: i for i, s in enumerate(F[d])} for d in F}
assert [len(F[d]) for d in range(4)] == [12, 42, 44, 9]

def boundary(d):
    B = zeros(len(F[d-1]), len(F[d]))
    for j, simplex in enumerate(F[d]):
        for i in range(d + 1):
            B[I[d - 1][simplex[:i] + simplex[i+1:]], j] = (-1) ** i
    return B

D1, D2, D3 = (boundary(d) for d in (1, 2, 3))
assert D1 * D2 == zeros(12, 44) and D2 * D3 == zeros(42, 9)
assert [B.rank() for B in (D1, D2, D3)] == [11, 31, 9]
# A 31 x 31 unit minor exhibits the integral kernel of D2 without denominators.
ROWS = [0,1,2,3,4,5,7,8,9,10,11,12,14,15,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,35,36]
COLS = list(range(30)) + [31]
U = D2.extract(ROWS, COLS)
assert U.det() == -1
FREE = [j for j in range(44) if j not in COLS]
assert FREE == [30,32,33,34,35,36,37,38,39,40,41,42,43]
INV = U.inv()
K = zeros(44, 13)
for h, j in enumerate(FREE):
    K[j,h] = 1
    vals = -INV * D2.extract(ROWS, [j])
    for i, c in enumerate(COLS): K[c,h] = vals[i]
assert D2 * K == zeros(42,13)
# The nine boundaries inside ker(D2) are primitive by a 9 x 9 unit minor.
T = D3.extract(FREE, range(9))
TROWS = [0,1,4,5,8,9,10,11,12]
assert abs(T.extract(TROWS, range(9)).det()) == 1
Q = zeros(4, 13)
Q[0,2] = 1
Q[1,1] = Q[1,3] = 1
Q[2,6] = 1
Q[3,0] = Q[3,7] = 1
assert Q*T == zeros(4,9)
BASIS_INDICES = [2,3,6,7]
assert Q.extract(range(4), BASIS_INDICES) == eye(4)
# Thus Q identifies H2(K;Z) with Z^4 and detects each basis cycle K[:,BASIS_INDICES[i]].

def bit(v, i): return (v >> i) & 1

def action_on_edges(p, t):
    vp = [t ^ sum(bit(v, i) << p[i] for i in range(3)) for v in V]
    edge_perm = [EDGES.index(tuple(sorted(vp[v] for v in e))) for e in EDGES]
    return vp, edge_perm

def simplicial_sign(z):
    return (-1) ** sum(z[i] > z[j] for i in range(len(z)) for j in range(i+1,len(z)))

def C_action(d, ep):
    A=zeros(len(F[d]),len(F[d]))
    for i, s in enumerate(F[d]):
        z=[ep[e] for e in s]
        A[I[d][tuple(sorted(z))],i]=simplicial_sign(z)
    return A

def diagonals_perm(vp):
    diagonals=[frozenset((v,v^7)) for v in range(4)]
    return tuple(diagonals.index(frozenset((vp[v],vp[v^7]))) for v in range(4))

def parity_perm(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

A2 = []
for p in permutations(range(3)):
    for t in range(8):
        vp,ep=action_on_edges(p,t)
        A=C_action(2,ep)
        action=Q * (A * K).extract(FREE,BASIS_INDICES)
        assert all(x.q==1 for x in action)
        chi= -1 + sum((-1)**d * sum(C_action(d,ep)[i,i] for i in range(len(F[d]))) for d in range(4))
        b=diagonals_perm(vp)
        eps=(-1)**sum(bit(t,i) for i in range(3))
        expected=parity_perm(b)*(sum(i==b[i] for i in range(4))-1)+eps
        assert chi == expected == action.trace(), (p,t,chi,expected,action.trace())
        assert action.det() in (1,-1)
        A2.append((p,t,action))
        if p==(0,1,2) and t==7:
            J=action

assert len(A2)==48
assert J==Matrix([[0,0,1,0],[1,1,-1,0],[1,0,0,0],[0,0,0,1]])
assert J*J==eye(4)
# Both eigensublattices are saturated: all solutions over Z follow directly from Jv=+/-v.
PLUS=Matrix.hstack(Matrix([0,1,0,0]),Matrix([1,0,1,0]),Matrix([0,0,0,1]))
MINUS=Matrix([1,-1,-1,0])
assert J*PLUS==PLUS and J*MINUS==-MINUS
assert abs(Matrix.hstack(PLUS,MINUS).det())==2
# Every even-parity translation automorphism fixes the minus generator.
assert all(a*MINUS==MINUS for p,t,a in A2 if (t.bit_count()%2)==0)
assert all(a*MINUS==-MINUS for p,t,a in A2 if (t.bit_count()%2)==1)
assert Matrix.vstack(*[a-eye(4) for p,t,a in A2]).rank() == 4
assert Matrix.vstack(*[a-eye(4) for p,t,a in A2 if t.bit_count()%2 == 0]).rank() == 3
# The central eigensublattices have ranks 3 and 1; their direct sum has index 2.
print('VERIFIED f_vector=(12,42,44,9), boundary_ranks=(11,31,9)')
print('VERIFIED integral_H2=Z^4, all_other_reduced_integral_homology=0')
print('VERIFIED group_order=48, rational_character=sign(body_diagonals)*(fixed_diagonals-1)+translation_parity')
print('VERIFIED central_involution_eigenranks=(3,1), integral_sum_index=2')
print('VERIFIED full_group_fixed_H2=0, even_translation_kernel_fixed_H2=Z (rank 1)')
print('VERIFY_OK')
