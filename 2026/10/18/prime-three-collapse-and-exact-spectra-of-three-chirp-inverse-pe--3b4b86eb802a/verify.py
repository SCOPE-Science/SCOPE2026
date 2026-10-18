#!/usr/bin/env python3
"""Exact, self-contained finite-field checks for quadratic-chirp pencil filters."""
from itertools import product
from collections import Counter


def inv_det(a, p):
    n = len(a)
    mat = [[v % p for v in row] + [int(i == j) for j in range(n)] for i, row in enumerate(a)]
    det = 1
    for k in range(n):
        i = next((i for i in range(k, n) if mat[i][k]), None)
        if i is None:
            return 0, None
        if i != k:
            mat[k], mat[i] = mat[i], mat[k]
            det = -det
        pivot = mat[k][k]
        det = det * pivot % p
        mat[k] = [(v * pow(pivot, -1, p)) % p for v in mat[k]]
        for i in range(n):
            if i == k:
                continue
            x = mat[i][k]
            mat[i] = [(u - x*v) % p for u, v in zip(mat[i], mat[k])]
    return det % p, [row[n:] for row in mat]


def add(a, b, j, p):
    return [[(u+j*v) % p for u, v in zip(row1, row2)] for row1, row2 in zip(a, b)]


def quad(a, x, p):
    return sum(x[i] * a[i][j] * x[j] for i in range(len(x)) for j in range(len(x))) % p


def dot(a, b, p):
    return sum(u*v for u, v in zip(a, b)) % p


def convolve(a, b):
    p = len(a)
    ans = [0]*p
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            ans[(i+j) % p] += u*v
    return ans


def canon(a):
    return tuple(x-a[-1] for x in a[:-1])


def legendre(a, p):
    if a % p == 0: return 0
    return 1 if pow(a % p, (p-1)//2, p)==1 else -1


def count_zero(a, p):
    return sum(quad(a, x, p)==0 for x in product(range(p),repeat=len(a)))


def verify(p, u, v):
    d=len(u)
    mats=[add(u,v,j,p) for j in range(3)]
    pairs=[inv_det(a,p) for a in mats]
    assert all(det != 0 for det,_ in pairs)
    w=[legendre(det,p) for det,_ in pairs]
    invs=[m for _,m in pairs]
    points=list(product(range(p), repeat=d))
    g=[0]*p
    for t in range(p): g[t*t%p]+=1
    gd=[1]+[0]*(p-1)
    for _ in range(d): gd=convolve(gd,g)
    inv4=pow(4,-1,p)
    total_zeros=0
    geom_rank=0
    for xi in points:
        left=[0]*p
        for x in points:
            for j, a in enumerate(invs):
                left[(quad(a,x,p)-dot(xi,x,p))%p] += w[j]
        # From the elementary completing-the-square Gauss identity.
        uq=(-inv4*quad(u,xi,p))%p
        vq=(-inv4*quad(v,xi,p))%p
        rhs=[0]*p
        for j in range(3):
            shift=(uq+j*vq)%p
            for t in range(p): rhs[(t+shift)%p]+=gd[t]
        assert canon(left)==canon(rhs), ('Fourier formula',p,d,xi,left,rhs)
        zero=(canon(left)==(0,)*(p-1))
        expected=(p==3 and quad(v,xi,p)!=0)
        assert zero==expected, ('zero set',p,d,xi,zero,expected)
        total_zeros+=int(zero)
        geom_rank+=int(not zero)
    assert geom_rank == (count_zero(v,p) if p==3 else p**d)
    return (p,d,len(points),geom_rank,total_zeros, tuple(w))


def main():
    u2=[[1,0],[0,1]]
    v2=[[1,1],[1,2]]
    cases=[
        (3,u2,v2),
        (3,[[1,0,0],[0,1,0],[0,0,1]], [[1,1,0],[1,2,0],[0,0,0]]),
        (5,u2,[[1,0],[0,1]]),
        (7,u2,v2),
        (11,u2,[[1,0],[0,1]])
    ]
    checks=[]
    for p,u,v in cases:
        checks.append(verify(p,u,v))
    print('VERIFY_OK exact_cyclotomic_Fourier_coefficients=PASS; cases=',checks)

def count_spectrum(p, d, diag):
    """Check the complete quadratic-form value count for diagonal test forms."""
    r=sum(a % p != 0 for a in diag)
    delta=1
    for a in diag:
        if a % p: delta=delta*a%p
    pts=product(range(p), repeat=d)
    counts=Counter(sum(a*x*x for a,x in zip(diag,pt))%p for pt in pts)
    m=r//2
    for a in range(p):
        if r==0:
            predicted=p**d if a==0 else 0
        elif r%2:
            predicted=p**(d-1)+legendre(((-1)**m*a*delta)%p,p)*p**(d-m-1)
        else:
            sig=legendre(((-1)**m*delta)%p,p)
            predicted=p**(d-1)+sig*(p-1 if a==0 else -1)*p**(d-m-1)
        assert predicted==counts[a],('quadratic form census',p,d,diag,a,predicted,counts[a])


_orig_main=main
def main():
    _orig_main()
    tests=0
    for p,d in [(3,2),(3,3),(3,4),(5,2),(5,3),(7,3),(11,2)]:
        for r in range(d+1):
            for a in (1,2):
                diag=[1]*(max(r-1,0))+([a] if r else [])+[0]*(d-r)
                count_spectrum(p,d,diag)
                tests+=1
    print('VERIFY_OK diagonal_quadratic_level_set_censuses=',tests)

if __name__=='__main__':
    main()
