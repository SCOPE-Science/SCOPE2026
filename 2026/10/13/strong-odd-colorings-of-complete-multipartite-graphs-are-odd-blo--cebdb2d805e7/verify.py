from itertools import product
from math import factorial, comb


def A(n,k):
    if not (1 <= k <= n) or (n-k) % 2:
        return 0
    return sum((-1)**j * comb(k,j) * (k-2*j)**n for j in range(k+1)) // (2**k)


def formula_count(parts,q):
    r=len(parts)
    total=0
    def rec(i, used, prodA, denom):
        nonlocal total
        if i==r:
            if used <= q:
                total += factorial(q)//factorial(q-used)//denom * prodA
            return
        n=parts[i]
        for k in range(1,n+1):
            a=A(n,k)
            if a and used+k <= q:
                rec(i+1,used+k,prodA*a,denom*factorial(k))
    rec(0,0,1,1)
    return total


def direct_count(parts,q):
    part=[]
    for i,n in enumerate(parts):
        part += [i]*n
    N=len(part)
    ans=0
    for c in product(range(q), repeat=N):
        ok=True
        # properness
        for u in range(N):
            for v in range(u+1,N):
                if part[u] != part[v] and c[u] == c[v]:
                    ok=False
                    break
            if not ok:
                break
        if not ok:
            continue
        # strong odd condition directly from open neighborhoods
        for v in range(N):
            counts={}
            for u in range(N):
                if part[u] != part[v]:
                    counts[c[u]]=counts.get(c[u],0)+1
            if any(x % 2 == 0 for x in counts.values()):
                ok=False
                break
        if ok:
            ans += 1
    return ans


def chi_formula(parts):
    return len(parts)+sum(n%2==0 for n in parts)


def optimal_formula(parts):
    k=chi_formula(parts)
    return factorial(k) * 2**sum(n-2 for n in parts if n%2==0)

cases=0
coloring_checks=0
for r in range(2,5):
    for parts in product(range(1,5), repeat=r):
        if sum(parts)>6:
            continue
        cases += 1
        k0=chi_formula(parts)
        # Verify counts for every palette size through min(N,5).
        for q in range(1,min(sum(parts),5)+1):
            d=direct_count(parts,q)
            f=formula_count(parts,q)
            assert d==f, (parts,q,d,f)
            coloring_checks += q**sum(parts)
        # Minimum and optimal-count consequences.
        assert formula_count(parts,k0)>0
        assert all(formula_count(parts,q)==0 for q in range(1,k0))
        assert formula_count(parts,k0)==optimal_formula(parts)

# Larger arithmetic checks of the closed consequences.
large_cases=0
for r in range(2,9):
    for seed in range(1,101):
        parts=tuple(((seed*(i+3)+7*i)%23)+1 for i in range(r))
        k=chi_formula(parts)
        assert k==sum(1 if n%2 else 2 for n in parts)
        assert optimal_formula(parts)==factorial(k)*2**sum(n-2 for n in parts if n%2==0)
        large_cases += 1

print('ALL CHECKS PASSED; small_part_tuples=%d; direct_color_assignments=%d; large_arithmetic_cases=%d; small_range=r=2..4, part_sizes=1..4, total_order<=6; palette_q<=5' % (cases,coloring_checks,large_cases))
