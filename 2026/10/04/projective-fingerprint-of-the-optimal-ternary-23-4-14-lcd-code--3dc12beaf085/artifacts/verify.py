#!/usr/bin/env python3
from pathlib import Path
from itertools import product, combinations
from collections import Counter, defaultdict
import json, math

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
G = cert["generator_matrix"]

def inv3(a):
    a %= 3
    if a == 1: return 1
    if a == 2: return 2
    raise ZeroDivisionError

def rank3(rows):
    if not rows: return 0
    A = [[x%3 for x in r] for r in rows]
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        s=inv3(A[r][c]); A[r]=[(s*x)%3 for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                a=A[i][c]; A[i]=[(A[i][j]-a*A[r][j])%3 for j in range(n)]
        r+=1
        if r==m: break
    return r

def det3(M):
    A=[[x%3 for x in r] for r in M]; n=len(A); det=1
    for c in range(n):
        p=next((i for i in range(c,n) if A[i][c]),None)
        if p is None:return 0
        if p!=c:A[c],A[p]=A[p],A[c];det=(-det)%3
        pv=A[c][c];det=det*pv%3;s=inv3(pv);A[c]=[(s*x)%3 for x in A[c]]
        for i in range(c+1,n):
            a=A[i][c];A[i]=[(A[i][j]-a*A[c][j])%3 for j in range(n)]
    return det

assert rank3(G)==4
Gram=[[sum(G[i][t]*G[j][t] for t in range(23))%3 for j in range(4)] for i in range(4)]
assert Gram==[[1,1,0,2],[1,2,1,1],[0,1,0,0],[2,1,0,0]]
assert det3(Gram)==1

dist=Counter()
for a in product(range(3),repeat=4):
    w=[sum(a[i]*G[i][j] for i in range(4))%3 for j in range(23)]
    dist[sum(x!=0 for x in w)]+=1
expected_dist={int(k):v for k,v in cert["weight_distribution"].items()}
assert dict(sorted(dist.items()))==expected_dist

def normalize(v):
    v=tuple(x%3 for x in v)
    for x in v:
        if x:
            s=inv3(x);return tuple((s*y)%3 for y in v)
    raise ValueError

cols=[tuple(G[i][j] for i in range(4)) for j in range(23)]
Slist=[normalize(v) for v in cols];S=set(Slist)
assert len(S)==23
PG=sorted({normalize(v) for v in product(range(3),repeat=4) if any(v)})
assert len(PG)==40

def line(a,b):
    pts=set()
    for x,y in product(range(3),repeat=2):
        if x==y==0:continue
        pts.add(normalize(tuple((x*a[i]+y*b[i])%3 for i in range(4))))
    assert len(pts)==4
    return frozenset(pts)

lines={line(a,b) for a,b in combinations(PG,2)}
assert len(lines)==130
ls=Counter(len(L&S) for L in lines)
assert dict(sorted(ls.items()))=={int(k):v for k,v in cert["line_intersection_spectrum"].items()}
assert sum(ls.values())==130
assert sum(j*n for j,n in ls.items())==23*13
assert sum(math.comb(j,2)*n for j,n in ls.items())==math.comb(23,2)

hs=Counter()
for a in PG:
    hs[sum(sum(a[t]*v[t] for t in range(4))%3==0 for v in Slist)]+=1
assert dict(sorted(hs.items()))=={int(k):v for k,v in cert["hyperplane_intersection_spectrum"].items()}
assert sum(hs.values())==40
assert sum(j*n for j,n in hs.items())==23*13
assert sum(math.comb(j,2)*n for j,n in hs.items())==4*math.comb(23,2)
from_hyp={0:1}
for z,n in hs.items():from_hyp[23-z]=2*n
assert from_hyp==expected_dist

edge={}
for i,j in combinations(range(23),2):
    edge[i,j]=len(line(Slist[i],Slist[j])&S)
def ec(i,j):
    if i==j:return 0
    return edge[min(i,j),max(i,j)]

sigs=[];classes=defaultdict(list)
for i in range(23):
    sig=tuple(sorted(Counter(ec(i,j) for j in range(23) if j!=i).items()))
    sigs.append(sig);classes[sig].append(i)
order=sorted(range(23),key=lambda i:(len(classes[sigs[i]]),i))
autos=[];mapping={};used=set()
def bt(pos=0):
    if pos==len(order):
        autos.append([mapping[i] for i in range(23)]);return
    u=order[pos]
    for v in classes[sigs[u]]:
        if v in used:continue
        if all(ec(u,u2)==ec(v,v2) for u2,v2 in mapping.items()):
            mapping[u]=v;used.add(v);bt(pos+1);used.remove(v);del mapping[u]
bt()
assert len(autos)==4
assert sorted(autos)==sorted(cert["projective_automorphism_permutations"])

def mat_apply(A,v):
    return tuple(sum(A[i][j]*v[j] for j in range(4))%3 for i in range(4))
for perm,A in zip(cert["projective_automorphism_permutations"],cert["projective_automorphism_matrices"]):
    assert rank3(A)==4
    for i,v in enumerate(Slist):
        assert normalize(mat_apply(A,v))==Slist[perm[i]]

def pord(p):
    seen=[False]*len(p);ans=1
    for i in range(len(p)):
        if not seen[i]:
            j=i;c=0
            while not seen[j]:seen[j]=True;c+=1;j=p[j]
            ans=math.lcm(ans,c)
    return ans
assert sorted(pord(p) for p in autos)==[1,2,2,2]
print("VERIFY_OK")
