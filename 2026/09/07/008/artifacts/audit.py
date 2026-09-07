"""Audit script: reruns all verifications from stored artifacts.
Requires: numpy + sympy only. Must run <60s on a laptop.
Verifies: completeness (377k enumeration), exact rank 3, exact NMF factors,
fooling lower bounds, census counts 713/6/0.
"""
import numpy as np, itertools, time, json, csv, sys, os
from fractions import Fraction

BASE = os.path.dirname(os.path.abspath(__file__))
t0=time.time()
def log(m):
    print(f"[audit {time.time()-t0:.1f}s] {m}",flush=True)

Mrep=np.load(os.path.join(BASE,"Mrep_rank3.npy"))
codes=np.load(os.path.join(BASE,"canon_code_per_orbit.npy"))
sizes=np.load(os.path.join(BASE,"orbit_sizes_rank3.npy"))
foolmax=np.load(os.path.join(BASE,"foolmax.npy"))
rect=np.load(os.path.join(BASE,"rectcover.npy"))
with open(os.path.join(BASE,"exact_factors.json")) as fh:
    fac=json.load(fh)
with open(os.path.join(BASE,"fooling_witnesses.json")) as fh:
    wit=json.load(fh)
log(f"loaded: Mrep {Mrep.shape}, codes {codes.shape}")

# 1. counts
assert len(Mrep)==719 and len(codes)==719 and len(sizes)==719, "count mismatch"
assert len(np.unique(codes))==719, "codes not distinct"
assert int(sizes.sum())==63015, f"sizes sum {sizes.sum()} != 63015"
assert len(fac)==719, "factors count"
r3=sum(1 for k in fac if fac[str(k)]["r"]==3)
r4=sum(1 for k in fac if fac[str(k)]["r"]==4)
assert r3==713 and r4==6, f"r3={r3} r4={r4} != 713/6"
log(f"counts OK: 713 rankplus3, 6 rankplus4")

# 2. exact rank 3 via Bareiss + sympy
def bareiss_rank(M):
    A=[[int(M[i,j]) for j in range(5)] for i in range(5)]
    prev=1; row=0; rank=0
    for col in range(5):
        piv=None
        for i in range(row,5):
            if A[i][col]!=0:
                piv=i; break
        if piv is None: continue
        A[row],A[piv]=A[piv],A[row]
        for i in range(row+1,5):
            for j in range(col+1,5):
                A[i][j]=(A[i][j]*A[row][col]-A[i][col]*A[row][j])//prev
            A[i][col]=0
        prev=A[row][col]; row+=1; rank+=1
    return rank
for k in range(719):
    assert bareiss_rank(Mrep[k])==3, f"Bareiss rank fail {k}"
log("Bareiss rank==3 for all 719 OK")
import sympy as sp
for k in range(719):
    assert sp.Matrix(Mrep[k].tolist()).rank()==3, f"sympy rank fail {k}"
log("SymPy rank==3 for all 719 OK")

# 3. exact factor verification
def toF(x):
    if isinstance(x,Fraction): return x
    if isinstance(x,str): return Fraction(x)
    return Fraction(int(x))
for k in range(719):
    M=Mrep[k]; f=fac[str(k)]; r=f["r"]
    W=[[toF(v) for v in row] for row in f["W"]]
    H=[[toF(v) for v in row] for row in f["H"]]
    assert len(W)==5 and len(W[0])==r and len(H)==r and len(H[0])==5
    for row in W+H:
        for v in row: assert v>=0, f"negativity {k}"
    for i in range(5):
        for j in range(5):
            assert sum(W[i][a]*H[a][j] for a in range(r))==Fraction(int(M[i,j])), f"factor mismatch {k}"
log("exact M=W*H >=0 for all 719 OK")

# 4. fooling witnesses for the six r=4 cases
assert set(wit.keys())=={str(k) for k in range(719) if fac[str(k)]["r"]==4}, "witness keys"
for ks, w in wit.items():
    k=int(ks); M=Mrep[k]
    rs,cs,pi=w
    assert len(rs)==4 and len(cs)==4 and len(pi)==4
    assert len(set(rs))==4 and len(set(cs))==4 and sorted(pi)==[0,1,2,3]
    for a in range(4):
        assert int(M[rs[a],cs[pi[a]]])>0, f"fooling diag {k}"
    for a in range(4):
        for b in range(a+1,4):
            assert int(M[rs[a],cs[pi[b]]])*int(M[rs[b],cs[pi[a]]])==0, f"fooling cross {k}"
log("fooling-4 witnesses valid for all six gap cases OK")
# fooling implies rank_+>=4; with r=4 factor => ==4. r=3 factors => ==3 (rank lower bound).
# universal NMF<=4: r=3 factors pad to r=4, so no class needs >=5.
log("classification logic OK: 713x rankplus=3, 6x rankplus=4, 0x >=5")

# 5. completeness: re-enumerate 377k column multisets, ranks, canon codes
log("re-enumerating 377k multisets for completeness ...")
vals=list(itertools.combinations_with_replacement(range(32),5))
V=np.array(vals,dtype=np.int64)
N=V.shape[0]
assert N==376992
M=np.zeros((N,5,5),dtype=np.uint8)
for i in range(5):
    M[:,i,:]=((V>>i)&1)
chunk=20000
ranks=np.zeros(N,dtype=np.int64)
for s in range(0,N,chunk):
    e=min(s+chunk,N)
    ranks[s:e]=np.linalg.matrix_rank(M[s:e].astype(np.float64))
from collections import Counter
c=Counter(ranks.tolist())
log(f"rank histogram {dict(c)}")
assert c[3]==63015, "rank-3 multiset count changed"
idx=np.where(ranks==3)[0]
V3=V[idx]
# row values
pow2=np.array([1,2,4,8,16],dtype=np.int64)
W3=(M[idx].astype(np.int64)*pow2[None,None,:]).sum(axis=2)
perms=list(itertools.permutations(range(5)))
lut=np.zeros((120,32),dtype=np.int64)
for p,perm in enumerate(perms):
    for v in range(32):
        bits=[(v>>k)&1 for k in range(5)]
        lut[p,v]=sum(bits[perm[i]]*(1<<i) for i in range(5))
pow32=np.array([32**4,32**3,32**2,32,1],dtype=np.int64)
best=np.full(len(idx),np.int64(32**5))
for p in range(120):
    code=(np.sort(lut[p][V3],axis=1)*pow32).sum(axis=1)
    np.minimum(best,code,out=best)
    code2=(np.sort(lut[p][W3],axis=1)*pow32).sum(axis=1)
    np.minimum(best,code2,out=best)
uniq=np.unique(best)
assert len(uniq)==719, f"orbit count {len(uniq)} !=719"
assert set(uniq.tolist())==set(codes.tolist()), "canon code set mismatch"
log("completeness OK: 719 orbits, code sets match")
# spot-check SVD vs Bareiss agreement on 500 random matrices (exactness of prefilter)
rng=np.random.default_rng(0)
for t in range(500):
    j=rng.integers(0,N)
    assert bareiss_rank(M[j])==int(ranks[j]), f"SVD/Bareiss mismatch {j}"
log("SVD/Bareiss agreement on 500 random OK")
log(f"AUDIT PASS in {time.time()-t0:.1f}s: 713x rank_+=3, 6x rank_+=4, 0x >=5; binary stratum max is 4.")
