"""Independent finite-field tests for automorphisms of monomial square-zero complete intersections.
Run: python3 verify.py. Standard library only.
"""
from itertools import product
from math import factorial, prod


def ff_add(a,b,q):
    return a ^ b if q in (2,4) else (a+b)%q


def ff_mul(a,b,q):
    if q != 4:
        return a*b%q
    z=0
    while b:
        if b&1:
            z ^= a
        b >>= 1
        a <<= 1
        if a&4:
            a ^= 7  # irreducible T^2+T+1
    return z


def multiply(f,g,d,q):
    z=[0]*(1<<d)
    for s,a in enumerate(f):
        if a==0: continue
        for t,b in enumerate(g):
            if b and not(s&t):
                j=s|t
                z[j]=ff_add(z[j],ff_mul(a,b,q),q)
    return tuple(z)


def mat_invertible(rows,q):
    n=len(rows)
    a=[list(r) for r in rows]
    h=0
    for c in range(n):
        pivot=next((i for i in range(h,n) if a[i][c]),None)
        if pivot is None:continue
        a[h],a[pivot]=a[pivot],a[h]
        scale=next(t for t in range(1,q) if ff_mul(t,a[h][c],q)==1)
        a[h]=[ff_mul(v,scale,q) for v in a[h]]
        for i in range(n):
            if i!=h and a[i][c]:
                coef=a[i][c]
                a[i]=[ff_add(a[i][j],ff_mul(coef,a[h][j],q),q)
                      if q in (2,4) else (a[i][j]-ff_mul(coef,a[h][j],q))%q
                      for j in range(n)]
        h+=1
    return h==n


def expected(d,q):
    if q%2==0:
        gl=prod(q**d-q**j for j in range(d))
        return gl*q**(d*(2**d-d-1))
    return factorial(d)*(q-1)**d * q**(d*(2**(d-1)-1))


def candidates(d,q):
    n=1<<d
    for a in product(range(q),repeat=n-1):
        f=(0,)+a
        if multiply(f,f,d,q)==(0,)*n:
            yield f


def exhaustive(d,q):
    good=list(candidates(d,q))
    counts={}
    for f in good:
        linear=tuple(f[1<<i] for i in range(d))
        counts[linear]=counts.get(linear,0)+1
    found=0
    for linear_tuple in product(counts,repeat=d):
        if mat_invertible(linear_tuple,q):
            w=1
            for linear in linear_tuple:w*=counts[linear]
            found+=w
    assert found==expected(d,q),(d,q,found,expected(d,q))
    print(f"(d,q)=({d},{q}), admissible_generator_images={len(good)}, automorphisms={found}")
    return found


def derivation_dimension(d,q):
    # A derivation is determined by f_i=D(x_i), subject to 2 x_i f_i=0.
    # Count solution vectors and take log_q, independently using basis multiplication.
    n=1<<d
    dim=0
    for i in range(d):
        constraints=[]
        xi=tuple(int(j==1<<i) for j in range(n))
        for j in range(n):
            basis=tuple(int(t==j) for t in range(n))
            xif=multiply(xi,basis,d,q)
            twice=tuple(ff_add(t,t,q) for t in xif)
            constraints.append(twice)
        # each nonzero constraint is a distinct independent basis direction
        matrix=[[constraints[j][t] for j in range(n)] for t in range(n)]
        # rank over GF(q)
        h=0
        for col in range(n):
            pivot=next((j for j in range(h,n) if matrix[j][col]),None)
            if pivot is None:continue
            matrix[h],matrix[pivot]=matrix[pivot],matrix[h]
            scale=next(s for s in range(1,q) if ff_mul(s,matrix[h][col],q)==1)
            matrix[h]=[ff_mul(a,scale,q) for a in matrix[h]]
            for row in range(n):
                if row!=h and matrix[row][col]:
                    cc=matrix[row][col]
                    matrix[row]=[(matrix[row][j]-ff_mul(cc,matrix[h][j],q))%q if q%2 else ff_add(matrix[row][j],ff_mul(cc,matrix[h][j],q),q) for j in range(n)]
            h+=1
        dim+=n-h
    assert dim==(d*2**d if q%2==0 else d*2**(d-1))
    print(f"(d,q)=({d},{q}), derivation_tangent_dim={dim}")


if __name__=='__main__':
    for d,q in ((2,2),(2,3),(2,4),(2,5),(3,2),(3,3)):
        exhaustive(d,q)
        derivation_dimension(d,q)
    print('SQUARE_ZERO_COMPLETE_INTERSECTION_AUT_OK')
