"""Independent finite checker of support-resolved commuting partial bijections.
Standard-library only; run: python checker.py
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, gcd


def allowed_cycles(p, d):
    for i in range(len(p)):
        j = i
        for _ in range(d):
            j = p[j]
        if j != i:
            return False
    return True


def bounded_partial_perms(n, d):
    for k in range(n + 1):
        for support in combinations(range(n), k):
            for images in permutations(range(k)):
                if not allowed_cycles(images, d):
                    continue
                p = [-1] * n
                for i, j in enumerate(images):
                    p[support[i]] = support[j]
                yield tuple(p)


def compose(p, q):
    return tuple(-1 if qx < 0 else p[qx] for qx in q)


def count_direct(n, a, b):
    fset = list(bounded_partial_perms(n, a))
    gset = list(bounded_partial_perms(n, b))
    result = Counter()
    for f in fset:
        for g in gset:
            fg = compose(f, g)
            if fg != compose(g, f):
                continue
            rf = sum(t >= 0 for t in f)
            rg = sum(t >= 0 for t in g)
            ri = sum(t >= 0 for t in fg)
            result[(rf, rg, ri)] += 1
    return result


def subgroup_counts_cyclic_pair(a, b):
    # From Hermite normal form of lattices containing (a,0),(0,b).
    out = Counter()
    for r in range(1, a + 1):
        if a % r: continue
        for s in range(1, b + 1):
            if b % s: continue
            out[r * s] += gcd(r, b // s)
    return out


def count_formula(nmax, a, b):
    # Coefficients of exp(E(x,u,v,w)); no partial permutations constructed.
    E = [Counter() for _ in range(nmax + 1)]
    if nmax >= 1: E[1][(0,0,0)] = Fraction(1)
    for d in range(1, a + 1):
        if a % d == 0 and d <= nmax: E[d][(d,0,0)] += Fraction(1,d)
    for d in range(1, b + 1):
        if b % d == 0 and d <= nmax: E[d][(0,d,0)] += Fraction(1,d)
    for k, count in subgroup_counts_cyclic_pair(a,b).items():
        if k <= nmax: E[k][(k,k,k)] += Fraction(count,k)
    A = [Counter() for _ in range(nmax + 1)]
    A[0][(0,0,0)] = Fraction(1)
    for n in range(1,nmax+1):
        for k in range(1,n+1):
            for (i,j,h), c in E[k].items():
                for (x,y,z), d in A[n-k].items():
                    A[n][(i+x,j+y,h+z)] += Fraction(k,n)*c*d
    out=[]
    for n, C in enumerate(A):
        chk=Counter()
        for key, f in C.items():
            value = f*factorial(n)
            assert value.denominator == 1, (n,key,value)
            chk[key] = value.numerator
        out.append(chk)
    return out


def count_direct_triples(n):
    pset=list(bounded_partial_perms(n,2))
    count=0
    for a,b,c in product(pset, repeat=3):
        if (compose(a,b) == compose(b,a) and
            compose(a,c) == compose(c,a) and
            compose(b,c) == compose(c,b)):
            count+=1
    return count


def triple_formula_total(nmax):
    # C_2^r has Gaussian-binomial counts of subgroups of each index.
    subgroup_by_r = {1: {1:1,2:1},
                     2: {1:1,2:3,4:1},
                     3: {1:1,2:7,4:7,8:1}}
    E=[Fraction(0)]*(nmax+1)
    if nmax>=1: E[1]+=1
    for r in range(1,4):
        ways = {1:3,2:3,3:1}[r]
        for k,c in subgroup_by_r[r].items():
            if k<=nmax: E[k]+=Fraction(ways*c,k)
    A=[Fraction(0)]*(nmax+1); A[0]=1
    for n in range(1,nmax+1):
        A[n]=sum(Fraction(k,n)*E[k]*A[n-k] for k in range(1,n+1))
    return [int(A[i]*factorial(i)) for i in range(nmax+1)]




def subgroup_counts_by_closure(a,b):
    """Independent closure enumeration, not using lattice normal forms."""
    universe=[(i,j) for i in range(a) for j in range(b)]
    def add(x,y): return ((x[0]+y[0])%a,(x[1]+y[1])%b)
    found={frozenset([(0,0)])}
    frontier=list(found)
    while frontier:
        H=frontier.pop()
        for g in universe:
            if g in H: continue
            K=set(H)
            while True:
                more={add(x,y) for x in K for y in K}
                more.add(g)
                if more<=K:break
                K|=more
            F=frozenset(K)
            if F not in found:
                found.add(F);frontier.append(F)
    return Counter({k:sum(a*b//len(H)==k for H in found) for k in range(1,a*b+1) if (a*b)%k==0})

def main():
    for a,b,limit in [(1,1,5),(1,3,5),(2,2,5),(2,3,5),(3,3,4),(2,4,4)]:
        predicted=count_formula(limit,a,b)
        for n in range(limit+1):
            observed=count_direct(n,a,b)
            assert observed == predicted[n], (a,b,n,observed-predicted[n],predicted[n]-observed)
        print('PAIR',a,b,'n0..'+str(limit),[sum(x.values()) for x in predicted])
    for a,b in [(2,2),(2,3),(3,3),(4,4),(2,6),(4,6)]:
        predicted=subgroup_counts_cyclic_pair(a,b)
        direct=subgroup_counts_by_closure(a,b)
        assert predicted == direct,(a,b,predicted,direct)
    print('SUBGROUP_INDEX_CHECKS_PASSED')
    trip=triple_formula_total(3)
    assert trip == [count_direct_triples(n) for n in range(4)]
    print('TRIPLE_INVOLUTIONS',trip)
    print('ALL_EXACT_CHECKS_PASSED')

if __name__=='__main__':
    main()
