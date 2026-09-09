"""Re-certify perturbed v2 instance: find_all + alpha + Krawczyk + separation + exact Q(i) dets."""
import sys,json; sys.path.insert(0,'.')
from fractions import Fraction as Q
import numpy as np
from build_solve import build_system, to_float, find_all, F_eval, J_eval
G=[[Q(s) for s in g] for g in json.load(open('narrow_groups_v2.json'))]
sysQ=build_system(G); const,lin,quad=sysQ
S=to_float(sysQ)
sols=find_all(S,nstarts=2000,seed=61)
print("n:",len(sols))
mags=[max(abs(v.imag) for v in x) for x in sols]
order=np.argsort(mags); sols=[sols[i] for i in order]; mags=[mags[i] for i in order]
print("imag:",[f"{m:.2e}" for m in mags])
# second seed confirm
sols2=find_all(S,nstarts=1500,seed=62)
m2=sorted(max(abs(v.imag) for v in x) for x in sols2)
print("seed62 n:",len(sols2),"imag:",[f"{m:.2e}" for m in m2])
DEN=10**12
class CQ:
    __slots__=("r","i")
    def __init__(s,r,i): s.r=r; s.i=i
    def __add__(s,o): return CQ(s.r+o.r,s.i+o.i)
    def __sub__(s,o): return CQ(s.r-o.r,s.i-o.i)
    def __mul__(s,o): return CQ(s.r*o.r-s.i*o.i, s.r*o.i+s.i*o.r)
    def __neg__(s): return CQ(-s.r,-s.i)
    def __truediv__(s,o):
        d=o.r*o.r+o.i*o.i; return CQ((s.r*o.r+s.i*o.i)/d,(s.i*o.r-s.r*o.i)/d)
    def __abs__(s): return float(s.r*s.r+s.i*s.i)**0.5
    def iszero(s): return s.r==0 and s.i==0
def csolve(A,b):
    n=len(A); M=[[A[i][j] for j in range(n)]+[b[i]] for i in range(n)]
    for c in range(n):
        piv=next((r for r in range(c,n) if not M[r][c].iszero()),None)
        if piv is None: raise ValueError("singular")
        M[c],M[piv]=M[piv],M[c]; pv=M[c][c]
        for r in range(n):
            if r!=c and not M[r][c].iszero():
                f=M[r][c]/pv
                for k in range(c,n+1): M[r][k]=M[r][k]-f*M[c][k]
    return [M[i][n]/M[i][i] for i in range(n)]
def cinv(A):
    n=len(A); I=[[CQ(Q(1),Q(0)) if i==j else CQ(Q(0),Q(0)) for j in range(n)] for i in range(n)]
    M=[list(A[i])+list(I[i]) for i in range(n)]
    for c in range(n):
        piv=next((r for r in range(c,n) if not M[r][c].iszero()),None)
        if piv is None: raise ValueError("singular")
        M[c],M[piv]=M[piv],M[c]; pv=M[c][c]
        for k in range(2*n): M[c][k]=M[c][k]/pv
        for r in range(n):
            if r!=c and not M[r][c].iszero():
                f=M[r][c]
                for k in range(2*n): M[r][k]=M[r][k]-f*M[c][k]
    return [row[n:] for row in M]
def cdet(A):
    n=len(A); M=[list(r) for r in A]; det=CQ(Q(1),Q(0)); sign=1
    for c in range(n):
        piv=next((r for r in range(c,n) if not M[r][c].iszero()),None)
        if piv is None: return CQ(Q(0),Q(0))
        if piv!=c: M[c],M[piv]=M[piv],M[c]; sign=-sign
        pv=M[c][c]; det=det*pv
        for r in range(c+1,n):
            if M[r][c].iszero(): continue
            f=M[r][c]/pv
            for k in range(c,n): M[r][k]=M[r][k]-f*M[c][k]
    return det if sign>0 else CQ(-det.r,-det.i)
def F_cq(m):
    out=[]
    for e in range(8):
        s=CQ(const[e],Q(0))
        for a in range(8):
            s=s+CQ(lin[e][a],Q(0))*m[a]
            for b in range(8): s=s+CQ(quad[e][a][b],Q(0))*m[a]*m[b]
        out.append(s)
    return out
def J_cq(m):
    J=[[None]*8 for _ in range(8)]
    for e in range(8):
        for c_ in range(8):
            s=CQ(lin[e][c_],Q(0))
            for a in range(8): s=s+CQ(quad[e][c_][a]+quad[e][a][c_],Q(0))*m[a]
            J[e][c_]=s
    return J
Sbound=max(sum(abs(quad[e][a][b]+quad[e][b][a])/2 for a in range(8) for b in range(8)) for e in range(8))
print("Sbound:",float(Sbound))
res=[]; okall=True
for idx,x in enumerate(sols):
    m=[CQ(Q(int(round(v.real*DEN)),DEN),Q(int(round(v.imag*DEN)),DEN)) for v in x]
    F=F_cq(m); J=J_cq(m); Ji=cinv(J)
    dx=csolve(J,[CQ(-f.r,-f.i) for f in F])
    beta=max(abs(z) for z in dx); g=max(sum(abs(z) for z in row) for row in Ji)*float(Sbound)
    alpha=beta*g; ok=alpha<0.157671; okall=okall and ok
    d=cdet(J)
    print(f"sol{idx}: beta={beta:.2e} gamma<={g:.2e} alpha<={alpha:.2e} cert={ok} detQ(i)!=0={not d.iszero()} imag={mags[idx]:.2e}",flush=True)
    res.append({"beta":beta,"gamma":g,"alpha":alpha,"imag":mags[idx],"det_nonzero":not d.iszero()})
print("ALL ALPHA:",okall, "ALL DET:", all(r["det_nonzero"] for r in res))
json.dump(res,open("alpha_narrow_v2.json","w"),indent=1)
dmin=min(max(abs(a-b)) for i,a in enumerate(sols) for b in sols[i+1:])
print("dmin:",dmin)
np.save("narrow_sols_v2.npy",np.array(sols))
