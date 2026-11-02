"""Exact checks for pair-codegree proportional group voting and Fano comparison.
This file uses only the Python standard library.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations

N = 7
FANO = [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
K7 = list(combinations(range(N),2))
FULL = (1 << N)-1


def maskset(e):
    return sum(1 << i for i in e)


def pairweights(n, edges):
    return {(i,j):sum(rate for edge,rate in edges if i in edge and j in edge)
            for i,j in combinations(range(n),2)}


def out_rates(mask, edges):
    """Return off-diagonal generator rates, including absorption destinations."""
    rates = defaultdict(F)
    for edge,rate in edges:
        e = maskset(edge)
        a = (mask&e).bit_count()
        r = len(edge)
        if 0<a<r:
            rates[mask | e] += rate * F(a,r)
            rates[mask & ~e] += rate * F(r-a,r)
    return dict(rates)


def H(mask,n):
    k=mask.bit_count()
    return k*(n-k)


def exact_generator_H(mask,n,edges):
    return sum(rate*(H(dst,n)-H(mask,n)) for dst,rate in out_rates(mask,edges).items())


def solve(M,b):
    n=len(M)
    A=[[F(v) for v in M[i]] + [F(b[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None)
        assert pivot is not None
        A[j],A[pivot]=A[pivot],A[j]
        p=A[j][j]
        A[j]=[v/p for v in A[j]]
        for i in range(n):
            if i!=j:
                f=A[i][j]
                if f:A[i]=[A[i][k]-f*A[j][k] for k in range(n+1)]
    return [A[i][-1] for i in range(n)]


def fano_class(mask):
    k=mask.bit_count()
    j=min(k,N-k)
    if not j:return 0
    if j<3:return j
    minority=mask if k==3 else FULL ^ mask
    return 3 if minority in {maskset(edge) for edge in FANO} else 4


def k7_class(mask):
    return min(mask.bit_count(), N-mask.bit_count())


def quotient_rates(edges,classifier,cats):
    edges=[(edge,F(1)) for edge in edges]
    classes=defaultdict(list)
    for mask in range(1,FULL):
        classes[classifier(mask)].append(mask)
    assert set(classes)==set(cats)
    Q=[]
    for category in cats:
        row0=None
        for mask in classes[category]:
            d=defaultdict(F)
            for dst,rate in out_rates(mask,edges).items():
                dstcat=classifier(dst)
                if dstcat!=category:d[dstcat]+=rate
            row=tuple(d.get(dest,F(0)) for dest in [0]+cats)
            if row0 is None:row0=row
            assert row==row0,(category,mask,row,row0)
        Q.append(row0)
    matrix=[]
    for i,row in enumerate(Q):
        off={cat:row[1+j] for j,cat in enumerate(cats)}
        m=[-off[cat] for cat in cats]
        m[i]=row[0]+sum(v for cat,v in off.items() if cat != cats[i])
        matrix.append(m)
    return matrix,Q


def main():
    for label,raw in [('Fano',FANO),('K7',K7)]:
        edges=[(edge,F(1)) for edge in raw]
        weights=pairweights(N,edges)
        assert set(weights.values())=={F(1)}, (label,weights)
        for mask in range(1<<N):
            assert exact_generator_H(mask,N,edges)==-H(mask,N)
        classes=[1,2,3,4] if label=='Fano' else [1,2,3]
        cls=fano_class if label=='Fano' else k7_class
        matrix,Q=quotient_rates(raw,cls,classes)
        times=solve(matrix,[1]*len(classes))
        print(label,'pair weights',len(weights),'all one; exact generator 128 states OK')
        print(label,'-Q:')
        for row in matrix:print('  ',list(map(str,row)))
        print(label,'times',list(map(str,times)))
        assert times[0]==(F(16,21) if label=='Fano' else F(7,10))
        if label=='Fano':
            assert times==[F(16,21),F(47,42),F(9,7),F(215,168)]
        else:
            assert times==[F(7,10),F(16,15),F(37,30)]
    # Nonconstant weighted pair codegrees: test general generator cut identity.
    mixed_edges=[((0,1,2),F(2,5)),((1,2,3),F(3,7)),((0,3),F(1,2))]
    w=pairweights(4,mixed_edges)
    for mask in range(16):
        cut=sum(value for (i,j),value in w.items() if ((mask>>i)^(mask>>j)) & 1)
        assert exact_generator_H(mask,4,mixed_edges)==-cut
    print('Arbitrary nonbalanced weighted 4-node hypergraph: all 16 cuts checked.')
    print('Fano vs K7 mean-time difference:',F(16,21)-F(7,10))
    print('PASS')

if __name__=='__main__':
    main()
