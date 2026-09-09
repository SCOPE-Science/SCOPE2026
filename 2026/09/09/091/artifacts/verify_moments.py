"""Stdlib exact recomputation of expected traces E Tr A_G^k (k<=6) for uniform S3 3-lifts of K7.
Enumerates all base closed walks (7*6^k), groups by edge-pattern, exact E[Fix] via 6^m enumeration.
Prints VERIFY_OK. ~60-120s."""
import itertools
from fractions import Fraction
from collections import Counter
S3=list(itertools.permutations([0,1,2]))
INV=[]
for p in S3:
    q=[0]*3
    for i in range(3): q[p[i]]=i
    INV.append(S3.index(tuple(q)))
def compose(p,q): return (p[q[0]],p[q[1]],p[q[2]])
ID=(0,1,2)
def efix(blocks,oris):
    m=max(blocks)+1
    if len(set(blocks))==len(blocks): return Fraction(1,1)  # uniform independent product
    tot=0; N=6**m
    for code in range(N):
        dig=[]; t=code
        for _ in range(m): dig.append(t%6); t//=6
        cur=(0,1,2)
        for b,o in zip(blocks,oris):
            s=S3[dig[b]] if o==1 else S3[INV[dig[b]]]
            cur=compose(s,cur)
        tot+=sum(1 for i in range(3) if cur[i]==i)
    return Fraction(tot,N)
def closed_walks(k):
    out=[]
    def rec(path):
        if len(path)==k+1:
            if path[-1]==path[0]:
                em={}; bl=[]; ori=[]
                for j in range(1,k+1):
                    a,b=path[j-1],path[j]
                    e=(a,b) if a<b else (b,a)
                    if e not in em: em[e]=len(em)
                    bl.append(em[e]); ori.append(1 if a<b else -1)
                out.append((tuple(bl),tuple(ori)))
            return
        for w in range(7):
            if w!=path[-1]: rec(path+[w])
    for v0 in range(7): rec([v0])
    return out
EXPECT={1:0,2:126,3:210,4:2226,5:7770,6:59136}
for k in range(1,7):
    w=closed_walks(k)
    base_check=6**k+6*((-1)**k) if k>=1 else 0
    assert len(w)==base_check,(k,len(w),base_check)
    cnt=Counter(w); tot=Fraction(0)
    for pat,c in cnt.items(): tot+=c*efix(list(pat[0]),list(pat[1]))
    assert tot==EXPECT[k],(k,tot)
    print(f"k={k}: walks={len(w)} patterns={len(cnt)} ETr={tot} OK",flush=True)
print("VERIFY_OK")
