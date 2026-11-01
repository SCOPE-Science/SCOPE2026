"""Exact, standalone verification of the cuboctahedral matching-complex symmetry character.
No external libraries or network access are required. Python 3.9+.
"""
from itertools import permutations
from collections import defaultdict, Counter, deque

# A cube vertex is a binary word of length three. Its twelve edges are
# the cuboctahedral vertices, and incident cube edges are cuboctahedral edges.
cube_edges = sorted((a,b) for a in range(8) for b in range(a+1,8) if a^b in (1,2,4))
cubo_edges = sorted((i,j) for i in range(12) for j in range(i+1,12) if set(cube_edges[i]) & set(cube_edges[j]))
assert len(cube_edges)==12 and len(cubo_edges)==24
faces=[()]
for j,(a,b) in enumerate(cubo_edges):
    old=tuple(faces)
    faces.extend(f+(j,) for f in old if all(a not in cubo_edges[k] and b not in cubo_edges[k] for k in f))
faces=set(faces)
assert len(faces)==2649
bydim=defaultdict(list)
for f in faces:
    if f: bydim[len(f)-1].append(f)
for group in bydim.values(): group.sort()
assert tuple(len(bydim[d]) for d in range(6))==(24,204,744,1116,528,32)

# Greedy pivot matching, with the empty face excluded.
unmatched=set(faces)-{()}
partner={}
for j in range(24):
    pairs=[]
    for f in sorted(unmatched,key=lambda f:(len(f),f)):
        if j not in f:
            upper=tuple(sorted(f+(j,)))
            if upper in unmatched: pairs.append((f,upper))
    for lo,hi in pairs:
        if lo in unmatched and hi in unmatched:
            partner[lo]=hi
            partner[hi]=lo
            unmatched.remove(lo);unmatched.remove(hi)
assert len(partner)==2574 and len(unmatched)==74
cr=Counter(len(f)-1 for f in unmatched)
assert cr=={0:1,3:65,4:8},cr

# Full Hasse digraph reverses each matched incidence. An exact topological
# sorting certifies acyclicity, rather than assuming it from the pivot order.
adj=defaultdict(list);indeg={f:0 for f in faces if f}
arrow_count=0
for hi in indeg:
    if len(hi)<2: continue
    for i in range(len(hi)):
        lo=hi[:i]+hi[i+1:]
        if partner.get(lo)==hi: u,v=lo,hi
        else: u,v=hi,lo
        adj[u].append(v);indeg[v]+=1;arrow_count+=1
q=deque(f for f,d in indeg.items() if d==0)
visited=0
while q:
    f=q.popleft();visited+=1
    for x in adj[f]:
        indeg[x]-=1
        if indeg[x]==0:q.append(x)
assert visited==len(faces)-1 and arrow_count==9936,(visited,arrow_count)

# Compute the integral Morse 4-to-3 attaching-degree matrix. We express each
# 3-simplex in terms of the critical 3-cells via the relations from matched
# 4-simplices. Signs come from increasing-edge orientations.
crit3=sorted(f for f in unmatched if len(f)==4)
crit4=sorted(f for f in unmatched if len(f)==5)
index={f:i for i,f in enumerate(crit3)}
cache={};active=set()
def reduction(tau):
    if tau in cache: return cache[tau]
    if tau in active:raise AssertionError('gradient cycle')
    active.add(tau)
    if tau in unmatched:
        assert tau in index
        out={index[tau]:1}
    elif len(partner[tau])==3: # upper partner of a 2-to-3 match
        out={}
    else:
        beta=partner[tau]
        assert len(beta)==5
        k=beta.index(next(x for x in beta if x not in tau))
        den=(-1)**k
        out={}
        for i in range(5):
            sub=beta[:i]+beta[i+1:]
            if sub==tau:continue
            c=-(-1)**i*den
            for row,val in reduction(sub).items():out[row]=out.get(row,0)+c*val
        out={row:v for row,v in out.items() if v}
    active.remove(tau)
    cache[tau]=out
    return out
M=[[0]*len(crit4) for _ in crit3]
for col,beta in enumerate(crit4):
    for i in range(5):
        for row,val in reduction(beta[:i]+beta[i+1:]).items():
            M[row][col]+=(-1)**i*val
minor_rows=[6,41,4,5,52,15,36,37]
minor=[[M[r][c] for c in range(8)] for r in minor_rows]
assert all(minor[i][j]==((1 if i==0 else -1) if i==j else 0) for i in range(8) for j in range(8)),minor
assert [hex(sum(1<<j for j in crit3[r])) for r in minor_rows]==['0x404802','0x140048','0x22802','0x402802','0x800908','0x402044','0x80148','0x800148']
# Thus the reduced integral homology is Z^57 in degree 3 and zero elsewhere.

