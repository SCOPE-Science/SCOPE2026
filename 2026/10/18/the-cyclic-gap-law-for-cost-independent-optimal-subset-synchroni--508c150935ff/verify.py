"""Reproduce cyclic-gap synchronization statements for finite automata.
Uses only the Python standard library; no external datasets.
"""
from heapq import heappush, heappop
from collections import deque
from itertools import combinations
from random import Random


def act(n, mask, letter):
    if letter == 'a':
        return ((mask << 1) & ((1 << n) - 1)) | (mask >> (n - 1))
    assert letter == 'b'
    return ((mask & ((1 << (n-1))-1)) | (1 if (mask >> (n-1)) else 0))


def gap_data(n, mask):
    points = [j for j in range(n) if (mask >> j) & 1]
    if len(points) <= 1:
        return None
    gs = [((points[(j+1) % len(points)] - points[j]) % n,
           points[(j+1) % len(points)]) for j in range(len(points))]
    G = max(g for g,t in gs)
    t = max(t for g,t in gs if g == G)
    return G, t


def potential(n, mask, alpha, beta):
    dat=gap_data(n, mask)
    if dat is None:
        return 0
    G,t=dat
    return (n-G)*((n-1)*alpha+beta)-alpha*t


def prescribed(n, mask):
    G,t=gap_data(n,mask)
    r=n-G
    return 'a'*(n-1-t)+'b'+('a'*(n-1)+'b')*(r-1)


def reverse_distance(n, alpha, beta):
    size=1<<n
    top=1<<(n-1)
    dist=[None]*size
    pq=[]
    for i in range(n):
        m=1<<i;dist[m]=0;heappush(pq,(0,m))
    while pq:
        d,s=heappop(pq)
        if d!=dist[s]:continue
        # Inverse of the cyclic rotation a.
        t=(s>>1)|((s&1)<<(n-1))
        z=d+alpha
        if dist[t] is None or z<dist[t]:dist[t]=z;heappush(pq,(z,t))
        # Every predecessor of the collapsing letter b.
        if s&top:continue
        preds=(s,s|top,(s^1)|top) if s&1 else (s,)
        z=d+beta
        for t in preds:
            if dist[t] is None or z<dist[t]:dist[t]=z;heappush(pq,(z,t))
    return dist


def check():
    count=0
    for n in range(2,17):
        for mask in range(1,1<<n):
            if mask.bit_count()==1:continue
            G,t=gap_data(n,mask)
            optimal='b' if t==n-1 else 'a'
            for alpha,beta in [(1,1),(2,5),(7,1),(1,11)]:
                v=potential(n,mask,alpha,beta)
                drops={letter:v-potential(n,act(n,mask,letter),alpha,beta)
                       for letter in 'ab'}
                assert drops[optimal]=={'a':alpha,'b':beta}[optimal],(n,mask,drops,alpha,beta)
                other='a' if optimal=='b' else 'b'
                assert drops[other]<{'a':alpha,'b':beta}[other],(n,mask,drops,alpha,beta)
            count+=1
        if n<=12:
            for alpha,beta in [(1,1),(2,5),(7,1)]:
                dist=reverse_distance(n,alpha,beta)
                for mask in range(1,1<<n):
                    assert dist[mask]==potential(n,mask,alpha,beta),(n,mask,dist[mask])
        print('n',n,'Bellman checked', (1<<n)-n-1, 'Dijkstra', n<=12)
    rng=Random(374893)
    for n in list(range(2,20))+[32,50,80,128]:
        masks=list(range(1,1<<n)) if n<=9 else [rng.randrange(1,1<<n) for _ in range(150)]
        for mask in masks:
            if mask.bit_count()<=1:continue
            word=prescribed(n,mask)
            result=mask
            for letter in word:
                result=act(n,result,letter)
            assert result.bit_count()==1,(n,mask,word)
            assert word.count('a')+2*word.count('b')==potential(n,mask,1,2),(n,mask)
    print('VERIFICATION_OK; checked',count,'non-singleton subsets by weighted strict Bellman inequalities')

if __name__=='__main__':check()
