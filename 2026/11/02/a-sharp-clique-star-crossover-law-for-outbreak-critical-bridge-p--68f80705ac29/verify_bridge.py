"""Exact rational checks for a clique--star bridge-placement theorem.

The universal proof is algebraic; these tests check its formulas and a sharp
seven-vertex crossover, not every possible network or real parameter.
Run with: python3 verify_bridge.py
"""
from fractions import Fraction as Q
from math import isqrt


def tree_clique_star(r, s):
    """Adjacency of K_r joined from its vertex 0 to hub r of K_(1,s)."""
    n = r + s + 1
    A = [[Q(0) for _ in range(n)] for _ in range(n)]
    def edge(i, j):
        A[i][j] = A[j][i] = Q(1)
    for i in range(r):
        for j in range(i+1, r):
            edge(i, j)
    for j in range(r+1, n):
        edge(r, j)
    edge(0, r)
    return A


def inverse(M):
    n = len(M)
    a = [[Q(x) for x in row] + [Q(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for k in range(n):
        p = next((i for i in range(k,n) if a[i][k]), None)
        if p is None:
            raise ValueError('singular matrix')
        a[k], a[p] = a[p], a[k]
        t = a[k][k]
        a[k] = [z/t for z in a[k]]
        for i in range(n):
            if i == k: continue
            t = a[i][k]
            if t:
                a[i] = [x-t*y for x,y in zip(a[i],a[k])]
    return [row[n:] for row in a]


def is_positive_definite(M):
    n = len(M)
    l = [[Q(0)]*n for _ in range(n)]
    d = [Q(0)]*n
    for i in range(n):
        d[i] = M[i][i]-sum(l[i][k]*l[i][k]*d[k] for k in range(i))
        if d[i] <= 0:
            return False
        for j in range(i+1,n):
            l[j][i] = (M[j][i] -sum(l[j][k]*l[i][k]*d[k] for k in range(i)))/d[i]
    return True


def positive_shift(A,q):
    return [[q*int(i==j)-A[i][j] for j in range(len(A))] for i in range(len(A))]


def formulas(r,s,q):
    f=(q-r+2)/((q+1)*(q-r+1))
    g=q/(q*q-s)
    return f/(1-f*g),g/(1-f*g)


def winner_algebraic(r,s,q):
    d=s*(r-2)+(r-1-s)*q
    return 'clique' if d>0 else ('star' if d<0 else 'tie')


def phase(r,s,q):
    A=tree_clique_star(r,s)
    M=positive_shift(A,q)
    if not is_positive_definite(M):
        return False
    diag=[V[i][i] for i,V in enumerate([inverse(M)]*len(M))]
    da, dc=formulas(r,s,q)
    assert diag[0] == da, (r,s,q,diag[0],da)
    assert diag[r] == dc, (r,s,q,diag[r],dc)
    assert da>diag[1], (r,s,q,'clique connector is not dominant among clique vertices')
    assert dc>diag[r+1], (r,s,q,'hub is not dominant among star leaves')
    winners=[i for i,d in enumerate(diag) if d==max(diag)]
    expected=winner_algebraic(r,s,q)
    assert winners == ({'clique':[0],'star':[r],'tie':[0,r]}[expected]), (r,s,q,winners,expected)
    return True


def check_witness():
    r=s=3
    assert phase(r,s,Q(5,2))
    assert phase(r,s,Q(3))
    assert phase(r,s,Q(4))
    d1,d2=formulas(r,s,Q(5,2))
    assert (d1,d2)==(Q(78,31),Q(70,31))
    assert formulas(r,s,Q(3))==(Q(2,3),Q(2,3))
    assert formulas(r,s,Q(4))==(Q(39,118),Q(20,59))
    # Three alternative receiver graphs, checking the exact Schur threshold.
    for H in [ [[Q(0)]], [[Q(0),Q(1)],[Q(1),Q(0)]],
              [[Q(0),Q(1),Q(0)],[Q(1),Q(0),Q(1)],[Q(0),Q(1),Q(0)]] ]:
        q=Q(4); v=0; T=tree_clique_star(3,3)
        rh=inverse(positive_shift(H,q))[v][v]
        for u in [0,3,4]:
            dt=inverse(positive_shift(T,q))[u][u]
            critical_sq=1/(dt*rh)
            for w in [Q(1,4),Q(1,2),Q(1),Q(2),Q(3),Q(4)]:
                n=len(T); m=len(H)
                combined=[[Q(0)]*(n+m) for _ in range(n+m)]
                for i in range(n):
                    for j in range(n):combined[i][j]=T[i][j]
                for i in range(m):
                    for j in range(m):combined[n+i][n+j]=H[i][j]
                combined[u][n+v]=combined[n+v][u]=w
                expected=w*w < critical_sq
                actual=is_positive_definite(positive_shift(combined,q))
                assert actual==expected, (q,u,w,critical_sq,expected,actual)
    return 3*3*6


def main():
    checks=0
    for r in range(3,7):
        for s in range(1,11):
            A=tree_clique_star(r,s)
            # q above the maximum degree gives a safe subcritical test.
            q=Q(max(r,s+1)+1)
            assert phase(r,s,q)
            checks+=1
            # Rational points near any proposed crossing, only when SPD.
            if s>=r:
                qs=Q(s*(r-2),s-r+1)
                for x in [qs-Q(1,10),qs,qs+Q(1,10)]:
                    if x>max(Q(r-1),Q(isqrt(s))) and phase(r,s,x):checks+=1
    witness_checks=check_witness()
    # Exact algebraic transition sign at the upper root, using integer samples.
    for r in range(3,24):
        for s in range(1, (r-1)**2+4):
            c= -s*s+(r*r-3*r+4)*s-r+1
            if s<=r-1: assert (r-1-s)>=0
            if s>=r and s<(r-1)**2:
                qstar=Q(s*(r-2),s-r+1)
                f=(qstar-r+2)/((qstar+1)*(qstar-r+1))
                g=qstar/(qstar*qstar-s)
                assert f==g
                assert ((f<1)==(c>0)), (r,s,c,f)
    print('PASS: exact matrix inverses and endpoint maxima on',checks,'clique-star trials')
    print('PASS: witness diagonal values at q=5/2,3,4')
    print('PASS: Schur criterion at',witness_checks,'weighted external couplings')
    print('PASS: exact crossover polynomial identity for all r=3..23, s in tested ranges')

if __name__=='__main__':main()
