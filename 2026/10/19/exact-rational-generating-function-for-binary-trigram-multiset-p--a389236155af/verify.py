"""Independent finite verification for binary trigram-multispectrum profile theorem."""
from itertools import product
from math import comb

COEFF = [1,8,15,28,52,92,151,240,363,532,757,1048,1416,1880,2449,3140]
EDGES = ((0,0),(0,1),(1,2),(1,3),(2,0),(2,1),(3,2),(3,3))

def direct(n):
    output=set()
    for w in product((0,1),repeat=n):
        counts=[0]*8
        for i in range(n-2):counts[4*w[i]+2*w[i+1]+w[i+2]]+=1
        output.add(tuple(counts))
    return len(output)

def weakly_connected(counts):
    active=set()
    adjacency=[set() for _ in range(4)]
    for k,quantity in enumerate(counts):
        if quantity:
            a,b=EDGES[k]
            active.update((a,b)); adjacency[a].add(b); adjacency[b].add(a)
    if not active:return True
    found={min(active)}
    while True:
        expanded=found|set().union(*(adjacency[v] for v in found))
        if expanded==found:return active==found
        found=expanded

def is_trail(counts):
    if not weakly_connected(counts):return False
    out=[0]*4;inn=[0]*4
    for i,k in enumerate(counts):
        a,b=EDGES[i];out[a]+=k;inn[b]+=k
    delta=[a-b for a,b in zip(out,inn)]
    return all(-1<=x<=1 for x in delta) and (delta.count(1)==delta.count(-1) in (0,1))

def compositions(total,parts):
    if parts==1:
        yield (total,)
    else:
        for k in range(total+1):
            for r in compositions(total-k,parts-1):yield (k,)+r

def by_flows(N):
    return sum(is_trail(c) for c in compositions(N,8))

if __name__=='__main__':
    for n in range(2,18):
        observed=direct(n)
        target=COEFF[n-2]
        assert observed==target,(n,observed,target)
        print('direct',n,observed)
    for N in range(0,14):
        observed=by_flows(N)
        target=COEFF[N]
        assert observed==target,(N,observed,target)
        print('flows',N,observed)
    print('VERIFY_OK: 16 direct counts and 14 independent graph-flow counts')
