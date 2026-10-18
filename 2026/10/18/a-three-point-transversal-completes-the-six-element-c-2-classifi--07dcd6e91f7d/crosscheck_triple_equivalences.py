"""Independent exact Burnside and pairwise checks for three equivalences."""
import itertools, collections, math
from verify_triple_equivalences import partitions, get_objs, wl

def renorm(seq):
    d={};out=[]
    for v in seq:
        if v not in d:d[v]=len(d)
        out.append(d[v])
    return tuple(out)

def independent_orbit_count(n):
    p=partitions(n); total=0
    for perm in itertools.permutations(range(n)):
        fixed=sum(renorm(q[i] for i in perm)==q for q in p)
        total+=fixed**3
    assert total % math.factorial(n)==0
    return total//math.factorial(n)

def exact_iso(a,b):
    n=len(a[0]);
    for pi in itertools.permutations(range(n)):
        if all(all((pa[i]==pa[j])==(pb[pi[i]]==pb[pi[j]]) for i in range(n) for j in range(n)) for pa,pb in zip(a,b)):
            return True
    return False

def pair_wl_independent(a,b):
    n=len(a[0]); structs=(a,b); colors=[[0]*n for _ in range(2)]
    for rnd in range(2*n+1):
        new=[]; all_sigs=[]
        for s in range(2):
            cols=[]
            for i in range(n):
                a1,a2,a3=structs[s]
                sig=(colors[s][i],tuple(sorted((int(a1[i]==a1[j]),int(a2[i]==a2[j]),int(a3[i]==a3[j]),colors[s][j]) for j in range(n) if i!=j)))
                cols.append(sig);all_sigs.append(sig)
            new.append(cols)
        unique={v:k for k,v in enumerate(sorted(set(all_sigs)))}
        colors=[[unique[sig] for sig in arr] for arr in new]
    return collections.Counter(colors[0])==collections.Counter(colors[1])

if __name__=='__main__':
    print('Burnside classes:')
    for n in range(1,7):
        b=independent_orbit_count(n)
        pp,objs,_=get_objs(n)
        assert b==len(objs)
        print(n,b)
    pp,objs,_=get_objs(6)
    buckets=wl(pp,objs,6)
    groups=[ids for ids in buckets.values() if len(ids)>1]
    assert len(groups)==8 and all(len(g)==2 for g in groups)
    for k,pair in enumerate(groups,1):
        a,b=(tuple(pp[t] for t in objs[i]) for i in pair)
        assert not exact_iso(a,b)
        assert pair_wl_independent(a,b)
        print('doubleton',k,'noniso and C2 equivalent',objs[pair[0]],objs[pair[1]])
    # classify the eight doubletons under permutations of relation labels
    # map all iso representative triples to index for name-swaps
    key_to_i={tuple(x):i for i,x in enumerate(objs)}
    # we need canonicalize per first-part E under relabelings
    perms=list(itertools.permutations(range(6)))
    def code(tr):
        return min(tuple(renorm(p[i] for i in perm) for p in tr) for perm in perms)
    normalized_pairs={frozenset(code(tuple(pp[t] for t in objs[i])) for i in g):j for j,g in enumerate(groups)}
    def act_pair(g,perm):
        return frozenset(code(tuple(pp[objs[i][j]] for j in perm)) for i in g)
    orbits=[];unseen=set(range(len(groups)))
    while unseen:
        k=min(unseen)
        orbit={normalized_pairs[act_pair(groups[k],p)] for p in itertools.permutations(range(3))}
        assert orbit <=set(range(len(groups)))
        unseen-=orbit;orbits.append(sorted(orbit))
    print('relation-name symmetry orbits',orbits)
