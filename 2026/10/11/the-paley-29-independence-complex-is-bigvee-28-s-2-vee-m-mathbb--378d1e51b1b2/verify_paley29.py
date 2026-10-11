#!/usr/bin/env python3
from itertools import combinations
from collections import deque
from functools import lru_cache

N = 29
QR = {pow(x,2,N) for x in range(1,N)}
EXPECTED_F = [29,203,406,203]
EXPECTED_PAIRS = 397
EXPECTED_CRIT = {1:1, 3:37, 4:9}
EXPECTED_COVERS = 2436
MINOR8_ROWS = (1,7,15,20,23,24,25,28)
MINOR8_COLS = (0,1,2,3,5,6,7,8)
MINOR9_ROWS = (0,4,5,17,20,23,32,33,35)
MINOR9_COLS = tuple(range(9))


def bitcount(x):
    return x.bit_count()


def verts(mask):
    return tuple(i for i in range(N) if mask >> i & 1)


def independent(mask):
    vs = verts(mask)
    for i,a in enumerate(vs):
        for b in vs[i+1:]:
            if (a-b) % N in QR:
                return False
    return True


def incidence(upper, lower):
    u = verts(upper)
    lset = set(verts(lower))
    removed = [i for i,v in enumerate(u) if v not in lset]
    assert len(removed) == 1
    return -1 if removed[0] % 2 else 1


def det_bareiss(A):
    A = [list(map(int,row)) for row in A]
    n = len(A)
    if n == 0:
        return 1
    assert all(len(row)==n for row in A)
    sign = 1
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            p = next((r for r in range(k+1,n) if A[r][k]), None)
            if p is None:
                return 0
            A[k],A[p] = A[p],A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j] = (A[i][j]*pivot - A[i][k]*A[k][j]) // prev
        prev = pivot
        for i in range(k+1,n):
            A[i][k] = 0
        for j in range(k+1,n):
            A[k][j] = 0
    return sign*A[n-1][n-1]


def rank_mod2_rows(rows, ncols):
    basis = {}
    for x in rows:
        y = x
        while y:
            p = y.bit_length()-1
            if p in basis:
                y ^= basis[p]
            else:
                basis[p] = y
                break
    return len(basis)


def matrix_rank_mod2(M):
    rows=[]
    for row in M:
        m=0
        for j,x in enumerate(row):
            if x & 1:
                m |= 1<<j
        rows.append(m)
    return rank_mod2_rows(rows, len(M[0]) if M else 0)

# Generate all nonempty independent faces. Alpha(P_29)=4 is checked exhaustively.
faces=[]
by_size={}
for k in range(1,6):
    layer=[]
    for c in combinations(range(N),k):
        m=sum(1<<v for v in c)
        if independent(m):
            layer.append(m)
    by_size[k]=layer
    faces.extend(layer)
assert [len(by_size[k]) for k in range(1,5)] == EXPECTED_F
assert len(by_size[5]) == 0
face_set=set(faces)

# Deterministic staged vertex matching on the nonempty face poset.
unmatched=set(faces)
pairs=[]
for v in range(N):
    for a in sorted(tuple(unmatched)):
        if (a>>v)&1:
            continue
        b=a | (1<<v)
        if b in unmatched:
            unmatched.remove(a); unmatched.remove(b)
            pairs.append((a,b))
assert len(pairs)==EXPECTED_PAIRS
critical=sorted(unmatched, key=lambda m:(bitcount(m),m))
crit_counts={}
for m in critical:
    crit_counts[bitcount(m)] = crit_counts.get(bitcount(m),0)+1
assert crit_counts == EXPECTED_CRIT

# Every Hasse cover, and acyclicity of the full Morse-oriented Hasse graph.
pair_set=set(pairs)
adj={m:[] for m in faces}
indeg={m:0 for m in faces}
cover_count=0
for upper in faces:
    if bitcount(upper)<2:
        continue
    for v in verts(upper):
        lower=upper ^ (1<<v)
        if lower not in face_set:
            continue
        cover_count += 1
        if (lower,upper) in pair_set:
            src,dst=lower,upper
        else:
            src,dst=upper,lower
        adj[src].append(dst)
        indeg[dst]+=1
assert cover_count == EXPECTED_COVERS
q=deque([m for m in faces if indeg[m]==0])
seen=0
while q:
    x=q.popleft(); seen+=1
    for y in adj[x]:
        indeg[y]-=1
        if indeg[y]==0:
            q.append(y)
assert seen == len(faces), 'Morse orientation has a directed cycle'

