"""Independent check of genuine automorphism-group orbits against WL classes."""
from itertools import product, combinations_with_replacement, permutations
from collections import defaultdict, Counter
from math import prod

def evaluate(ms):
    V=list(product(*[range(m) for m in ms]));idx={v:i for i,v in enumerate(V)};n=len(V)
    pred=[[] for _ in V];succ=[[] for _ in V]
    for i,v in enumerate(V):
        for j,w in enumerate(V):
            if i!=j and all(a<=b for a,b in zip(v,w)):
                succ[i].append(j);pred[j].append(i)
    labels=[0]*n
    for _ in range(sum(m-1 for m in ms)+2):
        sig=[(labels[i],tuple(sorted(Counter(labels[j] for j in pred[i]).items())),tuple(sorted(Counter(labels[j] for j in succ[i]).items()))) for i in range(n)]
        keys={x:k for k,x in enumerate(sorted(set(sig)))}
        new=[keys[x] for x in sig]
        if new==labels:break
        labels=new
    groups=defaultdict(list)
    for i,m in enumerate(ms):groups[m].append(i)
    automaps=[]
    for permseq in product(*[list(permutations(ids)) for ids in groups.values()]):
        mapping=list(range(len(ms)))
        for ids,permuted in zip(groups.values(),permseq):
            for old,new in zip(ids,permuted):mapping[old]=new
        # candidate coordinate automorphism: action x_i -> x_{mapping_i}
        automaps.append([idx[tuple(v[mapping[i]] for i in range(len(ms)))] for v in V])
    orbit_sets=[]
    for i in range(n):orbit_sets.append(frozenset(p[i] for p in automaps))
    assert all((labels[i]==labels[j]) == (j in orbit_sets[i]) for i in range(n) for j in range(n))
    return n,len(set(labels))

if __name__=='__main__':
    tested=0;points=0
    for d in range(1,6):
        for ms in combinations_with_replacement(range(2,6),d):
            if prod(ms)>110:continue
            n,k=evaluate(ms);tested+=1;points+=n
    print('PASS',tested,'independent coordinate-automorphism checks,',points,'vertices')
    print('witness (2,3,4) ->', evaluate((2,3,4)), 'WL-first-round collision vertices (0,2,1) and (1,0,2)')
