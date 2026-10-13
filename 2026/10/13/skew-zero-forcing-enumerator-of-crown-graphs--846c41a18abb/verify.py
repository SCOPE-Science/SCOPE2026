from collections import Counter
from math import comb


def crown_adj(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def skew_force(n, mask):
    adj=crown_adj(n); N=2*n
    blue={v for v in range(N) if (mask>>v)&1}
    changed=True
    while changed:
        changed=False
        for u in range(N):
            white=[v for v in adj[u] if v not in blue]
            if len(white)==1:
                v=white[0]
                if v not in blue:
                    blue.add(v); changed=True
                    break
    return len(blue)==N

def ordinary_force(n, mask):
    adj=crown_adj(n); N=2*n
    blue={v for v in range(N) if (mask>>v)&1}
    changed=True
    while changed:
        changed=False
        for u in list(blue):
            white=[v for v in adj[u] if v not in blue]
            if len(white)==1:
                v=white[0]
                blue.add(v); changed=True
                break
    return len(blue)==N

def expected_coeff(n):
    # A_n(x)=x^n+n x^(n-1)+C(n,2)x^(n-2); square it
    a={n:1,n-1:n,n-2:comb(n,2)}
    c=Counter()
    for i,ai in a.items():
        for j,aj in a.items(): c[i+j]+=ai*aj
    return c

subset_checks=skew_sets=ordinary_comparison_checks=coefficient_checks=0
for n in range(3,9):
    N=2*n
    got=Counter()
    for mask in range(1<<N):
        subset_checks+=1
        I={i for i in range(n) if not ((mask>>i)&1)}
        J={j for j in range(n) if not ((mask>>(n+j))&1)}
        sk=skew_force(n,mask)
        criterion=(len(I)<=2 and len(J)<=2)
        assert sk==criterion, (n,mask,I,J,sk,criterion)
        if sk:
            skew_sets+=1; got[mask.bit_count()]+=1
        ordz=ordinary_force(n,mask)
        ordinary_comparison_checks+=1
        extra=sk and not ordz
        expected_extra=(len(I)==2 and I==J)
        assert extra==expected_extra, (n,mask,I,J,sk,ordz)
    exp=expected_coeff(n)
    assert got==exp, (n,got,exp)
    coefficient_checks += len(set(got)|set(exp))
    assert min(got)==2*n-4
    assert got[2*n-4]==comb(n,2)**2
print(f'VERIFY_OK n_range=3..8 subset_checks={subset_checks} skew_sets={skew_sets} ordinary_comparison_checks={ordinary_comparison_checks} coefficient_checks={coefficient_checks} max_order=16')
