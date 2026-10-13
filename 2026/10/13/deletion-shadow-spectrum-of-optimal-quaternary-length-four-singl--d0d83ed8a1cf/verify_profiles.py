#!/usr/bin/env python3
import itertools, json, hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix

HERE=Path(__file__).resolve().parent
Q=range(4)
words=list(itertools.product(Q,repeat=4))
outs=list(itertools.product(Q,repeat=3))
out_index={y:i for i,y in enumerate(outs)}
word_index={''.join(map(str,w)):i for i,w in enumerate(words)}

def shadow(w):
    return frozenset(w[:i]+w[i+1:] for i in range(4))

shadows=[shadow(w) for w in words]
sizes=np.array([len(s) for s in shadows],dtype=float)
assert len(words)==256 and len(outs)==64
assert {k:sum(1 for s in shadows if len(s)==k) for k in range(1,5)}=={1:4,2:36,3:108,4:108}

A=lil_matrix((64,256),dtype=float)
for j,s in enumerate(shadows):
    for y in s:
        A[out_index[y],j]=1.0
A=A.tocsr()
base=LinearConstraint(A, -np.inf*np.ones(64), np.ones(64))
bounds=Bounds(np.zeros(256),np.ones(256))
integrality=np.ones(256)
ones=np.ones(256)

def solve(c, extra=()):
    r=milp(c=np.asarray(c,dtype=float),integrality=integrality,bounds=bounds,
           constraints=[base,*extra],options={'mip_rel_gap':0.0,'time_limit':180.0,'presolve':True})
    return r

def int_opt_value(r, sign=1):
    assert r.status==0 and r.success and r.fun is not None, (r.status,r.message)
    v=sign*r.fun
    iv=round(v)
    assert abs(v-iv)<1e-7, v
    return int(iv)

# Independently re-establish the published optimum cardinality.
r=solve(-ones)
maximum=int_opt_value(r,sign=-1)
assert maximum==24

eq24=LinearConstraint(ones.reshape(1,-1),[24.0],[24.0])
mincov=int_opt_value(solve(sizes,[eq24]))
maxcov=int_opt_value(solve(-sizes,[eq24]),sign=-1)
assert (mincov,maxcov)==(60,64)

coverage_feasible={}
for cov in range(60,65):
    eqcov=LinearConstraint(sizes.reshape(1,-1),[float(cov)],[float(cov)])
    rr=solve(np.zeros(256),[eq24,eqcov])
    if rr.status==0:
        coverage_feasible[cov]=True
    elif rr.status==2:
        coverage_feasible[cov]=False
    else:
        raise AssertionError((cov,rr.status,rr.message))
assert coverage_feasible=={60:True,61:False,62:True,63:False,64:True}

G={k:np.array([1.0 if len(shadows[j])==k else 0.0 for j in range(256)]) for k in range(1,5)}
feasible_profiles=[]
for n1 in range(5):
    for n2 in range(25):
        for n3 in range(25-n1-n2):
            n4=24-n1-n2-n3
            if n4<0:
                continue
            cov=n1+2*n2+3*n3+4*n4
            if cov<60 or cov>64:
                continue
            cons=[eq24]
            for k,n in ((1,n1),(2,n2),(3,n3),(4,n4)):
                cons.append(LinearConstraint(G[k].reshape(1,-1),[float(n)],[float(n)]))
            rr=solve(np.zeros(256),cons)
            if rr.status==0:
                feasible_profiles.append((n1,n2,n3,n4))
            elif rr.status!=2:
                raise AssertionError(((n1,n2,n3,n4),rr.status,rr.message))
expected=[(4,8,4,8),(4,9,2,9),(4,10,0,10),(4,10,2,8),(4,11,0,9),(4,12,0,8)]
assert sorted(feasible_profiles)==sorted(expected), feasible_profiles

# Check explicit witnesses without relying on the optimizer's selected incumbent.
witnesses=json.loads((HERE/'witnesses.json').read_text(encoding='utf-8'))
assert set(witnesses)=={','.join(map(str,p)) for p in expected}
for key,code in witnesses.items():
    p=tuple(map(int,key.split(',')))
    assert len(code)==24 and len(set(code))==24
    ids=[word_index[w] for w in code]
    union=set()
    hist=[0,0,0,0,0]
    for j in ids:
        s=shadows[j]
        assert not (union & s)
        union.update(s)
        hist[len(s)]+=1
    assert tuple(hist[1:])==p
    assert len(union)==sum((i+1)*p[i] for i in range(4))

# The explicit q=4 optimum printed as Table 2 in Kim--Lee--Oh has the defect-four endpoint profile.
paper_code='''0000 1111 2222 3333 0011 0022 0033 1100 1122 1133 2200 2211 2233 3300 3311 3322 0230 1231 2012 3013 0321 2103 1302 3120'''.split()
ph=[0,0,0,0,0]; punion=set()
for w in paper_code:
    s=shadows[word_index[w]]
    assert not (punion & s)
    punion.update(s); ph[len(s)]+=1
assert tuple(ph[1:])==(4,12,0,8) and len(punion)==60

canon=json.dumps(witnesses,sort_keys=True,separators=(',',':')).encode('utf-8')
digest=hashlib.sha256(canon).hexdigest()
profiles_text=';'.join(','.join(map(str,p)) for p in sorted(expected,key=lambda p:(sum((i+1)*p[i] for i in range(4)),p)))
print('VERIFY_OK vertices=256 outputs=64 maximum=24 coverage_values=60,62,64 profiles='+profiles_text+' paper_table2_profile=4,12,0,8 witnesses_sha256='+digest)
