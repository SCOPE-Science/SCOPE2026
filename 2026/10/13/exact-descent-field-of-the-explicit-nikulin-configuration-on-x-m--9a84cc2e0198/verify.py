from itertools import combinations

# Gaussian integers a+bi.
def ga(z,w): return (z[0]+w[0],z[1]+w[1])
def gn(z): return (-z[0],-z[1])
def gm(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def gc(z): return (z[0],-z[1])
def gz(z): return z==(0,0)
ONE=(1,0); ZERO=(0,0); II=(0,1)
UNITS=[ONE,(-1,0),II,(0,-1)]
def ginv_unit(z): return gc(z)  # norm one

# R = Z[i][r]/(r^4-r^2-1); tuple coefficients of 1,r,r^2,r^3.
def ra(x,y): return tuple(ga(a,b) for a,b in zip(x,y))
def rn(x): return tuple(gn(a) for a in x)
def rz(x): return all(gz(a) for a in x)
def rfromg(z): return (z,ZERO,ZERO,ZERO)
def rpow1(): return (ZERO,ONE,ZERO,ZERO)
def rm(x,y):
    c=[ZERO]*7
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            c[i+j]=ga(c[i+j],gm(a,b))
    for k in range(6,3,-1):
        t=c[k]
        if not gz(t):
            c[k-2]=ga(c[k-2],t)
            c[k-4]=ga(c[k-4],t)
            c[k]=ZERO
    return tuple(c[:4])
def rci(x): return tuple(gc(a) for a in x)
def rsr(x): return tuple(a if j%2==0 else gn(a) for j,a in enumerate(x))
def req(x,y): return x==y

R0=rfromg(ZERO); R1=rfromg(ONE); RI=rfromg(II); RR=rpow1(); RPHI=rm(RR,RR)

def rscale_g(x,u): return tuple(gm(a,u) for a in x)

# Gaussian 6x6 matrix helpers.
def matmul(A,B):
    out=[]
    for i in range(6):
        row=[]
        for j in range(6):
            s=ZERO
            for k in range(6): s=ga(s,gm(A[i][k],B[k][j]))
            row.append(s)
        out.append(tuple(row))
    return tuple(out)
def eye6():
    return tuple(tuple(ONE if i==j else ZERO for j in range(6)) for i in range(6))
def canon_proj(A):
    first=next(z for row in A for z in row if not gz(z))
    u=ginv_unit(first)
    return tuple(tuple(gm(z,u) for z in row) for row in A)
def diag(vals):
    return tuple(tuple(vals[i] if i==j else ZERO for j in range(6)) for i in range(6))

g1=(
(ZERO,ZERO,ONE,ZERO,ZERO,ZERO),
(ZERO,ZERO,ZERO,ZERO,II,ZERO),
((-1,0),ZERO,ZERO,ZERO,ZERO,ZERO),
(ZERO,ZERO,ZERO,II,ZERO,ZERO),
(ZERO,II,ZERO,ZERO,ZERO,ZERO),
(ZERO,ZERO,ZERO,ZERO,ZERO,(0,-1)))
g2=(
(ZERO,ZERO,(0,-1),ZERO,ZERO,ZERO),
(ZERO,(0,-1),ZERO,ZERO,ZERO,ZERO),
((0,-1),ZERO,ZERO,ZERO,ZERO,ZERO),
(ZERO,ZERO,ZERO,ZERO,ZERO,(0,-1)),
(ZERO,ZERO,ZERO,ZERO,II,ZERO),
(ZERO,ZERO,ZERO,(0,-1),ZERO,ZERO))
g3=diag([ONE,ONE,ONE,(-1,0),ONE,(-1,0)])
g4=diag([ONE,(-1,0),ONE,(-1,0),(-1,0),(-1,0)])
GENS=[g1,g2,g3,g4]

# Projective subgroup A/mu_2.
G={canon_proj(eye6())}
front=list(G)
while front:
    a=front.pop()
    for b in GENS:
        c=canon_proj(matmul(a,b))
        if c not in G:
            G.add(c); front.append(c)
assert len(G)==16
G=sorted(G, key=repr)

# The three diagonal quadrics q1,q2,q3, using phi=r^2.
q1=[R1,R0,R0,R1,rn(RPHI),RPHI]
q2=[R0,R1,R0,rn(RPHI),R1,rn(RPHI)]
q3=[R0,R0,R1,RPHI,rn(RPHI),R1]
QS=[q1,q2,q3]

def q_transform_coeff(q,g):
    # q(g x), valid because g is monomial.
    out=[R0]*6
    for row in range(6):
        nz=[j for j,z in enumerate(g[row]) if not gz(z)]
        assert len(nz)==1
        j=nz[0]; u=g[row][j]
        out[j]=ra(out[j], rm(q[row], rfromg(gm(u,u))))
    return out

def in_qspan(v):
    lam=v[:3]
    target=[]
    for j in range(6):
        s=R0
        for k in range(3): s=ra(s,rm(lam[k],QS[k][j]))
        target.append(s)
    return all(req(a,b) for a,b in zip(v,target))
for g in GENS:
    for q in QS:
        assert in_qspan(q_transform_coeff(q,g))

# Plane P0 parametrization for C: x=(a,b,r*c,r*b,r*a,c).
P0=[
[R1,R0,R0],
[R0,R1,R0],
[R0,R0,RR],
[R0,RR,R0],
[RR,R0,R0],
[R0,R0,R1],
]

def g_times_P(g,P):
    out=[]
    for i in range(6):
        row=[]
        for j in range(3):
            s=R0
            for k in range(6): s=ra(s,rm(rfromg(g[i][k]),P[k][j]))
            row.append(s)
        out.append(row)
    return out

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    term1=rm(a, ra(rm(e,i), rn(rm(f,h))))
    term2=rm(b, ra(rm(d,i), rn(rm(f,g))))
    term3=rm(c, ra(rm(d,h), rn(rm(e,g))))
    return ra(ra(term1, rn(term2)), term3)
COMB=list(combinations(range(6),3))
def plucker(P): return tuple(det3([P[i] for i in J]) for J in COMB)

def same_proj(v,w):
    js=[j for j in range(len(v)) if not rz(v[j]) and not rz(w[j])]
    if not js: return False
    j=js[0]
    for k in range(len(v)):
        if not req(rm(v[k],w[j]),rm(w[k],v[j])): return False
    return True

planes=[plucker(g_times_P(g,P0)) for g in G]
for i in range(16):
    for j in range(i): assert not same_proj(planes[i],planes[j])

def image_vec(v,which):
    if which=='ci': return tuple(rci(x) for x in v)
    if which=='sr': return tuple(rsr(x) for x in v)
    if which=='both': return tuple(rci(rsr(x)) for x in v)
    raise ValueError

def action(which):
    p=[]
    for v in planes:
        vv=image_vec(v,which)
        hits=[j for j,w in enumerate(planes) if same_proj(vv,w)]
        p.append(hits)
    return p
aci=action('ci'); asr=action('sr'); ab=action('both')
assert all(len(h)==1 for h in aci)
perm=[h[0] for h in aci]
assert sorted(perm)==list(range(16))
assert all(len(h)==0 for h in asr)
assert all(len(h)==0 for h in ab)
fixed=sum(perm[i]==i for i in range(16))
trans=sum(i<perm[i] and perm[perm[i]]==i for i in range(16))
assert fixed==8 and trans==4

# Verify C lies on X: restrictions of q_i to P0 are scalar multiples of c=a^2-b^2-c^2.
# Since all q_i are diagonal, compute coefficients in a^2,b^2,c^2.
def restrict_diag(q,P):
    out=[R0,R0,R0]
    for xj in range(6):
        for a in range(3):
            if not rz(P[xj][a]):
                # P0 has one nonzero parameter per row, so no cross terms.
                out[a]=ra(out[a],rm(q[xj],rm(P[xj][a],P[xj][a])))
    return out
rest=[restrict_diag(q,P0) for q in QS]
base=[R1,rn(R1),rn(R1)]
# Scalar proportionality in the coefficient triple.
assert all(same_proj(tuple(v),tuple(base)) for v in rest)

# Field conclusions: Gal(L/K0)=<sr,ci>, K0=Q(sqrt5), r^2=phi.
# Stabilizer of unordered 16-set is exactly <ci>; fixed field is K0(r)=Q(r).
print('VERIFY_OK projective_A=16 planes=16 ci_fixed=8 ci_pairs=4 r_conjugate_overlap=0 both_overlap=0 config_field=Q(r) component_fields=8xQ(r)+8xQ(r,i) minpoly_r=r^4-r^2-1')
