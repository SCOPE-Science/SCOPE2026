"""Real Krawczyk r=1e-6 for the 12 real sols of narrow instance + exact det check."""
import sys,json; sys.path.insert(0,'.')
from fractions import Fraction as Q
import numpy as np
from build_solve import build_system, to_float, J_eval
G=[[Q(s) for s in g] for g in json.load(open('narrow_groups.json'))]
sysQ=build_system(G); const,lin,quad=sysQ
S=to_float(sysQ)
sols=np.load("narrow_sols.npy")
mags=np.array([max(abs(v.imag) for v in x) for x in sols])
order=np.argsort(mags); sols=sols[order]; mags=mags[order]
DEN=10**12
def krawczyk_real(m, r, Y):
    Blo=[mi-r for mi in m]; Bhi=[mi+r for mi in m]
    Fm=[const[e]+sum(lin[e][a]*m[a] for a in range(8))+sum(quad[e][a][b]*m[a]*m[b] for a in range(8) for b in range(8)) for e in range(8)]
    YFm=[sum(Y[i][k]*Fm[k] for k in range(8)) for i in range(8)]
    inside=True
    for i in range(8):
        clo=Q(0); chi=Q(0)
        for j in range(8):
            slo=Q(0); shi=Q(0)
            for k in range(8):
                Yik=Y[i][k]
                jlo=lin[k][j]; jhi=lin[k][j]
                for a in range(8):
                    c=quad[k][j][a]+quad[k][a][j]
                    if c>=0: jlo+=c*Blo[a]; jhi+=c*Bhi[a]
                    else: jlo+=c*Bhi[a]; jhi+=c*Blo[a]
                if Yik>=0: slo+=Yik*jlo; shi+=Yik*jhi
                else: slo+=Yik*jhi; shi+=Yik*jlo
            d=Q(1) if i==j else Q(0)
            Mlo=d-shi; Mhi=d-slo
            cands=[Mlo*(-r),Mlo*r,Mhi*(-r),Mhi*r]
            clo+=min(cands); chi+=max(cands)
        c=m[i]-YFm[i]
        if not (c+clo>m[i]-r and c+chi<m[i]+r): inside=False
    return inside
def det_frac(A):
    n=len(A); M=[list(r) for r in A]; det=Q(1)
    for c in range(n):
        piv=next((r for r in range(c,n) if M[r][c]!=0),None)
        if piv is None: return Q(0)
        if piv!=c: M[c],M[piv]=M[piv],M[c]; det=-det
        det*=M[c][c]; pv=M[c][c]
        for r in range(c+1,n):
            f=M[r][c]/pv
            for k in range(c,n): M[r][k]-=f*M[c][k]
    return det
okc=0
for i in range(12):
    x=sols[i]
    m=[Q(int(round(v.real*DEN)),DEN) for v in x]
    Jf=J_eval(S,np.array([float(v) for v in m]))
    Yf=np.linalg.inv(Jf)
    Y=[[Q(int(round(Yf[i,j]*10**12)),10**12) for j in range(8)] for i in range(8)]
    ok=krawczyk_real(m,Q(1,10**6),Y)
    # exact det
    J=[[lin[e][c]+sum(quad[e][c][a]*m[a]+quad[e][a][c]*m[a] for a in range(8)) for c in range(8)] for e in range(8)]
    d=det_frac(J)
    print(f"real{i}: Kraw {ok} det!=0 {d!=0} imag={mags[i]:.1e}")
    okc+=ok
print("kraw ok:",okc,"/12")
# exact dets for complex pair centers too
for i in [12,13]:
    x=sols[i]
    mr=[Q(int(round(v.real*DEN)),DEN) for v in x]; mi_=[Q(int(round(v.imag*DEN)),DEN) for v in x]
    print(f"sol{i}: re={ [float(v) for v in mr][:2]} immax={mags[i]:.3e}")
