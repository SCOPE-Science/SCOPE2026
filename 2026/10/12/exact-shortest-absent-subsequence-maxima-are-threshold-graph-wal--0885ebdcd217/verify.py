#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json

def extremal_word(sigma,k):
    p=tuple(range(sigma))
    q=p[::-1]
    return tuple(x for b in range(k) for x in (p if b%2==0 else q))

def is_subseq(u,w):
    j=0
    for x in w:
        if j<len(u) and u[j]==x:
            j+=1
    return j==len(u)

def weak_zigzag(u):
    return all((u[i]>=u[i+1]) if i%2==0 else (u[i]<=u[i+1])
               for i in range(len(u)-1))

def threshold_walk_count(sigma,m):
    # m variable vertices, preceded by the universal start vertex sigma-1.
    v=[0]*sigma
    v[sigma-1]=1
    for _ in range(m):
        v=[sum(v[j] for j in range(sigma) if i+j>=sigma-1)
           for i in range(sigma)]
    return sum(v)

def reverse_accumulate_row(sigma,m):
    # Displayed row sigma-1 of OEIS A050447.
    v=[1]*sigma
    row=[1]
    for _ in range(m):
        acc=0
        nv=[]
        for x in reversed(v):
            acc+=x
            nv.append(acc)
        v=nv
        row.append(v[-1])
    return row

expected={
    2:[3,5,8,13,21,34],
    3:[6,14,31,70,157,353],
    4:[10,30,85,246,707,2037],
    5:[15,55,190,671,2353,8272],
    6:[21,91,371,1547,6405,26585],
}

# Engine A: direct word/subsequence enumeration for the claimed extremal word.
for sigma in range(2,6):
    for k in range(1,6):
        W=extremal_word(sigma,k)
        absent=[]
        for u in product(range(sigma), repeat=k+1):
            a=not is_subseq(u,W)
            z=weak_zigzag(u)
            assert a==z,(sigma,k,u,a,z)
            if a:
                absent.append(u)
        assert len(absent)==threshold_walk_count(sigma,k+1)

# Engine B: threshold-graph dynamic programming and the OEIS reverse-accumulate
# recurrence agree for the checked rectangle, independently of word enumeration.
for sigma in range(2,10):
    row=reverse_accumulate_row(sigma,12)
    for m in range(1,13):
        assert row[m]==threshold_walk_count(sigma,m),(sigma,m,row[m],threshold_walk_count(sigma,m))

for sigma,vals in expected.items():
    got=[threshold_walk_count(sigma,k+1) for k in range(1,7)]
    assert got==vals,(sigma,got,vals)

# Finite stress test of the published extremality statement on small instances.
# We inspect all full-alphabet words through length 7 and compare every word of
# universality k=1 or 2 with the claimed bound.
def universality(w,sigma):
    k=0
    while True:
        L=k+1
        if all(is_subseq(u,w) for u in product(range(sigma), repeat=L)):
            k=L
        else:
            return k

def sas_count(w,sigma):
    k=universality(w,sigma)
    if k<1:
        return None,k
    L=k+1
    return sum(not is_subseq(u,w) for u in product(range(sigma), repeat=L)),k

checked=0
for sigma,maxn in ((2,7),(3,7)):
    for n in range(sigma,maxn+1):
        for w in product(range(sigma),repeat=n):
            if len(set(w))<sigma:
                continue
            c,k=sas_count(w,sigma)
            if k in (1,2):
                assert c<=threshold_walk_count(sigma,k+1),(sigma,n,w,k,c)
                checked+=1

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text())
assert cert["oeis"]=="A050447"
assert cert["shortest_absent_pattern"]=="x0>=x1<=x2>=x3<=..."

print("VERIFY_OK direct_extremal_sigma=2..5_k=1..5 "
      "threshold_vs_reverse_accumulate_sigma=2..9_m=1..12 "
      f"small_all_words_checked={checked} "
      "pattern=weak_zigzag oeis=A050447")
