"""Exact checks for colored finite total-preorder modal algebras."""
from itertools import product
from fractions import Fraction
from math import comb, factorial
from collections import Counter

def bisim_count(clusters):
    labels = [c for block in clusters for c in block]
    levels = [i for i, block in enumerate(clusters) for _ in block]
    n = len(labels)
    part = labels[:]
    for _ in range(n+2):
        sig = [(labels[i], tuple(sorted({part[j] for j in range(n) if levels[j]>=levels[i]}))) for i in range(n)]
        code = {s:t for t,s in enumerate(sorted(set(sig)))}
        nxt = [code[s] for s in sig]
        if len(set(nxt)) == len(set(part)):
            return len(set(nxt))
        part = nxt
    raise AssertionError('refinement failed')

def support_count(clusters):
    state = set()
    ans = 0
    for block in reversed(clusters):
        support = set(block)
        if not support <= state:
            ans += len(support)
            state = support
    return ans

def stirling(n,k):
    a = [[0]*(k+1) for _ in range(n+1)]
    a[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            a[i][j] = j*a[i-1][j]+a[i-1][j-1]
    return a[n][k]

def stationary(q,r):
    p={j:Fraction(factorial(j)*stirling(r,j),q**r) for j in range(1,r+1)}
    pi={}
    for j in range(r,0,-1):
        cover = sum(Fraction(comb(q-j,l-j))*pi[l] for l in range(j+1,r+1))
        pi[j] = p[j]*(1-cover)/(1-Fraction(j,q)**r+p[j])
    assert sum(comb(q,j)*pi[j] for j in pi)==1
    mu=sum(comb(q,j)*pi[j]*(q*(1-Fraction(q-1,q)**r)-j*(Fraction(j,q)**r-Fraction(j-1,q)**r)) for j in pi)
    return pi,mu

def main():
    tests=0
    for q,r,m in [(2,1,6),(2,2,5),(3,1,5),(3,2,4),(4,1,5),(4,2,3)]:
        for word in product(range(q),repeat=r*m):
            blocks=[word[i*r:(i+1)*r] for i in range(m)]
            assert bisim_count(blocks)==support_count(blocks)
            tests+=1
    assert tests>=13000
    for q,r,m in [(2,2,5),(3,2,3),(4,2,3)]:
        hist=Counter()
        for word in product(range(q),repeat=r*m):
            hist[support_count([word[i*r:(i+1)*r] for i in range(m)])]+=1
        # Exact distribution of the retained-support Markov chain.
        states={frozenset(t) for j in range(1,min(q,r)+1) for t in __import__('itertools').combinations(range(q),j)}
        weights={C:Fraction(factorial(len(C))*stirling(r,len(C)),q**r) for C in states}
        f={(C,len(C)):w for C,w in weights.items()}
        for _ in range(m-1):
            new=Counter()
            for (A,z),w in f.items():
                for C,p in weights.items():
                    if C <= A:
                        new[(A,z)]+=w*p
                    else:
                        new[(C,z+len(C))]+=w*p
            f=new
        predicted=Counter()
        for (A,z),w in f.items():predicted[z]+=w
        assert predicted=={z:Fraction(n,q**(r*m)) for z,n in hist.items()}
    pi,mu=stationary(4,2)
    assert pi[1]==Fraction(1,28) and pi[2]==Fraction(1,7)
    assert mu==Fraction(159,112)
    for q in range(2,8):
        for r in range(1,q):
            pi,mu=stationary(q,r)
            assert 0<mu<=r
    print(f'ALL_CHECKS_OK exhaustive_bisimulation_cases={tests} exact_distribution_cases=3 stationary_cases=21')

if __name__=='__main__':main()
