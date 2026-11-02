#!/usr/bin/env python3
"""Independent finite verification of Dyck greedy-arch defect theorem (standard library)."""
from collections import defaultdict
from math import comb

# 0 is upstep, 1 downstep.
def arches(word):
    seen = None; count = 0
    for x in word:
        if seen is None: seen = x
        elif seen != x:
            count += 1; seen = None
    return count

def dyck(n):
    def rec(u, v, prefix):
        if u == n and v == n:
            yield prefix
        if u < n: yield from rec(u+1, v, prefix + '0')
        if v < u: yield from rec(u, v+1, prefix+'1')
    yield from rec(0,0,'')

# Alternative symbol-by-symbol transition construction, independent of the printed pair table.
def process(state, pair):
    seen = {0:None,1:'0',2:'1'}[state]
    completed = 0
    for x in pair:
        if seen is None: seen=x
        elif seen != x: seen=None;completed+=1
    return {None:0,'0':1,'1':2}[seen],completed

def dp_counts(max_n, D):
    dp = {(0,0,0):1}
    rows=[]
    for n in range(max_n+1):
        rows.append([sum(v for (height, state, bad),v in dp.items() if height==0 and bad==d) for d in range(D+1)])
        nd=defaultdict(int)
        for (height,state,bad),v in dp.items():
            for block,change in [('00',1),('01',0),('10',0),('11',-1)]:
                if height==0 and block=='10': continue
                if height+change < 0 or height+change > D: continue
                ns,k=process(state,block)
                assert k in (0,1)
                nb=bad+1-k
                if nb<=D:nd[(height+change,ns,nb)]+=v
        dp=nd
    return rows

def rational_series(numer, den, count):
    a=[]
    for i in range(count):
        t=numer[i] if i<len(numer) else 0
        for j in range(1,min(i,len(den)-1)+1):t-=den[j]*a[i-j]
        assert t%den[0]==0
        a.append(t//den[0])
    return a

def convolution(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def power(poly,k):
    res=[1]
    for _ in range(k):res=convolution(res,poly)
    return res

N=80; D=3
mat=dp_counts(N,D)
num=[[1],[0,0,1],[0,0,0,1,-1],[0,0,0,0,1,-3,4,-2]]
den=[[1,-1],convolution([1,-1],[1,-2]),power([1,-2],3),power([1,-2],5)]
for d in range(4):
    coeffs=rational_series(num[d],den[d],N+1)
    for n in range(N+1):assert mat[n][d]==coeffs[n],(d,n,mat[n][d],coeffs[n])
print(f'SERIES_OK defects=0..{D} semilength=0..{N}')
total=0
for n in range(12):
    brute=[0]*4
    for w in dyck(n):
        defect=n-arches(w)
        assert defect>=0
        if defect<4:brute[defect]+=1
        total+=1
    assert brute==mat[n],(n,brute,mat[n])
print(f'WORDS_OK semilength=0..11 checked={total} Dyck_words')
for n in range(2,81):
    assert mat[n][1] == 2**(n-1)-1
for n in range(3,81):
    # 2**(n-5) rational for n=3,4: check integer by multiplication
    assert 32*mat[n][2]==(2**n)*(n-2)*(n+1)
print('COEFFICIENT_OK first two deficiency strata')
