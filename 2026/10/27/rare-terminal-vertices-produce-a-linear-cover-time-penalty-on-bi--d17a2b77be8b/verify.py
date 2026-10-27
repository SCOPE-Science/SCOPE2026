"""Exact checks of the biased-cycle last-vertex/cover-time formula.

Uses rational arithmetic, a direct subset-state Markov-chain solution, and
an independent first-exit factorization. Standard-library only.
"""
from fractions import Fraction as F


def solve(matrix, rhs):
    # Gauss-Jordan rational solve, multiple right sides.
    m = len(matrix)
    k = len(rhs[0])
    a = [list(matrix[i]) + list(rhs[i]) for i in range(m)]
    for col in range(m):
        piv = next(i for i in range(col, m) if a[i][col] != 0)
        a[col], a[piv] = a[piv], a[col]
        c = a[col][col]
        a[col] = [z / c for z in a[col]]
        for row in range(m):
            if row != col and a[row][col] != 0:
                c = a[row][col]
                a[row] = [a[row][u] - c*a[col][u] for u in range(m+k)]
    return [row[m:] for row in a]


def exhaustive(n, p):
    q = 1-p
    allset = (1 << n)-1
    done = {}
    for mask in range(allset, 0, -1):
        if not (mask & 1):
            continue  # only subsets containing the fixed start 0
        sites = [x for x in range(n) if mask & (1 << x)]
        if mask == allset:
            for x in sites:
                done[mask, x] = (
                    [F(int(x == j)) for j in range(1,n)],
                    [F(0) for _ in range(1,n)])
            continue
        idx = {x: u for u,x in enumerate(sites)}
        size = len(sites)
        a = [[F(int(i==j)) for j in range(size)] for i in range(size)]
        bp = [[F(0) for _ in range(n-1)] for x in sites]
        for row,x in enumerate(sites):
            for y,w in [((x+1)%n,p),((x-1)%n,q)]:
                nxt = mask | (1 << y)
                if nxt == mask:
                    a[row][idx[y]] -= w
                else:
                    v,_ = done[nxt,y]
                    bp[row] = [bp[row][j] + w*v[j] for j in range(n-1)]
        pp = solve(a,bp)
        bh = [[F(0) for _ in range(n-1)] for x in sites]
        for row,x in enumerate(sites):
            for y,w in [((x+1)%n,p),((x-1)%n,q)]:
                nxt = mask | (1 << y)
                if nxt == mask:
                    v = pp[idx[y]]
                    bh[row] = [bh[row][j]+w*v[j] for j in range(n-1)]
                else:
                    v,h = done[nxt,y]
                    bh[row] = [bh[row][j]+w*(v[j]+h[j]) for j in range(n-1)]
        hh = solve(a,bh)
        for row,x in enumerate(sites):
            done[mask,x] = pp[row],hh[row]
    P,H = done[1,0]
    return {j:(P[j-1], H[j-1]/P[j-1]) for j in range(1,n)}


def analytic(n, j, p):
    q = 1-p
    r = q/p
    d = p-q
    N = n-2
    i = n-j-1
    C = lambda m: (1+r**m)/(1-r**m)
    prob = (1-r)*r**i/(1-r**(n-1))
    beta = r**(j-1)*(1-r**i)/(1-r**N)
    t2 = ((N+1)*C(N+1)-C(1))/d
    h = lambda y: (1-r**y)/(1-r**n)
    t3B = (n*h(n-1)-(n-1))/d
    t3A = (n*h(1)-1)/d
    if i == N:
        # The first endpoint must be N; only the B-first route is possible.
        tB = t2+t3A
        return prob,tB
    t1A = (N*C(N)-(N-i)*C(N-i))/d
    tA = t1A+t2+t3B
    if i == 0:
        return prob,tA
    t1B = (N*C(N)-i*C(i))/d
    tB = t1B+t2+t3A
    return prob, (1-beta)*tA+beta*tB


def main():
    checks=0
    for p in [F(3,5),F(2,3),F(3,4)]:
        for n in range(3,9):
            actual=exhaustive(n,p)
            for j in range(1,n):
                expectation=analytic(n,j,p)
                assert expectation==actual[j],(p,n,j,expectation,actual[j])
                checks+=2
            assert sum(v[0] for v in actual.values())==1
            checks+=1
    # Verify uniform bulk remainder scales relative to n*r^(j-1),
    # but do not treat these finite tests as proof of the asymptotic.
    for p in [F(3,5),F(2,3),F(3,4)]:
        q=1-p;r=q/p;d=p-q
        for n in [10,20,30,40]:
            for j in [2,3,n//3,n//2,n-2,n-1]:
                if j>=n:continue
                _,t=analytic(n,j,p)
                base=F(2*n-j-1)/d-1/d**2
                ratio=abs(t-base)/(n*r**(j-1))
                assert ratio < F(1000,1), (n,j,p,ratio)
                checks+=1
    print('PASS',checks,'exact equality and finite-bound assertions')
    for p in [F(2,3), F(3,4)]:
        n=30
        for j in [n//4,n//2,3*n//4]:
            prob,t=analytic(n,j,p)
            print('diagnostic p=%s n=%d j=%d P=%0.9g mean=%0.9f normalized=%0.9f' %
                  (p,n,j,float(prob),float(t),float(t/n)))

if __name__=='__main__':
    main()
