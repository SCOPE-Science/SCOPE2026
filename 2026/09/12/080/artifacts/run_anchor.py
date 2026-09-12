import sys; sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1321/output/artifacts')
import numpy as np, json
from core import angles_to_qp,H,step,wdens
A=(0.840,0.842,1.918,1.782)
q0,p0=angles_to_qp(*A); print("anchor H0=%.4f w=%.2f"%(H(q0,p0),wdens(q0,p0)))
out={"anchor":{"th1":A[0],"th2":A[1],"w1":A[2],"w2":A[3],"H0":float(H(q0,p0)),"w":float(wdens(q0,p0))},"runs":[]}
for h in [0.01,0.005]:
    qq,pp=q0.copy(),p0.copy(); N=int(round(10.0/h)); mx=0.0; tw=0.0
    for k in range(N):
        qq,pp,mu,nu=step(qq,pp,h)
        tw+=float(np.linalg.norm(mu)+np.linalg.norm(nu)); mx=max(mx,float(np.linalg.norm(mu)+np.linalg.norm(nu)))
    dH=float(H(qq,pp)-H(q0,p0)); N3=N*h**3
    rec={"h":h,"N":N,"dH":dH,"absdH_over_h2":abs(dH)/h**2,"absdH_over_Nh3":abs(dH)/N3,
         "Nmax":N*mx,"C1eff":abs(dH)/(N*mx),"need_c1Nh3":400*N3,"need_C1Nmax":10*N*mx}
    out["runs"].append(rec); print(rec)
rng=np.random.default_rng(11)
ball=[]
for i in range(5):
    dth=rng.uniform(-0.03,0.03,2); dw=rng.uniform(-0.06,0.06,2)
    pt=(A[0]+dth[0],A[1]+dth[1],A[2]+dw[0],A[3]+dw[1])
    q,p=angles_to_qp(*pt); H0=H(q,p)
    if not(-12<=H0<=-8): continue
    qq,pp=q.copy(),p.copy(); h=0.005; N=int(round(10.0/h)); mx=0.0
    for k in range(N):
        qq,pp,mu,nu=step(qq,pp,h); mx=max(mx,float(np.linalg.norm(mu)+np.linalg.norm(nu)))
    dH=float(H(qq,pp)-H0)
    ball.append({"pt":[float(x) for x in pt],"H0":float(H0),"dH":dH,"adH_h2":abs(dH)/h**2,"C1eff":abs(dH)/(N*mx)})
    print(ball[-1])
out["ball"]=ball
json.dump(out,open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1321/output/artifacts/table_anchor.json','w'),indent=1)
print("saved")
