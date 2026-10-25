#!/usr/bin/env python3
"""Reproducible finite-field rank certificate for an affine action on Paley-23 flag homology.
Pure Python 3; no external dependencies or network access needed.
"""
from itertools import combinations

P=23; A=2
RESIDUES={x*x%P for x in range(1,P)}
assert len(RESIDUES)==11 and 22 not in RESIDUES
assert pow(A,11,P)==1 and all(pow(A,i,P)!=1 for i in range(1,11))

def arrow(u,v): return (v-u)%P in RESIDUES

def transitive_append(face,v):
    for u,w in combinations(face,2):
        if (arrow(u,w) and arrow(w,v) and arrow(v,u)) or (arrow(w,u) and arrow(u,v) and arrow(v,w)):
            return False
    return True

F=[[(i,) for i in range(P)]]
while len(F[-1][0])<7:
    cur=[f+(v,) for f in F[-1] for v in range(f[-1]+1,P) if transitive_append(f,v)]
    if not cur: break
    F.append(cur)
assert [len(x) for x in F]==[23,253,1265,2530,1518]

# Canonical sorted-simplex orientation. The induced permutation sign is essential.
def image(face):
    w=[(A*v)%P for v in face]
    inv=sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
    return tuple(sorted(w)), (-1 if inv&1 else 1)

def make_orbits(faces):
    seen=set(); out=[]
    for face in faces:
        if face in seen: continue
        x=face; s=1; orb=[]
        while x not in seen:
            seen.add(x);orb.append((x,s))
            x,sgn=image(x);s*=sgn
        assert x==face and s==1 and len(orb) in (1,11)
        out.append(orb)
    return out
O=[make_orbits(f) for f in F]
assert [len(a) for a in O]==[3,23,115,230,138]
assert [sum(len(o)==1 for o in x) for x in O]==[1,0,0,0,0]

def columns_eigenspace(k,lam):
    rows=[o for o in O[k-1] if len(o)==11 or lam==1]
    cols=[o for o in O[k] if len(o)==11 or lam==1]
    targets={orb[0][0]:i for i,orb in enumerate(rows)}
    output=[]
    for orb in cols:
        # v=sum_j lam^(-j)* A^j(base), so A*v=lam*v
        values={}
        for j,(simplex,sgn) in enumerate(orb):
            weight=sgn*pow(lam,-j,P)
            for t in range(len(simplex)):
                f=simplex[:t]+simplex[t+1:]
                r=targets.get(f)
                if r is not None:
                    values[r]=(values.get(r,0)+(-1 if t&1 else 1)*weight)%P
        output.append({r:c for r,c in values.items() if c})
    return output,len(rows)

def rank_sparse(columns):
    piv={}
    for col in columns:
        cur=col.copy()
        while cur:
            lead=max(cur)
            if lead not in piv:
                inv=pow(cur[lead],-1,P)
                piv[lead]={r:(v*inv)%P for r,v in cur.items()}
                break
            scale=cur[lead]
            for r,v in piv[lead].items():
                new=(cur.get(r,0)-scale*v)%P
                if new:cur[r]=new
                else:cur.pop(r,None)
    return len(piv)

# Each distinct root of x^11-1 in F23 gives a semisimple eigenspace.
results=[]
for exponent in range(11):
    lam=pow(A,exponent,P)
    dims=[sum(len(o)==11 or lam==1 for o in q) for q in O]
    ranks=[0]
    for k in range(1,5):
        c,n=columns_eigenspace(k,lam)
        assert n==dims[k-1] and len(c)==dims[k]
        ranks.append(rank_sparse(c))
    betti=[dims[k]-ranks[k]-(ranks[k+1] if k<4 else 0) for k in range(5)]
    results.append((exponent,lam,dims,ranks,betti))
    print('j=%2d lambda=%2d ranks=%s H3=%d H4=%d'%(exponent,lam,ranks,betti[3],betti[4]))
expected=[]
for j in range(11):
    r4=133 if j in (0,10) else 134
    b3=3 if j in (0,10) else 2
    b4=5 if j in (0,10) else 4
    expected.append(([0,2,21,94,r4],b3,b4))
for (j,l,d,r,b),(r_expected,h3,h4) in zip(results,expected):
    assert r==r_expected and b[3]==h3 and b[4]==h4
    assert b[:3]==([1,0,0] if j==0 else [0,0,0])
assert sum(item[-1][3] for item in results)==24
assert sum(item[-1][4] for item in results)==46
assert sum(item[3][4] for item in results)==1472
print('VERIFY_OK: unique extra mod-23 H4 eigenvalue is 12 = 2^{-1} mod 23')

# Independent invariant-chain check in characteristic two.
# As 11 is invertible mod 2, the orbit-sum invariant chains compute invariants on H4(F2).
def rank_f2(cols):
    piv={}
    for col in cols:
        w=set(col)
        while w:
            h=max(w)
            if h in piv:w.symmetric_difference_update(piv[h])
            else:piv[h]=w;break
    return len(piv)
inv2=[0]
for k in range(1,5):
    rows={o[0][0]:i for i,o in enumerate(O[k-1])}
    cols=[]
    for orb in O[k]:
        touched=set()
        for face,_ in orb:
            for j in range(len(face)):
                row=rows.get(face[:j]+face[j+1:])
                if row is not None:
                    if row in touched:touched.remove(row)
                    else:touched.add(row)
        cols.append(touched)
    inv2.append(rank_f2(cols))
assert inv2==[0,2,21,94,133],inv2
assert len(O[4])-inv2[4]==5
print('CHAR2_OK: C11-invariant H4(F2) has dimension 5')
