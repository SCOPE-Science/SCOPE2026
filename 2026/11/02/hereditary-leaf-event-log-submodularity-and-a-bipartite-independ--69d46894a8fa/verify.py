"""Independent finite checks for leaf-set laws in multipartite spanning trees."""
from itertools import product, combinations
from fractions import Fraction
from math import prod
from collections import Counter
import heapq


def multipartitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for k in range(minimum, n+1):
            if k == n:
                yield (k,)
            else:
                for tail in multipartitions(n-k, k):
                    yield (k,)+tail


def prufer_edges(code,n):
    deg=[1]*n
    for x in code:deg[x]+=1
    pq=[i for i in range(n) if deg[i]==1]
    heapq.heapify(pq)
    edges=[]
    for v in code:
        u=heapq.heappop(pq)
        edges.append((u,v))
        deg[u]-=1;deg[v]-=1
        if deg[v]==1:heapq.heappush(pq,v)
    u=heapq.heappop(pq);v=heapq.heappop(pq)
    edges.append((u,v))
    return edges


def count_expected(sizes,s_indices):
    n=sum(sizes);m=len(s_indices);r=len(sizes)
    if m==n:return Fraction(0)
    part=[]
    for k,sz in enumerate(sizes):part.extend([k]*sz)
    s=[sum(part[v]==i for v in s_indices) for i in range(r)]
    out=Fraction(n-m,n)**(r-2)
    for i,sz in enumerate(sizes):
        out*=Fraction(n-sum(s)+s[i]-sz, n-sz)**(sz-1)
    return out


def one_case(sizes):
    n=sum(sizes);r=len(sizes)
    if r<2:return 0,0,0
    part=[]
    for k,sz in enumerate(sizes):part.extend([k]*sz)
    freq=[0]*(1<<n)
    accepted=0
    for code in product(range(n),repeat=n-2):
        edges=prufer_edges(code,n)
        if any(part[u]==part[v] for u,v in edges):continue
        degree=[0]*n
        for u,v in edges:degree[u]+=1;degree[v]+=1
        leafmask=sum(1<<v for v,d in enumerate(degree) if d==1)
        freq[leafmask]+=1;accepted+=1
    moments=freq[:]
    for bit in range(n):
        for m in range(1<<n):
            if not m&(1<<bit): moments[m]+=moments[m|(1<<bit)]
    for mask,count in enumerate(moments):
        assert Fraction(count,accepted)==count_expected(sizes,[i for i in range(n) if mask&(1<<i)]),(sizes,mask,count,accepted,count_expected(sizes,[i for i in range(n) if mask&(1<<i)]))
    comparisons=0
    for a in range(1<<n):
        for b in range(1<<n):
            assert moments[a|b]*moments[a&b] <= moments[a]*moments[b],(sizes,a,b)
            comparisons+=1
    return accepted,len(moments),comparisons


def run():
    total_matchings=total_prob=total_pair=0
    cases=0
    for n in range(3,8):
        for sizes in multipartitions(n):
            if len(sizes)<2:continue
            a,p,c=one_case(sizes)
            cases+=1;total_matchings+=a;total_prob+=p;total_pair+=c
    print('PASS:',cases,'distinct multipartitions,',total_matchings,'admissible trees,',total_prob,'exact joint-event identities,',total_pair,'submodular inequalities')

if __name__=='__main__':run()
