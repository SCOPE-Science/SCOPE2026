"""Exact duad--syntheme matching and forcing-set census; Python 3 stdlib."""
import itertools
from collections import Counter
from math import comb

points=range(6)
duads=tuple(itertools.combinations(points,2))
def partitions(xs):
    if not xs:
        yield ()
        return
    a=xs[0]
    for b in xs[1:]:
        rest=tuple(x for x in xs if x!=a and x!=b)
        for pairs in partitions(rest):
            yield tuple(sorted(((a,b),)+pairs))
synthemes=tuple(sorted(partitions(tuple(points))))
assert len(duads)==len(synthemes)==15
adj=tuple(tuple(j for j,s in enumerate(synthemes) if d in s) for d in duads)
assert all(len(row)==3 for row in adj)
matchings=[]
def search(i, used, path):
    if i==15:
        matchings.append(tuple(path))
        return
    for j in adj[i]:
        if used&(1<<j)==0:
            search(i+1,used|1<<j,path+[j])
search(0,0,[])
assert len(matchings)==len(set(matchings))==288
matchings.sort()
indices_d={d:i for i,d in enumerate(duads)}
indices_s={s:i for i,s in enumerate(synthemes)}
perm_data=[]
for p in itertools.permutations(range(6)):
    def relabel_edge(d):return tuple(sorted(p[x] for x in d))
    di=tuple(indices_d[relabel_edge(d)] for d in duads)
    sj=tuple(indices_s[tuple(sorted(relabel_edge(d) for d in s))] for s in synthemes)
    perm_data.append((di,sj))
assert len(perm_data)==720
matchset=set(matchings)
def orbit(m):
    z=set()
    for di,sj in perm_data:
        new=[-1]*15
        for i,j in enumerate(m):new[di[i]]=sj[j]
        new=tuple(new)
        assert new in matchset
        z.add(new)
    return z
reps=[]
remaining=matchset.copy()
while remaining:
    m=min(remaining)
    o=orbit(m)
    assert o<=remaining
    reps.append((m,o))
    remaining-=o
assert len(reps)==2 and [len(o) for _,o in reps]==[144,144]
FULL=1<<15
vectors=[]
for m,group in reps:
    # frequency of intersection masks with the current matching
    freq=[0]*FULL
    for n in matchings:
        intersection=sum(1<<i for i in range(15) if m[i]==n[i])
        freq[intersection]+=1
    # superset zeta transform: count matching extensions for every chosen edge subset
    for i in range(15):
        bit=1<<i
        for mask in range(FULL):
            if not mask&bit:
                freq[mask]+=freq[mask|bit]
    v=[0]*16
    for mask,ct in enumerate(freq):
        assert ct>=1
        if ct==1:v[mask.bit_count()]+=1
    assert sum(v[k] for k in range(16))<FULL
    assert all(0<=v[k]<=comb(15,k) for k in range(16))
    vectors.append(v)
assert [v[5] for v in vectors]==[240,240]
assert sorted(v[6] for v in vectors)==[1355,1380]
assert all(v[k]==0 for v in vectors for k in range(5))
aggregate=[sum(len(reps[i][1])*vectors[i][k] for i in range(2)) for k in range(16)]
assert aggregate[15]==288 and sum(aggregate)==5443920
print('MATCHINGS=288; S6_ORBITS=144,144')
for i,(m,o) in enumerate(reps):
    print('REP_%d='%i,','.join(map(str,m)))
    print('VECTOR_%d='%i,','.join(map(str,vectors[i])))
print('AGGREGATE=',','.join(map(str,aggregate)))
print('VERIFY_OK')
