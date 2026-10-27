"""Independent construction with frozenset triple hyperedges and explicit swaps.

Requires Python 3.9+ standard library; run: python verify_pairwise.py
"""
from itertools import combinations
from collections import deque
from math import comb


def check(n):
    U = frozenset(range(n))
    all_triples = {frozenset(t) for t in combinations(U, 3)}
    family = []
    labels = []
    for triangle in combinations(U, 3):
        triangle = frozenset(triangle)
        f = frozenset(t for t in all_triples if len(t & triangle) >= 2)
        labels.append(('triangle', tuple(sorted(triangle))))
        family.append(f)
    for center in range(n):
        for special in combinations(U - {center}, 3):
            s = frozenset(special)
            f = frozenset([s]+[t for t in all_triples if center in t and t & s])
            labels.append(('hilton', center, tuple(sorted(s))))
            family.append(f)
    assert len(family) == (n-2)*comb(n, 3)
    assert len(set(family)) == len(family)
    for f in family:
        assert len(f) == 3*n-8
        assert not frozenset.intersection(*f)
        assert all(a & b for a, b in combinations(f, 2))
    E = set()
    for i in range(len(family)):
        for j in range(i):
            diff = len(family[i]-family[j])
            assert diff >= n-4
            if diff == n-4: E.add((j, i))
    assert len(E) == (n-2)*comb(n, 3)*3*(n-3)//2
    adj = [set() for _ in family]
    for i,j in E: adj[i].add(j);adj[j].add(i)
    assert all(len(q)==3*(n-3) for q in adj)
    expected = set()
    for i in range(len(labels)):
        for j in range(i):
            a,b=labels[i],labels[j]
            if a[0]==b[0]=='hilton' and a[1]==b[1] and len(set(a[2]) & set(b[2]))==2:
                expected.add((j,i))
            elif a[0]!=b[0]:
                h = a if a[0]=='hilton' else b
                t = a if a[0]=='triangle' else b
                if h[1] in t[1] and set(t[1])-{h[1]}<=set(h[2]):
                    expected.add((j,i))
    assert E==expected
    def radius(source):
        ds=[-1]*len(family);ds[source]=0
        q=deque([source])
        while q:
            i=q.popleft()
            for j in adj[i]:
                if ds[j]<0:ds[j]=ds[i]+1;q.append(j)
        return max(ds), ds.count(-1)
    assert radius(0)==(5,0)
    assert radius(comb(n,3))==(5,0)
    if n==7:
        assert all(radius(i)[0]==5 for i in range(len(family)))
    print('n=%d families=%d threshold=%d edges=%d degree=%d radius=diameter=5' %
          (n,len(family),n-4,len(E),3*(n-3)))

if __name__=='__main__':
    for n in (7,8,9):check(n)
    print('PASS: independent finite hyperedge construction and exact exchange graph')
