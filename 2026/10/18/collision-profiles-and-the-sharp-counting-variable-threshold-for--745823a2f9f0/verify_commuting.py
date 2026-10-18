"""Exact small-order conjugacy and local-profile census for two commuting bijections."""
from itertools import permutations
from collections import Counter, defaultdict

def inverse(p):
    q=[0]*len(p)
    for i,j in enumerate(p): q[j]=i
    return tuple(q)

def compose(p,q):
    return tuple(p[q[x]] for x in range(len(p)))

def profile(p,q):
    ip,iq=inverse(p),inverse(q)
    result=Counter()
    for x in range(len(p)):
        terms=(x,p[x],ip[x],q[x],iq[x])
        classes={}; pattern=[]
        for y in terms:
            if y not in classes: classes[y]=len(classes)
            pattern.append(classes[y])
        result[tuple(pattern)]+=1
    return tuple(sorted(result.items()))

expected=[(1,1,1),(2,4,4),(3,8,8),(4,21,21),(5,39,38),(6,92,82)]
for n,want_iso,want_c2 in expected:
    ps=list(permutations(range(n)))
    pairs={(p,q) for p in ps for q in ps if compose(p,q)==compose(q,p)}
    representatives=[]
    while pairs:
        p,q=min(pairs)
        representatives.append((p,q))
        orbit=set()
        for s in ps:
            t=inverse(s)
            orbit.add((tuple(s[p[t[i]]] for i in range(n)),
                       tuple(s[q[t[i]]] for i in range(n))))
        pairs.difference_update(orbit)
    by_signature=defaultdict(list)
    for p,q in representatives: by_signature[profile(p,q)].append((p,q))
    assert len(representatives)==want_iso
    assert len(by_signature)==want_c2
    print(f'n={n} isomorphism_types={len(representatives)} C2_signatures={len(by_signature)}')
print('commuting census PASS')
