#!/usr/bin/env python3
import re
from math import comb

def C(n,k):
    return comb(n,k) if n >= k >= 0 else 0

def R_formula(L):
    return C(L//2,3) + 2*C((L-1)//2,3) + C((L-2)//2,3)

def fibs_to(n):
    F=[0,1]
    while len(F) <= n:
        F.append(F[-1]+F[-2])
    return F

def fib_word(N):
    a,b="0","01"
    while len(b) < N:
        a,b=b,b+a
    return b[:N]

def zeckendorf(n,F):
    if n == 0:
        return ""
    k=len(F)-1
    while F[k] > n:
        k-=1
    # canonical weights F_k,F_{k-1},...,F_2
    bits=[]
    rem=n
    for j in range(k,1,-1):
        if F[j] <= rem:
            bits.append("1")
            rem-=F[j]
        else:
            bits.append("0")
    assert rem == 0
    s="".join(bits)
    assert s and s[0]=="1" and "11" not in s
    return s

pat=re.compile(r'^(10)+0(?:0|10)(?:00)*0(?:0(?:10)*(?:1)?)$')

def cube_ending_bits(w):
    # Direct definition check, not the source regex.
    ans=[]
    for e in range(1,len(w)+1):
        ok=False
        for p in range(1,e//3+1):
            x=w[e-3*p:e-2*p]
            if x == w[e-2*p:e-p] == w[e-p:e]:
                ok=True
                break
        ans.append(1 if ok else 0)
    return ans

def run_starts(bits,v):
    out=[]
    prev=1-v
    for i,x in enumerate(bits):
        if x==v and (i==0 or bits[i-1]!=v):
            out.append(i)
    return out

def run_lengths(bits,v):
    out=[]
    i=0
    while i<len(bits):
        if bits[i]!=v:
            i+=1
            continue
        j=i
        while j<len(bits) and bits[j]==v:
            j+=1
        out.append(j-i)
        i=j
    return out

# Exact regular-expression counting through a wide range.
for L in range(0,41):
    generated=set()
    for A in range(0,30):
        for b in range(0,30):
            for c in range(0,30):
                a=A+1
                for middle in ("0","10"):
                    for e in ("","1"):
                        s=("10"*a)+"0"+middle+("00"*b)+"0"+"0"+("10"*c)+e
                        if len(s) <= L:
                            assert s[0]=="1" and "11" not in s and pat.fullmatch(s)
                            generated.add(s)
    assert len(generated)==R_formula(L), (L,len(generated),R_formula(L))

# Direct word check at a length large enough to contain many runs.
N=2400
w=fib_word(N)
bits=cube_ending_bits(w)
F=fibs_to(40)

one_starts=run_starts(bits,1)
regex_starts=[i for i in range(N) if pat.fullmatch(zeckendorf(i,F))]
# Ignore a final brute run if it could extend past the truncated word:
assert one_starts[:-1] == regex_starts[:len(one_starts)-1]
assert one_starts[0] == 13

# All complete zero-runs have the published permitted lengths.
zlengths=run_lengths(bits,0)
assert set(zlengths[:-1]).issubset({1,2,3,7,8,13})
assert zlengths[0]==13

# Exact counts of one-run starts below Fibonacci cutoffs.
for L in range(6,16):
    cutoff=F[L+2]
    brute=sum(1 for i in one_starts if i < cutoff)
    assert brute==R_formula(L), (L,cutoff,brute,R_formula(L))

# Check the proved sandwich on all prefixes in the brute range.
z=0
for n in range(2,N+1):
    z += 1-bits[n-1]
    # find L with F[L+1] <= n < F[L+2]
    L=2
    while not (F[L+1] <= n < F[L+2]):
        L+=1
    assert R_formula(L-1) <= z <= 13*(R_formula(L)+1), (n,L,z)

print(
    "VERIFY_OK "
    "regex_counts_L<=40 "
    "direct_cube_prefix=2400 "
    "run_starts_matched "
    "zero_run_lengths_subset=1,2,3,7,8,13 "
    "Fibonacci_cutoffs_L=6..15 "
    "prefix_sandwich_n=2..2400"
)
