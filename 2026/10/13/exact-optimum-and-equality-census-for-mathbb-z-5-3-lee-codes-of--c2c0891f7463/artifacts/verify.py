from itertools import product, permutations, combinations
from collections import Counter
V=list(product(range(5), repeat=3)); idx={v:i for i,v in enumerate(V)}; N=len(V)
def lee1(a,b):
    d=(a-b)%5
    return min(d,5-d)
def lee(a,b): return sum(lee1(x,y) for x,y in zip(a,b))
def ball(a):
    out={a}
    for k in range(3):
        for e in (-1,1):
            b=list(a); b[k]=(b[k]+e)%5; out.add(tuple(b))
    return out
balls=[ball(v) for v in V]
adj=[0]*N
for i in range(N):
    for j in range(i+1,N):
        ok=lee(V[i],V[j])>=3
        ok2=balls[i].isdisjoint(balls[j])
        assert ok==ok2
        if ok:
            adj[i]|=1<<j; adj[j]|=1<<i

def color_sort(P):
    # returns vertices in nondecreasing greedy-color blocks, with color numbers
    order=[]; bounds=[]; rem=P; color=0
    while rem:
        color+=1; avail=rem
        while avail:
            lb=avail & -avail; v=lb.bit_length()-1
            order.append(v); bounds.append(color)
            rem &= ~lb; avail &= ~lb
            avail &= ~adj[v]
    return order,bounds

best=[]; nodes=0
def expand(R,P):
    global best,nodes
    nodes+=1
    if not P:
        if len(R)>len(best): best=R[:]
        return
    order,bounds=color_sort(P)
    for i in range(len(order)-1,-1,-1):
        if len(R)+bounds[i] <= len(best): return
        v=order[i]; bit=1<<v
        if P & bit:
            expand(R+[v], P & adj[v])
            P &= ~bit

expand([], (1<<N)-1)
assert len(best)==15, len(best)
# enumerate all 15-cliques containing zero, with ordered indices to avoid duplicates
z=idx[(0,0,0)]; target=15; norm=[]; enum_nodes=0
def enum(R,P,minv):
    global enum_nodes
    enum_nodes+=1
    need=target-len(R)
    if need==0:
        norm.append(frozenset(R)); return
    if P.bit_count()<need: return
    _,b=color_sort(P)
    if not b or b[-1]<need: return
    # ascending candidates; after choose v retain only >v
    Q=P
    while Q:
        lb=Q & -Q; v=lb.bit_length()-1
        Q &= ~lb
        later=P & ~((1<<(v+1))-1)
        enum(R+[v], later & adj[v], v+1)
        P &= ~lb

enum([z], adj[z] & ~((1<<(z+1))-1), z+1)
# z is index 0, so okay
assert len(norm)==24, len(norm)
# translations generate every maximum; double count via translating one member to zero
allc=set()
for C in norm:
    pts=[V[i] for i in C]
    for t in V:
        allc.add(frozenset(idx[tuple((p[k]+t[k])%5 for k in range(3))] for p in pts))
assert len(allc)==200
# every max universal profile and balance
profiles=Counter(); balances=Counter()
for C in allc:
    pts=[V[i] for i in C]
    profiles[tuple(sorted(Counter(lee(a,b) for a,b in combinations(pts,2)).items()))]+=1
    balances[tuple(tuple(sorted(Counter(p[k] for p in pts).values())) for k in range(3))]+=1
assert profiles=={((3,45),(4,45),(6,15)):200}, profiles
assert balances=={((3,3,3,3,3),(3,3,3,3,3),(3,3,3,3,3)):200}, balances
# natural isometry action: coordinate permutations, independent sign reversals, translations
perms=list(permutations(range(3))); signs=list(product((1,-1),repeat=3)); trans=V
C0=next(iter(allc)); pts=[V[i] for i in C0]; orbit=set()
for pm in perms:
  for sg in signs:
    base=[tuple((sg[k]*p[pm[k]])%5 for k in range(3)) for p in pts]
    for t in trans:
      D=frozenset(idx[tuple((q[k]+t[k])%5 for k in range(3))] for q in base)
      assert D in allc
      orbit.add(D)
assert len(orbit)==200
assert 6000//len(orbit)==30
witness=sorted(V[i] for i in best)
assert min(lee(a,b) for a,b in combinations(witness,2))>=3
print('VERIFY_OK vertices=125 ball_size=7 maximum=15 normalized_maxima=24 labeled_maxima=200 natural_group=6000 orbits=1 orbit_size=200 stabilizer=30 distance_profile=3x45,4x45,6x15 balanced=3_each_symbol_per_coordinate max_nodes=%d enum_nodes=%d' % (nodes,enum_nodes))
print('WITNESS',' '.join(''.join(map(str,x)) for x in witness))
