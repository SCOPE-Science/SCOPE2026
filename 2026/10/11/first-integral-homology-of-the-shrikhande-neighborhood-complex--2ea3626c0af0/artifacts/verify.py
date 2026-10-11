#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V=[(i,j) for i in range(4) for j in range(4)]
idx={v:k for k,v in enumerate(V)}
S={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
adj=[]
for v in V:
    adj.append({idx[((v[0]+a)%4,(v[1]+b)%4)] for a,b in S})
assert all(len(N)==6 for N in adj)
for i in range(16):
    for j in range(i+1,16):
        assert len(adj[i]&adj[j])==2

faces=set()
for N in adj:
    N=sorted(N)
    for r in range(1,7):
        faces.update(combinations(N,r))
bydim={d:sorted(f for f in faces if len(f)==d+1) for d in range(6)}
fvec=[len(bydim[d]) for d in range(6)]
assert fvec==[16,120,320,240,96,16]
assert len(faces)==808

def boundary(d):
    lo,hi=bydim[d-1],bydim[d]
    pos={f:i for i,f in enumerate(lo)}
    M=sp.MutableSparseMatrix(len(lo),len(hi),{})
    for j,sig in enumerate(hi):
        for k in range(len(sig)):
            tau=sig[:k]+sig[k+1:]
            M[pos[tau],j]=1 if k%2==0 else -1
    return M

B=[None]+[boundary(d) for d in range(1,6)]
ranks=[None]+[B[d].rank() for d in range(1,6)]
assert ranks[1:]==[15,105,160,80,16]

# Since the 1-skeleton is K_16, the rooted triangle cycles
# c_{ij}=[i,j]-[0,j]+[0,i] (1<=i<j<=15) form an integral basis of ker(d_1).
# Express each 2-simplex boundary in this basis; coefficients are read from non-root edges.
basis=list(combinations(range(1,16),2))
pos={e:i for i,e in enumerate(basis)}
M=sp.zeros(len(basis),len(bydim[2]))
for j,t in enumerate(bydim[2]):
    a,b,c=t
    for e,coef in [((b,c),1),((a,c),-1),((a,b),1)]:
        if 0 not in e:
            M[pos[e],j]=coef
D=smith_normal_form(M,domain=ZZ)
diag=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]!=0]
assert Counter(diag)==Counter({1:104,2:1})
# Hence coker(M)=Z/2, exactly H_1 of the neighborhood complex.

# Rational homology ranks for context.
dims=fvec
betti_Q=[0]*6
betti_Q[0]=dims[0]-ranks[1]
for d in range(1,5):
    betti_Q[d]=dims[d]-ranks[d]-ranks[d+1]
betti_Q[5]=dims[5]-ranks[5]
assert betti_Q==[1,0,55,0,0,0]

# Independent field checks at small characteristics.
def rank_mod_p(A,p):
    m,n=A.rows,A.cols
    rows=[]
    for i in range(m):
        row={}
        for j in range(n):
            x=int(A[i,j])%p
            if x: row[j]=x
        rows.append(row)
    rank=0
    for c in range(n):
        piv=None
        for i in range(rank,m):
            if rows[i].get(c,0)%p:
                piv=i; break
        if piv is None: continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        inv=pow(rows[rank][c],-1,p)
        rows[rank]={j:(x*inv)%p for j,x in rows[rank].items() if (x*inv)%p}
        for i in range(m):
            if i==rank: continue
            q=rows[i].get(c,0)%p
            if not q: continue
            rr=dict(rows[i])
            for j,x in rows[rank].items():
                y=(rr.get(j,0)-q*x)%p
                if y: rr[j]=y
                elif j in rr: del rr[j]
            rows[i]=rr
        rank+=1
        if rank==m: break
    return rank
field_ranks={}
for p in (2,3,5):
    field_ranks[str(p)]=[rank_mod_p(B[d],p) for d in range(1,6)]
assert field_ranks['2']==[15,104,160,80,16]
assert field_ranks['3']==[15,105,160,80,16]
assert field_ranks['5']==[15,105,160,80,16]

print(json.dumps({
    'graph':'Shrikhande Cayley graph on Z4^2',
    'degree':6,
    'common_neighbors_each_distinct_pair':2,
    'nonempty_faces':808,
    'f_vector':fvec,
    'boundary_ranks_over_Q':ranks[1:],
    'triangle_boundary_snf_in_cycle_basis':{'1':104,'2':1},
    'H1_integral':'Z/2',
    'rational_betti':betti_Q,
    'boundary_ranks_mod_p':field_ranks,
    'status':'VERIFY_OK'
},sort_keys=True))
