#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations, product
import json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE,'certificate.json'),'r',encoding='utf-8') as f:
    CERT=json.load(f)

V=tuple(range(8))
def bits(v): return ((v>>2)&1,(v>>1)&1,v&1)
def vid(t): return (t[0]<<2)|(t[1]<<1)|t[2]
def adjacent(u,v): return (u^v).bit_count()==1

def connected(S):
    S=set(S)
    if not S: return True
    seen={next(iter(S))}
    stack=list(seen)
    while stack:
        u=stack.pop()
        for v in S-seen:
            if adjacent(u,v):
                seen.add(v); stack.append(v)
    return seen==S

disconnected_triples=[t for t in combinations(V,3) if not connected(t)]
facets=sorted(tuple(v for v in V if v not in t) for t in disconnected_triples)
faces=[]
for d in range(5):
    fs=set()
    for F in facets:
        fs.update(combinations(F,d+1))
    faces.append(sorted(fs))
index=[{s:i for i,s in enumerate(fs)} for fs in faces]

assert len(disconnected_triples)==CERT['disconnected_triples']
assert [len(x) for x in faces]==CERT['f_vector']

# Dense boundary matrix from C_k to C_{k-1}, rows x cols.
def boundary(k):
    if k==0: return []
    M=[[0]*len(faces[k]) for _ in range(len(faces[k-1]))]
    for j,s in enumerate(faces[k]):
        for i in range(len(s)):
            t=s[:i]+s[i+1:]
            M[index[k-1][t]][j]= -1 if i%2 else 1
    return M

B=[None]+[boundary(k) for k in range(1,5)]

def matmul(A,Bm):
    if not A or not Bm: return []
    m,n,p=len(A),len(A[0]),len(Bm[0])
    out=[[0]*p for _ in range(m)]
    for i in range(m):
        for k in range(n):
            a=A[i][k]
            if a:
                for j in range(p): out[i][j]+=a*Bm[k][j]
    return out
for k in range(2,5):
    P=matmul(B[k-1],B[k])
    assert all(x==0 for row in P for x in row)

def rank_q(A):
    A=[list(map(Fraction,row)) for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r
ranks=[rank_q(B[k]) for k in range(1,5)]
assert ranks==CERT['boundary_ranks']
# beta_0 and higher beta_k
betti=[len(faces[0])-ranks[0]]
for k in range(1,4): betti.append(len(faces[k])-ranks[k-1]-ranks[k])
betti.append(len(faces[4])-ranks[3])
assert betti==CERT['betti']

# sparse H3 cycle z and dual cocycle c, indexed in lexicographic list of tetrahedra.
z=[0]*len(faces[3]); c=[0]*len(faces[3])
for i,a in CERT['h3_cycle_sparse']: z[i]=a
for i,a in CERT['h3_cocycle_sparse']: c[i]=a
# B3 z = 0
assert all(sum(B[3][i][j]*z[j] for j in range(len(z)))==0 for i in range(len(B[3])))
# c B4 = 0
assert all(sum(c[i]*B[4][i][j] for i in range(len(c)))==0 for j in range(len(faces[4])))
assert sum(c[i]*z[i] for i in range(len(z)))==1

def perm_sign(vals):
    inv=0
    for i in range(len(vals)):
        for j in range(i+1,len(vals)):
            if vals[i]>vals[j]: inv+=1
    return -1 if inv%2 else 1

def map_simplex(s,mp):
    raw=[mp[v] for v in s]
    sign=perm_sign(raw)
    return tuple(sorted(raw)),sign

def act_vec(vec,k,mp):
    out=[0]*len(faces[k])
    for j,a in enumerate(vec):
        if a:
            t,sgn=map_simplex(faces[k][j],mp)
            out[index[k][t]] += a*sgn
    return out

def trace_chain(k,mp):
    tr=0
    for s in faces[k]:
        t,sgn=map_simplex(s,mp)
        if t==s: tr+=sgn
    return tr

def parity_perm(p): return perm_sign(list(p))
body_diags=sorted({tuple(sorted((v,v^7))) for v in V})
assert len(body_diags)==4

def apply_diag(d,mp): return tuple(sorted((mp[d[0]],mp[d[1]])))

rows=[]
for p in permutations(range(3)):
    for b in product((0,1), repeat=3):
        mp={}
        for v in V:
            x=bits(v)
            y=tuple(x[p[i]]^b[i] for i in range(3))
            mp[v]=vid(y)
        assert len(set(mp.values()))==8
        assert all(adjacent(u,v)==adjacent(mp[u],mp[v]) for u in V for v in V)
        for k in range(5):
            assert all(tuple(sorted(mp[v] for v in s)) in index[k] for s in faces[k])
        eps=-1 if sum(b)%2 else 1
        omega=parity_perm(p)*eps
        gz=act_vec(z,3,mp)
        chi3=sum(c[i]*gz[i] for i in range(len(c)))
        assert chi3==omega
        chain_tr=[trace_chain(k,mp) for k in range(5)]
        L=sum(((-1)**k)*chain_tr[k] for k in range(5))
        chi4=L-1+chi3
        fixed=sum(1 for d in body_diags if apply_diag(d,mp)==d)
        assert chi4==eps*fixed
        rows.append({'perm':list(p),'b':list(b),'eps':eps,'omega':omega,'fixed_body_diagonals':fixed,'chi3':chi3,'chi4':chi4})
assert len(rows)==48
# Full automorphism group: affine maps give 48; any cube automorphism is determined by image of 000 (8 choices)
# and a permutation of its three neighbors (at most 6), so there can be at most 48.

print('VERIFY_OK')
print('disconnected triples:',len(disconnected_triples))
print('f-vector:',[len(x) for x in faces])
print('boundary ranks:',ranks)
print('Betti numbers:',betti)
from collections import Counter
bucket=Counter((r['chi3'],r['chi4'],r['eps'],r['fixed_body_diagonals']) for r in rows)
print('trace buckets:',sorted((count,key) for key,count in bucket.items()))
