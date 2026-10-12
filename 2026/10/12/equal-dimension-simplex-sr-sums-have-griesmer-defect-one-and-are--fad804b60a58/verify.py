from collections import Counter
from itertools import product


def griesmer(q, K, d):
    return sum((d + q**i - 1)//q**i for i in range(K))


def rank_mod_p(rows, p):
    a=[list(map(lambda x:x%p,row)) for row in rows]
    if not a:
        return 0
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]%p),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for i in range(m):
            if i!=r and a[i][c]%p:
                f=a[i][c]%p
                a[i]=[(x-f*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r


def direct_prime_check(q,k):
    # For prime q, K(S_{k,q}) may be represented by all nonzero columns of F_q^k.
    cols=[v for v in product(range(q), repeat=k) if any(v)]
    pairs=[(u,v) for u in cols for v in cols]
    rows=[]
    for r in range(k):
        rows.append([u[r] for u,v in pairs])
    for r in range(k):
        rows.append([v[r] for u,v in pairs])
    assert rank_mod_p(rows,q)==2*k
    dist=Counter()
    for msg in product(range(q), repeat=2*k):
        a=msg[:k]; b=msg[k:]
        w=0
        for u,v in pairs:
            x=(sum(ai*ui for ai,ui in zip(a,u))+sum(bi*vi for bi,vi in zip(b,v)))%q
            w += (x != 0)
        dist[w]+=1
    N=(q**k-1)**2
    w_hi=q**(k-1)*(q-1)*(q**k-1)
    d=(q-1)*q**(k-1)*(q**k-2)
    expected=Counter({0:1,w_hi:2*(q**k-1),d:(q**k-1)**2})
    assert dist==expected, (q,k,dist,expected)
    assert griesmer(q,2*k,d)==N-1
    assert griesmer(q,2*k,d+1)>N


def arithmetic_check(q,k):
    N=(q**k-1)**2
    d=(q-1)*q**(k-1)*(q**k-2)
    assert griesmer(q,2*k,d)==N-1
    expected_increment=k+1 if q==2 else k
    assert griesmer(q,2*k,d+1)-griesmer(q,2*k,d)==expected_increment
    assert griesmer(q,2*k,d+1)-N==(k if q==2 else k-1)

for q in (2,3,4,5,7,8,9,11,16,25):
    for k in range(2,9):
        arithmetic_check(q,k)

for q,k in ((2,2),(2,3),(2,4),(3,2),(3,3),(5,2)):
    direct_prime_check(q,k)

print('VERIFY_OK')
