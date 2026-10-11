#!/usr/bin/env python3
from collections import defaultdict, deque

N=18
LCF=[5,7,-7,7,-7,-5]*3
TOGGLE=[10,5,16,17,9,0,15,14,3,6,11,13,12,7,1,8,2,4]
EXPECTED_F=(18,126,438,801,756,348,90,18,2)
EXPECTED_CHAIN_TRACES={
 0:(18,126,438,801,756,348,90,18,2),
 1:(0,0,6,0,0,9,0,0,2),
 2:(0,0,6,0,0,9,0,0,2),
}
EXPECTED_H4_CHAR=(10,-2,-2)

# Reconstruct the standard Pappus graph from its LCF presentation.
E=set()
for i in range(N):
    E.add(tuple(sorted((i,(i+1)%N))))
for i,s in enumerate(LCF):
    E.add(tuple(sorted((i,(i+s)%N))))
assert len(E)==27
adj=[0]*N
for a,b in E:
    adj[a]|=1<<b; adj[b]|=1<<a
assert all(x.bit_count()==3 for x in adj)

# Exhaustive independent-set enumeration.
faces=[]
for m in range(1,1<<N):
    ok=True
    t=m
    while t:
        b=t & -t; i=b.bit_length()-1; t-=b
        if adj[i] & m:
            ok=False; break
    if ok: faces.append(m)
F=set(faces)
bydim=defaultdict(list)
for m in faces: bydim[m.bit_count()-1].append(m)
fvec=tuple(len(bydim[d]) for d in range(max(bydim)+1))
assert fvec==EXPECTED_F
assert len(faces)==2597

# Sequential toggle matching on the nonempty face poset.
unmatched=set(F); pairs=[]
for v in TOGGLE:
    bit=1<<v
    for lo in list(unmatched):
        hi=lo|bit
        if (lo & bit)==0 and hi in unmatched:
            unmatched.remove(lo); unmatched.remove(hi); pairs.append((lo,hi,v))
crit=sorted(unmatched)
crit_profile=defaultdict(int)
for m in crit: crit_profile[m.bit_count()-1]+=1
assert dict(crit_profile)=={0:1,4:10}
assert len(pairs)==1293

# Verify every pair is a Hasse cover and the Forman orientation is acyclic.
pairset={(lo,hi) for lo,hi,_ in pairs}
assert len(pairset)==len(pairs)
for lo,hi,v in pairs:
    assert lo in F and hi in F
    assert hi==lo|(1<<v) and not (lo&(1<<v))
    assert hi.bit_count()==lo.bit_count()+1

indeg={m:0 for m in F}; out={m:[] for m in F}; covers=0
for hi in F:
    t=hi
    while t:
        b=t & -t; lo=hi^b; t-=b
        if lo==0: continue
        a,c=(hi,lo) if (lo,hi) in pairset else (lo,hi)
        out[a].append(c); indeg[c]+=1; covers+=1
q=deque(m for m,d in indeg.items() if d==0); seen=0
while q:
    x=q.popleft(); seen+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert seen==len(F)
assert covers==sum((d+1)*len(bydim[d]) for d in bydim if d>0)

# Independent exact boundary-rank cross-check over several prime fields.
def rank_mod_p(cols,p):
    piv={}; r=0
    for col in cols:
        v={k:(x%p) for k,x in col.items() if x%p}
        while v:
            j=min(v)
            if j not in piv:
                inv=pow(v[j],-1,p)
                v={k:(x*inv)%p for k,x in v.items() if (x*inv)%p}
                piv[j]=v; r+=1; break
            c=v[j]; pv=piv[j]
            for k,x in pv.items():
                z=(v.get(k,0)-c*x)%p
                if z:v[k]=z
                elif k in v:del v[k]
    return r
for prime in (2,3,5):
    ranks={0:0}
    for d in range(1,max(bydim)+1):
        ridx={m:i for i,m in enumerate(bydim[d-1])}
        cols=[]
        for m in bydim[d]:
            vs=[i for i in range(N) if (m>>i)&1]
            cols.append({ridx[m^(1<<v)]:(-1 if j%2 else 1) for j,v in enumerate(vs)})
        ranks[d]=rank_mod_p(cols,prime)
    betti=[]
    for d in range(max(bydim)+1):
        betti.append(len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0))
    assert tuple(betti)==(1,0,0,0,10,0,0,0,0)

# Order-three automorphism r(i)=i+6 mod 18.
def ppow(k): return [(i+6*k)%N for i in range(N)]
def image_mask(m,p):
    z=0
    for i in range(N):
        if (m>>i)&1:z|=1<<p[i]
    return z
def sign_on_simplex(m,p):
    vs=[i for i in range(N) if (m>>i)&1]
    imgs=[p[i] for i in vs]
    inv=sum(imgs[a]>imgs[b] for a in range(len(imgs)) for b in range(a+1,len(imgs)))
    return -1 if inv&1 else 1

chars=[]
for k in range(3):
    p=ppow(k)
    assert {tuple(sorted((p[a],p[b]))) for a,b in E}==E
    chain=[]
    for d in range(max(bydim)+1):
        tr=0
        for m in bydim[d]:
            if image_mask(m,p)==m:
                tr+=sign_on_simplex(m,p)
        chain.append(tr)
    assert tuple(chain)==EXPECTED_CHAIN_TRACES[k]
    L=sum(((-1)**d)*chain[d] for d in range(len(chain)))
    chars.append(L-1) # H_0 has trace 1; all other homology is H_4.
assert tuple(chars)==EXPECTED_H4_CHAR

# Rational C3 representation: a*1 + b*V, where V has character (2,-1,-1).
a=(EXPECTED_H4_CHAR[0]+2*EXPECTED_H4_CHAR[1])//3
b=(EXPECTED_H4_CHAR[0]-EXPECTED_H4_CHAR[1])//3
assert (a,b)==(2,4)
assert a+2*b==10 and a-b==-2

print('PAPPUS_C3_VERIFY_OK')
print('vertices=18 edges=27 faces=2597 f_vector='+str(fvec))
print('matching_pairs=1293 critical_cells={0:1,4:10} hasse_covers='+str(covers))
print('chain_traces='+str(EXPECTED_CHAIN_TRACES))
print('H4_character='+str(EXPECTED_H4_CHAR))
print('Q[C3]_decomposition=2*trivial+4*cyclotomic2d')
