"""Independent finite checks for rectangular torus edge monitoring.
Run: python verify_rectangular_torus.py
Requires Python 3.9+ standard library only.
"""
from collections import deque
from itertools import combinations

EXCEPTIONS = {
    (5, 6): ('.X.X.X', 'XXX.X.', 'X.XXXX', '.X.X.X', 'X.X.X.'),
    (7, 8): ('X.X..X..', '.X.XX..X', 'X.X..XX.', '.X..X..X',
             'X..X..X.', '..XX.X.X', '.X..X.X.'),
}

def sensors(m, n):
    if (m, n) in EXCEPTIONS:
        return EXCEPTIONS[(m, n)]
    offsets = {0, (m+2)//3, (2*m+2)//3}
    return tuple(''.join('X' if ((i-(j*m//n))%m) in offsets else '.'
                         for j in range(n)) for i in range(m))

def gaps(indices, length):
    return [(indices[(k+1)%len(indices)]-indices[k])%length
            for k in range(len(indices))]

def certificate(m, n):
    data=sensors(m,n)
    assert len(data)==m and all(len(row)==n for row in data)
    assert sum(row.count('X') for row in data)==3*n
    for j in range(n):
        v=[i for i in range(m) if data[i][j]=='X']
        assert len(v)==3 and max(gaps(v,m)) <= (m-1)//2
    for i in range(m):
        v=[j for j in range(n) if data[i][j]=='X']
        assert len(v)>=3 and max(gaps(v,n)) <= (n-1)//2

def distance(adjacency, start, end, deleted=None):
    q=deque([(start,0)]); seen={start}
    while q:
        a,d=q.popleft()
        if a==end:return d
        for b in adjacency[a]:
            if deleted is not None and (min(a,b),max(a,b))==deleted:
                continue
            if b not in seen:
                seen.add(b);q.append((b,d+1))
    return float('inf')

def graph(m,n):
    N=m*n
    edges=set()
    for i in range(m):
        for j in range(n):
            u=i*n+j
            for r,c in (((i+1)%m,j),(i,(j+1)%n)):
                v=r*n+c
                if u!=v: edges.add((min(u,v),max(u,v)))
    edges=sorted(edges)
    adj=[set() for _ in range(N)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    return adj,edges

def check_cycle_gap_equivalence():
    count=0
    for n in range(5,12):
        adj=[{(i-1)%n,(i+1)%n} for i in range(n)]
        edges=sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)})
        monitored={}
        for a,b in combinations(range(n),2):
            before=distance(adj,a,b)
            monitored[a,b]=sum((1<<k) for k,e in enumerate(edges)
                               if distance(adj,a,b,e)>before)
        for bits in range(1<<n):
            selected=[i for i in range(n) if bits&(1<<i)]
            actual=0
            for a,b in combinations(selected,2):
                actual |=monitored[a,b]
            actual = actual == (1<<len(edges))-1
            predicted = (len(selected)>=3 and
                         max(gaps(selected,n)) <= (n-1)//2)
            assert actual==predicted, (n, selected)
            count+=1
    return count

def check_original_definition(m,n):
    data=sensors(m,n)
    selected=[i*n+j for i in range(m) for j in range(n)
              if data[i][j]=='X']
    adj,edges=graph(m,n)
    for deleted in edges:
        assert any(distance(adj,u,v,deleted)>distance(adj,u,v)
                   for u,v in combinations(selected,2)),(m,n,deleted)
    return len(edges)

if __name__=='__main__':
    cases=0
    for m in range(5,37):
        for n in range(m,81):
            certificate(m,n);cases+=1
    print('PASS cyclic-gap certificates on',cases,'rectangular grids, 5<=m<=36 and m<=n<=80')
    count=check_cycle_gap_equivalence()
    print('PASS original-definition versus gap equivalence on',count,'cycle subsets (n=5..11)')
    sizes=((5,5),(5,6),(5,7),(5,8),(5,11),(6,6),(6,7),(6,9),
           (7,7),(7,8),(7,9),(8,8),(8,9),(9,10))
    num=sum(check_original_definition(m,n) for m,n in sizes)
    print('PASS original shortest-path distance-change test on',num,
          'edges across',len(sizes),'rectangular tori')
    print('Exceptional optimal placements:')
    for key,data in EXCEPTIONS.items():
        print('  dimensions:',key)
        print('\n'.join('  '+row for row in data))
    print('ALL CHECKS PASSED')
