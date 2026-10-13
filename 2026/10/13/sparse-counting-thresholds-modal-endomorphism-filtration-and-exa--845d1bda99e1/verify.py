"""Direct finite enumerations for sparse graded S5 Boolean algebras.

Usage: python verify.py. Requires only Python standard library.
"""
from collections import Counter
from itertools import product
from math import factorial, comb


def stirling(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    row = [1] + [0] * k
    for a in range(1, n+1):
        nxt = [0] * (k+1)
        for b in range(1, min(a, k)+1):
            nxt[b] = b*row[b] + row[b-1]
        row = nxt
    return row[k]


def partitions(n):
    # Set partitions by restricted growth words.
    for tails in product(range(n), repeat=n-1):
        codes = (0,)+tails
        if all(codes[i] <= 1+max(codes[:i]) for i in range(1,n)):
            yield tuple(tuple(i for i,c in enumerate(codes) if c==j)
                        for j in range(max(codes)+1))


def weight(a,b,k):
    if a >= k:
        return factorial(a) if a==b else 0
    return factorial(b)*stirling(a,b) if b <= a else 0


def direct(p, f, k):
    n = sum(map(len,p))
    containing = [None]*n
    for block in p:
        for x in block:
            containing[x] = block
    # Exact Boolean-operator preservation on all subsets.
    for mask in range(1<<n):
        pre = sum(1<<w for w in range(n) if mask>>f[w]&1)
        for grade in (1,k):
            left = sum(1<<w for w in range(n)
                       if sum(bool(mask>>v&1) for v in containing[f[w]]) >= grade)
            right = sum(1<<w for w in range(n)
                        if sum(bool(pre>>v&1) for v in containing[w]) >= grade)
            if left != right:
                return False
    return True


def structural(p, f, k):
    for block in p:
        target = next(b for b in p if f[block[0]] in b)
        if set(f[i] for i in block)!=set(target):
            return False
        if len(block)>=k and (len(target)!=len(block)
                             or len(set(f[i] for i in block))!=len(block)):
            return False
    return True


def predicted(p,k):
    a = [len(b) for b in p]
    endo=1
    for size in a:
        endo *= sum(weight(size,t,k) for t in a)
    idem=Counter()
    for chosen in range(1,1<<len(p)):
        J=[j for j in range(len(p)) if chosen>>j&1]
        ways=1
        for i in range(len(p)):
            if i not in J:
                ways *= sum(weight(a[i],a[j],k) for j in J)
        if ways:
            size=sum(a[j] for j in J)
            idem[1<<size]+=ways
    full = Counter()
    for chosen in range(1, 1<<len(p)):
        J = [j for j in range(len(p)) if chosen>>j & 1]
        ways = 0
        # Inclusion-exclusion over target-block support.
        for sub in range(1<<len(J)):
            K = [J[t] for t in range(len(J)) if sub>>t & 1]
            v = 1
            for source in a:
                v *= sum(weight(source,a[j],k) for j in K)
            ways += (-1)**(len(J)-len(K))*v
        if ways:
            full[1<<sum(a[j] for j in J)] += ways
    return endo, idem, full


def run():
    total=0; structures=0; direct_tests=0; endo_accepted=0; idem_checked=0; spectral_checked=0; strict_checks=0
    for n in range(1,6):
        for p in partitions(n):
            structures+=1
            fs=list(product(range(n),repeat=n))
            for k in range(2,n+2):
                actual=0; idem=Counter(); image_rank=Counter()
                for f in fs:
                    s=structural(p,f,k)
                    d=direct(p,f,k)
                    assert s==d,(n,p,k,f,s,d)
                    direct_tests+=1
                    if d:
                        actual+=1
                        image_rank[1<<len(set(f))]+=1
                        if all(f[f[w]]==f[w] for w in range(n)):
                            idem[1<<len(set(f))]+=1
                expect, ie, full = predicted(p,k)
                assert actual==expect,(p,k,actual,expect)
                assert idem==ie,(p,k,idem,ie)
                assert image_rank==full,(p,k,image_rank,full)
                spectral_checked+=len(full)
                total+=1; endo_accepted+=actual; idem_checked+=sum(idem.values())
    # Verify the exact grade-filtration jump criterion independently by counts.
    jumps = 0
    for n in range(1,6):
        for p in partitions(n):
            sizes = [len(b) for b in p]
            for k in range(2,n+1):
                e_k = predicted(p,k)[0]
                e_k1 = predicted(p,k+1)[0]
                assert e_k <= e_k1
                assert (e_k < e_k1) == (k in sizes and min(sizes)<k)
                jumps += 1
    # Boundary example: three clusters of sizes 1, 2, 3.
    p=((0,),(1,2),(3,4,5))
    assert [predicted(p,k)[0] for k in (2,3,4)] == [12,18,39]
    print('VERIFY_OK', 'partition_shapes',structures,'grade_instances',total,
          'function_grade_comparisons',direct_tests,
          'endomorphism_instances',endo_accepted,
          'idempotent_instances',idem_checked,
          'distinct_nonzero_rank_cases', spectral_checked,
          'filtration_jump_comparisons', jumps,
          'boundary_counts_1_2_3', [12,18,39])

if __name__=='__main__':
    run()
