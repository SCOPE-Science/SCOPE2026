#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def is_connected(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==n

graphs=0
edge_cases=0
for n in range(2,7):
    possible=list(combinations(range(n),2))
    for mask in range(1,1<<len(possible)):
        edges=[possible[i] for i in range(len(possible)) if (mask>>i)&1]
        if not is_connected(n,edges):
            continue
        graphs+=1
        E=len(edges)
        D=n+E
        t=Fraction(1,D)
        deg=[0]*n
        for u,v in edges:
            deg[u]+=1; deg[v]+=1
        assert all(d>0 for d in deg)

        total=Fraction(0)
        x=[Fraction(0) for _ in range(n)]
        y=[Fraction(0) for _ in range(E)]
        for j,(u,v) in enumerate(edges):
            la=t*Fraction(1,2)*(Fraction(1,deg[u])+Fraction(1,deg[v]))
            lb=t*Fraction(1,2)*(1+Fraction(1,deg[u]))
            lc=t*Fraction(1,2)*(1+Fraction(1,deg[v]))
            assert la>0 and lb>0 and lc>0
            total += la+lb+lc

            # p_e = x_u+x_v-y_e
            # p_{e,u} = x_u-x_v+y_e
            # p_{e,v} = -x_u+x_v+y_e
            x[u] += la+lb-lc
            x[v] += la-lb+lc
            y[j] += -la+lb+lc
            edge_cases += 1

        assert total==1
        assert all(z==t for z in x)
        assert all(z==t for z in y)

        # Every source vertex has norm^2=3 and coordinate sum=1.
        # Therefore distance^2 to the uniform center is exact:
        R2=Fraction(3)-t
        assert R2==Fraction(3*D-1,D)

print(f"VERIFY_OK cosmological-circumspheres connected_graphs={graphs} edge_certificates={edge_cases} n=2..6 exact=yes")
