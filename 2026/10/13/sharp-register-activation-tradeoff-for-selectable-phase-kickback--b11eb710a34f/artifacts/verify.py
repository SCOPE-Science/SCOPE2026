from math import comb, gcd

def check(n, a=1):
    N=(1<<n)-1
    assert gcd(a,N)==1
    labels=[(a*(1<<i))%N for i in range(n)]
    best=[None]*N
    for mask in range(1<<n):
        residue=sum(labels[i] for i in range(n) if (mask>>i)&1)%N
        weight=mask.bit_count()
        if best[residue] is None or weight<best[residue]:
            best[residue]=weight
    assert all(v is not None for v in best)
    assert max(best)==n-1
    assert sum(comb(n,j) for j in range(n-1)) < N
    assert sum(comb(n,j) for j in range(n)) == N

for n in range(2,13):
    check(n)
print("VERIFY_OK")
