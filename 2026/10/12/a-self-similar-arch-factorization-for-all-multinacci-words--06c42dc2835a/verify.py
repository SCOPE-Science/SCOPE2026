#!/usr/bin/env python3
"""Finite independent checks for the multinacci arch decomposition.
No claim of infinite certification is made by these checks.
"""
from collections import Counter
from itertools import product


def images(m):
    return [tuple((0,i+1)) if i < m-1 else (0,) for i in range(m)]


def apply(word, img):
    out=[]
    for a in word:
        out.extend(img[a])
    return tuple(out)


def iterate(seed,img,n):
    for _ in range(n):
        seed=apply(seed,img)
    return seed


def arch_endpoints(word,m):
    found=set();pos=[]
    for i,a in enumerate(word,1):
        found.add(a)
        if len(found)==m:
            pos.append(i)
            found.clear()
    return pos


def is_subsequence(sub,src):
    j=0
    for a in src:
        if j<len(sub) and a==sub[j]:j+=1
    return j==len(sub)


def defining_index(word,m):
    k=0
    while k+1<=len(word)//m+1:
        if all(is_subsequence(p,word) for p in product(range(m),repeat=k+1)):
            k+=1
        else:
            return k
    return k


def check(m):
    img=images(m)
    tau=[iterate((i,),img,m-1) for i in range(m)]
    assert len(tau[0])==2**(m-1)
    assert tau[0][-1]==m-1 and tau[0].count(m-1)==1
    assert set(tau[0])==set(range(m))
    for j in range(1,m):
        assert len(tau[j])==2**(m-1)-2**(j-1)
        assert m-1 not in tau[j]
        assert tau[j]==tuple(v for t in range(m-2,j-2,-1) for v in iterate((0,),img,t))
    arches=[tau[j+1]+tau[0] if j<m-1 else tau[0] for j in range(m)]
    for j,a in enumerate(arches):
        assert len(a)==2**m-2**j
        assert arch_endpoints(a,m)==[len(a)]

    word=(0,)
    while len(word)<30000:
        word=apply(word,img)
    # The fixed-point identity is tested at every position of a long prefix.
    n=15000
    decomposition=tau[0]+tuple(v for j in word for v in arches[j])
    assert decomposition[:n]==word[:n]
    ends=arch_endpoints(word[:n],m)
    markers=[i for i,x in enumerate(word[:n],1) if x==m-1]
    assert ends==markers
    assert ends[0]==2**(m-1)
    for j in range(min(len(ends)-1,1500)):
        assert ends[j+1]-ends[j]==2**m-2**word[j]
    hist=Counter(ends[j+1]-ends[j] for j in range(len(ends)-1))
    assert set(hist).issubset({2**m-2**j for j in range(m)})  # finite prefix need not exhibit every rare gap
    # All-prefix statement, not just arch endpoints.
    seen=0
    marker_count=0
    ends_set=set(ends)
    for N in range(1,n+1):
        seen+= N in ends_set
        marker_count += (word[N-1]==m-1)
        assert seen==marker_count
    for N in range(min(n,25 if m<=3 else 16)):
        assert defining_index(word[:N],m)==sum(x==m-1 for x in word[:N])
    for t in range(m, m+6):
        p=iterate((0,),img,t)
        rhs=len(iterate((0,),img,t-m))
        assert p.count(m-1)==rhs
    return len(word),len(ends),len(hist)

if __name__=='__main__':
    records=[]
    for m in range(2,9):records.append((m,*check(m)))
    print('VERIFY_OK symbolic_m=2..8 independent_direct_prefixes=15000 each exact_gap_coding=all arch_boundaries=all substitution_levels=m..m+5 sampled_subsequence_prefixes=small')
    print('CHECK_COUNTS',records)
