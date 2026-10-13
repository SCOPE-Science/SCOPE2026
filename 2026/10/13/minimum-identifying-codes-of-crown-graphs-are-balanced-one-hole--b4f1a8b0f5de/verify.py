from itertools import combinations


def traces(n, mask):
    # vertices 0..n-1 are a_i; n..2n-1 are b_i
    C=set(i for i in range(2*n) if mask>>i & 1)
    out=[]
    for v in range(2*n):
        if v<n:
            i=v
            N={v}|{n+j for j in range(n) if j!=i}
        else:
            i=v-n
            N={v}|{j for j in range(n) if j!=i}
        out.append(frozenset(N&C))
    return out

def identifying(n, mask):
    t=traces(n,mask)
    return all(t) and len(set(t))==2*n

def classified_min(n, mask):
    if mask.bit_count()!=n-1:
        return False
    occ=[]
    P=[];Q=[]
    for i in range(n):
        ai=(mask>>i)&1
        bi=(mask>>(n+i))&1
        occ.append(ai+bi)
        if ai:P.append(i)
        if bi:Q.append(i)
    return occ.count(0)==1 and occ.count(1)==n-1 and occ.count(2)==0 and len(P)>=2 and len(Q)>=2

total_subsets=0
basis_checks=0
for n in range(5,10):
    minsize=None; mins=[]
    for mask in range(1<<(2*n)):
        total_subsets += 1
        if minsize is not None and mask.bit_count()>minsize:
            continue
        if identifying(n,mask):
            s=mask.bit_count()
            if minsize is None or s<minsize:
                minsize=s; mins=[mask]
            elif s==minsize:
                mins.append(mask)
    assert minsize==n-1,(n,minsize)
    expected=n*((1<<(n-1))-2*n)
    assert len(mins)==expected,(n,len(mins),expected)
    for m in mins:
        basis_checks += 1
        assert classified_min(n,m),(n,m)
    # Also every classified candidate is identifying.
    class_count=0
    for r in range(n):
        others=[i for i in range(n) if i!=r]
        for k in range(2,n-2):
            for P in combinations(others,k):
                P=set(P); mask=0
                for i in others:
                    if i in P: mask |= 1<<i
                    else: mask |= 1<<(n+i)
                class_count += 1
                assert identifying(n,mask)
    assert class_count==expected
print(f"VERIFY_OK n_range=5..9 subset_checks={total_subsets} basis_checks={basis_checks} max_order=18")
