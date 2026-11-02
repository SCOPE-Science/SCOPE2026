"""Independent finite-field enumeration for characteristic-two chain evolution algebra.
Run: python verify.py. All tests are direct defining-equation checks.
"""
from itertools import product

def gf_mul(a, b, q):
    if q == 2:
        return a & b
    modulus = {4: 0b111, 8: 0b1011}[q]
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= modulus
    return ans

def algebra_multiply(x,y,q):
    n = len(x)
    return (0,) + tuple(gf_mul(x[i], y[i], q) for i in range(n-1))

def apply_r(columns, v, q):
    n=len(columns)
    out=[0]*n
    for j, coef in enumerate(v):
        if coef:
            for i, z in enumerate(columns[j]):
                out[i] ^= gf_mul(coef, z, q)
    return tuple(out)

def rank(columns,q):
    # Column elimination without relying on normal-form structure.
    n=len(columns)
    vectors=[list(row) for row in zip(*columns)]
    r=0
    for c in range(n):
        pivot=next((z for z in range(r,n) if vectors[z][c]),None)
        if pivot is None: continue
        vectors[r],vectors[pivot]=vectors[pivot],vectors[r]
        coeff=vectors[r][c]
        inv=next(x for x in range(1,q) if gf_mul(x,coeff,q)==1)
        vectors[r]=[gf_mul(inv,x,q) for x in vectors[r]]
        for j in range(n):
            if j!=r and vectors[j][c]:
                fac=vectors[j][c]
                vectors[j]=[u^gf_mul(fac,v,q) for u,v in zip(vectors[j],vectors[r])]
        r+=1
    return r

def direct_rb(columns,q):
    n=len(columns)
    for i in range(n):
        for j in range(i,n):
            lhs=algebra_multiply(columns[i],columns[j],q)
            one=algebra_multiply(columns[i],tuple(int(k==j) for k in range(n)),q)
            two=algebra_multiply(tuple(int(k==i) for k in range(n)),columns[j],q)
            basic=tuple(one[k]^two[k]^(int(k==i+1) if i==j and i<n-1 else 0) for k in range(n))
            rhs=apply_r(columns,basic,q)
            if lhs!=rhs:
                return False
    return True

def columns_from_first(v,q):
    columns=[tuple(v)]
    for j in range(1,len(v)):
        columns.append(algebra_multiply(columns[-1],columns[-1],q))
    return columns

def expected_rank_count(n,q):
    d={0:1,1:q-1,n:(n-1)*q*(q-1)}
    for r in range(2,n):d[r]=q*(q-1)
    return d

def check(n,q):
    observed={r:0 for r in range(n+1)}
    for v in product(range(q),repeat=n):
        cols=columns_from_first(v,q)
        if direct_rb(cols,q):
            observed[rank(cols,q)]+=1
    predicted=expected_rank_count(n,q)
    assert observed=={r:predicted.get(r,0) for r in range(n+1)}, (n,q,observed,predicted)
    print(f'PASS q={q} n={n} total={sum(observed.values())} ranks={observed}')

if __name__=='__main__':
    for q,nmax in [(2,8),(4,6),(8,5)]:
        for n in range(2,nmax+1):check(n,q)
    print('VERIFY_OK')
