from fractions import Fraction
from itertools import combinations, product


def connected(n, edges):
    adj=[[] for _ in range(n)]
    for i,j in edges:
        adj[i].append(j); adj[j].append(i)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for u in adj[v]:
            if u not in seen:
                seen.add(u); stack.append(u)
    return len(seen)==n


def cut_weight(mask, edges, weights):
    s=0
    for (i,j),w in zip(edges,weights):
        if ((mask>>i)&1) != ((mask>>j)&1):
            s += w
    return s


def phi2_sq(n, edges, weights):
    best=None
    for mask in range(1,(1<<n)-1):
        k=mask.bit_count()
        cw=cut_weight(mask,edges,weights)
        val=Fraction(cw*cw*n, k*(n-k))
        if best is None or val < best:
            best=val
    return best


def tv(x, edges, weights):
    return sum(w*abs(x[i]-x[j]) for (i,j),w in zip(edges,weights))


graphs=0
weightings=0
vector_checks=0
cut_checks=0
for n in range(2,6):
    all_edges=list(combinations(range(n),2))
    for emask in range(1,1<<len(all_edges)):
        edges=[e for k,e in enumerate(all_edges) if (emask>>k)&1]
        if not connected(n,edges):
            continue
        graphs += 1
        weight_sets=[]
        weight_sets.append(tuple(1 for _ in edges))
        weight_sets.append(tuple(1+(k%3) for k,_ in enumerate(edges)))
        for weights in weight_sets:
            weightings += 1
            p2=phi2_sq(n,edges,weights)
            attained=False
            for mask in range(1,(1<<n)-1):
                k=mask.bit_count()
                cw=cut_weight(mask,edges,weights)
                ratio2=Fraction(cw*cw*n,k*(n-k))
                assert ratio2 >= p2
                attained |= ratio2 == p2
                cut_checks += 1
            assert attained
            for x in product((-1,0,1), repeat=n):
                if not any(x) or sum(x)!=0:
                    continue
                lhs=tv(x,edges,weights)
                norm2=sum(a*a for a in x)
                assert Fraction(lhs*lhs, norm2) >= p2
                vector_checks += 1

print(f"VERIFY_OK graphical-zonotope-inradius connected_graphs={graphs} weightings={weightings} cut_checks={cut_checks} vector_checks={vector_checks} n=2..5")
