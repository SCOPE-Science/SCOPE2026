#!/usr/bin/env python3
"""Exact rational verification of cyclic-band Birkhoff face sensitivity.
Uses only Python's standard library, with row-by-row Gauss-Jordan arithmetic.
"""
from fractions import Fraction as F


def inverse(mat):
    N=len(mat)
    A=[[F(v) for v in row]+[F(int(i==j)) for j in range(N)] for i,row in enumerate(mat)]
    for p in range(N):
        q=next(i for i in range(p,N) if A[i][p])
        A[p],A[q]=A[q],A[p]
        a=A[p][p]
        A[p]=[z/a for z in A[p]]
        for i in range(N):
            if i==p or not A[i][p]:continue
            c=A[i][p]
            A[i]=[v-c*w for v,w in zip(A[i],A[p])]
    return [r[N:] for r in A]


def evaluate(n,k):
    E=[(i,(i+j)%n) for i in range(n) for j in range(k)]
    R=2*n-1
    B=[[0]*len(E) for _ in range(R)]
    for e,(i,j) in enumerate(E):
        B[i][e]=1
        if j<n-1: B[n+j][e]=1
    L=[[sum(B[i][e]*B[j][e] for e in range(len(E))) for j in range(R)] for i in range(R)]
    Inv=inverse(L)
    norms=[]
    for d in range(k):
        src=d
        rhs=[B[i][src] for i in range(R)]
        h=[sum((Inv[i][j]*rhs[j] for j in range(R)),F(0)) for i in range(R)]
        nr=sum((abs(F(e==src)-sum((B[i][e]*h[i] for i in range(R)),F(0))) for e in range(len(E))),F(0))
        norms.append(nr)
    return max(norms),norms

def verify_finite_pair():
    """Positive-input attainment at the first cyclic-band departure."""
    n,k=13,7
    edges=[(i,(i+j)%n) for i in range(n) for j in range(k)]
    R=2*n-1
    B=[[0]*len(edges) for _ in range(R)]
    for e,(i,j) in enumerate(edges):
        B[i][e]=1
        if j<n-1:B[n+j][e]=1
    L=[[sum(B[i][e]*B[j][e] for e in range(len(edges))) for j in range(R)] for i in range(R)]
    Hi=inverse(L)
    def pot(z):
        rhs=[sum(B[i][e]*z[e] for e in range(len(edges))) for i in range(R)]
        return [sum((Hi[i][j]*rhs[j] for j in range(R)),F(0)) for i in range(R)]
    def gradient(v):
        return [sum((B[i][e]*v[i] for i in range(R)),F(0)) for e in range(len(edges))]
    source=0  # edge (0,0)
    delta=[int(e==source) for e in range(len(edges))]
    qrow=[F(a)-b for a,b in zip(delta,gradient(pot(delta)))]
    signs=[int(x>0)-int(x<0) for x in qrow]
    assert all(signs)
    h=pot(signs)
    qsign=[F(z)-v for z,v in zip(signs,gradient(h))]
    assert all(sum((B[i][e]*qsign[e] for e in range(len(edges))),F(0))==0 for i in range(R))
    v=F(3745290244,1096631627)
    assert sum(abs(x) for x in qrow)==qsign[source]==v
    t=F(1,1000)
    assert min(F(1,k)+t*x for x in qsign)>0
    edge_set=set(edges)
    # Off-face KKT multipliers remain positive when the input baseline
    # is shifted by 2, yielding two strictly positive observation matrices.
    multipliers=[F(1)+t*(h[i]+(h[n+j] if j<n-1 else 0))
                 for i in range(n) for j in range(n) if (i,j) not in edge_set]
    assert min(multipliers)>0
    # The baseline observed matrix equals 2+1/k on supported edges, 1 elsewhere.
    # The perturbed input differs by t*signs only on supported edges.
    assert min(F(2,1)+F(1,k)+t*z for z in signs)>0
    assert max(abs(t*z) for z in signs)==t
    print('exact positive-input finite pair verified, output/input ratio:',v)
    print('strict smallest on-face projection entry:',min(F(1,k)+t*x for x in qsign))
    print('strict smallest off-face multiplier:',min(multipliers))

def main():
    checks=0
    for n in range(3,14):
        baseline=F(4*(n-1)*(n-1),n*n)
        attained=[]
        for k in range(2,n+1):
            maxv, by_d=evaluate(n,k)
            checks+=len(by_d)
            if n<=12:
                assert maxv <= baseline, (n,k,maxv,baseline)
            if n==13 and maxv>baseline:attained.append((k,maxv,by_d.index(maxv)))
            if k==n:
                assert maxv==baseline
        if n==13:
            assert attained==[(7,F(3745290244,1096631627),0)],attained
            assert F(3745290244,1096631627)-baseline==F(99556468,14256211151)
        print(f'n={n}: verified cyclic-band faces k=2..{n}, baseline={baseline}')
    print('n=13: unique over-baseline band width k=7, norm=3745290244/1096631627')
    print('first departure excess=99556468/14256211151')
    print('row norms checked:',checks)
    verify_finite_pair()
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__':main()
