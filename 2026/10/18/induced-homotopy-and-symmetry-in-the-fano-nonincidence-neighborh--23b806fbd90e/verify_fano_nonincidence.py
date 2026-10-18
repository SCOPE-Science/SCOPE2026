#!/usr/bin/env python3
"""Exact finite checks for the Fano nonincidence-neighborhood theorem.

Python >=3.9, standard library only. No external datasets are needed.
The topological arguments (fundamental-group contractions and collapses) are
stated in RESULT.md; the executable verifies their finite combinatorial inputs.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product

POINTS=tuple(range(1,8))
LINES=tuple(sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(POINTS,2)}))
assert len(LINES)==7 and all(len(s)==3 for s in LINES)
CAPS=tuple(sorted(tuple(x for x in POINTS if x not in l) for l in LINES))
assert len(CAPS)==7

FACES={d: tuple(sorted(set(c for f in CAPS for c in combinations(f,d+1)))) for d in range(4)}
assert [len(FACES[d]) for d in range(4)]==[7,21,28,7]
INDEX={d: {face:i for i,face in enumerate(FACES[d])} for d in FACES}

# There is exactly one Fano line through a pair and exactly one cap
# containing each noncollinear three-point subset.
assert all(sum({a,b}<=set(l) for l in LINES)==1 for a,b in combinations(POINTS,2))
assert all(sum(set(t)<=set(c) for c in CAPS)==1 for t in FACES[2])
assert all(sum(set(t)<=set(c) for c in CAPS)==0 for t in LINES)
assert len(FACES[2])+len(LINES)==35
assert all(len(set(a)&set(b))==2 for a,b in combinations(CAPS,2))

def sparse_rank(rows, modulus=None):
    """Ordinary exact Gaussian rank (Fractions) or optional finite-field check."""
    if not rows: return 0
    if modulus is None:
        A=[[Fraction(v) for v in row] for row in rows]
    else:
        A=[[int(v)%modulus for v in row] for row in rows]
    m=len(A); n=len(A[0]); r=0
    for col in range(n):
        pivot=next((i for i in range(r,m) if A[i][col]),None)
        if pivot is None:continue
        A[pivot],A[r]=A[r],A[pivot]
        v=A[r][col]
        if modulus is None:
            A[r][col:]=[x/v for x in A[r][col:]]
        else:
            inv=pow(v,-1,modulus)
            A[r][col:]=[(x*inv)%modulus for x in A[r][col:]]
        for i in range(r+1,m):
            c=A[i][col]
            if c:
                A[i][col:]=[(x-c*y) if modulus is None else (x-c*y)%modulus
                             for x,y in zip(A[i][col:],A[r][col:])]
        r+=1
        if r==m:break
    return r

def bd(d,where):
    low=tuple(f for f in FACES[d-1] if set(f)<=where)
    high=tuple(f for f in FACES[d] if set(f)<=where)
    ix={f:i for i,f in enumerate(low)}
    mat=[[0 for _ in high] for _ in low]
    for j,t in enumerate(high):
        for i in range(d+1):mat[ix[t[:i]+t[i+1:]]][j]=(-1)**i
    return mat,low,high

# Full-vertex and restricted chain complexes. For W of size >=4,
# the homotopy proof gives 1-skeleton K_s, pi_1=0 and reduction to 2D.
checks=Counter(); summary=Counter()
for size in range(1,8):
    for W in combinations(POINTS,size):
        S=set(W)
        sub={d: tuple(f for f in FACES[d] if set(f)<=S) for d in range(4)}
        cnt=tuple(len(sub[d]) for d in range(4))
        L=sum(set(l)<=S for l in LINES)
        T=sum(set(c)<=S for c in CAPS)
        assert cnt[0]==size
        assert cnt[1]==size*(size-1)//2 if size>=2 else cnt[1]==0
        assert cnt[2]==len(list(combinations(W,3)))-L
        assert cnt[3]==T
        assert all(sum(set(t)<=set(c) for c in sub[3])<=1 for t in sub[2])
        reduced_euler=sum((-1)**i*cnt[i] for i in range(4))-1
        if size<=2: expected=0
        elif size==3: expected=-1 if tuple(W) in LINES else 0
        elif size==4: expected=0
        elif size==5: expected=1
        elif size==6: expected=3
        else: expected=6
        assert reduced_euler==expected,(W,reduced_euler,expected)
        checks[(size,reduced_euler)]+=1
        # Finite exact rational chain computation: 0,1,2,3-dimensional boundaries.
        mats={d:bd(d,S)[0] for d in (1,2,3)}
        ranks={d:sparse_rank(mats[d]) for d in (1,2,3)}
        b1=cnt[1]-ranks[1]-ranks[2]
        b2=cnt[2]-ranks[2]-ranks[3]
        b3=cnt[3]-ranks[3]
        assert b1==(1 if size==3 and tuple(W) in LINES else 0)
        assert b2==(expected if size>=4 else 0)
        assert b3==0
        summary[(size,b1,b2,b3)]+=1

# Every 2-simplex is contained in at most one tetrahedron; hence its
# coefficient in the boundary of that tetrahedron isolates its coefficient.
# This verifies the key combinatorial hypothesis for injection on H_2.
for tau in FACES[2]:
    assert sum(set(tau)<=set(c) for c in CAPS)==1

# Enumerate GL_3(F_2) using images of the standard basis in [1,7].
def apply(v,cols):
    out=0
    for j in range(3):
        if v>>j & 1:out ^= cols[j]
    return out

def perm_order(perm):
    current={p:p for p in POINTS}
    for n in range(1,169):
        current={p:perm[current[p]] for p in POINTS}
        if all(current[p]==p for p in POINTS):return n
    raise AssertionError('permutation order exceeds 168')

def oriented_trace(face, perm):
    image=tuple(perm[p] for p in face)
    if set(image)!=set(face):return 0
    inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
    return (-1)**inversions

groups=defaultdict(list)
for cols in product(POINTS,repeat=3):
    perm={p:apply(p,cols) for p in POINTS}
    if len(set(perm.values()))!=7:continue
    order=perm_order(perm)
    # Since only H_0 and H_2 are nonzero: trace H_2 = Lefschetz number -1.
    lefschetz=sum((-1)**d*sum(oriented_trace(f,perm) for f in FACES[d]) for d in range(4))
    groups[order].append(lefschetz-1)
expected_groups={1:(1,6),2:(21,-2),3:(56,0),4:(42,2),7:(48,-1)}
assert sum(len(v) for v in groups.values())==168
for order,(count,value) in expected_groups.items():
    assert len(groups[order])==count and set(groups[order])=={value},(order,groups[order])
# The pair of conjugate 3-dimensional complex characters has summed
# values (6,-2,0,2,-1,-1). Hence this is one rational irreducible.
char_self_inner=sum(count*value*value for count,value in expected_groups.values())
assert char_self_inner==2*168
print('VERIFY_OK 127_INDUCED_SUBCOMPLEXES F_VECTOR_7_21_28_7')
print('RESTRICTED_HOMOLOGY',sorted(summary.items()))
print('SYMMETRY_168 CHARACTER_ORDER_1_2_3_4_7', [expected_groups[k] for k in (1,2,3,4,7)])
print('INJECTIVE_INDUCED_H2_FROM_UNIQUE_TRIANGLE_PROPERTY')
