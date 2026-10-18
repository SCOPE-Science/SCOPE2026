"""Exact finite-field checks for commuting affine idempotents.

Run: python affine_semilattice_checker.py. Uses only the Python standard library.
Direct checks enumerate affine maps independently of the orbit formula.
"""
from itertools import product
from math import prod, factorial

def gl_order(n, q):
    ans = 1
    for j in range(n):
        ans *= q**n - q**j
    return ans

def dimension_vectors(n, m):
    if m==1:
        yield (n,)
    else:
        for d in range(n+1):
            for rest in dimension_vectors(n-d,m-1):
                yield (d,)+rest

def prediction(n,q,k):
    labels=1<<k
    z=0
    orbit_counts={}
    for ds in dimension_vectors(n,labels):
        s=q**(n-ds[-1])*gl_order(n,q)//prod(gl_order(d,q) for d in ds)
        assert q**(n-ds[-1])*gl_order(n,q)%prod(gl_order(d,q) for d in ds)==0
        z+=s
        orbit_counts[ds]=s
    return z,orbit_counts

def matmul(A,B,q):
    n=len(A)
    return tuple(tuple(sum(A[i][h]*B[h][j] for h in range(n))%q for j in range(n)) for i in range(n))

def apply(A,b,v,q):
    n=len(b)
    return tuple((sum(A[i][j]*v[j] for j in range(n))+b[i])%q for i in range(n))

def all_affine_idempotents(q,n):
    vectors=list(product(range(q),repeat=n))
    good=[]
    for mflat in product(range(q),repeat=n*n):
        A=tuple(mflat[i*n:(i+1)*n] for i in range(n))
        if matmul(A,A,q)!=A: continue
        for b in vectors:
            if apply(A,b,b,q)!=b:  # equivalently A b = 0
                continue
            good.append((A,b))
    return good

def compose(f,g,q):
    A,b=f;B,c=g
    return (matmul(A,B,q),tuple((sum(A[i][j]*c[j] for j in range(len(b)))+b[i])%q for i in range(len(b))))

def matrix_rank(A,q):
    mat=[list(row) for row in A]
    m=len(mat); rank=0
    for col in range(m):
        i=next((j for j in range(rank,m) if mat[j][col]%q),None)
        if i is None: continue
        mat[rank],mat[i]=mat[i],mat[rank]
        inv=pow(mat[rank][col],-1,q)
        mat[rank]=[(inv*x)%q for x in mat[rank]]
        for j in range(m):
            if j!=rank:
                t=mat[j][col]
                mat[j]=[(u-t*v)%q for u,v in zip(mat[j],mat[rank])]
        rank+=1
    return rank

def check(q,n):
    maps=all_affine_idempotents(q,n)
    actual_profile={}
    for a in maps:
        for b in maps:
            ab=compose(a,b,q)
            if ab!=compose(b,a,q):continue
            t=(matrix_rank(a[0],q),matrix_rank(b[0],q),matrix_rank(ab[0],q))
            actual_profile[t]=actual_profile.get(t,0)+1
    total=sum(actual_profile.values())
    expected,orbit_counts=prediction(n,q,2)
    predicted_profile={}
    for ds,mult in orbit_counts.items():
        key=(ds[1]+ds[3], ds[2]+ds[3], ds[3])
        predicted_profile[key]=predicted_profile.get(key,0)+mult
    assert actual_profile==predicted_profile,(actual_profile,predicted_profile)
    print(f'PROFILE q={q}, n={n}, rank_cells={len(actual_profile)}')
    print(f'RESULT q={q}, n={n}, idempotents={len(maps)}, commuting_pairs={total}, expected={expected}')
    assert total==expected

def check_triples_line(q):
    # n=1 has q constant maps plus identity, tuples commute iff all nonidentities have the same constant.
    for k in [2,3,4]:
        expected,_=prediction(1,q,k)
        actual=1+q*((2**k)-1)
        assert expected==actual,(expected,actual)
        print(f'RESULT q={q}, n=1, k={k}, tuples={actual}')

if __name__=='__main__':
    for q,n in [(2,1),(3,1),(2,2),(3,2),(2,3)]: check(q,n)
    for q in [2,3,5]:check_triples_line(q)
    print('ALL_AFFINE_CHECKS_PASSED')
