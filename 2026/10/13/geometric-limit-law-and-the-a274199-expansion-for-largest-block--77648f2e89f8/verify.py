#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import math

def unbordered_counts(q, N):
    u=[0]*(N+1)
    u[0]=1
    for n in range(1,N+1):
        if n%2:
            u[n]=q*u[n-1]
        else:
            u[n]=q*u[n-1]-u[n//2]
    return u

def is_unbordered(w):
    n=len(w)
    return all(w[:j] != w[n-j:] for j in range(1,n))

def shortest_border(w):
    n=len(w)
    for j in range(1,n//2+1):
        if w[:j]==w[-j:]:
            return j
    return None

def largest_bp_width(w):
    m=0
    while w:
        j=shortest_border(w)
        if j is None:
            return 2*m+1
        m+=1
        w=w[j:-j]
    return 2*m

def pair_count(w):
    m=0
    while w:
        j=shortest_border(w)
        if j is None:
            break
        m+=1
        w=w[j:-j]
    return m

# Recurrence for the OEIS A274190 defining array.
def g(N,K, memo={}):
    if K==0:
        return 1
    if K>N or K<0:
        return 0
    key=(N,K)
    if key in memo:
        return memo[key]
    if N==0:
        return 0
    memo[key]=g(N-1,K-1)+g(N-1,2*K)
    return memo[key]

def compositions(n):
    if n==0:
        yield ()
        return
    for a in range(1,n+1):
        for rest in compositions(n-a):
            yield (a,)+rest

def good_comp(c):
    return all(c[i] < 2*c[i+1] for i in range(len(c)-1))

def comp_counts(N):
    out=[1]
    for n in range(1,N+1):
        out.append(sum(1 for c in compositions(n) if good_comp(c)))
    return out

# Source recurrence checked against direct unbordered enumeration.
for q in (2,3):
    u=unbordered_counts(q,8)
    for n in range(0,8):
        brute=sum(is_unbordered("".join(map(str,w))) for w in product(range(q), repeat=n))
        assert brute==u[n], (q,n,brute,u[n])

# Shortest-border count identity:
# q^m-u_m = sum_{j<=m/2} u_j q^(m-2j).
for q in range(2,8):
    u=unbordered_counts(q,40)
    for m in range(1,41):
        assert q**m-u[m] == sum(u[j]*q**(m-2*j) for j in range(1,m//2+1))

# A274199: limiting reverse row equals good-composition count.
b=comp_counts(16)
for d in range(0,17):
    for N in range(max(d,2*d-1), max(d,2*d-1)+6):
        assert g(N,N-d)==b[d], (d,N,g(N,N-d),b[d])
known=[1,1,2,3,5,8,12,19,29,44,67,101,152,228,342,511,763]
assert b==known

# Exact finite tail-count identity by brute force.
# P(M_n>=r) = sum_{m_1+...+m_r<=n/2} prod(u_m/q^(2m)).
for q in (2,3):
    u=unbordered_counts(q,8)
    for n in range(1,9):
        words=["".join(map(str,w)) for w in product(range(q), repeat=n)]
        for r in range(1,4):
            brute=sum(pair_count(w)>=r for w in words)
            # Count without probabilities.
            total=0
            def rec(left, depth, prod_u):
                nonlocal_total[0] += 0
                if depth==0:
                    return prod_u * q**(n-2*left)
                return 0
            # Enumerate layer-length compositions directly.
            def seqs(depth, sofar=()):
                if depth==0:
                    yield sofar
                    return
                for m in range(1,n//2+1):
                    yield from seqs(depth-1, sofar+(m,))
            calc=0
            for ms in seqs(r):
                s=sum(ms)
                if 2*s<=n:
                    prod_u=1
                    for m in ms:
                        prod_u*=u[m]
                    calc += prod_u*q**(n-2*s)
            assert calc==brute, (q,n,r,calc,brute)

# Numerical limiting constants and source-table rounding.
source_table={2:6.4686,3:2.5908,4:1.9080,5:1.6314,6:1.4827,
              7:1.3902,8:1.3272,9:1.2817,10:1.2472}
vals={}
for q in range(2,11):
    u=unbordered_counts(q,120)
    S=sum(Fraction(u[m], q**(2*m)) for m in range(1,121))
    E=(1+S)/(1-S)
    ef=float(E)
    vals[q]=ef
    assert abs(ef-source_table[q]) < 1.1e-4, (q,ef,source_table[q])

# Formal-series check to order 16.
# a_m(x)=x^m(1-sum_{j<=m/2}a_j(x)); B=S/(1-S).
N=16
# Polynomials as coefficient lists.
def add(A,B):
    C=[0]*(max(len(A),len(B)))
    for i,a in enumerate(A): C[i]+=a
    for i,bv in enumerate(B): C[i]+=bv
    return C[:N+1]
def shift(A,s):
    C=[0]*(N+1)
    for i,a in enumerate(A):
        if i+s<=N: C[i+s]+=a
    return C
a=[None]*(N+1)
S=[0]*(N+1)
for m in range(1,N+1):
    inner=[0]*(N+1); inner[0]=1
    for j in range(1,m//2+1):
        for d,c in enumerate(a[j]):
            if d<=N: inner[d]-=c
    a[m]=shift(inner,m)
    S=add(S,a[m])
# B = S + S^2 + ... via coefficient recurrence B=S+S*B.
B=[0]*(N+1)
for n in range(1,N+1):
    B[n]=S[n]+sum(S[j]*B[n-j] for j in range(1,n))
assert B[1:]==b[1:N+1]

print(
    "VERIFY_OK "
    "unbordered_recurrence_bruteforce_q=2,3_n<=7 "
    "shortest_border_identity_q=2..7_m<=40 "
    "finite_tail_identity_q=2,3_n<=8_r<=3 "
    "A274190_reverse_row=A274199_compositions_d<=16 "
    "formal_series_coefficients_d<=16 "
    "source_constants_q=2..10"
)
print("E2=%.15f E3=%.15f E10=%.15f" % (vals[2],vals[3],vals[10]))
