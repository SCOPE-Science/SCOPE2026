"""Exhaustive small-modulus audit using polynomial division."""
from collections import defaultdict, Counter


def vanishes(B,p,j):
    stride=p**j
    order=stride*p
    a=[0]*order
    for b in B:
        a[b%order]+=1
    # Remainder after division by 1+X^stride+...+X^((p-1)*stride).
    for i in range(order-1,order-stride-1,-1):
        c=a[i]
        for s in range(1,p):
            a[i-s*stride]-=c
    return not any(a[:order-stride])


def audit(p,k):
    N=p**k
    by_mask=defaultdict(list)
    for b in range(1,2**N):
        B=tuple(i for i in range(N) if b>>i&1)
        mask=sum(1<<j for j in range(k) if vanishes(B,p,j))
        by_mask[mask].append(B)
    for required in range(2**k):
        valid=[B for mask,sets in by_mask.items() if mask&required==required for B in sets]
        minsize=min(map(len,valid))
        best=[B for B in valid if len(B)==minsize]
        J={j for j in range(k) if required>>j&1}
        other=set(range(k))-J
        E=sum(p**sum(h<j for h in J) for j in other)
        S=1+max(other) if other else 0
        assert (minsize,len(best))==(p**len(J),p**E)
        canon=set()
        for B in best:
            shifts=[tuple(sorted((b+t)%N for b in B)) for t in range(N)]
            assert [t for t,b in enumerate(shifts) if b==B]==list(range(0,N,p**S))
            canon.add(min(shifts))
            for j in range(k):
                children={b%p**(j+1) for b in B}
                arities=Counter(c%p**j for c in children)
                assert set(arities.values())=={p if j in J else 1}
        assert len(canon)==p**(E-S)
    print(f'N={N}, p={p}, k={k}: {2**N-1} sets, {2**k} profiles PASS')


if __name__=='__main__':
    for p,k in ((2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(5,1),(7,1)):
        audit(p,k)
