#!/usr/bin/env python3
"""Exact verifier for the stated homotopy type of the Desargues independence complex.
Uses only the Python standard library and exhaustive finite enumeration.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N=20
# Generalized Petersen graph G(10,3): outer 0..9, inner 10..19.
edges=set()
for i in range(10):
    edges.add(tuple(sorted((i,(i+1)%10))))
    edges.add((i,10+i))
    edges.add(tuple(sorted((10+i,10+((i+3)%10)))))
assert len(edges)==30
adj=[0]*N
for a,b in edges:
    adj[a]|=1<<b; adj[b]|=1<<a
assert all(x.bit_count()==3 for x in adj)

faces=[]
for m in range(1,1<<N):
    x=m; ok=True
    while x:
        b=x&-x; i=b.bit_length()-1; x-=b
        if adj[i]&x:
            ok=False; break
    if ok: faces.append(m)
face_set=set(faces)
fvec=Counter(m.bit_count()-1 for m in faces)
assert len(faces)==6211
assert dict(sorted(fvec.items()))=={0:20,1:160,2:660,3:1510,4:1924,5:1320,6:480,7:115,8:20,9:2}

# Deterministic staged element matching. Empty face is not in the poset.
order=[8,19,10,5,6,11,9,7,0,17,15,2,4,16,18,1,12,14,3,13]
unmatched=set(faces); up={}; down={}
for v in order:
    bit=1<<v
    for m in list(unmatched):
        h=m|bit
        if not (m&bit) and h in unmatched:
            unmatched.remove(m); unmatched.remove(h)
            up[m]=h; down[h]=m
assert len(up)==3102
critical=sorted(unmatched)
cdims=Counter(m.bit_count()-1 for m in critical)
assert cdims==Counter({5:5,0:1,4:1})

# Verify acyclicity by orienting matched covers downward and all other Hasse covers upward.
indeg={m:0 for m in faces}; outs={m:[] for m in faces}; covers=0
for h in faces:
    if h.bit_count()==1: continue
    x=h
    while x:
        b=x&-x; x-=b; l=h^b; covers+=1
        if up.get(l)==h: a,z=h,l
        else: a,z=l,h
        outs[a].append(z); indeg[z]+=1
q=deque(m for m,d in indeg.items() if d==0); seen=0
while q:
    a=q.popleft(); seen+=1
    for z in outs[a]:
        indeg[z]-=1
        if indeg[z]==0: q.append(z)
assert covers==30360 and seen==len(faces)

# Oriented simplicial incidence coefficient [sigma:tau].
def inc(sig,tau):
    diff=sig^tau
    assert diff and not(diff&(diff-1))
    v=diff.bit_length()-1
    pos=sum(1 for i in range(v) if (sig>>i)&1)
    return -1 if pos%2 else 1

# Exact Morse boundary from dimension 5 to dimension 4 via gradient-path recursion.
p=4
crit4=[m for m in critical if m.bit_count()-1==4]
crit5=[m for m in critical if m.bit_count()-1==5]
assert len(crit4)==1 and len(crit5)==5
@lru_cache(None)
def reduce_p(alpha):
    if alpha in crit4:
        return {alpha:1}
    beta=up.get(alpha)
    if beta is None or beta.bit_count()-1!=p+1:
        return {}
    den=inc(beta,alpha)
    out=defaultdict(int)
    x=beta
    while x:
        b=x&-x; x-=b; tau=beta^b
        if tau==alpha or tau==0: continue
        coeff=-(inc(beta,tau)//den)
        for c,val in reduce_p(tau).items(): out[c]+=coeff*val
    return dict(out)
mb={}
for top in crit5:
    out=defaultdict(int); x=top
    while x:
        b=x&-x; x-=b; alpha=top^b
        for c,val in reduce_p(alpha).items(): out[c]+=inc(top,alpha)*val
    mb[top]=[out[c] for c in crit4]
assert all(v==[0] for v in mb.values())

# Independent mod-2 chain-rank computation on the full simplicial complex.
bydim=defaultdict(list)
for m in faces: bydim[m.bit_count()-1].append(m)
def rank_gf2(cols):
    basis={}; r=0
    for x in cols:
        while x:
            pivot=x.bit_length()-1
            if pivot in basis: x^=basis[pivot]
            else: basis[pivot]=x; r+=1; break
    return r
ranks={}
for d in range(1,max(bydim)+1):
    row={m:i for i,m in enumerate(bydim[d-1])}; cols=[]
    for s in bydim[d]:
        x=0; t=s
        while t:
            b=t&-t; t-=b; x ^= 1<<row[s^b]
        cols.append(x)
    ranks[d]=rank_gf2(cols)
assert ranks=={1:19,2:141,3:519,4:991,5:932,6:383,7:97,8:18,9:2}
betti={}
for d in sorted(bydim):
    if d==0: b=len(bydim[0])-ranks.get(1,0)-1
    else: b=len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
    betti[d]=b
assert betti=={0:0,1:0,2:0,3:0,4:1,5:5,6:0,7:0,8:0,9:0}

print(json_line := __import__('json').dumps({
    "status":"VERIFY_OK","vertices":N,"edges":len(edges),"nonempty_faces":len(faces),
    "f_vector":[fvec[d] for d in range(10)],"matching_pairs":len(up),"hasse_covers":covers,
    "critical_by_dimension":dict(sorted(cdims.items())),"morse_boundary_5_to_4":mb,
    "mod2_boundary_ranks":ranks,"reduced_mod2_betti":betti
},sort_keys=True))
