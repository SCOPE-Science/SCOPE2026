#!/usr/bin/env python3
"""Complete exact enumeration of prism 3-colouring reconfiguration components.
Only the standard Python library is required. All arithmetic is integral.
"""
from collections import Counter, defaultdict, deque
from math import comb


def coefficient(n, s):
    # Coefficient of z^s in (z^{-1}+1+z)^n.
    if abs(s) > n:
        return 0
    return sum(comb(n, j)*comb(j, (j+s)//2)
               for j in range(abs(s), n+1)
               if (j-s)%2 == 0)


def prescribed(n, w):
    if (n-w)%2 or abs(3*w)>n:
        return (0,0)
    return (6*coefficient(n, 3*w),
            6*n*(coefficient(n-1, 3*w)+coefficient(n-2, 3*w)))


def enumerate_colorings(n):
    # Explicit colours, rather than the sign-transfer representation.
    pairs=[(a,b) for a in range(3) for b in range(3) if a!=b]
    compatibility={p:[q for q in pairs if p[0]!=q[0] and p[1]!=q[1]]
                   for p in pairs}
    result=[]
    def rec(seq):
        if len(seq)==n:
            if seq[-1] in compatibility[seq[0]]:
                result.append(tuple(seq))
            return
        for x in compatibility[seq[-1]]:
            rec(seq+[x])
    for p in pairs: rec([p])
    return result


def winding(seq):
    n=len(seq)
    inc=[1 if (seq[(i+1)%n][0]-seq[i][0])%3==1 else -1 for i in range(n)]
    assert sum(inc)%3==0
    return sum(inc)//3


def neighbors(seq):
    n=len(seq)
    for i in range(n):
        for row in range(2):
            current=seq[i][row]
            occupied={seq[i][1-row],seq[(i-1)%n][row],seq[(i+1)%n][row]}
            for new in range(3):
                if new==current or new in occupied:
                    continue
                change=list(seq)
                replacement=list(change[i]); replacement[row]=new
                change[i]=tuple(replacement)
                yield tuple(change)


def test(n):
    colorings=enumerate_colorings(n)
    ids={x:i for i,x in enumerate(colorings)}
    adj=[set() for _ in colorings]
    for i,x in enumerate(colorings):
        for y in neighbors(x):
            j=ids[y]
            assert i!=j
            adj[i].add(j)
    assert all(i in adj[j] for i, row in enumerate(adj) for j in row)
    components=[]; unseen=set(range(len(colorings)))
    while unseen:
        i=unseen.pop(); queue=[i]; c={i}
        while queue:
            u=queue.pop()
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v);c.add(v);queue.append(v)
        components.append(c)
    by_w=defaultdict(list)
    for c in components:
        ww={winding(colorings[u]) for u in c}
        assert len(ww)==1
        w=ww.pop()
        count=len(c)
        edges=sum(len(adj[u]) for u in c)//2
        by_w[w].append((count,edges))
    W=[w for w in range(-n//3-1,n//3+2)
       if 3*w>=-n and 3*w<=n and (w-n)%2==0]
    assert set(by_w)==set(W)
    for w in W:
        size,edges=prescribed(n,w)
        if 3*abs(w)==n:
            assert by_w[w]==[(1,0)]*6, (n,w,by_w[w])
            assert size==6 and edges==0
        else:
            assert by_w[w]==[(size,edges)],(n,w,by_w[w],size,edges)
    assert sum(size for w,group in by_w.items() for size,e in group)==len(colorings)
    assert len(colorings)==3**n+1+2*(-2)**n
    print('n=%d colorings=%d components=%d components_by_w=%s' %
          (n,len(colorings),len(components),dict(sorted(by_w.items()))))

if __name__=='__main__':
    for n in range(3,11):test(n)
    print('PRISM_DIRECT_COMPONENTS_PASS')
