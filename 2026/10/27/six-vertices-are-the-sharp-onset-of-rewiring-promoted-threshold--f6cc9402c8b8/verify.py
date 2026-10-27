"""Exact enumeration for connected simple graphs of order <=5.
One homophilic active-edge rewiring, followed by deterministic strict-fraction threshold closure.
No external dependencies; Python 3.8+.
"""
from fractions import Fraction
from itertools import combinations

def connected(adj):
    seen=1
    while True:
        nxt=seen
        for j,x in enumerate(adj):
            if seen>>j&1:nxt|=x
        if nxt==seen:return seen==(1<<len(adj))-1
        seen=nxt

def closure(adj, seed, num,den):
    adopted=seed
    while True:
        nxt=adopted
        for j,nb in enumerate(adj):
            if not (adopted>>j&1) and (nb&adopted).bit_count()*den>num*nb.bit_count():
                nxt|=1<<j
        if nxt==adopted:return adopted
        adopted=nxt

def threshold_set(n):
    # All discontinuity points k/d in [0,1] plus a representative of every open cell.
    bounds=sorted({Fraction(k,d) for d in range(1,n) for k in range(d+1)}|{Fraction(0),Fraction(1)})
    return sorted(set(bounds)|{(x+y)/2 for x,y in zip(bounds,bounds[1:])})

def verify_small():
    total_initial=total_cases=total_rewires=0
    byorder={}
    for n in range(2,6):
        edges=list(combinations(range(n),2))
        ngraphs=nseeds=ncases=nrewires=0
        for graph_code in range(1<<len(edges)):
            adj=[0]*n
            for bit,(i,j) in enumerate(edges):
                if graph_code>>bit&1:
                    adj[i]|=1<<j; adj[j]|=1<<i
            if not connected(adj):continue
            ngraphs+=1
            for seed in range(1,(1<<n)-1):
                nseeds+=1
                for th in threshold_set(n):
                    base=closure(adj,seed,th.numerator,th.denominator)
                    ncases+=1
                    if base==(1<<n)-1:continue
                    for a in range(n):
                        if not (seed>>a&1):continue
                        for v in range(n):
                            if seed>>v&1 or not adj[a]>>v&1:continue
                            for w in range(n):
                                if w==v or (seed>>w&1) or (adj[v]>>w&1):continue
                                new=adj.copy()
                                new[a]^=1<<v;new[v]^=1<<a
                                new[v]|=1<<w;new[w]|=1<<v
                                final=closure(new,seed,th.numerator,th.denominator)
                                nrewires+=1
                                assert final.bit_count()<=base.bit_count(),(n,adj,seed,th,a,v,w,base,final)
        byorder[n]=(ngraphs,nseeds,ncases,nrewires)
        print('verified order',n,'connected graphs',ngraphs,'seed configurations',nseeds,'threshold configurations',ncases,'admissible rewiring tests',nrewires)
        total_initial+=ngraphs;total_cases+=ncases;total_rewires+=nrewires
    print('TOTAL',total_initial,total_cases,total_rewires)

def verify_witness():
    n=6
    adj=[0]*n
    for i,j in [(0,2),(0,4),(0,5),(1,2),(1,3)]:
        adj[i]|=1<<j;adj[j]|=1<<i
    seed=(1<<2)|(1<<3)
    assert connected(adj)
    a,v,w=2,1,0
    modified=adj.copy()
    modified[a]^=1<<v;modified[v]^=1<<a
    modified[v]|=1<<w; modified[w]|=1<<v
    assert connected(modified)
    assert sum(x.bit_count() for x in adj)==10
    assert sum(x.bit_count() for x in modified)==10
    static=closure(adj,seed,1,3)
    changed=closure(modified,seed,1,3)
    assert static==sum(1<<i for i in (1,2,3))
    assert changed==(1<<6)-1
    print('witness verified: initial tree edges [(0,2),(0,4),(0,5),(1,2),(1,3)], seeds {2,3}, theta=1/3; rewire (2,1)->(0,1); baseline 3 vs modified 6')

if __name__=='__main__':
    verify_small()
    verify_witness()
