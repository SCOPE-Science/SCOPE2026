"""Independent ascending-set dynamic programming for domination-game scores.

Run: python3 verify_tabular.py
Every covered-vertex mask is computed, even if unreachable in a game.
"""
from collections import defaultdict, Counter

def heawood():
    # Nonzero binary vectors represent Fano points and covectors;
    # incidence is the zero inner product over F_2.
    graph=[0]*14
    for x in range(1,8):
        for z in range(1,8):
            if ((x&z).bit_count()&1)==0:
                a=x-1;b=7+z-1
                graph[a]|=1<<b;graph[b]|=1<<a
    return graph

def pappus():
    # Independently construct the nine point triples on each line:
    # each of the three Latin squares defines one parallel class.
    graph=[0]*18
    for m in range(3):
        for b in range(3):
            line=9+3*m+b
            for x in range(3):
                y=(m*x+b)%3
                point=3*x+y
                graph[point]|=1<<line
                graph[line]|=1<<point
    return graph

def all_dist(graph):
    n=len(graph)
    dd=[]
    for v in range(n):
        distances=[100]*n;distances[v]=0
        wave=1<<v;visited=wave;radius=0
        while wave:
            nxt=0
            for i in range(n):
                if wave>>i&1:nxt|=graph[i]
            nxt &= ~visited
            radius+=1
            for i in range(n):
                if nxt>>i&1:distances[i]=radius
            visited|=nxt;wave=nxt
        assert all(q<100 for q in distances)
        dd.append(distances)
    return dd

def evaluate(name, graph, expected):
    n=len(graph);full=(1<<n)-1
    assert all(v.bit_count()==3 for v in graph)
    assert all((graph[i]>>j&1)==(graph[j]>>i&1) for i in range(n) for j in range(n))
    N=[graph[i]|(1<<i) for i in range(n)]
    valsD=bytearray(full+1);valsS=bytearray(full+1)
    # Each legal transition enlarges the covered-vertex bitmask,
    # so processing masks in decreasing integer order is a topological order.
    for mask in range(full-1,-1,-1):
        lo=255;hi=0
        for k in N:
            if k&~mask:
                nxt=mask|k
                x=1+valsS[nxt];y=1+valsD[nxt]
                if x<lo:lo=x
                if y>hi:hi=y
        valsD[mask]=lo;valsS[mask]=hi
    assert (valsD[0],valsS[0])==expected
    dd=all_dist(graph)
    patterns=[]
    for player in (0,1):
        tables=[]
        for first in range(n):
            groups=defaultdict(Counter)
            for second in range(n):
                union=N[first]|N[second]
                if union!=N[first]:
                    score=2+(valsD[union] if player==0 else valsS[union])
                    groups[dd[first][second]][int(score)]+=1
            tables.append(tuple((d,tuple(sorted(c.items()))) for d,c in sorted(groups.items())))
        assert len(set(tables))==1,(name,tables)
        patterns.append(tables[0])
    if name=='Heawood':
        assert patterns==[
            ((1,((7,3),)),(2,((5,6),)),(3,((5,4),))),
            ((1,((6,3),)),(2,((6,6),)),(3,((6,4),)))
        ]
    if name=='Pappus':
        assert patterns==[
            ((1,((8,3),)),(2,((7,6),)),(3,((7,6),)),(4,((7,2),))),
            ((1,((8,3),)),(2,((8,6),)),(3,((8,6),)),(4,((7,2),)))
        ]
    print(name,'order',n,'size',sum(m.bit_count() for m in graph)//2,
          'values',(int(valsD[0]),int(valsS[0])),'all_masks',full+1)
    for label,table in zip(('D-first','S-first'),patterns):
        print(' ',label,'second-ply distance -> {score: multiplicity}',table)

if __name__=='__main__':
    evaluate('Heawood',heawood(),(7,6))
    evaluate('Pappus',pappus(),(8,7))
    print('INDEPENDENT_VERIFY_OK')
