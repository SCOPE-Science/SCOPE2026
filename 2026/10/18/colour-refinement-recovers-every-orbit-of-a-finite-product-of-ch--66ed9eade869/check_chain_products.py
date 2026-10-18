"""Verify colour-refinement/orbit equality in finite products of chains.
Only finite corroboration, not proof of the unbounded statement.
"""
from collections import Counter, defaultdict
from itertools import product, combinations_with_replacement
from math import factorial, comb

def check(ms):
    vertices=list(product(*[range(m) for m in ms]))
    n=len(vertices); down=[[] for _ in vertices]; up=[[] for _ in vertices]
    for i,x in enumerate(vertices):
        for j,y in enumerate(vertices):
            if i!=j and all(a<=b for a,b in zip(x,y)):
                up[i].append(j);down[j].append(i)
    colors=[0]*n
    H=sum(m-1 for m in ms)
    for step in range(H+1):
        signatures=[(colors[i],tuple(sorted(Counter(colors[j] for j in down[i]).items())),tuple(sorted(Counter(colors[j] for j in up[i]).items()))) for i in range(n)]
        table={v:k for k,v in enumerate(sorted(set(signatures)))}
        colors=[table[z] for z in signatures]
    orbits=[tuple((m,tuple(sorted(x[i] for i in range(len(ms)) if ms[i]==m))) for m in sorted(set(ms))) for x in vertices]
    # Both refinements (not only their cardinality) must agree with orbit classes.
    ids_by_orbit={v:i for i,v in enumerate(sorted(set(orbits)))}
    bycolor=defaultdict(set);byorbit=defaultdict(set)
    for c,o in zip(colors,orbits):
        bycolor[c].add(ids_by_orbit[o]);byorbit[ids_by_orbit[o]].add(c)
    assert all(len(v)==1 for v in bycolor.values())
    assert all(len(v)==1 for v in byorbit.values())
    expected=1
    for m,r in Counter(ms).items():expected*=comb(r+m-1,m-1)
    assert len(bycolor)==expected
    for o in set(orbits):
        size=1
        for m,coords in o:
            c=Counter(coords);r=len(coords)
            size*=factorial(r)//__import__('math').prod(factorial(v) for v in c.values())
        assert sum(z==o for z in orbits)==size
    # A certificate using just rank and D/U of cover vertices, not the final WL color.
    rank=[sum(v) for v in vertices];D=[len(d)+1 for d in down];U=[len(d)+1 for d in up]
    for i,x in enumerate(vertices):
        pairs=[]
        for j in down[i]:
            if rank[j]==rank[i]-1:
                a=D[j]//(D[i]-D[j]);b=U[i]//(U[j]-U[i])-1
                # Divisions are integer for these one-coordinate covering ratios.
                assert a>0 and D[j]*(a+1)==D[i]*a and U[j]*(b+1)==U[i]*(b+2)
                pairs.append((a,b))
        for j in up[i]:
            if rank[j]==rank[i]+1:
                a=D[i]//(D[j]-D[i])-1;b=U[j]//(U[i]-U[j])
                if a==0:
                    assert D[j]*(a+1)==D[i]*(a+2) and U[i]*b==U[j]*(b+1)
                    pairs.append((a,b))
        assert sorted(pairs)==sorted((a,m-1-a) for a,m in zip(x,ms))
    return n,len(bycolor)

if __name__=='__main__':
    tests=0; vertices=0;maxn=0
    for d in range(1,6):
        for ms in combinations_with_replacement(range(2,7),d):
            n=__import__('math').prod(ms)
            if n>220:continue
            count,c=check(ms)
            tests+=1;vertices+=count;maxn=max(maxn,n)
    print(f'PASS {tests} chain-product configurations, {vertices} vertices, largest instance {maxn}')
    for ms in [(3,3,4),(3,4,5),(2,2,2,2,3)]:
        n,k=check(ms);print('witness',ms,'vertices',n,'orbits',k)
