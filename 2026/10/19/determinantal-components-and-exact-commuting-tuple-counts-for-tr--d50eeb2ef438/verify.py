"""Independent finite checks of commuting tuples in a truncated Witt Lie algebra.
Only Python's standard library is used; run with ``python verify.py``.
The finite calculations supplement, but do not establish, the general theorem.
"""
from itertools import product


def brackets_zero(u, v, p):
    n = len(u)
    for k in range(1, n):
        coefficient = 0
        for i in range(k + 1):
            j = k - i
            coefficient += (j - i) * u[i] * v[j]
        if coefficient % p:
            return False
    return True


def component_member(rows, i, p):
    n = len(rows[0]); m = n - 2 * i
    if any(any(row[:i]) for row in rows):
        return False
    # rank <= 1 of s by m matrix; compute 2x2 minors
    for a in range(len(rows)):
        for b in range(a + 1, len(rows)):
            for x in range(m):
                for y in range(x + 1, m):
                    if (rows[a][i + x]*rows[b][i + y]
                            - rows[a][i + y]*rows[b][i + x]) % p:
                        return False
    return True


def predicted(n, s, q):
    m = (n + 1)//2
    return q**(s*(n-m)) + (q**s-1) * sum(q**(s*i+n-2*i-1) for i in range(m))


def brute(n, s, p, check_cover):
    vectors = list(product(range(p), repeat=n))
    size = len(vectors)
    commuting = [[brackets_zero(a,b,p) for b in vectors] for a in vectors]
    result = 0
    if s == 2:
        for a in range(size):
            for b in range(size):
                actual = commuting[a][b]
                result += actual
                if check_cover:
                    covered = any(component_member((vectors[a],vectors[b]),i,p)
                                  for i in range((n+1)//2))
                    assert actual == covered, (n,s,p,a,b)
    elif s == 3:
        for a in range(size):
            for b in range(size):
                if not commuting[a][b]:
                    continue
                for c in range(size):
                    actual = commuting[a][c] and commuting[b][c]
                    result += actual
                    if check_cover:
                        covered = any(component_member(
                            (vectors[a],vectors[b],vectors[c]),i,p)
                            for i in range((n+1)//2))
                        assert actual == covered, (n,s,p,a,b,c)
    else:
        raise ValueError(s)
    target = predicted(n,s,p)
    assert result == target, (n,s,p,result,target)
    return result


def modular_rank(a,p):
    a = [row[:] for row in a]
    r=0; nrows=len(a); ncols=len(a[0])
    for c in range(ncols):
        pivot=next((k for k in range(r,nrows) if a[k][c] % p),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c] % p,-1,p)
        a[r]=[(z*inv)%p for z in a[r]]
        for rr in range(nrows):
            if rr != r and a[rr][c] % p:
                factor=a[rr][c]%p
                a[rr]=[(x-factor*y)%p for x,y in zip(a[rr],a[r])]
        r+=1
        if r==nrows: break
    return r


def rank_census(n,p):
    counts=[0]*(n+1)
    for v in product(range(p),repeat=n):
        # column j of ad_v: [v,e_j]_k = (j-(k-j)) v[k-j]
        mat=[]
        for k in range(n):
            mat.append([((2*j-k)*v[k-j])%p if j<=k else 0
                        for j in range(n)])
        r=modular_rank(mat,p)
        counts[r]+=1
    predicted_counts=[0]*(n+1)
    predicted_counts[0]=1
    middle=n-(n+1)//2
    for r in range(1,n):
        if r<=middle:
            predicted_counts[r]+=(p-1)*p**(r-1)
        if r>=middle:
            predicted_counts[r]+=(p-1)*p**r
    assert counts==predicted_counts,(n,p,counts,predicted_counts)
    assert sum(counts)==p**n
    return counts


def run():
    evidence=[]
    for n,s,p,cover in [(2,2,5,True),(2,3,5,True),
                         (3,2,5,True),(3,3,5,False)]:
        count=brute(n,s,p,cover)
        evidence.append((n,s,p,count))
    for n,p in [(2,5),(3,5),(4,7),(5,7)]:
        counts=rank_census(n,p)
        evidence.append(('ranks',n,p,counts))
    print('VERIFY_OK')
    for record in evidence: print(*record)

if __name__ == '__main__':
    run()
