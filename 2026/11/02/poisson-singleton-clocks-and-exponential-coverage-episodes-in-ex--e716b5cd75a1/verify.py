"""Exact finite checks for a sliding-window coupon-cover lifetime theorem.

Run with Python 3.10+; standard library only. Finite enumeration checks the
combinatorial identities and inequalities, not the asymptotic limit itself.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb

ASSERTIONS = 0

def check(statement, context):
    global ASSERTIONS
    assert statement, context
    ASSERTIONS += 1

def stirling(m, k):
    table = [[0] * (k + 1) for _ in range(m + 1)]
    table[0][0] = 1
    for i in range(1, m + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = j * table[i - 1][j] + table[i - 1][j - 1]
    return table[m][k]

def onto_words(N, m):
    return [w for w in product(range(1, N + 1), repeat=m)
            if len(set(w)) == N]

def direct_tail(n, M, t, words):
    favorable = 0
    for u in words:
        for fresh in product(range(n), repeat=t):
            w = tuple(u) + (0,)
            alive = True
            for v in fresh:
                w = w[1:] + (v,)
                if len(set(w)) < n:
                    alive = False
                    break
            favorable += alive
    return Fraction(favorable, len(words) * n**t)

def tail_bounds(n, M, t, words):
    no_expiring = 0
    expiring_sum = 0
    no_singletons = 0
    multi_expiring_sum = 0
    for u in words:
        counts = Counter(u)
        expired = sum(c not in u[t:] for c in counts)
        # Each letter appears in u; expiry by time t means absent from suffix.
        expiring_sum += expired
        no_expiring += (expired == 0)
        s = sum(counts[c] == 1 and c in u[:t] for c in counts)
        no_singletons += (s == 0)
        multi_expiring_sum += sum(counts[c] >= 2 and c not in u[t:]
                                    for c in counts)
    Nw = len(words)
    return (Fraction(no_expiring,Nw),
            Fraction(no_expiring,Nw)+Fraction(t*expiring_sum,n*Nw),
            Fraction(no_singletons,Nw),
            Fraction(multi_expiring_sum,Nw))

def direct_palm(n, M, words):
    # For fixed appended missing letter 0, every onto middle word is equiprobable.
    # The departing letter is any of the other n-1 letters.
    counts = {u: 0 for u in words}
    total = 0
    for old in range(n):
        for u in product(range(n), repeat=M-1):
            for new in range(n):
                wprev = (old,) + u
                wnext = u + (new,)
                if len(set(wprev)) < n and len(set(wnext)) == n and new == 0:
                    counts[u] += 1
                    total += 1
    check(total == (n-1)*len(words), ('palm total',n,M))
    for u in words:
        check(counts[u] == n-1, ('palm uniform middle',n,M,u))

def direct_stationary_mean(n, M):
    mass=0
    exit_count=0
    for w in product(range(n),repeat=M):
        if len(set(w)) < n: continue
        mass += 1
        for new in range(n):
            exit_count += (len(set(w[1:]+(new,)))<n)
    return Fraction(n*mass,exit_count)

def run():
    print('Scope: exact finite identities for conditional cover episodes.')
    for n in (2,3,4):
        for M in range(n,n+3):
            m=M-1
            N=n-1
            words=onto_words(N,m)
            check(len(words)==N*0+math_factorial(N)*stirling(m,N),('onto count',n,M))
            check(Fraction(n*stirling(M,n),(n-1)*stirling(M-1,n-1))
                ==direct_stationary_mean(n,M),('mean identity',n,M))
            direct_palm(n,M,words)
            # Exactly-counted singleton mean and uniform location subsets.
            singleton_count=sum(sum(v==1 for v in Counter(w).values()) for w in words)
            theo=Fraction(m*stirling(m-1,N-1),stirling(m,N))
            check(Fraction(singleton_count,len(words))==theo,('singleton mean',n,M))
            byK=defaultdict(Counter)
            for w in words:
                cc=Counter(w)
                loc=tuple(j for j,z in enumerate(w) if cc[z]==1)
                byK[len(loc)][loc]+=1
            for k,positions in byK.items():
                check(len(positions)==comb(m,k),('singleton location subsets',n,M,k))
                check(len(set(positions.values()))==1,('uniform singleton locations',n,M,k))
            for t in range(min(4,M)):
                p=direct_tail(n,M,t,words)
                lo,hi,p_no_single,j=tail_bounds(n,M,t,words)
                check(lo<=p<=hi,('tail sandwich',n,M,t,lo,p,hi))
                check(lo<=p_no_single,('singleton containment',n,M,t))
                check(p_no_single-lo<=j,('multi-expiration error',n,M,t))
                check(p<=1,('tail normalization',n,M,t))
    print(f'PASS: {ASSERTIONS} deterministic exact assertions.')
    print('Proof limits: no finite enumeration certifies the n-to-infinity limit;')
    print('the Poisson point-process and mean limits require the analytic argument.')

def math_factorial(k):
    a=1
    for j in range(2,k+1): a*=j
    return a

if __name__=='__main__':
    run()
