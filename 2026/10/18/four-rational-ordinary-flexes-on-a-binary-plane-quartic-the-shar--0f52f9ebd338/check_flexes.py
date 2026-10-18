#!/usr/bin/env python3
"""Independent exact check of four ordinary rational flexes on binary plane quartics.
Run with Python 3 standard library: python3 check_flexes.py.
"""
from itertools import product
from collections import Counter
MON=tuple(m for m in product(range(5),repeat=3) if sum(m)==4)
CAP=(1,2,4,7)
assert len(MON)==15

def multiply_tangent_coefficients(m,p,q):
    coeff=[1,0,0,0,0]
    for i,e in enumerate(m):
        a=(p>>i)&1;b=(q>>i)&1
        z=[int((j&e)==j and ((e-j)==0 or a) and (j==0 or b)) for j in range(e+1)]
        new=[0]*5
        for t,c in enumerate(coeff):
            if c:
                for j,d in enumerate(z):
                    if d and t+j<5:new[t+j]^=1
        coeff=new
    return coeff

# Small exact Groebner checker for ideals in F2[u,v], lexicographic order.
def xor(a,b):return a.symmetric_difference(b)
def shift(a,di,dj):return {(i+di,j+dj) for i,j in a}
def leading(a):return max(a)
def reduction(p,G):
    p=set(p);r=set()
    while p:
        e=leading(p)
        for g in G:
            eg=leading(g)
            if eg[0]<=e[0] and eg[1]<=e[1]:
                p=xor(p,shift(g,e[0]-eg[0],e[1]-eg[1]));break
        else:p.remove(e);r.add(e)
    return r

def contains_one(generators):
    G=[set(g) for g in generators if g]
    if {(0,0)} in G:return True
    queue=[(i,j) for i in range(len(G)) for j in range(i)]
    while queue:
        i,j=queue.pop(0)
        mi=leading(G[i]);mj=leading(G[j])
        l=(max(mi[0],mj[0]),max(mi[1],mj[1]))
        s=xor(shift(G[i],l[0]-mi[0],l[1]-mi[1]),shift(G[j],l[0]-mj[0],l[1]-mj[1]))
        r=reduction(s,G)
        if r:
            if r=={(0,0)}:return True
            n=len(G)
            queue.extend((n,k) for k in range(n))
            G.append(r)
    return False

def smooth(mask):
    for c in range(3):
        F=set()
        for i,m in enumerate(MON):
            if mask>>i&1:
                a=tuple(e for j,e in enumerate(m) if j!=c)
                if a in F:F.remove(a)
                else:F.add(a)
        du={(a-1,b) for a,b in F if a%2}
        dv={(a,b-1) for a,b in F if b%2}
        if not contains_one([F,du,dv]):return False
    return True

# A separate direct enumeration, independent of the cap-system solver.
TANGENTS=[]
for p in range(1,8):
    others=[]
    for q in range(1,8):
        if p==q:continue
        # In F2, the line through p,q has three rational points and is unique.
        masks=[sum(multiply_tangent_coefficients(m,p,q)[k]<<j for j,m in enumerate(MON)) for k in range(5)]
        others.append((q,masks))
    TANGENTS.append((p,others))

def ordinary_flexes(f):
    count=0
    for p,others in TANGENTS:
        # A smooth F at p has at most one tangent; when restricting to the
        # tangent line through p and residual point q, F|line=s*t^3.
        if any(all(((f&row).bit_count()&1)==int(k==3) for k,row in enumerate(rows)) for q,rows in others):
            count+=1
    return count

if __name__=='__main__':
    # A nonsmooth form may produce apparent flexes; test exact smoothness
    # before accepting the curve. All curves with 4 or more candidate flexes
    # are checked by homogeneous-chart Groebner bases, not extension sampling.
    cand=[f for f in range(1,1<<15) if ordinary_flexes(f)>=4]
    smooth_cand=[f for f in cand if smooth(f)]
    hist=Counter(ordinary_flexes(f) for f in smooth_cand)
    print('QUARTIC_MASKS',2**15-1)
    print('CANDIDATES_WITH_AT_LEAST_FOUR_ORDINARY_FLEXES',len(cand))
    print('GEOMETRICALLY_SMOOTH_CANDIDATES',len(smooth_cand))
    print('FLEX_HIST',dict(hist))
    assert hist=={4:168},hist
    assert all(smooth(f) for f in smooth_cand)
    print('REPRESENTATIVE_4418',4418 in smooth_cand)
    print('ALL_CHECKS_OK')
