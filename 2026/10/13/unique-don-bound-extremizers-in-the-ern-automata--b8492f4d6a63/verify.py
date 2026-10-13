#!/usr/bin/env python3
from collections import deque

def image(mask,T,n):
    z=0
    for i in range(n):
        if (mask>>i)&1: z |= 1<<T[i]
    return z

def check(n):
    A=[(i+1)%n for i in range(n)]
    B=list(range(n)); B[n-1]=0
    full=(1<<n)-1
    dist={full:0}; q=deque([full])
    while q:
        m=q.popleft()
        for T in (A,B):
            z=image(m,T,n)
            if z not in dist:
                dist[z]=dist[m]+1; q.append(z)
    assert len(dist)==(1<<n)-1
    for k in range(1,n):
        Sk=(1<<(n-1)) | ((1<<(k-1))-1 if k>=2 else 0)
        vals=[(d,m) for m,d in dist.items() if m.bit_count()==k]
        mx=max(d for d,m in vals)
        eq=[m for d,m in vals if d==mx]
        assert mx==n*(n-k), (n,k,mx)
        assert eq==[Sk], (n,k,eq,Sk)
        # Verify the explicit word (b a^(n-1))^(n-k).
        m=full
        for _ in range(n-k):
            m=image(m,B,n)
            for __ in range(n-1): m=image(m,A,n)
        assert m==Sk
    # Verify the one-step reverse-extension lemma for every nonempty proper set.
    for S in range(1,full):
        bd=[]
        for t in range(n):
            if ((S>>t)&1) and not ((S>>((t-1)%n))&1): bd.append(t)
        assert bd
        t=min(bd)
        # R = S a^{-t}
        R=0
        for x in range(n):
            if (S>>x)&1: R |= 1<<((x-t)%n)
        assert (R&1) and not ((R>>(n-1))&1)
        U=R | (1<<(n-1))
        # U b a^t = S
        V=image(U,B,n)
        for _ in range(t): V=image(V,A,n)
        assert V==S
        k=S.bit_count()
        Sk=(1<<(n-1)) | ((1<<(k-1))-1 if k>=2 else 0)
        assert ((t==n-1) == (S==Sk))
    return True

for n in range(2,13): check(n)
print('VERIFY_OK n=2..12 all_nonempty_subsets exact_reaching_distances unique_layer_extremizers reverse_extension_lemma')
