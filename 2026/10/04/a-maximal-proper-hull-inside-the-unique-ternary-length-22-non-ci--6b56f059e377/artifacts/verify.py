#!/usr/bin/env python3
from itertools import product
from collections import Counter
from pathlib import Path
import json, math

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))
P=3

def rank_rref(M):
    A=[[x%P for x in row] for row in M]
    r=0; piv=[]
    if not A: return 0,A,piv
    for c in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        inv=pow(A[r][c],-1,P)
        A[r]=[(inv*x)%P for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[(A[i][j]-f*A[r][j])%P for j in range(len(A[0]))]
        piv.append(c); r+=1
        if r==len(A): break
    return r,A,piv

def nullspace(M):
    r,R,piv=rank_rref(M)
    n=len(M[0])
    free=[j for j in range(n) if j not in piv]
    out=[]
    for f in free:
        x=[0]*n; x[f]=1
        for rr,pc in reversed(list(enumerate(piv))):
            x[pc]=(-sum(R[rr][j]*x[j] for j in free))%P
        out.append(x)
    assert len(out)==n-r
    return out

def msgmul(msg,G):
    return [sum(msg[i]*G[i][j] for i in range(len(G)))%P for j in range(len(G[0]))]

def inner(x,y):
    return sum(a*b for a,b in zip(x,y))%P

def gram(G):
    return [[inner(G[i],G[j]) for j in range(len(G))] for i in range(len(G))]

def weight_dist(G):
    ans=Counter()
    for msg in product(range(P),repeat=len(G)):
        w=msgmul(msg,G)
        ans[sum(x!=0 for x in w)]+=1
    return ans

def convert(d):
    return {int(k):v for k,v in d.items()}

src=cert['toeplitz']
t=src['t']; a=src['a']; b=src['b']; m=11
T=[]
for i in range(m):
    row=[]
    for j in range(m):
        if i==j: row.append(t)
        elif j>i: row.append(a[j-i-1])
        else: row.append(b[i-j-1])
    T.append(row)
G=[[1 if i==j else 0 for j in range(m)]+T[i] for i in range(m)]
exp=cert['expected']

rG,_,_=rank_rref(G)
assert rG==exp['rank_G']==11
M=gram(G)
rM,_,_=rank_rref(M)
assert rM==exp['rank_Gram']==1
K=nullspace(M)
assert len(K)==exp['hull_dimension']==10
H=[msgmul(x,G) for x in K]
assert rank_rref(H)[0]==10
assert rank_rref(gram(H))[0]==0

WC=weight_dist(G)
WH=weight_dist(H)
assert WC==Counter(convert(exp['code_weight_distribution']))
assert WH==Counter(convert(exp['hull_weight_distribution']))
assert sum(WC.values())==3**11
assert sum(WH.values())==3**10
assert min(w for w in WC if w)>0 and min(w for w in WC if w)==8
assert min(w for w in WH if w)>0 and min(w for w in WH if w)==9

# Select a codeword outside H by choosing a message not annihilating the Gram matrix.
out_msg=None
for j in range(11):
    e=[0]*11; e[j]=1
    if any(sum(e[i]*M[i][c] for i in range(11))%P for c in range(11)):
        out_msg=e; break
assert out_msg is not None
v=msgmul(out_msg,G)

def coset_dist(scale):
    ans=Counter(); vv=[scale*x%P for x in v]
    for msg in product(range(P),repeat=10):
        h=msgmul(msg,H)
        w=[(h[j]+vv[j])%P for j in range(22)]
        ans[sum(x!=0 for x in w)]+=1
    return ans

C1=coset_dist(1); C2=coset_dist(2)
EC=Counter(convert(exp['nonzero_coset_weight_distribution']))
assert C1==EC and C2==EC
assert WH+C1+C2==WC

# Directly verify all hull-generator rows are orthogonal to all ambient-generator rows.
for h in H:
    assert all(inner(h,g)==0 for g in G)

# Griesmer obstruction to a ternary [22,10,10] linear code.
griesmer=sum(math.ceil(10/(3**i)) for i in range(10))
assert griesmer==exp['griesmer_q3_k10_d10']==23
assert griesmer>22

print('VERIFY_OK')
