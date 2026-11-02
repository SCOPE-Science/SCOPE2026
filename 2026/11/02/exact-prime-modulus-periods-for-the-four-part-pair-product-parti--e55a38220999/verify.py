#!/usr/bin/env python3
"""Exact arithmetic checks for the four-part pair-product partition statistic."""
from collections import defaultdict
from itertools import combinations


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, c in enumerate(a): out[i] += c
    for i, c in enumerate(b): out[i] += c
    return trim(out)


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): out[i+j] += x*y
    return trim(out)


def power(a, n):
    out = [1]
    for _ in range(n): out = mul(out, a)
    return out


def poly_mod(a, b):
    assert b[-1] == 1
    out = a[:]
    while len(out) >= len(b):
        c = out[-1]
        shift = len(out)-len(b)
        for i, v in enumerate(b): out[shift+i] -= c*v
        trim(out)
    return out


def monomial_x(i):
    return tuple(int(j == i) for j in range(4))


def multiply_x(a, b):
    out = defaultdict(int)
    for ma, ca in a.items():
        for mb, cb in b.items():
            out[tuple(ma[i]+mb[i] for i in range(4))] += ca*cb
    return {m:c for m,c in out.items() if c}


def construct_numerator():
    zero = (0,0,0,0)
    A=[]
    for i in range(4):
        term={zero:1}
        for j in range(i,4): term[monomial_x(j)] = 1
        A.append(term)
    e2=defaultdict(int)
    for i,j in combinations(range(4),2):
        for m,c in multiply_x(A[i],A[j]).items(): e2[m]+=c
    N=[0]
    for m,c in e2.items():
        assert max(m)<=2
        piece=[0,0,0,0,c]
        for i, degree in enumerate(m,1):
            q_i=[0]*i+[1]
            if degree==0:
                g=power(add([1],[-v for v in q_i]),2)
            elif degree==1:
                g=mul(q_i,add([1],[-v for v in q_i]))
            else:
                g=mul(q_i,add([1],q_i))
            piece=mul(piece,g)
        N=add(N,piece)
    return N, e2

P = [6,15,34,57,95,121,146,126,106,72,50,25,11]
PHI1 = [-1,1]
PHI2 = [1,1]
PHI4 = [1,0,1]
PHI3 = [1,1,1]
H = mul(mul(power(PHI1,6),power(PHI2,4)),
        mul(power(PHI4,3),power(PHI3,3)))
D = [1]
for j in range(1,5):
    neg=[1]+[0]*(j-1)+[-1]
    D=mul(D,power(neg,3))
N,e2 = construct_numerator()
gcdfactor=mul(power(PHI1,6),power(PHI2,2))
assert N == mul(mul([0,0,0,0,1],P),gcdfactor)
assert D == mul(H,gcdfactor)
assert len(H)==23 and len(P)==13 and len(N)==25
for phi, residue in [(PHI1,864),(PHI2,32),(PHI4,-12),(PHI3,6)]:
    assert poly_mod(P,phi)==[residue]


def terms(mod, length):
    out=[]
    for n in range(length):
        v = P[n-4] if 4<=n<17 else 0
        for j in range(1,min(n,len(H)-1)+1): v-=H[j]*out[n-j]
        out.append(v%mod)
    return out


def direct_partitions(n):
    s=0
    for d in range(1,n//4+1):
        for c in range(d,(n-d)//3+1):
            for b in range(c,(n-d-c)//2+1):
                a=n-d-c-b
                if a < b: continue
                parts=(a,b,c,d)
                s+=sum(parts[i]*parts[j] for i,j in combinations(range(4),2))
    return s

integer_coeffs=[]
for n in range(41):
    v = P[n-4] if 4<=n<17 else 0
    for j in range(1,min(n,len(H)-1)+1): v-=H[j]*integer_coeffs[n-j]
    assert v==direct_partitions(n),(n,v,direct_partitions(n))
    integer_coeffs.append(v)

for prime in (5,7,11,13,17,37,101):
    T = 300 if prime==5 else 12*prime
    seq=terms(prime,2*T+20)
    assert all(seq[n]==seq[n+T] for n in range(T+20)),prime
    assert all(any(seq[n]!=seq[n+d] for n in range(T))
               for d in range(1,T) if T%d==0),prime
print('VERIFY_OK numerator_degree=24 reduced_denominator_degree=22 '
      'cyclotomic_residues=864,32,-12,6 direct_partition_terms=41 '
      'prime_periods=5:300,7:84,11:132,13:156,17:204,37:444,101:1212')
