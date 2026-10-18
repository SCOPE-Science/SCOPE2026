"""Direct, finite verification of color-refinement orbit profiles on multipartite line graphs."""
from itertools import product
from collections import Counter, defaultdict


def graph_for_parts(sizes):
    which = [i for i, a in enumerate(sizes) for _ in range(a)]
    edges = [(i,j) for i in range(len(which)) for j in range(i+1,len(which)) if which[i]!=which[j]]
    adj = [[] for _ in edges]
    for i,(a,b) in enumerate(edges):
        for j in range(i):
            c,d=edges[j]
            if a==c or a==d or b==c or b==d:
                adj[i].append(j)
                adj[j].append(i)
    types=[tuple(sorted((sizes[which[a]],sizes[which[b]]))) for a,b in edges]
    return adj,types


def canonical(l):
    keys={k:i for i,k in enumerate(sorted(set(l)))}
    return [keys[k] for k in l]


def refine(adj,c):
    sig=[(c[i], tuple(sorted(Counter(c[j] for j in adj[i]).items()))) for i in range(len(adj))]
    return canonical(sig)


def equivalent(a,b):
    return all((a[i]==a[j])==(b[i]==b[j]) for i in range(len(a)) for j in range(i))


def target_depth(types):
    seen={tuple(sorted(t)) for t in types}
    if len(seen)==1: return 0
    sums=[sum(t) for t in seen]
    return 1 if len(sums)==len(set(sums)) else 2


def verify():
    count=0;vertices=0;sharp=[]
    for r in range(2,6):
        for sizes in product(range(1,5), repeat=r):
            if list(sizes)!=sorted(sizes) or sum(sizes)>16: continue
            adj,types=graph_for_parts(sizes)
            oracle=canonical(types)
            c=[0]*len(adj)
            depth=target_depth(types)
            for t in range(3):
                if t==depth and not equivalent(c,oracle):
                    raise AssertionError((sizes, 'target',t))
                if t<depth and equivalent(c,oracle):
                    raise AssertionError((sizes,'early',t))
                if t<2: c=refine(adj,c)
            if sizes==(1,2,3,4):
                sharp=[len(set(canonical(types))), len(set(canonical([sum(t) for t in types])))]
            count+=1;vertices+=len(adj)
    assert sharp==[6,5],sharp
    print(f'PASS direct configurations={count}, line-graph vertices aggregated={vertices}; K_(1,2,3,4) orbit classes=6, round-one classes=5, round-two classes=6')

if __name__=='__main__': verify()
