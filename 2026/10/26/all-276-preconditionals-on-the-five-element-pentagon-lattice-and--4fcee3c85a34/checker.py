"""Self-contained exact check of the five-element pentagon preconditional census.
Run with Python 3.10+: python checker.py. No external dependencies.
"""
from itertools import product
from collections import Counter

V = range(5)  # 0 < a < c < 1, 0 < b < 1 (0,a,b,c,1)
ORDER = {(x,x) for x in V} | {(0,x) for x in V} | {(x,4) for x in V} | {(1,3)}
def le(x,y): return (x,y) in ORDER
MEET = {(x,y): next(z for z in V if le(z,x) and le(z,y)
        and all(z == w or not le(z,w) or not (le(w,x) and le(w,y)) for w in V))
        for x in V for y in V}
JOIN = {(x,y): next(z for z in V if le(x,z) and le(y,z)
        and all(z == w or not le(w,z) or not (le(x,w) and le(y,w)) for w in V))
        for x in V for y in V}

def direct_axioms(A):
    if any(not le(A[4][x],x) for x in V): return False  # P1
    if any(not le(MEET[a,b],A[a][b]) for a in V for b in V): return False  # P2
    if any(not le(A[a][b],A[a][MEET[a,b]]) for a in V for b in V): return False  # P3
    if any(not le(A[a][MEET[b,c]],A[a][b]) for a in V for b in V for c in V): return False  # P4
    if any(not le(A[a][A[MEET[a,b]][c]],A[MEET[a,b]][c])
           for a in V for b in V for c in V): return False  # P5
    return True

def row_candidates(a):
    sections=sorted({MEET[a,b] for b in V})
    for assignment in product(V, repeat=len(sections)):
        m=dict(zip(sections,assignment))
        row=tuple(m[MEET[a,b]] for b in V)
        if all(le(MEET[a,b],row[b]) for b in V) and all(
             not le(b,c) or le(row[b],row[c]) for b in V for c in V) and (a!=4 or row==tuple(V)):
            yield row

rows={a:sorted(set(row_candidates(a))) for a in V}
assert [len(rows[a]) for a in V] == [5,10,7,15,1]
assert rows[4] == [tuple(V)]
raw=tuple(product(*(rows[a] for a in V)))
assert len(raw)==5250
# Independent direct P1--P5 evaluation (not reduced P5).
accepted={p for p in raw if direct_axioms(p)}
assert len(accepted)==276
# Exact structural row-normal form: all P5 constraints are self,
# bottom row, and the only nontrivial comparable interior pair a<c.
selfrows={a:[r for r in rows[a] if all(le(r[r[x]],r[x]) for x in V)] for a in (1,2,3)}
assert [len(selfrows[a]) for a in (1,2,3)] == [7,6,9]
normal=set()
rows_by_d=[]
for d in V:
    A=[r for r in selfrows[1] if le(r[d],d)]
    B=[r for r in selfrows[2] if le(r[d],d)]
    C=[r for r in selfrows[3] if le(r[d],d)]
    ac=[(a,c) for a in A for c in C if all(le(c[a[x]],a[x]) for x in V)]
    local={((d,)*5,a,b,c,tuple(V)) for a,c in ac for b in B}
    normal |=local
    rows_by_d.append((d,len(B),len(ac),len(local)))
assert rows_by_d==[(0,2,8,16),(1,3,6,18),(2,2,13,26),(3,4,9,36),(4,6,30,180)]
assert accepted==normal
# Independent parameterization by antitone precomplementations.
induced=set()
for nu in product(V,repeat=5):
    if nu[4] or any(le(a,b) and not le(nu[b],nu[a]) for a in V for b in V): continue
    T=tuple(tuple(JOIN[nu[a],MEET[a,b]] for b in V) for a in V)
    assert T in accepted
    induced.add(T)
assert len(induced)==96
assert Counter(T[0][0] for T in induced)=={0:1,1:6,2:6,3:18,4:65}
assert len(accepted-induced)==180
mp=lambda A:all(le(MEET[a,A[a][b]],b) for a in V for b in V)
assert sum(map(mp,accepted))==59
assert Counter(A[0][0] for A in accepted if mp(A))=={0:10,1:6,2:7,3:8,4:28}
# The strong T and F subclasses are verification controls, not novelty claims.
is_t=lambda A:all(A[a][a]==4 and MEET[a,A[a][0]]==0 for a in V)
is_f=lambda A:is_t(A) and all(le(a,A[A[a][0]][0]) for a in V)
assert sum(map(is_t,accepted))==15
assert sum(map(is_f,accepted))==5
print('ALL_CHECKS_OK K=276 precomp_induced=96 genuinely_noninduced=180 MP=59 T=15 F=5')
