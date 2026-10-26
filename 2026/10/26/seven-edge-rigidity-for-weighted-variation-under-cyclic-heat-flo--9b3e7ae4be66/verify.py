#!/usr/bin/env python3
"""Exact finite diagnostics for the cyclic heat/weighted-variation theorem.

The infinite-dimensional-in-n assertion is proved analytically in RESULT.md.
These checks verify finite identities and explicit witnesses, not uniqueness in all n.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random


def gen(r):
    n = len(r)
    assert n >= 3
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        out[i][i] = -(r[i] + r[(i + 1) % n])
        out[i][(i - 1) % n] += r[i]
        out[i][(i + 1) % n] += r[(i + 1) % n]
    return out


def apply(mat, vec):
    return [sum(a * x for a, x in zip(row, vec)) for row in mat]


def rate(mat, w, i, j):
    n = len(w)
    step = [Q(int(k == i) - int(k == j)) for k in range(n)]
    b = apply(mat, step)
    return w[i] * b[i] - w[j] * b[j] + sum(
        w[k] * abs(b[k]) for k in range(n) if k != i and k != j
    )


def mu(mat, w):
    n = len(w)
    return max(rate(mat, w, i, j) / (w[i] + w[j])
               for i, j in combinations(range(n), 2))


def lap_weight(r, w):
    n = len(w)
    return [r[i] * (w[(i-1)%n]-w[i]) +
            r[(i+1)%n] * (w[(i+1)%n]-w[i]) for i in range(n)]


def dist(n, i, j):
    d = abs(i-j)
    return min(d, n-d)


def explicit_mass_one(n, w, i, j):
    d = dist(n,i,j)
    if n == 3:
        return -3 * (w[i] + w[j])
    if d == 1:
        if (j-i) % n != 1:
            i,j=j,i
        return -3*(w[i]+w[j])+w[(i-1)%n]+w[(i+2)%n]
    if n == 4 and d == 2:
        return -2*(w[i]+w[j])
    if d == 2:
        if (j-i) % n != 2:
            i,j=j,i
        return -2*(w[i]+w[j])+w[(i-1)%n]+w[(i+3)%n]
    rho = lap_weight([Q(1)]*n,w)
    return rho[i]+rho[j]


def do_checks():
    rnd = Random(20261024)
    counts = {'generator':0, 'rate':0, 'far_pair':0,
              'formulas':0, 'witness':0, 'far_graph':0, 'six_cycle':0, 'rigidity':0}
    for n in range(3, 20):
        for sample in range(7):
            r = [Q(rnd.randint(1,7),rnd.randint(1,7)) for _ in range(n)]
            w = [Q(rnd.randint(1,9),rnd.randint(1,7)) for _ in range(n)]
            mat=gen(r)
            for i in range(n):
                assert sum(mat[i])==0
                assert sum(mat[k][i] for k in range(n))==0
                for j in range(n):
                    assert mat[i][j]==mat[j][i]
                counts['generator']+=3
            rho=lap_weight(r,w)
            assert sum(rho)==0
            assert apply(mat,w)==rho
            for i,j in combinations(range(n),2):
                value=rate(mat,w,i,j)
                counts['rate']+=1
                if dist(n,i,j)>=3:
                    assert value==rho[i]+rho[j]
                    counts['far_pair']+=1
                if all(z==1 for z in r):
                    assert value==explicit_mass_one(n,w,i,j)
                    counts['formulas']+=1
    for n in range(3, 20):
        mat = gen([Q(1)] * n)
        for sample in range(15):
            w = [Q(rnd.randint(1,12),rnd.randint(1,12)) for _ in range(n)]
            for i,j in combinations(range(n),2):
                assert rate(mat,w,i,j)==explicit_mass_one(n,w,i,j)
                counts['formulas']+=1
    # Solve M u = rho with an antiperiodic nonzero rho in dimension six.
    # M has kernel constants; pin u_0=0 to obtain a five-by-five system.
    for sample in range(12):
        n=6
        r=[Q(rnd.randint(1,9),rnd.randint(1,9)) for _ in range(n)]
        mat=gen(r)
        target=[Q((-1)**i) for i in range(n)]
        rows=[mat[i][1:]+[target[i]] for i in range(1,n)]
        for col in range(n-1):
            pivot=next(k for k in range(col,n-1) if rows[k][col])
            rows[col],rows[pivot]=rows[pivot],rows[col]
            scale=rows[col][col]
            rows[col]=[v/scale for v in rows[col]]
            for k in range(n-1):
                if k!=col:
                    factor=rows[k][col]
                    rows[k]=[a-factor*b for a,b in zip(rows[k],rows[col])]
        u=[Q(0)]+[rows[i][-1] for i in range(n-1)]
        assert apply(mat,u)==target
        eps=Q(1,100000)/(1+max(abs(v) for v in u))
        w=[1+eps*z for z in u]
        assert min(w)>0 and len(set(w))>1
        assert mu(mat,w)<=0
        counts['six_cycle']+=1
    for n in range(3, 14):
        r=[Q(1)]*n
        mat=gen(r)
        w=[Q(2)]+[Q(1)]*(n-1)
        m=mu(mat,w)
        if n>=6:
            assert m>0
        else:
            assert m<=0
        counts['witness']+=1
    for n in [4,5,6]:
        w=[Q(2)]+[Q(1)]*(n-1)
        assert mu(gen([Q(1)]*n),w)<=0 if n in (4,5) else mu(gen([Q(1)]*n),w)>0
        counts['witness']+=1
    for e in [Q(1,4),Q(1,3),Q(1,2)]:
        w=[Q(1)+e*((-1)**i) for i in range(6)]
        assert (mu(gen([Q(1)]*6),w)<=0)==(e<=Q(1,3))
        counts['witness']+=1
    for n in range(7, 15):
        for sample in range(16):
            r=[Q(rnd.randint(1,12),rnd.randint(1,12)) for _ in range(n)]
            w=[Q(rnd.randint(1,12),rnd.randint(1,12)) for _ in range(n)]
            if len(set(w))>1:
                assert mu(gen(r),w)>0
                counts['rigidity']+=1
    for n in range(7, 80):
        graph=[[j for j in range(n) if dist(n,i,j)>=3] for i in range(n)]
        assert len({len(z) for z in graph})==1
        assert len(graph[0])==n-5
        colors={0:0};q=[0];odd=False
        while q:
            i=q.pop(0)
            for j in graph[i]:
                if j in colors:
                    if colors[j]==colors[i]: odd=True
                else:
                    colors[j]=1-colors[i];q.append(j)
        assert len(colors)==n and odd
        counts['far_graph']+=1
    # Exact explicit one-step expansion on C7 with a nonuniform variation weight.
    n=7;r=[Q(1)]*n;w=[Q(2)]+[Q(1)]*(n-1);A=gen(r)
    pair=max(combinations(range(n),2),key=lambda ij:rate(A,w,*ij)/(w[ij[0]]+w[ij[1]]))
    assert rate(A,w,*pair)>0
    x=[Q(int(k==pair[0])-int(k==pair[1])) for k in range(n)]
    t=Q(1,1000)
    mx=apply(A,x)
    y=[a+t*b for a,b in zip(x,mx)]
    old=sum(v*abs(a) for v,a in zip(w,x))
    new=sum(v*abs(a) for v,a in zip(w,y))
    assert new>old
    counts['witness']+=1
    return counts

if __name__=='__main__':
    checks=do_checks()
    print('PASS',checks,'TOTAL',sum(checks.values()))
