from itertools import product
from collections import Counter

def mat(vals,n):
    return tuple(tuple(vals[i*n+j] for j in range(n)) for i in range(n))

def mm(A,B,q):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%q for j in range(n)) for i in range(n))

def iszero(A):
    return all(x==0 for row in A for x in row)

def rank(A,q):
    a=[list(row) for row in A]; m=len(a); n=len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]%q),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        inv=pow(a[r][c],-1,q)
        a[r]=[(x*inv)%q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]%q:
                f=a[i][c]%q
                a[i]=[(a[i][j]-f*a[r][j])%q for j in range(n)]
        r+=1
    return r

def all_mats(n,q):
    for v in product(range(q), repeat=n*n):
        yield mat(v,n)

def degree_formula(n,q,r,sq):
    return 2*q**(n*(n-r))-q**((n-r)**2)-1-int(sq)

def gl(r,q):
    z=1
    for i in range(r): z*=q**r-q**i
    return z

def qbinom(n,r,q):
    if r<0 or r>n: return 0
    num=den=1
    for i in range(r):
        num*=q**(n-i)-1
        den*=q**(r-i)-1
    return num//den

def rank_count(n,r,q):
    num=1
    for i in range(r): num*=(q**n-q**i)**2
    return num//gl(r,q)

def sqzero_count(n,r,q):
    if 2*r>n: return 0
    return qbinom(n,r,q)*qbinom(n-r,r,q)*gl(r,q)

def direct_full_3_2():
    n=q=0
    n=3; q=2
    verts=[]
    for A in all_mats(n,q):
        r=rank(A,q)
        if 0<r<n:
            verts.append((A,r,iszero(mm(A,A,q))))
    C=Counter()
    for A,r,sq in verts:
        d=0
        for B,_,__ in verts:
            if B!=A and (iszero(mm(A,B,q)) or iszero(mm(B,A,q))): d+=1
        want=degree_formula(n,q,r,sq)
        assert d==want,(A,r,sq,d,want)
        C[(r,sq,d)]+=1
    assert len(verts)==343
    assert C[(1,True,110)]==21 and C[(1,False,111)]==28 and C[(2,False,13)]==294
    print('M3(F2): all 343 vertices and all degrees OK')

def representative_3_3():
    n=3;q=3
    verts=[]
    for A in all_mats(n,q):
        r=rank(A,q)
        if 0<r<n: verts.append((A,r,iszero(mm(A,A,q))))
    reps={}
    for A,r,sq in verts: reps.setdefault((r,sq),A)
    for (r,sq),A in sorted(reps.items()):
        d=sum(1 for B,_,__ in verts if B!=A and (iszero(mm(A,B,q)) or iszero(mm(B,A,q))))
        assert d==degree_formula(n,q,r,sq)
    print('M3(F3): representative degree strata OK')

def formula_checks():
    for q in [2,3,5,7]:
        for n in range(3,8):
            total=0
            degrees=[]
            for r in range(1,n):
                R=rank_count(n,r,q); S=sqzero_count(n,r,q)
                assert 0<=S<=R
                total+=R
                d=degree_formula(n,q,r,False)
                degrees.append(d)
                if S: degrees.append(d-1)
            assert len(degrees)==len(set(degrees))
            invertible=gl(n,q)
            assert total==q**(n*n)-invertible-1
    print('rank counts, square-zero counts, and degree separation OK')

if __name__=='__main__':
    direct_full_3_2()
    representative_3_3()
    formula_checks()
    print('VERIFY_OK')
