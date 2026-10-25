"""Exact combinatorial and rational-Picard checks for the Segre cubic forms."""
from itertools import combinations, permutations, product
from math import factorial
import sympy as sp

V = tuple(range(6))
M = tuple(sorted(set(tuple(sorted(tuple(sorted(pair)) for pair in pairing))
                     for pairing in ([(a,b),(c,d),(e,f)]
                     for a,b,c,d,e,f in permutations(V)))))
assert len(M) == 15
N = tuple(frozenset(a) for a in combinations(V,3) if 0 in a)
assert len(N) == 10

def node_of(A):
    A = frozenset(A)
    return A if 0 in A else frozenset(set(V) - A)

def matchings_at_node(A):
    B = sorted(set(V)-set(A))
    aa = sorted(A)
    return tuple((tuple(sorted(tuple(sorted((aa[i], b[i]))) for i in range(3))),
                   sum(b[i]>b[j] for i in range(3) for j in range(i+1,3))%2)
                 for b in permutations(B))

node_match = {A:matchings_at_node(A) for A in N}
for A, pairs in node_match.items():
    assert len(pairs) == 6 and sorted(x[1] for x in pairs)==[0,0,0,1,1,1]
R = tuple((A,p) for A in N for p in range(2))

def image_matching(m, perm):
    return tuple(sorted(tuple(sorted((perm[i],perm[j]))) for i,j in m))

def perm_for(cyc):
    perm = list(V); s=0
    for d in cyc:
        xs = list(range(s,s+d)); s+=d
        for i,j in zip(xs, xs[1:]+xs[:1]):perm[i]=j
    assert s == 6
    return tuple(perm)

def counts(cyc):
    perm=perm_for(cyc)
    m_fixed=sum(image_matching(m,perm)==m for m in M)
    n_fixed=sum(node_of(perm[i] for i in A)==A for A in N)
    r_fixed=0
    for A,par in R:
        newA = node_of(perm[i] for i in A)
        inp = (x for x,s in node_match[A] if s==par)
        inp_mapped={image_matching(x,perm) for x in inp}
        out_mapped={x for x,s in node_match[newA] if s==0}
        if inp_mapped==out_mapped:
            out_par=0
        else:
            assert inp_mapped=={x for x,s in node_match[newA] if s==1}
            out_par=1
        r_fixed += (newA==A and out_par==par)
    return m_fixed,n_fixed,r_fixed

TYPES = [
 (1,1,1,1,1,1), (2,1,1,1,1), (2,2,1,1), (2,2,2),
 (3,1,1,1), (3,2,1), (3,3), (4,1,1), (4,2), (5,1), (6,)
]
EXPECT = [(6,-4),(0,4),(2,0),(4,0),(0,-1),(0,1),(3,2),(2,2),(0,2),(1,1),(1,0)]
for typ,(a,b) in zip(TYPES, EXPECT):
    fm,fn,fr = counts(typ)
    aa,bb = 1+fm-fn,1+fm-fr
    assert (aa,bb)==(a,b),(typ,(fm,fn,fr),(a,b))
    assert fr%2==0
    print(f"{str(typ):20s} M={fm:2d} N={fn:2d} R={fr:2d} q2={aa:2d} q={bb:2d}")

# Keel's full boundary divisor presentation for Pic(Mbar_0,6).
D = [frozenset(s) for n in (2,3) for s in combinations(V,n) if n==2 or 0 in s]
D.sort(key=lambda a:(len(a),tuple(sorted(a))))
assert len(D)==25
index={s:i for i,s in enumerate(D)}
def d_index(S):
    s=frozenset(S)
    return index[s if s in index else frozenset(set(V)-s)]

def keel_rel(a,b,c,d):
    v=sp.zeros(25,1)
    for j,S in enumerate(D):
        if (a in S)==(b in S) and (c in S)==(d in S) and (a in S)!=(c in S):
            v[j]+=1
        if (a in S)==(c in S) and (b in S)==(d in S) and (a in S)!=(b in S):
            v[j]-=1
    return v
relations=[]
for a,b,c,d in combinations(V,4):
    relations.extend((keel_rel(a,b,c,d),keel_rel(a,b,d,c)))
REL=sp.Matrix.hstack(*relations)
assert REL.rank()==9
B=REL.columnspace()
assert len(B)==9
RB=sp.Matrix.hstack(*B)
plane_basis=sp.Matrix.hstack(*(sp.eye(25)[:,j] for j,S in enumerate(D) if len(S)==2))
exc_sum=sum((sp.eye(25)[:,j] for j,S in enumerate(D) if len(S)==3),sp.zeros(25,1))
assert sp.Matrix.hstack(RB,plane_basis).rank()==24
assert sp.Matrix.hstack(RB,plane_basis,exc_sum).rank()==25
print('KEEL_OK: 25 boundary classes, 9 relations, 15 plane classes plus one exceptional sum span rank 16')
print('VERIFY_OK: 11 arithmetic point-count profiles, 15 matchings, 10 nodes, 20 oriented rulings')
