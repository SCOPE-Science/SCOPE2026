# Assembled replay verifier for the virial-gradient lock + quadratic gap.
# Rebuilds EVERYTHING from scratch (Q via Petviashvili, spectrum, unstable pair,
# Lyapunov-Perron 2nd order, lock + gap normal form, Prop-3 symplectic projection,
# Prop-4 exact localized virial) with consistent FD operators. stdlib+numpy only.
# Pass criteria: Pohozaev defect small; e0>0 real; QFaa=-12; lock ratios = K_Q;
# corrected gap2 in (0.5,2.0), stable across step sizes; Prop-3 k_c>g1 margin;
# Prop-4 R* rule + V''_R*>0 (no sign rescue) + R->inf recovers 8K-6P;
# direct (eps,a) grid EMPTY of {ME>1,G<1,Vpp<0}. Dumps consolidated_numbers.json.
import numpy as np, json

R=14.0; N=1400; h=R/N
r=(np.arange(N)+0.5)*h; w=4*np.pi*r**2*h
a=np.zeros(N); b=np.zeros(N); c=np.zeros(N)
for j in range(N):
    rj=r[j]; conv=(2.0/rj)/(2*h)
    b[j]=2.0/h**2+1.0
    cl=-1.0/h**2+conv; cr=-1.0/h**2-conv
    if j>0: a[j]=cl
    else: b[j]+=cl
    if j<N-1: c[j]=cr
s=1.0+1.0/R; alpha=(1.0-h*s/2.0)/(1.0+h*s/2.0)
b[N-1]+=c[N-1]*alpha; c[N-1]=0.0
def thomas(aa,bb,cc,d):
    n=len(d); cp=np.zeros(n); dp=np.zeros(n); x=np.zeros(n)
    cp[0]=cc[0]/bb[0]; dp[0]=d[0]/bb[0]
    for i in range(1,n):
        m=bb[i]-aa[i]*cp[i-1]; cp[i]=cc[i]/m if i<n-1 else 0.0; dp[i]=(d[i]-aa[i]*dp[i-1])/m
    x[n-1]=dp[n-1]
    for i in range(n-2,-1,-1): x[i]=dp[i]-cp[i]*x[i+1]
    return x
def L0(v):
    out=b*v.copy(); out[1:]+=a[1:]*v[:-1]; out[:-1]+=c[:-1]*v[1:]; return out
coarse=np.load("output/artifacts/Q_profile.npz"); Q=np.interp(r,coarse["r"],coarse["Q"])
for it in range(200):
    Lq=L0(Q); num=np.dot(Q*Lq,w); den=np.dot(Q,Q**3*w); M=num/den
    Qn=thomas(a,b,c,(M**1.5)*(Q**3))
    if np.max(np.abs(Qn-Q))/np.max(np.abs(Qn))<1e-13: Q=Qn; break
    Q=Qn
def Mof(u): return float(np.dot((u.real**2+u.imag**2),w))
def Kof(u): return float(np.dot(u.real,L0(u.real)*w)+np.dot(u.imag,L0(u.imag)*w))-Mof(u)
def Pof(u): return float(np.dot((np.abs(u)**2)**2,w))
M_Q=Mof(Q); K_Q=Kof(Q); P_Q=Pof(Q); E_Q=0.5*K_Q-0.25*P_Q; ME_Q=M_Q*E_Q
Lp=np.diag(b-3*Q**2)+np.diag(a[1:],-1)+np.diag(c[:-1],1)
Lm=np.diag(b-Q**2)+np.diag(a[1:],-1)+np.diag(c[:-1],1)
sq=np.sqrt(w)
Sp=(np.diag(sq)@Lp@np.diag(1/sq)); Sp=(Sp+Sp.T)/2
Sm=(np.diag(sq)@Lm@np.diag(1/sq)); Sm=(Sm+Sm.T)/2
ev,V=np.linalg.eig(-Sp@Sm)
assert np.max(np.abs(ev.imag))==0.0, "nonreal spectrum"
idx=np.argsort(ev.real); e0sq=ev[idx[-1]].real; e0=float(np.sqrt(e0sq))
avec=(V[:,idx[-1]].real)/sq; avec/=np.sqrt(np.dot(avec*avec,w))
bvec=-(Lp@avec)/e0
p,q=avec,bvec
F2r=-(Q*(3*p**2+q**2)); F2i=-(Q*2*p*q)
S=4*e0**2*np.eye(N)+Lm@Lp
P2=np.linalg.solve(S,2*e0*F2r+Lm@F2i); Q2=(F2i-Lp@P2)/(2*e0)
Y=p+1j*q; ZZ=P2+1j*Q2
def FH(aa,ee):
    u=(1+aa)*(Q+ee*Y+ee**2*ZZ)
    M=Mof(u); K=Kof(u); P=Pof(u)
    return 1-M*K/(M_Q*K_Q), 8*K-6*P
