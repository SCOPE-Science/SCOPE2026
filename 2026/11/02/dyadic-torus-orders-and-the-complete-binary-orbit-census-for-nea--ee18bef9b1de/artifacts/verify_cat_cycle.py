"""Exact finite checks of the dyadic cyclic cat-map theorem.

Run with Python 3: python verify_cat_cycle.py
No external dependencies. Finite tests corroborate, but do not replace,
the all-size ring and 2-adic proof in RESULT.md.
"""
from collections import Counter


def coupling(n):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        c[i][(i-1) % n] = 1
        c[i][(i+1) % n] = 1
    return c


def matmul(a, b, modulus):
    rows, mids, cols = len(a), len(b), len(b[0])
    out = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for k in range(mids):
            if a[i][k]:
                aik = a[i][k]
                for j in range(cols):
                    out[i][j] += aik * b[k][j]
        for j in range(cols):
            out[i][j] %= modulus
    return out


def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def matrix(n, modulus):
    c = coupling(n)
    c2 = matmul(c,c,modulus)
    I=identity(n)
    z=[[0]*n for _ in range(n)]
    return [[*I[i], *c[i]] for i in range(n)] + [
           [*c[i], *((I[i][j]+c2[i][j])%modulus for j in range(n))]
           for i in range(n)]


def power(a, exponent, modulus):
    r=identity(len(a))
    while exponent:
        if exponent&1:
            r=matmul(r,a,modulus)
        exponent//=2
        if exponent:
            a=matmul(a,a,modulus)
    return r


def cycle_step(state,n):
    mask=(1<<n)-1
    q=state&mask
    p=state>>n
    def C(v):
        return (((v<<1)|(v>>(n-1))) ^ ((v>>1)|(v<<(n-1))))&mask
    return (q^C(p)) | ((p^C(q)^C(C(p))) << n)


def brute_orbit_census(n):
    N=1<<(2*n)
    visited=bytearray(N)
    counts=Counter()
    for start in range(N):
        if visited[start]:
            continue
        path=[]
        v=start
        while not visited[v]:
            visited[v]=1
            path.append(v)
            v=cycle_step(v,n)
        assert v==start, 'Invertible transition must revisit starting state.'
        counts[len(path)]+=1
    return counts


def rank_mod2(a):
    nrows,ncols=len(a),len(a[0])
    rows=[sum((int(v&1)<<j) for j,v in enumerate(row)) for row in a]
    rank=0
    for j in range(ncols):
        pivot=next((i for i in range(rank,nrows) if (rows[i]>>j)&1),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for i in range(nrows):
            if i != rank and ((rows[i]>>j)&1):
                rows[i]^=rows[rank]
        rank+=1
    return rank


def run():
    tests=0
    for n in (4,8,16,32):
        assert n&(n-1)==0
        t=n//2
        for s in range(1,7):
            mod=1<<s
            a=matrix(n,mod)
            T=t*(1<<(s-1))
            assert power(a,T,mod)==identity(2*n), (n,s,'upper')
            assert power(a,T//2,mod)!=identity(2*n), (n,s,'primitive')
            tests+=2
        a=matrix(n,2)
        h=1
        while h<=t:
            delta=power(a,h,2)
            for i in range(2*n): delta[i][i]^=1
            rank=rank_mod2(delta)
            expected_nullity=2*min(2*h,n)
            assert 2*n-rank==expected_nullity,(n,h,rank)
            tests+=1
            h*=2
    for n in (4,8):
        counts=brute_orbit_census(n)
        expected={}
        prev=0
        h=1
        while h<=n//2:
            fixed=1 << (2*min(2*h,n))
            expected[h]=(fixed-prev)//h
            prev=fixed
            h*=2
        assert dict(counts)==expected,(n,counts,expected)
        tests+=1
        print('n=',n,'exact primitive cycles:',dict(sorted(counts.items())))
    print('PASS:',tests,'independent matrix/finite-field/order/census comparisons')


if __name__=='__main__':
    run()
