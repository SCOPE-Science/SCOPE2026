"""Unify: build single replayable verifier verify_F0.py printing all four fallback logs.
Reuse exact routines; assert all values. Keep runtime moderate (~2-4 min)."""
import sympy as sp
import numpy as np
X,Y,Z=sp.symbols('X Y Z')
vars3=[X,Y,Z]
F0=X**7+Y**7+Z**7+X**3*Y**2*Z**2
D=7
print("F0 =",F0)
def exps(deg):
    out=[]
    def rec(i,rem,cur):
        if i==2: out.append(tuple(cur+[rem])); return
        for e in range(rem+1): rec(i+1,rem-e,cur+[e])
    rec(0,deg,[]); return out
def diff_act(op,F):
    g=F
    for _ in range(op[0]): g=sp.diff(g,X)
    for _ in range(op[1]): g=sp.diff(g,Y)
    for _ in range(op[2]): g=sp.diff(g,Z)
    return sp.expand(g)
# (0) HF
HF=[]
for d in range(8):
    ops=exps(d); tgt=exps(D-d)
    rows=[]
    for op in ops:
        g=diff_act(op,F0); P=sp.Poly(g,vars3); dd=P.as_dict() if P is not None else {}
        rows.append([sp.Rational(dd.get(e,0)) for e in tgt])
    HF.append(sp.Matrix(rows).rank())
print("HilbertFunction =", HF)
assert HF==[1,3,6,10,10,6,3,1], "HF FAIL"
# (i) Hess^2 factored
ops2=exps(2)
H2=sp.zeros(6)
for i,a in enumerate(ops2):
    for j,b in enumerate(ops2):
        H2[i,j]=diff_act((a[0]+b[0],a[1]+b[1],a[2]+b[2]),F0)
det2=sp.expand(H2.det())
assert det2!=0
print("Hess2_factored =", sp.factor(det2))
# (ii)+(iii) mult + rank + Jordan at L=x+2y+3z
def cat_mat(d):
    ops=exps(d); tgt=exps(D-d)
    M=sp.zeros(len(tgt),len(ops))
    for j,op in enumerate(ops):
        g=diff_act(op,F0); P=sp.Poly(g,vars3); dd=P.as_dict() if P is not None else {}
        for i,e in enumerate(tgt): M[i,j]=sp.Rational(dd.get(e,0))
    return M,ops
h=HF; Qb={}; Pr={}
for d in range(8):
    M,ops=cat_mat(d)
    chosen=[]; cr=0
    for j in range(len(ops)):
        if M[:,chosen+[j]].rank()>cr: chosen.append(j); cr+=1
    Qb[d]=[ops[j] for j in chosen]
    Pr[d]=(M[:,chosen].T*M[:,chosen]).inv()*M[:,chosen].T
offs=[]; s=0
for d in range(8): offs.append(s); s+=h[d]
N=s; Mx=sp.zeros(N); My=sp.zeros(N); Mz=sp.zeros(N)
for d in range(7):
    tgtops=exps(d+1); Mind,_=cat_mat(d+1)
    for k,m in enumerate(Qb[d]):
        for sh,Mm in [((1,0,0),Mx),((0,1,0),My),((0,0,1),Mz)]:
            me=(m[0]+sh[0],m[1]+sh[1],m[2]+sh[2])
            v=sp.zeros(len(tgtops),1); v[tgtops.index(me),0]=1
            c=Pr[d+1]*(Mind*v)
            for r2 in range(h[d+1]): Mm[offs[d+1]+r2,offs[d]+k]=c[r2]
print("L = x+2y+3z")
ML=Mx+2*My+3*Mz
prof=[]
for d in range(7):
    B=ML[offs[d+1]:offs[d+1]+h[d+1], offs[d]:offs[d]+h[d]]
    prof.append((B.rows,B.cols,B.rank()))
print("rank_profile =", prof)
Bmid=ML[offs[4]:offs[4]+10, offs[3]:offs[3]+10]
print("mid_block det =", Bmid.det(), " rank =", Bmid.rank())
assert Bmid.rank()==10
P=sp.eye(N); nulls=[0]
for k in range(1,10):
    P=P*ML; nk=N-P.rank(); nulls.append(nk)
print("ker_dims =", nulls)
dks=[nulls[k]-nulls[k-1] for k in range(1,len(nulls))]
part=[]
for k in range(1,len(dks)):
    part.extend([k]*(dks[k-1]-dks[k]))
part.sort(reverse=True)
print("Jordan =", part)
assert sum(part)==40 and part==[8,6,6,4,4,4,2,2,2,2]
# (iv) minimal generator degrees + BE comparison
Md={}; Ed={}; ker={}; dimI={}
for d in range(0,8):
    E=exps(d); Ed[d]=E
    M,_=cat_mat(d); Md[d]=M
    K=M.nullspace(); ker[d]=K; dimI[d]=len(K)
E1s=[(1,0,0),(0,1,0),(0,0,1)]
mus={}
for d in range(1,8):
    E=Ed[d]; idx={e:j for j,e in enumerate(E)}
    vecs=[]
    for v in ker[d-1]:
        co=list(v); Ep=Ed[d-1]
        for s in E1s:
            w=[sp.Rational(0)]*len(E)
            for c,e in zip(co,Ep):
                ne=(e[0]+s[0],e[1]+s[1],e[2]+s[2])
                if ne in idx: w[idx[ne]]+=c
            vecs.append(w)
    r=sp.Matrix(vecs).rank() if vecs else 0
    mus[d]=dimI[d]-r
print("ann_dims =", dimI)
print("gen_degs mu =", mus)
assert mus[4]==5 and mus[5]==2 and all(mus[d]==0 for d in [1,2,3,6,7])
print("BE_compare: 5 quartic gens => 5x5-pfaffian count; +2 quintic gens => total 7, "
      "7x7-pfaffian count; table is 5+2 (mixed), neither pure 5x5 (0 quintics) nor pure 7x7 (7 quartics).")
print("VERIFY_OK")
