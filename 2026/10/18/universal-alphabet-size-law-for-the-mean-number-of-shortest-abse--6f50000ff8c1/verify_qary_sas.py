#!/usr/bin/env python3
"""Independent finite checks for q-ary shortest absent scattered subsequence means.
Uses only the Python standard library.  This is a finite consistency test,
not a replacement for the all-length combinatorial proof.
"""
from itertools import product
from math import comb


def full(m, length):
    return sum((-1)**j * comb(m, j) * (m-j)**length for j in range(m+1))


def pre_x_post_y(m, length):
    # A preterminal word p x s: p has a y, s has no y,
    # neither p nor s uses the other's marked letter, and
    # all m unmarked letters occur somewhere.
    if length == 0:
        return 0
    total = 0
    for left in range(length):
        right = length-1-left
        for j in range(m+1):
            r=m-j
            total += (-1)**j * comb(m,j) * ((r+1)**left-r**left) * (r+1)**right
    return total


def predicted(q, max_n):
    a=[0]*(max_n+1)
    b=[0]*(max_n+1)
    f=[0]*(max_n+1)
    for length in range(1,max_n+1):
        a[length] = full(q-1,length-1)
        if length >= 2:
            a[length] += (q-1)*(length-1)*full(q-2,length-2)
        b[length] = full(q-1,length-1)
        if q>=3:
            b[length] += (q-2)*pre_x_post_y(q-3,length-1)
    row=[a[i]+(q-1)*b[i] for i in range(max_n+1)]
    for n in range(max_n+1):
        f[n] = q*(q-1)**n + sum(row[j]*f[n-j] for j in range(1,n+1))
    return a,b,f


def arches(word,q):
    count=0; seen=set()
    for c in word:
        seen.add(c)
        if len(seen)==q:
            count+=1;seen.clear()
    return count


def subsequence(pattern,source):
    j=0
    for c in source:
        if j<len(pattern) and pattern[j]==c:
            j+=1
    return j==len(pattern)


def direct_count(word,q):
    length=arches(word,q)+1
    return sum(not subsequence(p,word) for p in product(range(q),repeat=length))


def brute_arch_pair(q,x,y,length):
    ans=0
    for w in product(range(q),repeat=length):
        if len(set(w[:-1]))!=q-1 or w[-1] in w[:-1]:
            continue
        j=0
        for c in w:
            if j<2 and c==(x,y)[j]:
                j+=1
        if j==1:
            ans+=1
    return ans


def check():
    checked=0
    for q,max_len in [(2,10),(3,8),(4,6)]:
        a,b,model=predicted(q,35)
        for length in range(q,min(max_len,8)+1):
            assert brute_arch_pair(q,0,0,length)==a[length], ('same arch',q,length)
            assert brute_arch_pair(q,0,1,length)==b[length], ('different arch',q,length)
        for n in range(max_len+1):
            direct=sum(direct_count(w,q) for w in product(range(q),repeat=n))
            assert direct==model[n], ('direct',q,n,direct,model[n])
            checked+=q**n
        if q==3:
            coeff=[1,-4,5,-14,20,-4]
            for n in range(36):
                lhs=sum(coeff[j]*model[n-j] for j in range(min(n,5)+1))
                rhs=(3,-6,3)[n] if n<3 else 0
                assert lhs==rhs, ('ternary rational identity',n,lhs,rhs)
    print('QARY_SAS_CHECKS_PASS direct_source_words=%d alphabet_sizes=2,3,4' % checked)
    print('q3_aggregate_n0..8', predicted(3,35)[2][:9])
    print('q3_rational_coefficients_verified_through_n35')

if __name__=='__main__':
    check()