ok=True
def check(name,cond,val):
    global ok
    print(("PASS" if cond else "FAIL"),name,"=",val,flush=True)
    ok = ok and cond
check("pohozaev_K",abs(K_Q/(3*M_Q)-1)<5e-4,K_Q/(3*M_Q))
check("pohozaev_P",abs(P_Q/(4*M_Q)-1)<5e-4,P_Q/(4*M_Q))
check("e0_positive_real",e0>5.0 and e0<6.0,e0)
gaps=[]; g1s=[]; rec={}
rec.update({"M_Q":M_Q,"K_Q":K_Q,"P_Q":P_Q,"E_Q":E_Q,"e0":e0,
            "K_over_3M":K_Q/(3*M_Q),"P_over_4M":P_Q/(4*M_Q)})
for (ta,te) in [(2e-4,5e-3),(1e-4,2.5e-3)]:
    fA=(FH(ta,0)[0]-FH(-ta,0)[0])/(2*ta); fE=(FH(0,te)[0]-FH(0,-te)[0])/(2*te)
    hA=(FH(ta,0)[1]-FH(-ta,0)[1])/(2*ta); hE=(FH(0,te)[1]-FH(0,-te)[1])/(2*te)
    check(f"lock_A_ta{ta}",abs(hA/(4*fA)-K_Q)/K_Q<5e-4,hA/(4*fA))
    check(f"lock_E_te{te}",abs(hE/(4*fE)-K_Q)/K_Q<5e-4,hE/(4*fE))
    def d2(F,da,de): return (F(da,de)-F(da,-de)-F(-da,de)+F(-da,-de))/(4*da*de)
    def d2a(F,da): return (F(da,0)-2*F(0,0)+F(-da,0))/da**2
    def d2e(F,de): return (F(0,de)-2*F(0,0)+F(0,-de))/de**2
    Ff=lambda aa,ee: FH(aa,ee)[0]; Hf=lambda aa,ee: FH(aa,ee)[1]
    QFaa=d2a(Ff,ta); QFae=d2(Ff,ta,te); QFee=d2e(Ff,te)
    QHaa=d2a(Hf,ta); QHae=d2(Hf,ta,te); QHee=d2e(Hf,te)
    check(f"QFaa_exact-12_ta{ta}",abs(QFaa+12)<1e-2,QFaa)
    g1=-fE/fA; v1=-hE/hA
    check(f"linear_lock_g1v1_ta{ta}",abs(g1-v1)/abs(g1)<1e-3,(g1,v1))
    # corrected 2nd-order zero-curve coefficients (Taylor 1/2 factors on pure partials)
    g2=-(QFae*g1+0.5*QFee+0.5*g1**2*QFaa)/fA
    v2=-(QHae*v1+0.5*QHee+0.5*v1**2*QHaa)/hA
    gaps.append(v2-g2); g1s.append(g1)
    check(f"gap2_positive_ta{ta}",0.5<(v2-g2)<2.0,(g2,v2,v2-g2))
    rec[f"lock_ta{ta}"]={"fA":fA,"fE":fE,"hA":hA,"hE":hE,
        "hA_over_4fA":hA/(4*fA),"hE_over_4fE":hE/(4*fE)}
    rec[f"gap_ta{ta}"]={"g1":g1,"v1":v1,"g2":g2,"v2":v2,"gap2":v2-g2,"QFaa":QFaa}
check("gap2_stable",abs(gaps[0]-gaps[1])<0.05,gaps)
# ---- Prop 3: symplectic unstable projection; blowup-side slope vs G-crossing slope
LpP=Lp@p; bminus=LpP/e0
denom=2*np.dot(p*LpP,w)/e0
def lamq(aa,ee):
    u=(1+aa)*(Q+ee*Y+ee**2*ZZ)
    return (np.dot((u.real-Q)*bminus,w)+np.dot(u.imag*(-p),w))/denom
