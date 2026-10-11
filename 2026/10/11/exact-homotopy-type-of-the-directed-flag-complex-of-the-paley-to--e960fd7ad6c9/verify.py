#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
import json

Q=31
PIVOT_ORDER=[21,27,4,13,25,17,23,15,8,30,22,18,29,6,11,3,19,5,0,26,14,16,10,7,12,24,9,2,20,28,1]
RES={ (x*x)%Q for x in range(1,Q) }

def edge(i,j):
    return ((j-i)%Q) in RES

def vertices(mask):
    while mask:
        b=mask & -mask
        yield b.bit_length()-1
        mask-=b

def transitive(mask):
    vs=list(vertices(mask))
    k=len(vs)
    if k<=2: return True
    deg=[]
    for u in vs:
        d=sum(1 for v in vs if u!=v and edge(u,v))
        deg.append(d)
    return sorted(deg)==list(range(k))

# enumerate all nonempty faces by extension; avoid scanning 2^31 subsets
faces_by_size={1:{1<<i for i in range(Q)}}
all_faces=set(faces_by_size[1])
k=1
while faces_by_size.get(k):
    nxt=set()
    for m in faces_by_size[k]:
        mx=max(vertices(m))
        for v in range(mx+1,Q):
            nm=m|(1<<v)
            if transitive(nm): nxt.add(nm)
    if not nxt: break
    faces_by_size[k+1]=nxt
    all_faces.update(nxt)
    k+=1
face_vector=[len(faces_by_size.get(s,set())) for s in range(1,k+1)]
# verify the quadratic-residue orientation is a doubly regular tournament
assert len(RES)==15 and RES.isdisjoint({(-r)%Q for r in RES}) and RES|{(-r)%Q for r in RES}==set(range(1,Q))
outdegrees=[sum(edge(i,j) for j in range(Q) if j!=i) for i in range(Q)]
common_out=[]
for i in range(Q):
    for j in range(i+1,Q):
        common_out.append(sum(edge(i,u) and edge(j,u) for u in range(Q) if u not in (i,j)))
assert set(outdegrees)=={15} and set(common_out)=={7}

assert face_vector==[31,465,3255,9765,10695,3255,465], face_vector
assert len(all_faces)==27931

# repeated-toggle matching on currently unmatched faces
unmatched=set(all_faces)
up={}
down={}
for v in PIVOT_ORDER:
    bit=1<<v
    lows=[]
    for m in list(unmatched):
        if m & bit: continue
        hi=m|bit
        if hi in unmatched:
            lows.append((m,hi))
    for lo,hi in lows:
        if lo in unmatched and hi in unmatched:
            unmatched.remove(lo); unmatched.remove(hi)
            up[lo]=hi; down[hi]=lo
critical=sorted(unmatched)
critical_counts=Counter(m.bit_count()-1 for m in critical)
assert critical_counts==Counter({4:1049,3:89,0:1}), critical_counts
assert len(up)==13396

# check every Hasse cover and acyclicity of reversed matched Hasse graph
indeg={m:0 for m in all_faces}
adj=defaultdict(list)
hasse=0
for hi in all_faces:
    if hi.bit_count()<=1: continue
    for v in list(vertices(hi)):
        lo=hi & ~(1<<v)
        if lo==0: continue
        assert lo in all_faces
        hasse+=1
        if down.get(hi)==lo:
            a,b=lo,hi
        else:
            a,b=hi,lo
        adj[a].append(b); indeg[b]+=1
assert hasse==126015, hasse
q=deque([m for m,d in indeg.items() if d==0])
seen=0
while q:
    a=q.popleft(); seen+=1
    for b in adj.get(a,()):
        indeg[b]-=1
        if indeg[b]==0:q.append(b)
assert seen==len(all_faces), (seen,len(all_faces))

# orientations in canonical vertex order for simplicial signs
def ordered_vertices(mask):
    return sorted(vertices(mask))

def incidence(hi,lo):
    hv=ordered_vertices(hi)
    lv=ordered_vertices(lo)
    assert len(hv)==len(lv)+1 and (lo & hi)==lo
    missing=next(i for i,x in enumerate(hv) if not (lo>>x)&1)
    return -1 if missing%2 else 1

crit3=sorted([m for m in critical if m.bit_count()==4])
crit4=sorted([m for m in critical if m.bit_count()==5])
idx3={m:i for i,m in enumerate(crit3)}

