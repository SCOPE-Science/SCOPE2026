"""Exact integer certificate for two-point configurations on the octahedral graph.
Usage: python OCTAHEDRAL_CHECKER.py CERTIFICATE.json
Only Python's standard library is required.
"""
import json
import sys
from itertools import permutations, product

V = range(6)
E = [(a,b) for a in V for b in V if a<b and a//2 != b//2]
C0 = [(a,b) for a in V for b in V if a<b]
C1 = [(e,v) for e in E for v in V if v not in e]
C2 = [(e,f) for i,e in enumerate(E) for f in E[i+1:] if set(e).isdisjoint(f)]
I0={c:i for i,c in enumerate(C0)}
I1={c:i for i,c in enumerate(C1)}
I2={c:i for i,c in enumerate(C2)}
IE={e:i for i,e in enumerate(E)}

# Rows are oriented 1-cells and columns are oriented 2-cells.
B2=[[0]*len(C2) for _ in C1]
for j,((a,b),(c,d)) in enumerate(C2):
    for edge,vertex,coeff in [((c,d),b,+1),((c,d),a,-1),((a,b),d,-1),((a,b),c,+1)]:
        B2[I1[(edge,vertex)]][j]+=coeff

# The 1-skeleton of the cubical configuration complex is connected.
adj=[set() for _ in C0]
for (a,b),v in C1:
    u=I0[tuple(sorted((a,v)))]
    w=I0[tuple(sorted((b,v)))]
    adj[u].add(w);adj[w].add(u)
seen={0}; stack=[0]
while stack:
    for w in adj[stack.pop()]-seen:
        seen.add(w);stack.append(w)
assert len(seen)==len(C0)


def bareiss_det(a):
    a=[list(row) for row in a]
    n=len(a)
    if not n:return 1
    denom=1; sign=1
    for k in range(n-1):
        if a[k][k]==0:
            t=next((i for i in range(k+1,n) if a[i][k]),None)
            if t is None:return 0
            a[t],a[k]=a[k],a[t];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numer%denom==0
                a[i][j]=numer//denom
        for i in range(k+1,n):a[i][k]=0
        denom=pivot
    return sign*a[-1][-1]

with open(sys.argv[1],encoding='utf-8') as f: cert=json.load(f)
assert cert['cell_counts']==[15,48,30]
assert [len(C0),len(C1),len(C2)]==cert['cell_counts']
rows=cert['pivot_rows'];cols=cert['pivot_cols']
assert len(rows)==len(cols)==26 and len(set(rows))==26 and len(set(cols))==26
assert bareiss_det([[B2[i][j] for j in cols] for i in rows])==-1

Z=[]
for sparse in cert['kernel_generators']:
    z=[0]*len(C2)
    for index,coeff in sparse:
        assert 0<=index<len(C2) and z[index]==0 and coeff in [-1,1]
        z[index]=coeff
    assert all(sum(row[j]*z[j] for j in range(30))==0 for row in B2)
    Z.append(z)
free=[26,27,28,29]
assert len(Z)==4 and [[Z[j][i] for j in range(4)] for i in free]==[[int(i==j) for j in range(4)] for i in range(4)]
# The unimodular minor proves rank(B2)>=26; four independent nullcycles
# prove rank(B2)<=26. Connectivity gives rank(B1)=14.


def move_edge(e,p):
    endpoints=(p[e[0]],p[e[1]])
    return tuple(sorted(endpoints)), (1 if endpoints[0]<endpoints[1] else -1)


def signed_class(p):
    sigma=[p[2*i]//2 for i in range(3)]
    flips=[p[2*i]%2 for i in range(3)]
    seen=set(); positive=[];negative=[]
    for i in range(3):
        if i in seen:continue
        u=i;ell=0;twist=0
        while u not in seen:
            seen.add(u);ell+=1;twist^=flips[u];u=sigma[u]
        (negative if twist else positive).append(ell)
    return tuple(sorted(positive,reverse=True)),tuple(sorted(negative,reverse=True))


def permutation_sign(sigma):
    return -1 if sum(sigma[i]>sigma[j] for i in range(3) for j in range(i+1,3))%2 else 1

counts={};checks={}
sums=[0,0];rot_sums=[0,0]
for sigma in permutations(range(3)):
    for flips in product((0,1),repeat=3):
        p=tuple(2*sigma[i]+(u^flips[i]) for i in range(3) for u in range(2))
        determinant=permutation_sign(sigma)*(-1)**sum(flips)
        epsilon=(-1)**sum(flips)
        fixed_cube_corners=0
        for signs in product((0,1),repeat=3):
            image=[None]*3
            for i in range(3):image[sigma[i]]=signs[i]^flips[i]
            fixed_cube_corners+=(tuple(image)==signs)
        chi1_expected=determinant*fixed_cube_corners
        chi2_expected=epsilon+sum((-1)**flips[i] for i in range(3) if sigma[i]==i)
        # Cellular traces: C0 on unordered vertices, C1 oriented edges
        # with stationary vertices, and C2 products of disjoint edges.
        t0=sum(tuple(sorted([p[v] for v in q]))==q for q in C0)
        t1=sum(s if (e2,p[v])==(e,v) else 0
               for e,v in C1 for e2,s in [move_edge(e,p)])
        t2=0
        images=[]
        for e,f in C2:
            e2,se=move_edge(e,p);f2,sf=move_edge(f,p)
            s=se*sf
            if IE[e2]>IE[f2]:e2,f2=f2,e2;s=-s
            images.append((I2[(e2,f2)],s))
            if (e2,f2)==(e,f):t2+=s
        # Kernel coordinates are the four selected free columns.
        m=[[0]*4 for _ in range(4)]
        for j,z in enumerate(Z):
            transformed=[0]*30
            for c,coef in enumerate(z):
                if coef:
                    index,sgn=images[c]
                    transformed[index]+=sgn*coef
            for i,c in enumerate(free):m[i][j]=transformed[c]
            # Directly check that the action in the ambient cellular group
            # agrees with these four kernel coordinates.
            assert all(transformed[c]==sum(m[i][j]*Z[i][c] for i in range(4)) for c in range(30))
        chi2=sum(m[i][i] for i in range(4))
        chi1=1+chi2-t0+t1-t2   # Hopf trace identity
        assert (chi1,chi2)==(chi1_expected,chi2_expected),(p,chi1,chi2,chi1_expected,chi2_expected)
        cls=signed_class(p)
        counts[cls]=counts.get(cls,0)+1
        pair=(chi1,chi2)
        if cls in checks:assert checks[cls]==pair
        checks[cls]=pair
        sums[0]+=chi1;sums[1]+=chi2
        if determinant==1:rot_sums[0]+=chi1;rot_sums[1]+=chi2
assert len(counts)==10 and sum(counts.values())==48
assert sums==[0,0] and rot_sums==[24,0]
assert {str((a,b)):list(checks[a,b])+[counts[a,b]] for a,b in checks}==cert['signed_cycle_character_table']
print('OCTAHEDRAL_TWO_POINT_EQUIVARIANT_CERTIFICATE_OK')
print('chain_cells=15,48,30 boundary_ranks=14,26 homology_dimensions=1,8,4')
print('all_48_automorphisms=verified; rational_invariants_full=(1,0,0); rotations=(1,1,0)')
