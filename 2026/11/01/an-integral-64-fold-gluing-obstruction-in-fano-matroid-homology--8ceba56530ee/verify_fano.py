"""Exact integral equivariant-homology calculation for the seven-point Fano matroid.

Uses Python >=3.9 and SymPy; all finite inputs are constructed here.
"""
from collections import Counter
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
import json
import pathlib

V = tuple(range(1,8))
EDGES = tuple(combinations(V,2)); EI = {e:i for i,e in enumerate(EDGES)}
TRIS = tuple(t for t in combinations(V,3) if t[0]^t[1]^t[2] != 0)
TI = {t:i for i,t in enumerate(TRIS)}
assert len(EDGES) == 21 and len(TRIS) == 28
B = Matrix.zeros(21,28)
for j,t in enumerate(TRIS):
    for k in range(3):
        B[EI[t[:k] + t[k+1:]],j] = (-1)**k
PIVOTS = tuple(B.rref()[1])
assert PIVOTS == (0,1,2,3,4,5,6,7,8,9,10,11,12,16,19)
P = B[:,list(PIVOTS)]
assert P.rank() == 15
S = smith_normal_form(P, domain=ZZ)
assert [abs(int(S[i,i])) for i in range(15)] == [1]*15
FREE = tuple(i for i in range(28) if i not in PIVOTS)
Z = Matrix.zeros(28,13)
for k,j in enumerate(FREE):
    v,params = P.gauss_jordan_solve(-B[:,j])
    assert params.rows == 0 and all(int(w)==w for w in v)
    for i,ii in enumerate(PIVOTS): Z[ii,k]=v[i]
    Z[j,k] = 1
assert B*Z == Matrix.zeros(21,13)

def group_elements():
    out=[]
    for a in V:
        for b in V:
            if b==a: continue
            for c in V:
                if c in (a,b,a^b):continue
                out.append(tuple((a if x&1 else 0) ^ (b if x&2 else 0) ^ (c if x&4 else 0) for x in V))
    assert len(out)==168 and len(set(out))==168
    return tuple(out)
G = group_elements(); E = tuple(V)
def multiply(g,h): return tuple(g[h[i]-1] for i in range(7))
def inverse(g): return tuple(g.index(v)+1 for v in V)
def gorder(g):
    x=E
    for k in range(1,9):
        x=multiply(x,g)
        if x==E:return k
    raise AssertionError('bad group order')
def perm_type(g):
    seen=set();cy=[]
    for v in V:
        if v not in seen:
            w=v;n=0
            while w not in seen:
                seen.add(w);n+=1;w=g[w-1]
            cy.append(n)
    return tuple(sorted(cy))
def action(g):
    M = Matrix.zeros(28,28)
    for k,t in enumerate(TRIS):
        u=tuple(g[v-1] for v in t)
        inversions=sum(u[i]>u[j] for i in range(3) for j in range(i+1,3))
        M[TI[tuple(sorted(u))],k] = -1 if inversions%2 else 1
    A=M*Z
    assert B*A==Matrix.zeros(21,13)
    return A[list(FREE),:]
# Derive the 7-dimensional character by the eight Sylow-seven subgroups.
G7=[g for g in G if gorder(g)==7]
SYLOW=set()
for g in G7:
    powers={E}; x=E
    for i in range(1,7):
        x=multiply(x,g);powers.add(x)
    assert len(powers)==7
    SYLOW.add(frozenset(powers))
assert len(SYLOW)==8 and len(G7)==48
T = tuple(map(frozenset,SYLOW))

def chi7(g):
    inv=inverse(g)
    fixed=sum(1 for sub in T if frozenset(multiply(multiply(g,h),inv) for h in sub)==sub)
    return fixed-1

cycle_counts=Counter(); character={}; char7={}
C=Matrix.zeros(13,13)
for g in G:
    typ=perm_type(g)
    cycle_counts[typ]+=1
    A=action(g)
    chi=int(A.trace())
    if typ in character:assert character[typ]==chi
    character[typ]=chi
    ch7=chi7(g)
    if typ in char7:assert char7[typ]==ch7
    char7[typ]=ch7
    C += ch7*A
assert cycle_counts == Counter({(1,1,1,1,1,1,1):1,(1,1,1,2,2):21,(1,3,3):56,(1,2,4):42,(7,):48})
assert character == {(1,1,1,1,1,1,1):13,(1,1,1,2,2):-3,(1,3,3):1,(1,2,4):1,(7,):-1}
assert char7 == {(1,1,1,1,1,1,1):7,(1,1,1,2,2):-1,(1,3,3):1,(1,2,4):-1,(7,):0}
assert sum(cycle_counts[t]*char7[t]**2 for t in cycle_counts)==168
assert sum(cycle_counts[t]*character[t]*char7[t] for t in cycle_counts)==168
# Independent character check from the reduced Lefschetz trace of finite face permutations.
for g in G:
    fixed_v=sum(1 for v in V if g[v-1]==v)
    fixed_e=sum((-1 if g[a-1]>g[b-1] else 1) for a,b in EDGES if tuple(sorted((g[a-1],g[b-1])))==(a,b))
    fixed_t=0
    for t in TRIS:
        u=tuple(g[v-1] for v in t)
        if tuple(sorted(u))==t:
            inv=sum(u[i]>u[j] for i in range(3) for j in range(i+1,3))
            fixed_t+=(-1 if inv%2 else 1)
    assert int(action(g).trace()) == fixed_v-fixed_e+fixed_t-1

assert C*C==24*C and C.rank()==7 and (24*Matrix.eye(13)-C).rank()==6
D=smith_normal_form(C,domain=ZZ)
nonzero=[abs(int(D[i,i])) for i in range(13) if D[i,i]]
assert nonzero==[6,6,6,24,24,24,24]
quotient=[24//d for d in nonzero if d!=24]
assert quotient==[4,4,4]
RESULT={
 'vertices':7,'edges':21,'triangles':28,'boundary_rank':15,
 'pivot_triangle_indices_zero_based':list(PIVOTS),
 'boundary_pivot_smith_factors':[1]*15,
 'top_homology_rank':13,'automorphism_group_order':168,
 'permutation_class_counts':{','.join(map(str,k)):int(v) for k,v in sorted(cycle_counts.items())},
 'top_homology_character':{','.join(map(str,k)):int(v) for k,v in sorted(character.items())},
 'sylow_seven_subgroup_count':len(SYLOW),
 'seven_dimensional_character':{','.join(map(str,k)):int(v) for k,v in sorted(char7.items())},
 'projector_scalar':24,'central_matrix_smith_factors':nonzero,
 'integral_gluing_group_invariants':quotient,'integral_gluing_index':64,
}
if __name__=='__main__':
    fp=pathlib.Path(__file__).with_name('certificate.json')
    if fp.exists():
        expected=json.loads(fp.read_text('utf-8'))
        assert expected==RESULT,'certificate mismatch'
    print('FANO_INTEGRAL_GLUING_VERIFY_OK')
    print(json.dumps(RESULT,sort_keys=True))