# recursively reduce any 3-cell to critical 3-cells after Morse cancellation
memo={}
def add_scaled(out, vec, c):
    if c==0:return
    for i,a in vec.items():
        z=out.get(i,0)+c*a
        if z: out[i]=z
        elif i in out: del out[i]

def reduce3(alpha, stack=None):
    if alpha in memo:return memo[alpha]
    if alpha in idx3:
        memo[alpha]={idx3[alpha]:1}; return memo[alpha]
    # if alpha is upper member of 2<->3 matching, no 4-gradient path continues through it
    if alpha in down:
        memo[alpha]={}; return memo[alpha]
    beta=up.get(alpha)
    if beta is None:
        # critical 3 already handled; any remaining case would contradict matching partition
        raise AssertionError(('unclassified 3-cell',alpha))
    assert beta.bit_count()==5
    coeff=incidence(beta,alpha) # +/-1
    out={}
    for v in list(vertices(beta)):
        gamma=beta & ~(1<<v)
        if gamma==alpha: continue
        c=incidence(beta,gamma)
        add_scaled(out, reduce3(gamma), -c*coeff) # inverse(coeff)=coeff
    memo[alpha]=out
    return out

# Morse boundary rows indexed by critical 3-cells, columns by critical 4-cells
rows=[[0]*len(crit4) for _ in crit3]
for j,sigma in enumerate(crit4):
    col={}
    for v in list(vertices(sigma)):
        alpha=sigma & ~(1<<v)
        c=incidence(sigma,alpha)
        add_scaled(col, reduce3(alpha), c)
    for i,a in col.items(): rows[i][j]=a
nonzeros=sum(x!=0 for r in rows for x in r)
max_abs=max(abs(x) for r in rows for x in r)

# finite-field row rank
def rank_mod(mat,p):
    A=[[x%p for x in row] for row in mat]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

ranks={str(p):rank_mod(rows,p) for p in [2,3,5,7,101,601]}
assert all(r==89 for r in ranks.values()), ranks

# get pivot columns of row space mod 2; these form an invertible 89x89 minor mod2
def pivot_columns_mod(mat,p):
    A=[[x%p for x in row] for row in mat]
    m=len(A); n=len(A[0]); r=0; pcs=[]
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        pcs.append(c); r+=1
        if r==m:break
    return pcs
pcs=pivot_columns_mod(rows,2)
assert len(pcs)==89
minor=[[rows[i][j] for j in pcs] for i in range(89)]

def det_bareiss(A):
    B=[row[:] for row in A]; n=len(B); sign=1; denom=1
    for k in range(n-1):
        if B[k][k]==0:
            s=next((r for r in range(k+1,n) if B[r][k]!=0),None)
            if s is None:return 0
            B[k],B[s]=B[s],B[k]; sign=-sign
        pivot=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=B[i][j]*pivot-B[i][k]*B[k][j]
                assert num%denom==0
                B[i][j]=num//denom
            B[i][k]=0
        denom=pivot
    return sign*B[n-1][n-1]

det=det_bareiss(minor)
assert abs(det)==601, det
# Since rank mod 601 is full, gcd of all maximal minors is not divisible by 601;
# since it divides this minor (601), gcd is 1, hence all nonzero Smith factors are 1.

# Euler characteristic cross-check
chi=sum((1 if (s-1)%2==0 else -1)*len(faces_by_size[s]) for s in faces_by_size)
assert chi==961

out={
  'q':Q,
  'quadratic_residues':sorted(RES),
  'outdegree':15,
  'common_outdegree_of_distinct_pair':7,
  'face_vector_by_dimension':face_vector,
  'nonempty_faces':len(all_faces),
  'hasse_covers_nonempty':hasse,
  'pivot_order':PIVOT_ORDER,
  'matching_pairs':len(up),
  'matching_acyclic':True,
  'critical_cells_by_dimension':{str(k):critical_counts[k] for k in sorted(critical_counts)},
  'morse_boundary_shape':[len(crit3),len(crit4)],
  'morse_boundary_nonzeros':nonzeros,
  'morse_boundary_max_abs_entry':max_abs,
  'morse_boundary_ranks_mod_primes':ranks,
  'certifying_maximal_minor_columns':pcs,
  'certifying_maximal_minor_determinant':det,
  'smith_nonzero_diagonal':'1 repeated 89 times',
  'reduced_homology':'Z^960 in degree 4; zero otherwise',
  'euler_characteristic':chi,
  'conclusion':'dFl(Paley tournament on 31 vertices) ~= wedge of 960 copies of S^4'
}
print(json.dumps(out,sort_keys=True,separators=(',',':')))
