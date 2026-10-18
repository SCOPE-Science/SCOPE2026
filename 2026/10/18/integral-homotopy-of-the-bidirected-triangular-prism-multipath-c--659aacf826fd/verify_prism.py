"""Exact finite certificate for the fully bidirected triangular prism multipath complex.
All calculations use the Python standard library and integer/rational arithmetic.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction

EDGES = ((0,1),(0,2),(1,2),(3,4),(3,5),(4,5),(0,3),(1,4),(2,5))
ARCS = tuple(sorted([(a,b) for a,b in EDGES] + [(b,a) for a,b in EDGES]))
N = len(ARCS)
assert N == 18

def facets(mask):
    bits = [i for i in range(N) if (mask >> i) & 1]
    return [(mask ^ (1 << i), (-1)**k) for k,i in enumerate(bits)]

def direct_valid(mask):
    nxt = {}
    dest = set()
    for i,(a,b) in enumerate(ARCS):
        if mask & (1<<i):
            if a in nxt or b in dest: return False
            nxt[a] = b
            dest.add(b)
    for a in nxt:
        seen = set()
        q = a
        while q in nxt:
            if q in seen:return False
            seen.add(q)
            q = nxt[q]
    return True

# Exhaustively inspect every arc subset.  No model-dependent pruning.
FACES = {mask for mask in range(1<<N) if direct_valid(mask)}
fvec = tuple(sum(m.bit_count()==k for m in FACES) for k in range(6))
assert fvec == (1,18,108,260,240,60),fvec

# Independent backtracking enumerator: once an arc is inserted, a directed cycle
# exists precisely when its target already reaches its source.
def enumerate_dfs():
    out = {0}
    def visit(start,mask,uses_src,uses_dst,succ):
        for i in range(start,N):
            a,b = ARCS[i]
            if (uses_src>>a)&1 or (uses_dst>>b)&1:continue
            q=b
            while q in succ and q!=a:q=succ[q]
            if q==a:continue
            nxt=mask|(1<<i)
            out.add(nxt)
            succ[a]=b
            visit(i+1,nxt,uses_src|(1<<a),uses_dst|(1<<b),succ)
            del succ[a]
    visit(0,0,0,0,{})
    return out
assert FACES == enumerate_dfs()

# Toggle each arc in lexicographic order among not-yet-matched nonempty faces.
remaining = FACES - {0}
PAIRS = []
for i in range(N):
    stage = [(a,a|(1<<i)) for a in sorted(remaining)
             if not (a>>i)&1 and a|(1<<i) in remaining]
    for a,b in stage:
        assert a in remaining and b in remaining
        remaining.remove(a);remaining.remove(b)
    PAIRS.extend(stage)
CRIT = sorted(remaining)
assert len(PAIRS) == 326 and len(CRIT)==34
assert Counter(m.bit_count()-1 for m in CRIT)=={0:1,2:5,3:22,4:6}

# Verify acyclicity of the full directed Hasse graph (not merely a sampled region).
match_edges=set(PAIRS)
faces_nonempty=FACES-{0}
indegree = {f:0 for f in faces_nonempty}
outedges=defaultdict(list)
incidences=0
for upper in faces_nonempty:
    if upper.bit_count()==1:continue
    for lower,_ in facets(upper):
        incidences+=1
        if (lower,upper) in match_edges:
            u,v=lower,upper
        else:
            u,v=upper,lower
        outedges[u].append(v)
        indegree[v]+=1
queue=deque(x for x,d in indegree.items() if d==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in outedges[u]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert visited == len(faces_nonempty)

matched_lower={a:b for a,b in PAIRS}
matched_upper={b for a,b in PAIRS}
crit_set=set(CRIT)
critical_by_dim={d:sorted(x for x in CRIT if x.bit_count()-1==d) for d in range(5)}

# Unit-pivot elimination, implemented through a chain projection.  For a matched
# lower cell a with upper partner b, its image is obtained by the relation
# 0 = P(boundary b).  Matched upper cells project to 0.
visiting=set()
@lru_cache(None)
def projection(a):
    if a in crit_set:return {a:1}
    if a in matched_upper:return {}
    assert a in matched_lower
    assert a not in visiting
    visiting.add(a)
    b=matched_lower[a]
    sign=next(s for z,s in facets(b) if z==a)
    ans=defaultdict(int)
    for lower,co in facets(b):
        if lower==a or lower==0:continue
        for c,z in projection(lower).items():
            ans[c]-=sign*co*z
    visiting.remove(a)
    return {x:v for x,v in ans.items() if v}

def projected_boundary(b):
    ans=defaultdict(int)
    for a,s in facets(b):
        if a==0:continue
        for c,v in projection(a).items():ans[c]+=s*v
    return {x:v for x,v in ans.items() if v}

morse3=[]
morse4=[]
for c in critical_by_dim[3]:morse3.append(projected_boundary(c))
for c in critical_by_dim[4]:morse4.append(projected_boundary(c))
assert all(not x for x in morse3)
assert all(not x for x in morse4)

# Check that projection is a chain map in every nonnegative degree.
# The only nonzero Morse differentials are zero for this example.
for f in faces_nonempty:
    assert not projected_boundary(f) if f in matched_upper or f in crit_set else True
    if f.bit_count()>=2:
        assert not projected_boundary(f)

# Closed cochains dual to the five critical 2-cells.
C2=critical_by_dim[2]
C3=critical_by_dim[3]
C4=critical_by_dim[4]
faces_dim={d:sorted(x for x in faces_nonempty if x.bit_count()-1==d) for d in range(5)}
for tetra in faces_dim[3]:
    for c in C2:
        assert sum(sign*projection(tri).get(c,0) for tri,sign in facets(tetra))==0

# Confirm the five degree-two cocycles form a rational cohomology basis:
# their columns enlarge the degree-two coboundary span by five dimensions.
def rank_mod_columns(columns, p):
    piv = {}
    for old in columns:
        col = {j:v%p for j,v in old.items() if v%p}
        while col:
            r = min(col)
            if r not in piv:
                inv = pow(col[r], -1, p)
                piv[r] = {i:(v*inv)%p for i,v in col.items() if v%p}
                break
            co = col[r]
            for i,v in piv[r].items():
                k = (col.get(i,0)-co*v)%p
                if k:col[i]=k
                else:col.pop(i,None)
    return len(piv)

index2={x:i for i,x in enumerate(faces_dim[2])}
edge_to_cofaces=defaultdict(dict)
for triangle in faces_dim[2]:
    for edge,sign in facets(triangle):
        edge_to_cofaces[edge][index2[triangle]]=sign
B2_cochains=[edge_to_cofaces[edge] for edge in faces_dim[1]]
P2_cochains=[{index2[triangle]:projection(triangle).get(c,0)
              for triangle in faces_dim[2] if projection(triangle).get(c,0)}
             for c in C2]
for p in (2,101):
    assert rank_mod_columns(B2_cochains,p)==91
    assert rank_mod_columns(B2_cochains+P2_cochains,p)==96

# Exact rational nullspace of boundary C4 -> C3, by sparse column elimination.
# Keep each new reduced column's expression in the original C4 basis.
rows={x:i for i,x in enumerate(faces_dim[3])}
cols=faces_dim[4]
pivots={}
cycles=[]
for j,b in enumerate(cols):
    vec={rows[a]:Fraction(s) for a,s in facets(b)}
    source={j:Fraction(1)}
    while vec and min(vec) in pivots:
        t=min(vec)
        pvec,psrc=pivots[t]
        ratio=vec[t]
        for r,v in pvec.items():
            w=vec.get(r,0)-ratio*v
            if w:vec[r]=w
            else:vec.pop(r,None)
        for r,v in psrc.items():
            w=source.get(r,0)-ratio*v
            if w:source[r]=w
            else:source.pop(r,None)
    if vec:
        t=min(vec);z=vec[t]
        pivots[t]=({r:v/z for r,v in vec.items()},
                   {r:v/z for r,v in source.items()})
    else:
        cycles.append(source)
assert len(pivots)==54 and len(cycles)==6
for cycle in cycles:
    bd=defaultdict(Fraction)
    for j,co in cycle.items():
        for a,s in facets(cols[j]):bd[a]+=co*s
    assert not any(bd.values())

# Alexander--Whitney cup product of degree-two cochains, evaluated on a full
# basis of top cycles.  This detects Hopf and Whitehead components of 4-cell
# attaching maps once the 3-skeleton has been identified as a sphere wedge.
for i,a in enumerate(C2):
    for b in C2[i:]:
        values=[]
        for face in cols:
            bits=[q for q in range(N) if (face>>q)&1]
            front=sum(1<<q for q in bits[:3])
            back=sum(1<<q for q in bits[2:])
            values.append(projection(front).get(a,0)*projection(back).get(b,0))
        for cycle in cycles:
            assert sum(coeff*values[j] for j,coeff in cycle.items())==0

# Independently verify the complete mod-p Betti vector from original simplices.
def finite_field_rank(d,p):
    low = {x:i for i,x in enumerate(faces_dim[d-1])}
    piv={}
    for f in faces_dim[d]:
        col={low[a]:sign%p for a,sign in facets(f)}
        while col:
            t=min(col)
            if t not in piv:
                z=pow(col[t],-1,p)
                piv[t]={r:(v*z)%p for r,v in col.items() if (v*z)%p}
                break
            z=col[t]
            for r,v in piv[t].items():
                q=(col.get(r,0)-z*v)%p
                if q:col[r]=q
                else:col.pop(r,None)
    return len(piv)
for p in (2,101):
    ranks={d:finite_field_rank(d,p) for d in (1,2,3,4)}
    assert ranks=={1:17,2:91,3:164,4:54},(p,ranks)
    betti={d:len(faces_dim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(5)}
    assert betti=={0:1,1:0,2:5,3:22,4:6}

print('VERIFIED_PRISM_MULTIPATH_WEDGE')
print('faces_by_size',fvec,'pairs',len(PAIRS),'critical',[len(critical_by_dim[d]) for d in range(5)])
print('Hasse_incidences',incidences,'Hasse_acyclic_nodes',visited)
print('Morse_differentials_zero',True,'top_cycles',len(cycles),'cup_pairs_vanishing',15)
print('direct_mod_2_mod_101_boundary_ranks',(17,91,164,54))
