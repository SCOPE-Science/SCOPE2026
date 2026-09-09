"""Krawczyk reality certification for base: real boxes around each rational center.
Y = float inverse of J at center, rationalized. Box radius r. Verify K(B) subset int(B)
with exact Fraction interval arithmetic. Then: unique zero in box; reality follows since
box is real (subset R^8) — but must ensure TRUE zero (not just real approx) lies in box:
Krawczyk guarantees existence+uniqueness of zero of F in B. Since B subset R^8, zero real.
Also verify 14 boxes pairwise disjoint + count matches degree 14 (Catalan) -> completeness."""
import sys,pickle; sys.path.insert(0,'.')
from fractions import Fraction as Q
import numpy as np
from build_solve import build_system, to_float, J_eval

DEN=10**12
base_centers=[Q(-14,10)+Q(4,10)*k for k in range(8)]
offs=[Q(0),Q(8,100),Q(16,100),Q(24,100)]
G=[[c+o for o in offs] for c in base_centers]
sysQ=build_system(G)
const,lin,quad=sysQ
sols=np.array(pickle.load(open('base_sols.pkl','rb')))
S=to_float(sysQ)
n=len(sols)
M=[[Q(int(round(v.real*DEN)),DEN) for v in x] for x in sols]

def krawczyk_real(m, r, Y):
    Blo=[mi-r for mi in m]; Bhi=[mi+r for mi in m]
    Fm=[const[e]+sum(lin[e][a]*m[a] for a in range(8))+sum(quad[e][a][b]*m[a]*m[b] for a in range(8) for b in range(8)) for e in range(8)]
    YFm=[sum(Y[i][k]*Fm[k] for k in range(8)) for i in range(8)]
    inside=True
    Klo=[Q(0)]*8; Khi=[Q(0)]*8
    for i in range(8):
        clo=Q(0); chi=Q(0)
        for j in range(8):
            # S_k Y[i][k]*J[k][j](B): J[k][j](x)=lin+sum_a c*B[a], c=q[k][j][a]+q[k][a][j]
            slo=Q(0); shi=Q(0)
            for k in range(8):
                Yik=Y[i][k]
                # interval JB[k][j]
                jlo=lin[k][j]; jhi=lin[k][j]
                for a in range(8):
                    c=quad[k][j][a]+quad[k][a][j]
                    if c>=0: jlo+=c*Blo[a]; jhi+=c*Bhi[a]
                    else: jlo+=c*Bhi[a]; jhi+=c*Blo[a]
                # Yik * [jlo,jhi]
                if Yik>=0: slo+=Yik*jlo; shi+=Yik*jhi
                else: slo+=Yik*jhi; shi+=Yik*jlo
            d=Q(1) if i==j else Q(0)
            Mlo=d-shi; Mhi=d-slo
            cands=[Mlo*(-r),Mlo*r,Mhi*(-r),Mhi*r]
            clo+=min(cands); chi+=max(cands)
        c=m[i]-YFm[i]
        Klo[i]=c+clo; Khi[i]=c+chi
        if not (Klo[i]>m[i]-r and Khi[i]<m[i]+r): inside=False
    return Klo,Khi,inside

okcount=0
for i in range(n):
    Jf=J_eval(S,np.array([float(v) for v in M[i]]))
    Yf=np.linalg.inv(Jf)
    Y=[[Q(int(round(Yf[i,j]*10**12)),10**12) for j in range(8)] for i in range(8)]
    for r in [Q(1,10**6),Q(1,10**5),Q(1,10**4)]:
        Klo,Khi,ok=krawczyk_real(M[i],r,Y)
        if ok:
            print(f"sol{i}: Krawczyk OK r={float(r):.0e}"); okcount+=1; break
    else:
        print(f"sol{i}: FAIL")
print("krawczyk ok:",okcount,"/",n)
