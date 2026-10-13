"""Exact-rational checks for the price-dependent double-star spectral-gap formulas.

Usage: python3 checker.py
Standard library only; no numerical eigenvalue tolerances or random tests.
The full infinite-parameter proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def matmul(a, b):
    return [[sum(a[i][r]*b[r][j] for r in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank(a):
    m = [list(row) for row in a]
    if not m:
        return 0
    piv = 0
    for j in range(len(m[0])):
        t = next((i for i in range(piv, len(m)) if m[i][j]), None)
        if t is None:
            continue
        m[piv], m[t] = m[t], m[piv]
        d = m[piv][j]
        m[piv] = [v/d for v in m[piv]]
        for i in range(len(m)):
            if i != piv:
                c = m[i][j]
                if c:
                    m[i] = [x-c*y for x, y in zip(m[i], m[piv])]
        piv += 1
        if piv == len(m):
            break
    return piv


def case(k, l, q):
    assert k >= l >= 1 and q > 0
    n = k+l+2
    h = F(2*k*l+k+l, n)
    qc = F(k-l, l+1)
    high = q > qc
    A = 1+q/2
    Zlo = k+l+2*l*q+(l+1)*q*q
    Zhi = 2*h*(1+q)+F(h+1, 2)*q*q
    assert Zlo-Zhi == ((l+1)*q-(k-l))**2/n
    if not high:
        alpha = (l+(l+1)*q)/k
        assert 0 <= alpha <= 1 and k >= 2
        xl, xr, y = F(1), 1+q, 1+l+l/q
        Z = Zlo
        positions = [alpha]*k+[F(0), -q]+[-(q+1)]*l
        # Gram matrix of a regular simplex transverse to the common axis.
        G = [[positions[i]*positions[j] for j in range(n)] for i in range(n)]
        s = 1-alpha**2
        for i in range(k):
            for j in range(k):
                G[i][j] += s*(k-1 if i==j else -1)/F(k-1)
        assert (rank(G) == k if q < qc else rank(G) == 1)
    else:
        m = F(k-l, n)*A
        positions = [A-m]*k+[q/2-m, -q/2-m]+[-A-m]*l
        xl = 2*F(l+1,n)*A
        xr = 2*F(k+1,n)*A
        y = h/q+(h+1)/2
        Z = Zhi
        G = [[positions[i]*positions[j] for j in range(n)] for i in range(n)]
        assert rank(G) == 1
        assert xl > 1 and xr > 1
        U,V = positions[k],positions[k+1]
        assert U>0 and V<0
        # Schur complement after eliminating positive leaf blocks in L-I.
        d1 = y-1-k*xl/(xl-1)
        d2 = y-1-l*xr/(xr-1)
        assert d1==y*V/U and d2==y*U/V
        assert d1<0 and d2<0 and d1*d2==y*y
    edges=[]
    for i in range(k):
        edges.append((i,k,xl,F(1)))
    edges.append((k,k+1,y,q*q))
    for j in range(l):
        edges.append((k+1,k+2+j,xr,F(1)))
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    budget=F(0)
    for i,j,w,c in edges:
        L[i][i]+=w; L[j][j]+=w
        L[i][j]-=w; L[j][i]-=w
        budget+=w*c
        assert G[i][i]+G[j][j]-2*G[i][j] == c
    assert budget==Z
    assert sum(G[i][i] for i in range(n))==Z
    assert all(sum(G[i][j] for j in range(n))==0 for i in range(n))
    assert matmul(L,G)==G
    # Multiplicity of eigenvalue one: k at/below the switch, one above.
    P=[[L[i][j]-(F(1) if i==j else F(0)) for j in range(n)] for i in range(n)]
    assert n-rank(P) == (1 if high else k)
    if not high:
        # Principal block of L-I after deleting left hub is PSD: zero
        # k-by-k leaf block; grounded right-star Schur complement is zero.
        assert xl==1 and xr-1==q
        assert y-1-l*xr/(xr-1)==0
    return high


def main():
    tests=0; low=0; high=0
    qs=[F(1,9),F(1,4),F(1,2),F(1),F(3,2),F(2),F(3),F(5),F(10)]
    for k in range(1,8):
        for l in range(1,k+1):
            qc=F(k-l,l+1)
            Q=sorted(set(qs+([qc,F(qc,2),qc+F(1,7)] if qc else [])))
            for q in Q:
                if q <= 0:
                    continue
                b=case(k,l,q)
                tests+=1; high+=b; low+=not b
    print(f'VERIFY_OK {tests} exact rational cases; {low} low-price and {high} high-price; Gram eigenrelations, budgets, ranks and Schur certificates')

if __name__=='__main__':
    main()
