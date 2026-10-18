"""Exact, independent finite tournament checks for the statements in RESULT.md.

Run: python3 verify.py
Python standard library only.  Exhaustive tests do not replace the proof.
"""
from fractions import Fraction as F
from math import comb
from itertools import product


def moment(values):
    avg = sum(values, F(0)) / len(values)
    return avg, sum((v-avg)**2 for v in values) / len(values)


def check(n):
    assert n >= 3
    m = n - 1
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    dlist, clist, qlist = [], [], []
    by_s = [[] for _ in range(n)]
    assert len(edges) == n*m//2
    for bits in product((0,1),repeat=len(edges)):
        w = [[False]*n for _ in range(n)]
        d = [0]*n
        for (i,j),x in zip(edges,bits):
            if x:
                w[i][j] = True
                d[i] += 1
            else:
                w[j][i] = True
                d[j] += 1
        c = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if (w[i][j] and w[j][k] and w[k][i]) or (w[j][i] and w[k][j] and w[i][k]):
                        c += 1
        q = [(F(dv,1)-F(m,2))**2-F(m,4) for dv in d]
        dlist.append(d)
        clist.append(F(c))
        qlist.append(q)
        by_s[d[0]].append(F(c))
        assert F(c)-F(comb(n,3),4) == -sum(q,F(0))/2
    N = len(clist)
    assert N == 2**(n*m//2)
    ec,vc = moment(clist)
    assert ec == F(comb(n,3),4)
    assert vc == F(n*m*(m-1),32)
    for v in range(n):
        eq,vq = moment([q[v] for q in qlist])
        assert eq == 0 and vq == F(m*(m-1),8)
        assert sum((c-ec)*q[v] for c,q in zip(clist,qlist))/N == -vq/2
        assert sum((c-ec)*(F(d[v])-F(m,2)) for c,d in zip(clist,dlist))/N == 0
        for u in range(v):
            assert sum(q[v]*q[u] for q in qlist)/N == 0
    for s,values in enumerate(by_s):
        mu,vr = moment(values)
        assert mu == F(comb(m,3),4) + F(s*(m-s),2)
        assert vr == F(3*comb(m,3),16) + F(s*(m-s),4)
        assert mu == ec - ((F(s)-F(m,2))**2-F(m,4))/2
    explained = sum(F(len(values),N)*(moment(values)[0]-ec)**2 for values in by_s)
    assert explained == F(m*(m-1),32)
    assert explained / vc == F(1,n)
    print(f'n={n}: {N:,} tournaments checked; conditional moments, score orthogonality and 1/n identity passed')


if __name__ == '__main__':
    for n in range(3,7):
        check(n)
    print('PASS: all exact finite checks (n=3..6)')
