from itertools import product
from collections import Counter
from math import factorial, comb


def dominates(states):
    n=len(states)
    A=[s in (1,3) for s in states]
    B=[s in (2,3) for s in states]
    for i in range(n):
        if not A[i] and not any(B[j] for j in range(n) if j!=i):
            return False
        if not B[i] and not any(A[j] for j in range(n) if j!=i):
            return False
    return True


def secure(states):
    if not dominates(states):
        return False
    n=len(states)
    for i,s in enumerate(states):
        if s not in (1,3):
            ok=False
            for j,t in enumerate(states):
                if j==i or t not in (2,3):
                    continue
                z=list(states)
                z[j]={2:0,3:1}[z[j]]
                z[i]={0:1,2:3}[z[i]]
                if dominates(z):
                    ok=True
                    break
            if not ok:
                return False
        if s not in (2,3):
            ok=False
            for j,t in enumerate(states):
                if j==i or t not in (1,3):
                    continue
                z=list(states)
                z[j]={1:0,3:2}[z[j]]
                z[i]={0:2,1:3}[z[i]]
                if dominates(z):
                    ok=True
                    break
            if not ok:
                return False
    return True


def phi_counts(a,b,c,d):
    p=b+d
    q=c+d
    phiA=(a+c==0) or (q>=3) or (q==2 and (d>=1 or a==0)) or (q==1 and (a,c,d)==(1,0,1))
    phiB=(a+b==0) or (p>=3) or (p==2 and (d>=1 or a==0)) or (p==1 and (a,b,d)==(1,0,1))
    return phiA and phiB

subset_checks=0
classification_checks=0
coefficient_checks=0
minimum_checks=0
for n in range(3,9):
    brute=Counter()
    formula=Counter()
    for st in product(range(4), repeat=n):
        subset_checks += 1
        a,b,c,d=(st.count(k) for k in range(4))
        by_formula=phi_counts(a,b,c,d)
        by_def=secure(st)
        classification_checks += 1
        assert by_formula == by_def, (n, st, (a,b,c,d), by_formula, by_def)
        if by_def:
            p=b+d; q=c+d
            brute[(p,q)] += 1
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                if phi_counts(a,b,c,d):
                    mult=factorial(n)//(factorial(a)*factorial(b)*factorial(c)*factorial(d))
                    formula[(b+d,c+d)] += mult
    keys=set(brute)|set(formula)
    for k in keys:
        coefficient_checks += 1
        assert brute[k]==formula[k], (n,k,brute[k],formula[k])
    size_counts=Counter()
    for (p,q),v in brute.items():
        size_counts[p+q]+=v
    m=min(size_counts)
    minimum_checks += 1
    if n==3:
        assert (m,size_counts[m])==(3,14)
    elif n==4:
        assert (m,size_counts[m])==(4,62)
    else:
        expected=n*(n-1)*(2*n-3)//2
        assert (m,size_counts[m])==(4,expected), (n,m,size_counts[m],expected)
print(f"VERIFY_OK n_range=3..8 subset_checks={subset_checks} classification_checks={classification_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=16")
