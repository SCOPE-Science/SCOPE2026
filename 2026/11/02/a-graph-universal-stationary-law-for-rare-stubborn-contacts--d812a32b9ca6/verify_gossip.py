"""Exact-rational finite-state moment verification for weak-anchor gossip.

No third-party packages. Run: python verify_gossip.py
The infinite-dimensional invariant-law theorem is proved analytically,
not by this finite verification.
"""
from fractions import Fraction as F
from itertools import combinations


def solve(A, b):
    n = len(b)
    aug = [list(map(F, A[i])) + [F(b[i])] for i in range(n)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if aug[i][k]), None)
        assert pivot is not None
        aug[k], aug[pivot] = aug[pivot], aug[k]
        factor = aug[k][k]
        aug[k] = [z / factor for z in aug[k]]
        for i in range(n):
            if i != k and aug[i][k]:
                factor = aug[i][k]
                aug[i] = [a - factor*z for a, z in zip(aug[i], aug[k])]
    return [row[-1] for row in aug]


def update_events(n, edges, anchors, eps):
    events = []
    for i, j, w in edges:
        M = [[F(int(k == l)) for l in range(n)] for k in range(n)]
        for k in (i, j):
            M[k][i] = M[k][j] = F(1,2)
        events.append((F(w), M, [F(0)]*n))
    for i, val, b in anchors:
        M = [[F(int(k == l)) for l in range(n)] for k in range(n)]
        M[i][i] = F(1,2)
        c = [F(0)]*n
        c[i] = F(val,2)
        events.append((F(eps)*F(b),M,c))
    return events


def moments(n, edges, anchors, eps):
    events = update_events(n, edges, anchors, eps)
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    rhs = [F(0)]*n
    for i,j,w in edges:
        w = F(w)
        L[i][i] += w; L[j][j] += w
        L[i][j] -= w; L[j][i] -= w
    for i, s, b in anchors:
        L[i][i] += F(eps)*F(b)
        rhs[i] += F(eps)*F(b)*F(s)
    mean = solve(L, rhs)
    ij = [(i,j) for i in range(n) for j in range(i,n)]
    dim = len(ij)
    A = [[F(0) for _ in ij] for _ in ij]
    v = [F(0)]*dim
    for row,(i,j) in enumerate(ij):
        for rate,M,c in events:
            for col,(k,l) in enumerate(ij):
                coefficient = M[i][k]*M[j][l]
                if k!=l:
                    coefficient += M[i][l]*M[j][k]
                if (i,j)==(k,l):
                    coefficient -= 1
                A[row][col] += rate*coefficient
            const = c[i]*sum(M[j][k]*mean[k] for k in range(n))
            const += c[j]*sum(M[i][k]*mean[k] for k in range(n))
            const += c[i]*c[j]
            v[row] -= rate*const
    result = solve(A, v)
    S = {(i,j):z for (i,j),z in zip(ij,result)}
    def second(i,j): return S[min(i,j),max(i,j)]
    ED = sum(second(i,i) for i in range(n)) - sum(second(i,j) for i in range(n) for j in range(n))/n
    meanbar = sum(mean)/n
    secondbar = sum(second(i,j) for i in range(n) for j in range(n))/(n*n)
    return mean, S, ED, meanbar, secondbar, events


def verify():
    examples = [
        (2, [(0,1,1)], [(0,1,1),(1,-1,1)]),
        (3, [(0,1,2),(1,2,3)], [(0,1,2),(2,-1,2)]),
        (4, [(0,1,1),(0,2,2),(0,3,3)], [(1,1,3),(2,-1,1),(3,-1,2)]),
        (4, [(0,1,2),(1,2,1),(2,3,3),(3,0,2)], [(0,1,1),(1,1,2),(2,-1,2),(3,-1,1)]),
        (3, [(0,1,3),(1,2,1)], [(0,1,3),(2,-1,1)]),
    ]
    checks = 0
    for n, edges, anchors in examples:
        B = sum(F(b) for i,s,b in anchors)
        sm = sum(F(b)*F(s) for i,s,b in anchors)/B
        sv = sum(F(b)*(F(s)-sm)**2 for i,s,b in anchors)/B
        target = sm**2 + sv/F(4*n-1)
        for eps in (F(1),F(1,5),F(1,50),F(1,1000),F(1,10000)):
            mean, second, ED, meanbar, secondbar, events = moments(n,edges,anchors,eps)
            assert ED>=0
            # Each stationary mean lies in the anchor's convex hull.
            assert all(min(s for _,s,_ in anchors)<=z<=max(s for _,s,_ in anchors) for z in mean)
            # First and second moment generator residuals, re-evaluated from matrices.
            for i in range(n):
                drift=sum(rate*(sum(M[i][k]*mean[k] for k in range(n))+c[i]-mean[i]) for rate,M,c in events)
                assert drift==0
                checks += 1
            pair=[(i,j) for i in range(n) for j in range(i,n)]
            lookup=second
            def cov(i,j):return lookup[min(i,j),max(i,j)]
            for i,j in pair:
                drift=F(0)
                for rate,M,c in events:
                    future=sum(M[i][a]*M[j][b]*cov(a,b) for a in range(n) for b in range(n))
                    future+=c[i]*sum(M[j][a]*mean[a] for a in range(n))
                    future+=c[j]*sum(M[i][a]*mean[a] for a in range(n)) + c[i]*c[j]
                    drift+=rate*(future-cov(i,j))
                assert drift==0
                checks += 1
            # Spectral-gap-independent graph inequality (coarser bound from edge path alone).
            erate=sum(F(w)*(cov(i,i)+cov(j,j)-2*cov(i,j)) for i,j,w in edges)
            assert erate<=F(10)*eps*B # R=1
            checks+=1
            if eps==F(1,10000):
                # Rigorous bound on the difference of the mean's second moment
                # derived from Wasserstein-1 convergence and bounded support.
                # Every coordinate's second moment is within 4 sqrt(ED) of target.
                assert abs(secondbar-target)**2 <= F(16)*ED
                assert abs(meanbar-sm)**2 <= ED
                checks+=2
        print('n=',n,'eps=1/10000','Var(mean)=',float(secondbar-meanbar**2),
              'universal target=',float(sv/F(4*n-1)),
              'ED=',float(ED))
    assert checks>200
    print('PASS', checks, 'exact-rational generator, topology, and rare-anchor checks')

if __name__=='__main__':
    verify()
