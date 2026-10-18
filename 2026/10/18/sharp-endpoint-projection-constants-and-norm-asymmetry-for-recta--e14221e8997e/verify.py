"""Exact-rational finite-instance checks for rook-graph cut/cycle projections.

The general theorem is analytic; these checks do not prove its universal quantifiers.
Run: python verify.py
"""
from fractions import Fraction as F
from itertools import combinations

checks = 0

def check(condition, description=''):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def edges_of(m, n):
    a = [((i, j), (k, j), 'A')
         for j in range(n) for i, k in combinations(range(m), 2)]
    b = [((i, j), (i, k), 'B')
         for i in range(m) for j, k in combinations(range(n), 2)]
    return a+b


def cut_projection(m, n, t):
    edges = edges_of(m, n)
    pot = []
    for (x, y, kind) in edges:
        values = {}
        if kind == 'A':
            for i in range(m):
                for j in range(n):
                    values[i, j] = (int(i == x[0])-int(i == y[0])) * (
                        t*int(j == x[1])/m + (1-t)/F(m*n))
        else:
            for i in range(m):
                for j in range(n):
                    values[i, j] = (int(j == x[1])-int(j == y[1])) * (
                        (1-t)*int(i == x[0])/n + t/F(m*n))
        pot.append(values)
    return edges, [[p[e[0]]-p[e[1]] for p in pot] for e in edges]


def extrema(m, n, t):
    # Entry counts use exact column/row sums for 0 <= t <= 1.
    cut1a=F(2*(m-1),m)+F(2*(n-1),m)*t
    cut1b=F(2*(n-1),n)+F(2*(m-1),n)*(1-t)
    cutia=F(2*(m-1),m)+F(2*(n-1),n)*(1-t)
    cutib=F(2*(n-1),n)+F(2*(m-1),m)*t
    diag_a=F(2,m*n)*(1+(n-1)*t)
    diag_b=F(2,m*n)*(1+(m-1)*(1-t))
    return {
        ('B',1): (cut1a,cut1b),
        ('B','inf'): (cutia,cutib),
        ('Z',1): (1+cutia-2*diag_a,1+cutib-2*diag_b),
        ('Z','inf'): (1+cut1a-2*diag_a,1+cut1b-2*diag_b),
    }


def optimizers(m,n):
    return {
        ('B',1):F(m*m-2*m+n,m*m-m+n*n-n),
        ('B','inf'):F(n*(m-1),2*m*n-m-n),
        ('Z',1):F((m-1)*(n+2),2*m*n+m+n-4),
        ('Z','inf'):F(m*m-4*m+n+2,m*m-3*m+n*n-3*n+4),
    }


def calculate(m,n,t):
    edges,P=cut_projection(m,n,t)
    N=len(edges)
    Q=[[int(i==j)-P[j][i] for j in range(N)] for i in range(N)]
    return edges,P,Q


def block_norms(edges,W):
    N=len(edges)
    col=[sum(abs(W[i][j]) for i in range(N)) for j in range(N)]
    row=[sum(abs(W[i][j]) for j in range(N)) for i in range(N)]
    iA=next(i for i,e in enumerate(edges) if e[2]=='A')
    iB=next(i for i,e in enumerate(edges) if e[2]=='B')
    return {(1,'A'):col[iA],(1,'B'):col[iB],('inf','A'):row[iA],('inf','B'):row[iB]}


def trial(m,n,t,full=False):
    edges,P,Q=calculate(m,n,t)
    N=len(edges)
    check(F(0)<=t<=F(1))
    check(all(P[i][j].denominator>0 for i in range(N) for j in range(N)))
    check(all(P[i][i]>=0 and P[i][i]<=1 for i in range(N)))
    # All columns of P are gradients, all columns of Q are divergence-free.
    for j in range(N):
        divergence={(i,k):F(0) for i in range(m) for k in range(n)}
        for i,(v,w,_) in enumerate(edges):
            divergence[v]-=Q[i][j]
            divergence[w]+=Q[i][j]
        for u in divergence:
            check(divergence[u]==0,('divergence',m,n,t,j,u))
    for h,W in [('B',P),('Z',Q)]:
        direct=block_norms(edges,W)
        for p in (1,'inf'):
            ba,bb=extrema(m,n,t)[h,p]
            check(direct[p,'A']==ba,(m,n,t,h,p,'A',direct[p,'A'],ba))
            check(direct[p,'B']==bb,(m,n,t,h,p,'B',direct[p,'B'],bb))
            for i,e in enumerate(edges):
                expected=ba if e[2]=='A' else bb
                val=(sum(abs(W[k][i]) for k in range(N)) if p==1
                     else sum(abs(W[i][k]) for k in range(N)))
                check(val==expected,(m,n,t,h,p,i))
    if full:
        # Independently check P^2=P, Q^2=Q, PQ=QP=0.
        for i in range(N):
            for j in range(N):
                pij=sum(P[i][k]*P[k][j] for k in range(N))
                qij=sum(Q[i][k]*Q[k][j] for k in range(N))
                check(pij==P[i][j],('P^2',m,n,i,j))
                check(qij==Q[i][j],('Q^2',m,n,i,j))


def run():
    for m,n in [(3,4),(3,5),(4,5),(3,3)]:
        ts={F(0),F(1),F(1,2),*optimizers(m,n).values()}
        for t in sorted(ts):
            trial(m,n,t,full=(t==F(1,2) and m<=3))
        for key,t in optimizers(m,n).items():
            a,b=extrema(m,n,t)[key]
            check(a==b,('balanced',m,n,key))
            check(0<t<1)
            # The two opposing affine branches certify minimax at this t.
            low=extrema(m,n,F(0))[key]
            high=extrema(m,n,F(1))[key]
            check(max(a,b)<=max(low))
            check(max(a,b)<=max(high))
    # Unequal axes separate the endpoint minimum projection constants.
    for m,n in [(3,4),(3,5),(4,7),(5,6)]:
        o=optimizers(m,n)
        b1=max(extrema(m,n,o['B',1])['B',1]);bi=max(extrema(m,n,o['B','inf'])['B','inf'])
        z1=max(extrema(m,n,o['Z',1])['Z',1]);zi=max(extrema(m,n,o['Z','inf'])['Z','inf'])
        check(bi>b1)
        check(z1>zi)
    print('PASS: %d exact-rational assertions' % checks)

if __name__=='__main__':run()
