"""Exhaustive, standalone snub cubical Ising field census, no third-party packages.

Run: python3 verify_field_census.py snub_edges.txt
Reads 60 labelled edges; checks shape and computes every one of 2**24 configurations
using two independent traversal recurrences (Gray flip and increasing subsets).
"""
import sys
from array import array
from collections import Counter
from fractions import Fraction

N=24
EXPECTED_B=(0,5,10,15,20,25,30,35,40,41,42,43,44)
EXPECTED_C=(1,24,216,912,1854,1680,564,48,3,24,84,72,18)

def load_graph(path):
    edges=[]
    for line in open(path,encoding='ascii'):
        line=line.strip()
        if not line or line.startswith('#'): continue
        i,j=map(int,line.split())
        assert 0<=i<j<N
        edges.append((i,j))
    assert len(edges)==60 and len(set(edges))==60
    adj=[0]*N
    for i,j in edges:adj[i]|=1<<j;adj[j]|=1<<i
    assert all(a.bit_count()==5 for a in adj)
    return edges,adj

def census_gray(adj):
    best=[-1]*(N+1);counts=[0]*(N+1)
    state=0; size=0; cut=0
    best[0]=0;counts[0]=1
    for z in range(1,1<<N):
        bit=z&-z; i=bit.bit_length()-1
        old_up=bool(state&bit)
        u=(state&adj[i]).bit_count()
        cut+=(2*u-5) if old_up else (5-2*u)
        size+=-1 if old_up else 1
        state ^=bit
        if cut>best[size]:best[size]=cut;counts[size]=1
        elif cut==best[size]:counts[size]+=1
    assert state==1<<(N-1) and size==1
    return best,counts

def census_subsets(adj):
    # A different recurrence, processing each subset in increasing integer order:
    # cut(S)=cut(S\\{v})+deg(v)-2*|N(v) intersect (S\\{v})|, v=minimum element.
    cuts=array('B',[0])*(1<<N)
    best=[-1]*(N+1);counts=[0]*(N+1)
    best[0]=0;counts[0]=1
    for mask in range(1,1<<N):
        bit=mask&-mask; i=bit.bit_length()-1; prev=mask^bit
        b=cuts[prev]+5-2*(adj[i]&prev).bit_count()
        assert 0<=b<=60
        cuts[mask]=b; k=mask.bit_count()
        if b>best[k]:best[k]=b;counts[k]=1
        elif b==best[k]:counts[k]+=1
    return best,counts

def phase_summary(best,counts):
    # E = J*(60-2*max_cut), M = 2*k-24
    levels=[(2*k-N, 60-2*b, counts[k]) for k,b in enumerate(best)]
    for k in range(N+1):
        assert best[k]==best[N-k] and counts[k]==counts[N-k]
    def chosen(field):
        e0=min(Fraction(e)-field*m for m,e,c in levels)
        return [(m,e,c) for m,e,c in levels if Fraction(e)-field*m==e0]
    checks={
        Fraction(0):([(0,-28,18)]),
        Fraction(1,2):([(0,-28,18)]),
        Fraction(1):([(m,60-2*best[(m+24)//2],counts[(m+24)//2]) for m in (0,2,4,6,8)]),
        Fraction(3):([(8,-20,3)]),
        Fraction(5):([(m,60-2*best[(m+24)//2],counts[(m+24)//2]) for m in range(8,25,2)]),
        Fraction(6):([(24,60,1)]),
    }
    for h,want in checks.items():
        got=chosen(h)
        assert got==want,(h,got,want)
    # Find all candidate positive crossing fields; certify no other envelope changes
    cs={Fraction(0)}
    for m,e,c in levels:
        for n,f,d in levels:
            if m<n:
                t=Fraction(f-e,n-m)
                if t>=0:cs.add(t)
    ts=sorted(cs)
    intervals=[]
    for j,t in enumerate(ts):
        h=(t+ts[j+1])/2 if j+1<len(ts) else t+1
        sol=chosen(h)
        assert len(sol)==1
        intervals.append((h,sol[0][0]))
    assert set(m for h,m in intervals)=={0,8,24}
    real_cross=[t for t in ts if len(chosen(t))>1]
    assert real_cross==[Fraction(1),Fraction(5)]
    assert sum(c for _,_,c in chosen(Fraction(1)))==201
    assert sum(c for _,_,c in chosen(Fraction(5)))==5302
    return real_cross

def main():
    _,adj=load_graph(sys.argv[1] if len(sys.argv)>1 else 'snub_edges.txt')
    a=census_gray(adj)
    b=census_subsets(adj)
    assert a==b, (a,b)
    best,counts=a
    assert tuple(best[:13])==EXPECTED_B,(best[:13],EXPECTED_B)
    assert tuple(counts[:13])==EXPECTED_C,(counts[:13],EXPECTED_C)
    assert sum(counts[k] for k in range(N+1))>0
    print('COMPLETE: 2**24=16777216 spin states traversed in each of two independent enumerations')
    print('k B_k N_k for k=0..12:')
    for k in range(13):print(k,best[k],counts[k])
    print('positive critical field ratios h/J:',*[str(t) for t in phase_summary(best,counts)])
    print('degeneracies h=0, h/J=1, 1<h/J<5, h/J=5, h/J>5: 18 201 3 5302 1')
    print('PASS')
if __name__=='__main__':main()
