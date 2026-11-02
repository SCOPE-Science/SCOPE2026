"""Independent finite-field tests for radical-square-zero quiver unit groups.

No external packages are required. Execute with: python verify.py.
"""
from collections import Counter
from itertools import product
from math import prod


def field(q):
    if q == 4:
        # F_2[a]/(a^2+a+1), encoded using 0,1,a,1+a.
        add = lambda a, b: a ^ b
        def mul(a, b):
            out = 0
            for i in range(2):
                for j in range(2):
                    if (a >> i) & (b >> j) & 1:
                        out ^= 1 << (i+j)
            if out & 4:
                out ^= 7
            return out
        return add, mul, 2, (1, 2)
    assert q in (2, 3, 5)
    return (lambda a,b:(a+b)%q), (lambda a,b:(a*b)%q), (1 if q == 2 else 2), (1,)


def graph_rank(n, edges):
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for u, v in edges:
        a,b = find(u),find(v)
        if a != b:
            parent[a]=b
    return n-len({find(i) for i in range(n)})


def predicted(n,arrows,q):
    Q=q-1
    loops=sum(u==v for u,v in arrows)
    classes=Counter(tuple(sorted((u,v))) for u,v in arrows if u != v)
    pair_edges=list(classes)
    degrees=Counter()
    for mask in range(1<<len(pair_edges)):
        S=[e for i,e in enumerate(pair_edges) if mask>>i & 1]
        r=graph_rank(n,S)
        beta=len(S)-r
        components=n-r
        ways=(q**loops)*(Q**(components+beta))
        for e in S:
            ways*=sum(q**j for j in range(classes[e]))
        degrees[Q**r] += ways
    return degrees


def independent_test(n, edges, q):
    add,mul,primitive,basis=field(q)
    Q=q-1
    nonzero=tuple(range(1,q))
    inv={x:next(y for y in nonzero if mul(x,y)==1) for x in nonzero}
    neg=lambda a:next(b for b in range(q) if add(a,b)==0)
    m=len(edges)
    def times(x,y):
        d,a=x; e,b=y
        return (tuple(mul(d[i],e[i]) for i in range(n)),
                tuple(add(mul(d[u],b[k]),mul(a[k],e[v]))
                      for k,(u,v) in enumerate(edges)))
    def inverse(x):
        d,a=x
        di=tuple(inv[t] for t in d)
        return (di,tuple(neg(mul(mul(di[u],a[k]),di[v]))
                         for k,(u,v) in enumerate(edges)))
    # Directly enumerate characters of the additive radical and their diagonal-torus orbits.
    torus=list(product(nonzero,repeat=n))
    chars=set(product(range(q),repeat=m))
    orbit_count=Counter()
    while chars:
        base=next(iter(chars))
        orbit={tuple(mul(base[k],mul(d[v],inv[d[u]]))
                     for k,(u,v) in enumerate(edges)) for d in torus}
        assert orbit <= chars
        chars-=orbit
        degree=len(orbit)
        stabilizers=len(torus)//degree
        orbit_count[degree]+=stabilizers
    want=predicted(n,edges,q)
    assert orbit_count == want,(n,edges,q,orbit_count,want)
    order=(q-1)**n*q**m
    assert sum(multiplicity*degree*degree for degree,multiplicity in orbit_count.items())==order
    # Enumerate actual group conjugacy orbits, independently of the dual-orbit formula.
    group={(d,a) for d in torus for a in product(range(q),repeat=m)}
    assert len(group)==order
    one=(tuple([1]*n),tuple([0]*m))
    generators=[]
    for i in range(n):
        t=[1]*n;t[i]=primitive
        generators.append((tuple(t),one[1]))
    for k in range(m):
        for b in basis:
            a=[0]*m;a[k]=b
            generators.append((one[0],tuple(a)))
    conjugators=[(g,inverse(g)) for g in generators]
    pending=set(group)
    class_sizes=Counter()
    while pending:
        representative=pending.pop()
        seen={representative}
        stack=[representative]
        while stack:
            x=stack.pop()
            for g,gi in conjugators:
                y=times(times(g,x),gi)
                if y not in seen:
                    assert y in pending,(n,edges,q,y)
                    pending.remove(y)
                    seen.add(y)
                    stack.append(y)
        class_sizes[len(seen)]+=1
    assert sum(class_sizes.values())==sum(orbit_count.values()), (n,edges,q,class_sizes,orbit_count)
    assert sum(size*mult for size,mult in class_sizes.items())==order
    return order,dict(sorted(orbit_count.items())),dict(sorted(class_sizes.items()))


def main():
    cases=[
        (1,[],2),(1,[],3),(1,[(0,0)],3),(1,[(0,0),(0,0)],4),
        (2,[],3),(2,[(0,1)],2),(2,[(0,1)],3),
        (2,[(0,1)],4),(2,[(0,1)],5),
        (2,[(0,1),(0,1)],3),
        (2,[(0,1),(1,0)],4),
        (2,[(0,0),(0,1)],3),
        (3,[(0,1),(1,2)],3),
        (3,[(0,2),(1,2)],4),
        (3,[(0,1),(1,2),(2,0)],3),
        (3,[(0,0),(0,1),(1,0),(2,1)],3),
        (4,[(0,2),(1,2),(1,3)],3),
        (4,[(0,2),(0,3),(1,2),(1,3)],3),
        (4,[(0,2),(1,3)],4),
    ]
    for n,edges,q in cases:
        order, degrees, classes=independent_test(n,edges,q)
        print('case',n,edges,q,'order',order,'character degrees',degrees,
              'conjugacy class sizes',classes)
    print('VERIFY_OK',len(cases),'direct conjugacy censuses, diagonal-dual orbit censuses, degree-sum checks')

if __name__=='__main__':
    main()
