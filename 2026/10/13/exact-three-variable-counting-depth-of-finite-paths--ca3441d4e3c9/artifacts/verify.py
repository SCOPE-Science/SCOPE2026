from collections import Counter
from functools import lru_cache

def path(n):
    E=set()
    for i in range(n-1): E.add((i,i+1)); E.add((i+1,i))
    return n,E

def rival(m, cycles):
    N=m+sum(cycles); E=set()
    for i in range(m-1): E.add((i,i+1)); E.add((i+1,i))
    off=m
    for c in cycles:
        for i in range(c):
            a=off+i; b=off+(i+1)%c; E.add((a,b)); E.add((b,a))
        off+=c
    return N,E

def first_diag_diff(g,h,maxr=8):
    n,Eg=g; m,Eh=h; assert n==m
    N=2*n
    def edge(i,j):
        if i<n and j<n: return (i,j) in Eg
        if i>=n and j>=n: return (i-n,j-n) in Eh
        return False
    C=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j]=0 if i==j else (1 if edge(i,j) else 2)
    for r in range(maxr+1):
        a=Counter(C[i][i] for i in range(n))
        b=Counter(C[n+i][n+i] for i in range(n))
        if a!=b: return r
        sig=[[None]*N for _ in range(N)]
        for i in range(N):
            Ci=C[i]
            for j in range(N):
                cnt={}
                for z in range(N):
                    q=(Ci[z],C[z][j]); cnt[q]=cnt.get(q,0)+1
                sig[i][j]=(Ci[j],tuple(sorted(cnt.items())))
        mp={}; nxt=0; D=[[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                s=sig[i][j]
                if s not in mp: mp[s]=nxt; nxt+=1
                D[i][j]=mp[s]
        C=D
    raise AssertionError('no diff')

def parts(total, lo=3):
    # nondecreasing partitions into parts >=3
    out=[]
    def rec(rem, start, cur):
        if rem==0: out.append(tuple(cur)); return
        for x in range(start, rem+1):
            if x<3: continue
            if rem-x!=0 and rem-x< x: continue
            rec(rem-x,x,cur+[x])
    rec(total,lo,[])
    return out

def pred_pair(m,c):
    import math
    return min((m+2).bit_length()-1, 1+(c-1).bit_length()-1)

def pred_def(n):
    if n==1:return 1
    # 2 + floor(log2((n+1)/3)) without floating point
    q=(n+1)//3
    # floor(log2((n+1)/3)) needs rational floor; largest k with 3*2^k <= n+1
    k=0
    while 3*(1<<(k+1))<=n+1:k+=1
    return 2+k

count=0
for n in range(5,19):
    best=0
    for m in range(2,n-2):
        rem=n-m
        for cyc in parts(rem):
            if not cyc: continue
            d=first_diag_diff(path(n),rival(m,cyc),8)
            p=pred_pair(m,min(cyc))
            assert d==p,(n,m,cyc,d,p)
            best=max(best,d); count+=1
    R=pred_def(n)-1
    assert best==R,(n,best,R)
# Extremal one-cycle witnesses farther out
for n in range(19,41):
    R=pred_def(n)-1
    m=(1<<R)-2
    c=n-m
    assert c>=3
    d=first_diag_diff(path(n),rival(m,(c,)),8)
    assert d==R,(n,m,c,d,R)
print(f'VERIFY_OK decompositions={count} exhaustive_n=5..18 extremal_n=19..40')
