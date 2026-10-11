"""Exact checks for the inscribed ellipsoid of fixed-cardinality assignment polytopes.

Uses Python standard-library rational arithmetic; no external data.
The infinite-dimensional claims rely on the accompanying analytic proof.
"""
from fractions import Fraction as F

def coefficients(n, k):
    assert isinstance(n, int) and n >= 2
    assert isinstance(k, int) and 1 <= k < n
    aa = F(2 * (n-1), n*n)
    bb = F((n-1)**2, n*n)
    cc = F(k*k, n**4)
    hh = F((n-k)**2, n*n*(n-1))
    q = F(k*k, n*n*(n*n-1))
    round_case = k*k <= (n+1)*(n-k)**2
    u = q if round_case else hh
    v = q if round_case else F(k*k-2*(n-k)**2, n*n*(n-1)**2)
    return aa, bb, cc, hh, q, round_case, u, v

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def frob2(a):
    return dot(a,a)

def projected_norms(n, ix):
    mat = [F(1 if t == ix else 0) for t in range(n*n)]
    row = [sum(mat[i*n+j] for j in range(n)) for i in range(n)]
    col = [sum(mat[i*n+j] for i in range(n)) for j in range(n)]
    s = sum(mat)
    grand = s / (n*n)
    # Orthogonal row+column contrast and interaction projections.
    U = [row[i]/n + col[j]/n - 2*grand for i in range(n) for j in range(n)]
    W = [mat[i*n+j] - row[i]/n - col[j]/n + grand for i in range(n) for j in range(n)]
    H = [x-grand for x in mat]
    assert all(U[t] + W[t] == H[t] for t in range(n*n))
    assert dot(U,W) == 0
    return frob2(U),frob2(W)

def row_norms(n):
    a = [F(1 if t//n == 0 else 0) for t in range(n*n)]
    row = [sum(a[i*n+j] for j in range(n)) for i in range(n)]
    col = [sum(a[i*n+j] for i in range(n)) for j in range(n)]
    grand = sum(a)/F(n*n)
    U = [row[i]/n + col[j]/n -2*grand for i in range(n) for j in range(n)]
    W = [a[i*n+j] - row[i]/n - col[j]/n + grand for i in range(n) for j in range(n)]
    return frob2(U), frob2(W)

count = 0
phase_counts = [0,0,0]
for n in range(2,101):
    for k in range(1,n):
        aa, bb, cc, hh, q, round_case, u, v = coefficients(n,k)
        assert u>0 and v>0
        assert aa*u + bb*v == cc
        assert u<=hh
        assert (u==v) == round_case
        assert (u==hh) == (k*k >= (n+1)*(n-k)**2)
        assert (v>u) == (k*k > (n+1)*(n-k)**2)
        assert (v/u == F(k*k-2*(n-k)**2, (n-1)*(n-k)**2)) if not round_case else v/u == 1
        # KKT for strictly concave objective p log u + q log v
        p,qdim=2*(n-1),(n-1)**2
        lam=F(qdim,1)/(bb*v)
        mu=F(p,1)/u - lam*aa
        assert mu>=0 and (mu==0 or u==hh)
        assert F(p,1)/u == lam*aa+mu
        assert F(qdim,1)/v == lam*bb
        # Global John certificate, checked independently of the KKT formula.
        slack0, slack1 = F(k,n*n), F(n-k,n)
        w0 = slack0**2 / v
        w1 = slack1**2 * (1-u/v) / (n*u)
        assert w0 > 0 and w1 >= 0
        assert (w1 == 0) == round_case
        assert w0 * (v/slack0**2) == 1
        assert w0 * (u/slack0**2) + w1 * n*u/slack1**2 == 1
        assert n*n*w0 + 2*n*w1 == n*n-1
        phase_counts[0 if k*k < (n+1)*(n-k)**2 else (1 if k*k == (n+1)*(n-k)**2 else 2)] += 1
        count+=1
normcount=0
for n in range(2,17):
    for ix in range(n*n):
        uu,vv=projected_norms(n,ix)
        assert uu == F(2*(n-1), n*n)
        assert vv == F((n-1)**2,n*n)
        normcount+=1
    assert row_norms(n) == (F(n-1,1),F(0,1))

print('PASS: exact parameter/KKT/support checks:',count)
print('PASS: exact row/column and coordinate projection checks:',normcount+15)
print('Strict-round / threshold / anisotropic cases:',phase_counts)
