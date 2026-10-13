from itertools import product,permutations
from evol_verify import grank

def conj(M,p,n):
    out=[]
    for i in range(n):
        old=M[p[i]]
        out.append(sum(((old>>p[j])&1)<<j for j in range(n)))
    return tuple(out)

def idempotent_free(M,n):
    mtrows=[sum(((M[i]>>j)&1)<<i for i in range(n)) ^ (1<<j) for j in range(n)]
    return grank(mtrows,n)==n
for n in (2,3,4):
    P=list(permutations(range(n)))
    items=set()
    for M in product(range(2**n), repeat=n):
        if grank(M,n)==n and idempotent_free(M,n):items.add(M)
    initial=len(items)
    dist={}; reps=[]
    while items:
        M=next(iter(items))
        orbit={conj(M,p,n) for p in P}
        assert orbit<=items
        for A in orbit:items.remove(A)
        dist[len(orbit)]=dist.get(len(orbit),0)+1
        reps.append((len(orbit),M))
    print('n',n,'idempotent_free_presentations',initial,'isoclasses',len(reps),'orbit_size_histogram',sorted(dist.items()),'first_representatives',sorted(reps)[:3])
