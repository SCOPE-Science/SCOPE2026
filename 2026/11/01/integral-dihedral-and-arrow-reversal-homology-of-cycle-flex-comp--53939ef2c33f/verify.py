"""Finite cellular Lefschetz checks for polygon orientation-flex complexes.

For every independent set F of polygon vertices, a cubical cell is specified
by orientations of the edges not incident to F. A canonical base vertex has
all vertices of F as sinks. Cellular map signs are computed on oriented
cube axes sorted by vertex label.
"""
from itertools import combinations, product
from math import prod


def popcount(x):
    return x.bit_count()


def independent(F, n):
    return all((i+1)%n not in F for i in F)


def parity(permutation):
    s=1
    for i in range(len(permutation)):
        for j in range(i+1,len(permutation)):
            if permutation[i]>permutation[j]:s=-s
    return s


def action_vertices(i,n,j,refl):
    return (j-i)%n if refl else (i+j)%n


def act_bits(x,n,j,refl,comp):
    y=[0]*n
    for i in range(n):
        target=(j-i-1)%n if refl else (i+j)%n
        y[target]=x[i] ^ int(refl) ^ int(comp)
    return y


def cells(n):
    for d in range(n//2+1):
        for F1 in combinations(range(n),d):
            F=set(F1)
            if not independent(F,n):continue
            incident={j for i in F for j in ((i-1)%n,i)}
            free=sorted(set(range(n))-incident)
            for bits in product((0,1),repeat=len(free)):
                x=[None]*n
                for i in F:
                    x[(i-1)%n]=1
                    x[i]=0
                for e,b in zip(free,bits): x[e]=b
                assert all(v in (0,1) for v in x)
                yield F1,free,x


def cellular_trace(n,j,refl,comp):
    trace=[0]*(n//2+1)
    for F,free,x in cells(n):
        moved=tuple(sorted(action_vertices(i,n,j,refl) for i in F))
        if moved != F:continue
        y=act_bits(x,n,j,refl,comp)
        if any(y[e] != x[e] for e in free):continue
        permuted=[action_vertices(i,n,j,refl) for i in F]
        sign=parity(permuted) * (-1 if comp and len(F)%2 else 1)
        trace[len(F)]+=sign
    return trace


def predicted_traces(n,j,refl,comp):
    # A polygon reflection or global orientation reversal interchanges
    # particle-number component k and component n-k.
    swaps=bool(refl)^bool(comp)
    h0=(int(n%2==0) if swaps else n+1)
    # Each circular component has one primitive flux generator.
    # On it, orientation reversal changes the flux sign; geometric
    # reflections retain it (the reversal of edge order and arrows cancel).
    h1=(int(n%2==0) if swaps else n-1)*(-1 if comp else 1)
    return h0,h1


def run():
    cases=0
    for n in range(3,11):
        for j in range(n):
            for refl in (0,1):
                for comp in (0,1):
                    tr=cellular_trace(n,j,refl,comp)
                    lefschetz=sum(((-1)**d)*v for d,v in enumerate(tr))
                    h0,h1=predicted_traces(n,j,refl,comp)
                    assert lefschetz==h0-h1,(n,j,refl,comp,tr,h0,h1,lefschetz)
                    cases+=1
    print(f'PASS: {cases} signed cellular Lefschetz identities for polygons of lengths 3..10')
    for n in range(3,11):
        print(n, {x:cellular_trace(n,0,*( {'r':(0,0),'s':(1,0),'u':(0,1),'us':(1,1)}[x])) for x in ['r','s','u','us']})


if __name__=='__main__':run()
