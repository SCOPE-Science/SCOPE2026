"""Exact independent graph-level checker for minimum locating-total sets in K_n square K_2.
Only uses the mathematical graph definition and exhaustive vertex-subset enumeration.
"""
from itertools import combinations
from math import comb


def predicted(n):
    if n >= 5:
        return n - 1, n * (2**(n - 1) - 2*n)
    return n, (2 if n <= 3 else 8) + n*(n - 1)*2**(n - 2)


def graph_neighborhoods(n):
    # 0..n-1 first clique, n..2n-1 second clique.
    return [sum(1 << (j + n*layer2)
                for layer2 in range(2) for j in range(n)
                if (layer2 == (v // n) and j != v % n)
                or (layer2 != (v // n) and j == v % n))
            for v in range(2*n)]


def valid(code, nb, n):
    signatures = set()
    for v in range(2*n):
        s = nb[v] & code
        if not s:
            return False
        if not ((code >> v) & 1):
            if s in signatures:
                return False
            signatures.add(s)
    return True


def characterize(code, n):
    counts = [((code>>i)&1) + ((code>>(n+i))&1) for i in range(n)]
    a = sum((code>>i)&1 for i in range(n))
    b = sum((code>>(i+n))&1 for i in range(n))
    if n >= 5:
        return counts.count(0)==1 and counts.count(1)==n-1 and a>=2 and b>=2
    if counts.count(0)==0:
        return all(c==1 for c in counts) and (a==0 or b==0 or (a>=2 and b>=2))
    return counts.count(0)==1 and counts.count(2)==1 and counts.count(1)==n-2


def exhaustive(n):
    nb = graph_neighborhoods(n)
    k, goal = predicted(n)
    # Check no smaller solutions; exact count and exact characterization at k.
    for r in range(k+1):
        total=0; pattern=0
        for c in combinations(range(2*n),r):
            bits = sum(1<<v for v in c)
            ok = valid(bits,nb,n)
            if ok:
                total += 1
                assert r==k, (n,'smaller feasible set',r,c)
            if r==k:
                structure = characterize(bits,n)
                assert ok==structure,(n,'characterization',c,ok,structure)
                pattern += structure
        if r==k:
            assert total==goal and pattern==goal,(n,total,pattern,goal)
    return k, goal


def run():
    for n in range(2,11):
        k, ways=exhaustive(n)
        print(f'n={n}: min={k} count={ways}')
    # Non-enumerative mask checking for large n: all predicted constructions are valid.
    for n in [11,12,17,23,35]:
        nb=graph_neighborhoods(n)
        empty_cols=[0,n-1]
        # Nontrivial selected layer splits include smallest allowable 2.
        for blank in empty_cols:
            for a in [2,3,(n-1)//2,n-3]:
                cols=[i for i in range(n) if i!=blank]
                code=sum(1<<i for i in cols[:a])+sum(1<<(i+n) for i in cols[a:])
                assert characterize(code,n) and valid(code,nb,n)
    print('VERIFY_OK: exhaustive all smaller sets and complete equality-class comparison n=2..10; 40 long constructions')

if __name__=='__main__':
    run()
