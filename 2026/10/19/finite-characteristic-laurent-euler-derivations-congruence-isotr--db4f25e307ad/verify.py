"""Finite-matrix checks for the characteristic-p Laurent Euler isotropy and orbit formula.

Only elementary arithmetic over prime fields is required: an f-component column
models a weight in any f-dimensional vector space over the prime field.
Run with: python verify.py
"""
from itertools import product
from math import prod


def rank_mod(rows, p):
    if not rows:
        return 0
    m = [list(map(lambda x: x % p, row)) for row in rows]
    h, w, rank = len(m), len(m[0]), 0
    for col in range(w):
        pivot = next((i for i in range(rank, h) if m[i][col]), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        inv = pow(m[rank][col], -1, p)
        m[rank] = [(a * inv) % p for a in m[rank]]
        for i in range(h):
            if i != rank and m[i][col]:
                factor = m[i][col]
                m[i] = [(a-factor*b) % p for a,b in zip(m[i],m[rank])]
        rank += 1
        if rank == h:
            break
    return rank


def determinant_mod(mat, p):
    n = len(mat)
    a = [list(row) for row in mat]
    det = 1
    for k in range(n):
        piv = next((i for i in range(k,n) if a[i][k] % p), None)
        if piv is None:
            return 0
        if piv != k:
            a[k],a[piv] = a[piv],a[k]
            det = -det
        x=a[k][k] % p
        det=det*x % p
        inverse=pow(x,-1,p)
        for i in range(k+1,n):
            mult=a[i][k]*inverse % p
            for j in range(k,n):
                a[i][j]=(a[i][j]-mult*a[k][j]) % p
    return det % p


def matrices_image(p,n):
    allowed = {1 % p, (-1) % p}
    mats=[]
    for data in product(range(p),repeat=n*n):
        a=[data[i*n:(i+1)*n] for i in range(n)]
        if determinant_mod(a,p) in allowed:
            mats.append(data)
    return mats


def action(weight, mat, p, n, f):
    # Weight is a flattened f x n matrix; right multiplication by an exponent matrix.
    out=[]
    for i in range(f):
        for j in range(n):
            out.append(sum(weight[i*n+k]*mat[k*n+j] for k in range(n))%p)
    return tuple(out)


def gaussian(n,k,p):
    num=prod(p**n-p**i for i in range(k))
    den=prod(p**k-p**i for i in range(k))
    return num//den


def orbit_formula(p,n,f):
    delta=len({1%p, (-1)%p})
    return 1+sum(gaussian(f,r,p) for r in range(1,min(n-1,f)+1)) + (gaussian(f,n,p)*(p-1)//delta if n <= f else 0)


def check(p,n,f):
    mats=matrices_image(p,n)
    image_size=len(mats)
    delta=len({1%p, (-1)%p})
    full_gl=prod(p**n-p**i for i in range(n))
    assert image_size == full_gl*delta//(p-1), (p,n,image_size)
    seen=set()
    orbits=[]
    for w in product(range(p),repeat=n*f):
        if w in seen:
            continue
        actual={action(w,m,p,n,f) for m in mats}
        assert not (actual & seen)
        r=rank_mod([w[i*n:(i+1)*n] for i in range(f)],p)
        expected=(prod(p**n-p**i for i in range(r)) if r<n else image_size)
        assert len(actual)==expected, (p,n,f,r,len(actual),expected)
        # The index of the exponent stabilizer equals the size of the H-orbit.
        assert image_size % len(actual)==0
        # The number of cosets of the kernel lattice is p^r.
        values={tuple(sum(w[i*n+j]*v[j] for j in range(n))%p for i in range(f))
                for v in product(range(p),repeat=n)}
        assert len(values)==p**r
        seen.update(actual)
        orbits.append((r,len(actual)))
    assert len(seen)==p**(f*n)
    expected_orbits=orbit_formula(p,n,f)
    assert len(orbits)==expected_orbits, (p,n,f,len(orbits),expected_orbits)
    print('PASS p=%s n=%s f=%s: matrices=%s; derivations=%s; orbits=%s' %
          (p,n,f,image_size,len(seen),len(orbits)))


if __name__=='__main__':
    for p,n,f in [(2,1,2),(3,1,2),(5,1,2),
                  (2,2,2),(3,2,2),(5,2,2),(3,2,3),
                  (2,3,2),(3,3,1)]:
        check(p,n,f)
    print('ALL CHECKS PASSED')
