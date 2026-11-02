"""Independent exact checks for sunlet ordinary P3-convexity enumeration.

Run: python3 verify.py
Pure Python standard library; no outside files are used.
"""
from collections import Counter
from itertools import product
from math import comb


def brute_joint(n):
    # The adjacency sets are built from the literal sunlet edge definition.
    neighbors = [set() for _ in range(2*n)]
    for i in range(n):
        for a, b in ((i, (i+1)%n), (i, n+i)):
            neighbors[a].add(b)
            neighbors[b].add(a)
    result = Counter()
    for mask in range(1 << (2*n)):
        good = True
        for v in range(2*n):
            if not (mask >> v & 1):
                if sum((mask >> w) & 1 for w in neighbors[v]) > 1:
                    good = False
                    break
        if good:
            a = sum((mask >> i) & 1 for i in range(n))
            b = sum((mask >> (n+i)) & 1 for i in range(n))
            result[(a,b)] += 1
    return result


def predicted_joint(n):
    P = Counter()
    # Empty and complete selected core.
    for b in range(n+1):
        P[(0,b)] += comb(n,b)
        P[(n,b)] += comb(n,b)
    # m cyclic runs of selected core vertices and t selected core sites.
    for m in range(1, n//3+1):
        for t in range(m, n-2*m+1):
            total = n*comb(t-1,m-1)*comb(n-t-m-1,m-1)
            assert total % m == 0
            core_words = total//m
            for b in range(n-2*m+1):
                P[(t,b)] += core_words*comb(n-2*m,b)
    return P


def tr_univariate(n):
    # 4-state overlap transfer, independently from the cyclic-run formula.
    states = ((0,0),(0,1),(1,0),(1,1))
    T = []
    for a,b in states:
        edges = []
        for j,(d,c) in enumerate(states):
            if d != b: continue
            if b:
                edges.append((j,1,1))
                edges.append((j,2,1))
            elif a+c == 0:
                edges.append((j,0,1))
                edges.append((j,1,1))
            elif a+c == 1:
                edges.append((j,0,1))
        T.append(edges)
    out=Counter()
    for start in range(4):
        curr = {(start,0):1}
        for _ in range(n):
            nxt=Counter()
            for (state,k),v in curr.items():
                for j,d,mul in T[state]:nxt[(j,k+d)] += v*mul
            curr=nxt
        for (j,k),v in curr.items():
            if j==start:out[k]+=v
    return out


def recurrence_totals(nmax):
    a=[3,4,8]
    for n in range(3,nmax+1):
        a.append(4*a[-1]-4*a[-2]+2*a[-3])
    return a


def checked():
    for n in range(3,10):
        actual=brute_joint(n)
        claimed=predicted_joint(n)
        assert actual==claimed,('bivariate',n,actual,claimed)
    for n in range(3,23):
        joint=predicted_joint(n)
        univariate=Counter()
        for (a,b),count in joint.items():univariate[a+b]+=count
        traced=tr_univariate(n)
        assert univariate==traced,('transfer',n)
        total=sum(univariate.values())
        direct=2**(n+1)+sum(
          n*comb(n-m-1,2*m-1)*2**(n-2*m)//m
          for m in range(1,n//3+1)
        )
        assert total==direct,('Vandermonde',n)
        assert total==recurrence_totals(n)[n],('recurrence',n)
    print('BRUTE_JOINT_OK n=3..9')
    print('TRANSFER_AND_BINOMIAL_OK n=3..22')
    print('FIRST_TOTALS', [sum(predicted_joint(n).values()) for n in range(3,11)])
    print('VERIFY_OK')

if __name__=='__main__':checked()