# Exact cube automorphisms: a permutation of axes followed by bit flips.
qindex={frozenset(e):i for i,e in enumerate(cube_edges)}
cindex={frozenset(e):i for i,e in enumerate(cubo_edges)}
diagonals=(frozenset((0,7)),frozenset((1,6)),frozenset((2,5)),frozenset((3,4)))

def parity(seq):return -1 if sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])%2 else 1

def cubesym(axes,flip):
    return tuple(sum(((v>>i)&1)<<axes[i] for i in range(3))^flip for v in range(8))

def comp(g,h): return tuple(g[h[i]] for i in range(8))

# Odd determinant elements are central inversion times a proper rotation.
# The latter permutes the four antipodal body-diagonal pairs, giving S_4.
inv=cubesym((0,1,2),7)
byclass=defaultdict(set);class_counts=Counter();rows=[]
for axes in permutations(range(3)):
    for flip in range(8):
        g=cubesym(axes,flip)
        e=int(parity(axes)*(-1)**flip.bit_count()<0)
        r=comp(g,inv) if e else g
        dp=[diagonals.index(frozenset(r[v] for v in d)) for d in diagonals]
        cyc=[];seen=set()
        for j in range(4):
            if j not in seen:
                u=j;c=0
                while u not in seen:seen.add(u);u=dp[u];c+=1
                cyc.append(c)
        typ=tuple(sorted(cyc,reverse=True))
        qmap=[qindex[frozenset((g[a],g[b]))] for a,b in cube_edges]
        cmap=[cindex[frozenset((qmap[a],qmap[b]))] for a,b in cubo_edges]
        trace=[]
        for d in range(6):
            fixed=0
            for f in bydim[d]:
                image=[cmap[i] for i in f]
                if sorted(image)==list(f):fixed+=parity(image)
            trace.append(fixed)
        h3=1-sum((-1)**d*t for d,t in enumerate(trace))
        byclass[(typ,e)].add(h3)
        class_counts[(typ,e)]+=1
        rows.append((g,typ,e,h3,tuple(trace)))
assert len(rows)==48 and len({r[0] for r in rows})==48
assert all(len(s)==1 for s in byclass.values())
assert class_counts=={((1,1,1,1),0):1,((1,1,1,1),1):1,((2,1,1),0):6,((2,1,1),1):6,((2,2),0):3,((2,2),1):3,((3,1),0):8,((3,1),1):8,((4,),0):6,((4,),1):6}
cht={
 '4':{(1,1,1,1):1,(2,1,1):1,(2,2):1,(3,1):1,(4,):1},
 '31':{(1,1,1,1):3,(2,1,1):1,(2,2):-1,(3,1):0,(4,):-1},
 '22':{(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0},
 '211':{(1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1},
 '1111':{(1,1,1,1):1,(2,1,1):-1,(2,2):1,(3,1):1,(4,):-1}}
mult={}
for label,table in cht.items():
    for s in (1,-1):
        numerator=sum(chi*table[typ]*s**e for _,typ,e,chi,_ in rows)
        assert numerator%48==0
        mult[(label,s)]=numerator//48
assert mult=={('4',1):1,('4',-1):2,('31',1):5,('31',-1):2,('22',1):5,('22',-1):4,('211',1):2,('211',-1):2,('1111',1):2,('1111',-1):1}
assert sum(mult[(x,s)]*cht[x][(1,1,1,1)] for x,s in mult)==57
assert sum(chi for _,typ,e,chi,_ in rows if e==0)==24*3
assert sum(chi for _,typ,e,chi,_ in rows)==48
print('fvector',tuple(len(bydim[d]) for d in range(6)))
print('morse_pairs',len(partner)//2,'critical_counts',dict(sorted(cr.items())),'hasse_arrows',arrow_count,'visited',visited)
print('primitive_minor',minor,'morse_boundary_size',(len(crit3),len(crit4)))
print('class_table (cycle type, inversion e, size, degree-3 trace)')
for typ,e in sorted(byclass):print(typ,e,class_counts[(typ,e)],next(iter(byclass[(typ,e)])))
print('multiplicities (partition, inversion parity, multiplicity)',sorted((a,b,n) for (a,b),n in mult.items()))
print('H3_plus',34,'H3_minus',23,'full_group_invariants',1,'rotation_invariants',3)
print('VERIFY_OK')