tl=1e-4
dlamA=(lamq(tl,0)-lamq(-tl,0))/(2*tl); dlamE=(lamq(0,tl)-lamq(0,-tl))/(2*tl)
kc=-dlamE/dlamA
check("dlam_deps_unity",abs(dlamE-1.0)<0.05,dlamE)
check("dlam_da_negative",dlamA<-1.0,dlamA)
check("kc_exceeds_g1",kc>g1s[0]+0.2,(kc,g1s[0]))
rec["prop3"]={"dlam_da":dlamA,"dlam_deps":dlamE,"k_c":kc,"g1_ref":g1s[0]}
# ---- Prop 4: exact Holmer-Roudenko localized virial, rule R*, R->inf check
# C^4 cutoff: zeta=s^2 (s<=1), 3 (s>=2), degree-9 smooth-step blend; analytic derivs.
chi=np.zeros(10); chi[5]=126.; chi[6]=-420.; chi[7]=540.; chi[8]=-315.; chi[9]=70.
s1=np.array([1.,1.]); s2=np.convolve(s1,s1)
one11=np.array([1.]+[0.]*11); chi11=np.pad(chi,(0,2))
zeta_t=np.convolve(s2,one11-chi11)+3.0*np.pad(chi11,(0,2))
def pder(c): return np.array([k*c[k] for k in range(1,len(c))])
zt1=pder(zeta_t); zt2=pder(zt1); zt3=pder(zt2); zt4=pder(zt3)
def pval(c,t):
    t=np.asarray(t,dtype=float); res=np.zeros_like(t); pw=np.ones_like(t)
    for k in range(len(c)): res+=c[k]*pw; pw*=t
    return res
NZ=20001; sg=np.linspace(0,4,NZ)
z2g=np.zeros(NZ); zLg=np.zeros(NZ); zBg=np.zeros(NZ)
m1=sg<=1; z2g[m1]=2.0; zLg[m1]=6.0
m2=(sg>1)&(sg<2); tt=sg[m2]-1; ss=sg[m2]
d1=pval(zt1,tt); d2=pval(zt2,tt); d3=pval(zt3,tt); d4=pval(zt4,tt)
z2g[m2]=d2; zLg[m2]=d2+2*d1/ss
dLp=d3+2*(d2/ss-d1/ss**2)
dLpp=d4+2*(d3/ss-2*d2/ss**2+2*d1/ss**3)
zBg[m2]=dLpp+2*dLp/ss
def VppR(u,R):
    sc=r/R
    gu2=np.gradient(u.real,h)**2+np.gradient(u.imag,h)**2
    rho2=u.real**2+u.imag**2; rho4=rho2**2
    t1=4*float(np.dot(np.interp(sc,sg,z2g)*gu2,w))
    t2=float(np.dot(np.interp(sc,sg,zBg)*rho2,w))/R**2
    t3=float(np.dot(np.interp(sc,sg,zLg)*rho4,w))
    return t1-t2-t3
veps=0.02
vv=Q+veps*Y+veps**2*ZZ
P0=8*Kof(vv)-6*Pof(vv)
thr=abs(P0)/16
Rs=np.linspace(0.5,12,231); rhoQ=Q**2
ext=np.array([float(np.dot(rhoQ[r>R_],w[r>R_])) for R_ in Rs])
Rstar=float(Rs[np.where(ext<=thr)[0][0]])
full=8*Kof(vv)-6*Pof(vv)
vRs=VppR(vv,Rstar); vInf=VppR(vv,14.0)
check("Rstar_rule",2.0<Rstar<3.5,Rstar)
check("VppRstar_positive",vRs>1.0,(vRs,full))
check("VppRstar_no_sign_rescue",abs(vRs-full)<1.0,(vRs,full))
check("VppR_inf_recovers_full",abs(vInf-full)/abs(full)<0.02,vInf)
rec["prop4"]={"eps":veps,"P0":P0,"Rstar":Rstar,"VppRstar":vRs,"full_Vpp":full,"VppR_inf":vInf}
GG=np.sqrt(M_Q*K_Q); hits=0
for eps in [0.01,0.015,0.02,0.025,0.03,0.04]:
    for av in [0.0,0.002,0.004,0.006,0.008,0.010]:
        u=(1+av)*(Q+eps*Y+eps**2*ZZ)
        M=Mof(u); K=Kof(u); P=Pof(u); E=0.5*K-0.25*P
        if (M*E/ME_Q-1>0) and (np.sqrt(M*K)/GG<1) and (8*K-6*P<0): hits+=1
check("grid_empty_norogue_triple",hits==0,hits)
# audit-plan orientation: truncated/full virial velocity V'(0)>=0 on eps>0 branch
u0=Q+0.02*Y+0.02**2*ZZ
ur0=np.gradient(u0.real,h)+1j*np.gradient(u0.imag,h)
Vp0=4*float(np.dot((np.conj(u0)*(r*ur0)).imag,w))
check("Vp_orientation_positive",Vp0>0.3,Vp0)
rec["Vp_eps002"]=Vp0
json.dump(rec,open("output/artifacts/consolidated_numbers.json","w"),indent=1)
print("VERIFY_OK" if ok else "VERIFY_FAIL")
