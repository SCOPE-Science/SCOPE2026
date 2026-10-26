"""Exact integer spot checks for a primorial-controlled prime-extension criterion."""
from math import prod

def primes_to(n):
    a=bytearray(b'\x01')*(n+1)
    a[:2]=b'\x00\x00'
    for p in range(2,int(n**0.5)+1):
        if a[p]:a[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [p for p in range(n+1) if a[p]]

def radius(M, primes):
    P=1;k=1
    while P < k*M:
        best=k
        P*=primes[k-1]
        k+=1
    return M*best,best

def all_min_products(maxn, primes):
    vals=[None]*(maxn+1)
    vals[0]=1
    for p in primes:
        if p>maxn:break
        for n in range(maxn,p-1,-1):
            v=vals[n-p]
            if v is not None:
                w=v*p
                if vals[n] is None or w<vals[n]:vals[n]=w
    return vals

P=primes_to(10000)
for M,eK,eH in [(2,2,4),(3,3,9),(285,5,1425)]:
    H,K=radius(M,P)
    assert (K,H)==(eK,eH), (M,K,H)
for A in ([2],[3],[5],[2,7]):
    M=prod(A);H,K=radius(M,P)
    s=sum(A); hi=4000
    min_products=all_min_products(hi+s,P)
    assert min_products[s]==M,(A,min_products[s],M)
    eligible=[q for q in P if H<q<=hi and all(abs(q-r)>H for r in P if r!=q and abs(q-r)<=H)]
    for q in eligible:
        assert min_products[q+s]==q*M,(A,q,min_products[q+s],q*M)
    print(f'A={A}, M={M}, K={K}, H={H}, verified={len(eligible)}, first={eligible[:4]}')
print('VERIFY_OK')
