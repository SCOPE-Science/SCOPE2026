"""Exact finite regression for normalized consecutive tetrahedral numerical semigroups.

This test is supplementary to the symbolic proof in RESULT.md.
Python 3.9+; no external packages.
"""
from math import gcd
from heapq import heappush, heappop


def tetra(n):
    return n * (n + 1) * (n + 2) // 6


def data(n):
    k, r = divmod(n, 6)
    a = [2*k*(6*k+1), (3*k+1)*(6*k+1),
         2*(2*k+1)*(3*k+1), (2*k+1)*(3*k+2),
         2*(3*k+2)*(6*k+5), (k+1)*(6*k+5)][r]
    b = [(2*k+1)*(6*k+1), 2*(3*k+1)*(3*k+2),
         (2*k+1)*(6*k+5), 2*(k+1)*(3*k+2),
         (6*k+5)*(6*k+7), 2*(k+1)*(3*k+4)][r]
    c = [2*(2*k+1)*(3*k+2), (3*k+2)*(6*k+5),
         2*(k+1)*(6*k+5), (k+1)*(6*k+7),
         2*(3*k+4)*(6*k+7), (2*k+3)*(3*k+4)][r]
    h = [6*k+1, 3*k+1, 2*k+1, 3*k+2, 6*k+5, 3*k+4][r]
    f = [96*k**3+76*k*k+16*k-1,
         162*k**3+171*k*k+45*k-1,
         96*k**3+140*k*k+56*k+3,
         30*k**3+59*k*k+35*k+5,
         432*k**3+1188*k*k+1068*k+309,
         30*k**3+85*k*k+75*k+19][r]
    d = gcd(tetra(n), gcd(tetra(n+1), tetra(n+2)))
    return a, b, c, h, f, d


def direct_frobenius_genus(a, b, c):
    """Independent shortest-residue-path Apéry calculation."""
    m = min(a,b,c)
    dists = [-1]*m
    dists[0] = 0
    heap = [(0,0)]
    while heap:
        dist,r = heappop(heap)
        if dist != dists[r]: continue
        for step in (a,b,c):
            nr = (r+step) % m
            nd = dist+step
            if dists[nr] < 0 or nd < dists[nr]:
                dists[nr] = nd
                heappush(heap,(nd,nr))
    assert all(x >= 0 for x in dists)
    return max(dists)-m, sum(dists)//m-(m-1)//2


def main():
    count = 0
    for n in range(2,141):
        a,b,c,h,f,d = data(n)
        actual = tuple(tetra(n+j)//d for j in range(3))
        assert actual == (a,b,c), (n,'normalization',actual,(a,b,c))
        assert gcd(a,gcd(b,c)) == 1
        U,V,W = ((a,b,c) if n % 6 != 5 else (c,b,a))
        assert gcd(U,V) == h and gcd(h,W) == 1
        assert gcd(U//h,V//h) == 1
        k,r=divmod(n,6)
        coeff=[(0,2*(3*k+2)),(3*k+2,2),(0,2*(k+1)),
               (3*(k+1),2),(0,2*(3*k+4)),(k+1,2*k+1)][r]
        assert W == coeff[0]*(U//h)+coeff[1]*(V//h)
        assert f == U*V//h-U-V+(h-1)*W
        F,G = direct_frobenius_genus(a,b,c)
        assert (F,G) == (f,(f+1)//2), (n,F,G,f)
        count+=1
    expected = {2:3,3:5,4:309,5:19,6:187,9:129,10:2997,11:209,40:142797}
    for n,val in expected.items():
        assert data(n)[4] == val
    print('EXACT_REGRESSION_OK normalized_triplets=%d n=2..140; six phases; symmetry, Frobenius, genus, and witness checks' % count)

if __name__ == '__main__':
    main()
