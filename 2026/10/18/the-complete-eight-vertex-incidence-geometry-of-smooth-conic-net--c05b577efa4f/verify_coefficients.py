#!/usr/bin/env python3
"""Exact binary coefficient-space verification of smooth conic nets."""
from itertools import combinations,product
from collections import Counter

def smooth(m):
    a,b,c,d,e,f=((m>>i)&1 for i in range(6))
    return bool(a*f ^ b*e ^ c*d ^ d*e*f)

def span(vs):
    s={0}
    for v in vs:
        s|={v^w for w in tuple(s)}
    return frozenset(s)

def graph(alpha,beta,gamma):
    forms=[]
    for d,e,f in product(range(2),repeat=3):
        a=alpha*d ^ beta*e ^ f
        b=gamma*d ^ e ^ (1^beta)*f
        c=d ^ (1^gamma)*e ^ (1^alpha)*f
        forms.append(sum(bit<<i for i,bit in enumerate((a,b,c,d,e,f))))
    return frozenset(forms)

smooths={m for m in range(1,64) if smooth(m)}
assert len(smooths)==28
nets={graph(a,b,c) for a,b,c in product(range(2), repeat=3)}
assert len(nets)==8 and all(len(N)==8 and all(smooth(x) for x in N if x) for N in nets)
pencils={span((u,v)) for u,v in combinations(sorted(smooths),2) if smooth(u^v)}
assert len(pencils)==56 and all(len(P)==4 for P in pencils)
assert all(sum(P<=N for N in nets)==1 for P in pencils)
assert all(sum(c in N for N in nets)==2 for c in smooths)
assert all(len((A & B)-{0})==1 for A,B in combinations(nets,2))
assert all(not any(all(smooth(v^u) for u in N) for v in range(1,64) if v not in N) for N in nets)

# Generate all invertible 3x3 matrices over F2. Rows are bit masks.
def rank3(rows):
    a=list(rows);r=0
    for bit in range(3):
        k=next((j for j in range(r,3) if (a[j]>>bit)&1),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        for j in range(3):
            if j!=r and (a[j]>>bit)&1:a[j]^=a[r]
        r+=1
    return r==3
mats=[r for r in product(range(8),repeat=3) if rank3(r)]
assert len(mats)==168
# Apply variable substitution X,Y,Z -> linear forms in X,Y,Z.
monomials=[(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
def eval_poly(mask, v):
    return sum(((mask>>i)&1)*int(all(((v>>k)&1) or exponent==0 for k,exponent in enumerate(m))) for i,m in enumerate(monomials))%2
pts=list(range(1,8))
# reconstruct coefficient vector from seven F2 evaluations, augmented by formal polynomial arithmetic

def mul_linear(A,B):
    co=[0]*6
    for i in range(3):
      for j in range(3):
        if (A>>i)&1 and (B>>j)&1:
          e=[0,0,0];e[i]+=1;e[j]+=1
          co[monomials.index(tuple(e))]^=1
    return sum(b<<i for i,b in enumerate(co))

def transform(q,rows):
    a,b,c,d,e,f=((q>>i)&1 for i in range(6))
    xs=[mul_linear(rows[i],rows[j]) for i,j in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]]
    out=0
    for i,t in enumerate(xs):
        if(q>>i)&1:out^=t
    return out
N0=next(iter(nets))
transformed={frozenset(transform(q,R) for q in N0) for R in mats}
assert transformed==nets
stab=sum(frozenset(transform(q,R) for q in N0)==N0 for R in mats)
assert stab==21
print('smooth_conics',len(smooths))
print('all_smooth_pencils',len(pencils))
print('all_smooth_nets',len(nets))
print('pairwise_net_intersection_conics',Counter(len((A&B)-{0}) for A,B in combinations(nets,2)))
print('conic_net_multiplicity',Counter(sum(x in N for N in nets) for x in smooths))
print('pencil_net_multiplicity',Counter(sum(P<=N for N in nets) for P in pencils))
print('PGL3_order',len(mats))
print('net_orbit_size',len(transformed))
print('net_stabilizer_order',stab)
assert graph(0,0,0)==span((12,22,39))
print('representative_basis_decimal',(12,22,39))