lower_to_upper={a:b for a,b in pairs}
upper_to_lower={b:a for a,b in pairs}
crit2=sorted([m for m in critical if bitcount(m)==3], key=verts)
crit3=sorted([m for m in critical if bitcount(m)==4], key=verts)
idx2={m:i for i,m in enumerate(crit2)}

@lru_cache(None)
def project_triangle(t):
    # Coordinates in the critical 2-cell basis after cancelling matched pairs.
    if t in idx2:
        out=[0]*len(crit2); out[idx2[t]]=1; return tuple(out)
    if t in upper_to_lower:
        # This 2-cell is the upper cell of a 1--2 cancellation.
        return (0,)*len(crit2)
    b=lower_to_upper.get(t)
    assert b is not None and bitcount(b)==4
    s=incidence(b,t)
    out=[0]*len(crit2)
    for v in verts(b):
        u=b ^ (1<<v)
        if u==t: continue
        c=incidence(b,u)
        pu=project_triangle(u)
        factor=-s*c
        for i,z in enumerate(pu):
            out[i]+=factor*z
    return tuple(out)

M=[[0]*len(crit3) for _ in crit2]
for j,b in enumerate(crit3):
    for v in verts(b):
        t=b ^ (1<<v)
        c=incidence(b,t)
        pt=project_triangle(t)
        for i,z in enumerate(pt):
            M[i][j]+=c*z
assert len(M)==37 and len(M[0])==9
assert max(abs(x) for row in M for x in row) <= 1

A8=[[M[i][j] for j in MINOR8_COLS] for i in MINOR8_ROWS]
A9=[[M[i][j] for j in MINOR9_COLS] for i in MINOR9_ROWS]
d8=det_bareiss(A8)
d9=det_bareiss(A9)
assert abs(d8)==1
assert abs(d9)==2
assert matrix_rank_mod2(M)==8
# Therefore Smith invariant factors are 1^8,2: the unit 8-minor forces
# Delta_1=...=Delta_8=1; rank_mod2=8 makes every 9-minor even; the
# displayed 9-minor of absolute value 2 forces Delta_9=2.

# Independent mod-2 ranks of the original simplicial boundary maps.
def boundary_rows_mod2(k):
    # Matrix d_k: C_k -> C_{k-1}; rows indexed (k-1)-faces, cols k-faces.
    lows=by_size[k]
    ups=by_size[k+1]
    lowidx={m:i for i,m in enumerate(lows)}
    rowbits=[0]*len(lows)
    for j,u in enumerate(ups):
        for v in verts(u):
            l=u^(1<<v)
            rowbits[lowidx[l]] |= 1<<j
    return rowbits, len(ups)

r1_rows=[]
# augmented d1 from vertices to one connected component: ordinary d1 rank is n-1.
# Compute graph-edge incidence over F2 from 1-simplices (independent pairs).
for vertex in range(N):
    bits=0
    for j,e in enumerate(by_size[2]):
        if (e>>vertex)&1: bits |= 1<<j
    r1_rows.append(bits)
r1=rank_mod2_rows(r1_rows,len(by_size[2]))
r2_rows,nc2=boundary_rows_mod2(2)
r2=rank_mod2_rows(r2_rows,nc2)
r3_rows,nc3=boundary_rows_mod2(3)
r3=rank_mod2_rows(r3_rows,nc3)
assert (r1,r2,r3)==(28,175,202)
# Betti over F2: b0=1, b1=0, b2=29, b3=1.
b2_mod2=len(by_size[3])-r2-r3
b3_mod2=len(by_size[4])-r3
assert (b2_mod2,b3_mod2)==(29,1)

euler=sum((1 if (k-1)%2==0 else -1)*len(by_size[k]) for k in range(1,5))
assert euler==29

print('VERIFY_OK')
print('vertices=29 edges=203 quadratic_residues='+','.join(map(str,sorted(QR))))
print('face_vector='+repr(EXPECTED_F)+' total_nonempty_faces='+str(len(faces)))
print('hasse_covers='+str(cover_count)+' matching_pairs='+str(len(pairs))+' critical_counts='+repr(crit_counts))
print('morse_boundary_shape=37x9 max_abs_entry=1 rank_mod2=8')
print('minor8_det='+str(d8)+' minor9_det='+str(d9)+' smith_invariants=1^8,2')
print('original_mod2_boundary_ranks='+repr((r1,r2,r3))+' mod2_reduced_betti=(0,0,29,1)')
print('homology_Z: H2=Z^28+Z/2, H3=0; homotopy=wedge^28 S2 vee M(Z/2,2)')
