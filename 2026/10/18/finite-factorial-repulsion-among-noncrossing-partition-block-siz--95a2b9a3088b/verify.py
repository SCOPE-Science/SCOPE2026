"""Exact checks for finite factorial dependence in noncrossing partitions.

Standard-library-only reproducibility checks; no finite computation is used
as a substitute for the analytical proof.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial

checks = 0


def check(condition, explanation):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(explanation)


def catalan(n):
    return comb(2*n, n)//(n+1)


def fall(x, a):
    ans = 1
    for j in range(a):
        ans *= x-j
    return ans


def moment(n, marks):
    """Exact E prod_r (X_r)_{marks[r]} for uniform noncrossing partitions."""
    t = sum(marks.values())
    w = sum(r*a for r,a in marks.items())
    if w > n:
        return Fraction(0)
    return Fraction(fall(n+1,t)*comb(2*n-t-w, n-w), (n+1)*catalan(n))


def is_nc(blocks):
    owner = {}
    for j, block in enumerate(blocks):
        for x in block:
            owner[x] = j
    n = len(owner)
    for a in range(n):
        for b in range(a+1,n):
            for c in range(b+1,n):
                if owner[a] != owner[c]:
                    continue
                for d in range(c+1,n):
                    if owner[b] == owner[d] and owner[a] != owner[b]:
                        return False
    return True


def set_partitions(n):
    """Independent restricted-growth-string enumeration."""
    if n == 0:
        yield ()
        return
    def rec(i, labs, mx):
        if i == n:
            blocks = [[] for _ in range(mx+1)]
            for j,b in enumerate(labs):
                blocks[b].append(j)
            yield tuple(tuple(b) for b in blocks)
        else:
            for x in range(mx+2):
                labs.append(x)
                yield from rec(i+1,labs,max(mx,x))
                labs.pop()
    yield from rec(1,[0],0)


# Independent exhaustive Catalan enumeration and mixed factorial moments.
for n in range(1,9):
    nc = [part for part in set_partitions(n) if is_nc(part)]
    check(len(nc) == catalan(n), ('Catalan',n,len(nc)))
    profiles = [Counter(map(len, part)) for part in nc]
    for r in range(1,n+1):
        for a in range(1,min(n//r,3)+1):
            computed = Fraction(sum(fall(c[r],a) for c in profiles),len(nc))
            check(computed == moment(n,{r:a}), ('single',n,r,a))
    for r in range(1,n+1):
        for s in range(r+1,n+1):
            for a in range(1,min(n//r,2)+1):
                for b in range(1,min(n//s,2)+1):
                    computed = Fraction(sum(fall(c[r],a)*fall(c[s],b) for c in profiles),len(nc))
                    check(computed == moment(n,{r:a,s:b}),('mixed',n,r,s,a,b))

# All admissible finite factorial anticorrelation tests, even for infeasible pairs.
for n in range(2,31):
    for r in range(1,n+1):
        for s in range(r+1,n+1):
            for a in range(1,n//r+1):
                for b in range(1,n//s+1):
                    check(moment(n,{r:a,s:b}) < moment(n,{r:a})*moment(n,{s:b}),
                          ('strict',n,r,s,a,b))

# The local inequality in the proof, also for arbitrary residual weak compositions.
for N in range(2,26):
    for m in range(N+1,N+8):
        den=comb(N+m-1,m-1)
        for r in range(1,N):
            for s in range(1,N):
                if r+s>N:
                    continue
                one_r=Fraction(m*comb(N-r+m-2,m-2),den)
                one_s=Fraction(m*comb(N-s+m-2,m-2),den)
                double=Fraction(m*(m-1)*comb(N-r-s+m-3,m-3),den)
                check(double<=one_r*one_s,('composition',N,m,r,s))
                check(double<one_r*one_s or (N,m,r,s)==(2,3,1,1),
                      ('exception',N,m,r,s))

# Pairwise factorial anticorrelation and positive threshold-indicator covariance coexist.
check(moment(3,{1:1,2:1})-moment(3,{1:1})*moment(3,{2:1}) == Fraction(-3,25),
      'n=3 count covariance')
check(Fraction(3,5)-Fraction(4,5)*Fraction(3,5)==Fraction(3,25),
      'n=3 threshold-event covariance')
print(f'PASS {checks} exact assertions; exhaustive NC partitions n<=8')
