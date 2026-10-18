#!/usr/bin/env python3
"""Reproduce finite checks for length-two composition profile enumeration.
All inputs are literal mathematical word/edge definitions; stdlib only.
"""
from itertools import product
from collections import defaultdict
from math import comb

# Q=3 exact ternary rational series numerator and denominator.
NUM = [3,-6,6,9,-6,0,3,-3]
# (1-z)^6 (1+z)^2, obtained by ordinary convolution.
DEN = [0]*9
for i in range(7):
    for j,c in enumerate((1,2,1)):
        DEN[i+j] += (-1)**i*comb(6,i)*c
assert DEN[0]==1

def closed_series(mmax):
    out=[]
    for m in range(mmax+1):
        a = (NUM[m] if m < len(NUM) else 0)
        a -= sum(DEN[j]*out[m-j] for j in range(1,min(m,len(DEN)-1)+1))
        out.append(a)
    return out

def word_profile(word, q):
    vertex=tuple(word.count(v) for v in range(q))
    edges=tuple((i,j) for i in range(q) for j in range(i,q))
    em={e:k for k,e in enumerate(edges)}
    mult=[0]*len(edges)
    for a,b in zip(word,word[1:]):
        mult[em[(min(a,b),max(a,b))]]+=1
    return vertex+tuple(mult)

def word_count(q,n):
    return len({word_profile(w,q) for w in product(range(q),repeat=n)})

def multisets(total,num):
    if num==1:
        yield (total,)
    else:
        for i in range(total+1):
            for suffix in multisets(total-i,num-1):
                yield (i,)+suffix

def graph_count(q,n):
    if n==1:return q
    edges=[(i,j) for i in range(q) for j in range(i,q)]
    answer=0
    for counts in multisets(n-1,len(edges)):
        degree=[0]*q
        neighbors=[set() for _ in range(q)]
        for (i,j),cnt in zip(edges,counts):
            if not cnt:continue
            degree[i]+=cnt
            degree[j]+=cnt
            if i!=j:
                neighbors[i].add(j)
                neighbors[j].add(i)
        support=[i for i in range(q) if degree[i]]
        if not support:continue
        todo=[support[0]];seen={support[0]}
        while todo:
            for v in neighbors[todo.pop()]:
                if v not in seen:
                    seen.add(v);todo.append(v)
        if len(seen)!=len(support):continue
        odds=sum(d%2 for d in degree)
        answer += len(support) if odds==0 else (1 if odds==2 else 0)
    return answer

def main():
    a=closed_series(28)
    expected=[3,6,18,45,108,228,447,807,1377,2226,3456,5169]
    assert a[:len(expected)]==expected
    for n in range(1,12):
        w=word_count(3,n)
        assert w==a[n-1],(n,w,a[n-1])
    print('ternary word enumeration PASS: n=1..11')
    for n in range(1,29):
        g=graph_count(3,n)
        assert g==a[n-1],(n,g,a[n-1])
    print('independent ternary graph enumeration PASS: n=1..28')
    for n in range(1,8):
        w=word_count(4,n);g=graph_count(4,n)
        assert w==g,(n,w,g)
    print('four-letter structural lemma PASS: n=1..7')
    print('P_3(1..12)=',a[:12]);print('P_3(28)=',a[27]);print('denominator=',DEN)
if __name__=='__main__':main()
