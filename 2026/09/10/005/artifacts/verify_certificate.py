"""Replayable certificate check for lane-496 PRESET FALLBACK (stdlib only).
Frozen: beta=4pi, L=beta-pi/2, phi flat cap, rho with rates (1,2).
Checks (i) M subset bW; (ii) closed-form Levi on M + kernel vector X1;
(iii) winding bidegree (1,2); (iv) coupled 2x2 psi-system coefficients nonzero.
Run: python3 output/artifacts/verify_certificate.py
"""
import cmath, math
L = 7*math.pi/2
def phi(t):
    s = abs(t)-L
    if s <= 0: return 0.0
    return math.exp(s-1/s)
def rho(z1,z2,w):
    t = math.log(abs(w)**2)
    a = cmath.exp(1j*t); b = cmath.exp(2j*t)
    return abs(z1-a)**2 + abs(z2-z1*b)**2 + phi(t) - 1
def toR(z1,z2,w): return [z1.real,z1.imag,z2.real,z2.imag,w.real,w.imag]
def fromR(v): return (v[0]+1j*v[1], v[2]+1j*v[3], v[4]+1j*v[5])
def rhof(v): return rho(*fromR(v))
def hessR(v):
    h=1e-5; H=[[0.0]*6 for _ in range(6)]; f0=rhof(v)
    for j in range(6):
        for k in range(j,6):
            vp=list(v); vm=list(v); v2=list(v); v3=list(v)
            vp[j]+=h; vp[k]+=h; vm[j]+=h; vm[k]-=h; v2[j]-=h; v2[k]+=h; v3[j]-=h; v3[k]-=h
            val=(rhof(vp)-rhof(vm)-rhof(v2)+rhof(v3))/(4*h*h)
            H[j][k]=val; H[k][j]=val
    return H
def gradR(v):
    h=1e-7; g=[0.0]*6
    for j in range(6):
        vp=list(v); vm=list(v); vp[j]+=h; vm[j]-=h
        g[j]=(rhof(vp)-rhof(vm))/(2*h)
    return g
def leviM(v):
    H=hessR(v); M=[[0j]*3 for _ in range(3)]
    for j in range(3):
        for k in range(3):
            jx,jy=2*j,2*j+1; kx,ky=2*k,2*k+1
            M[j][k]=(H[jx][kx]+H[jy][ky]+1j*(H[jx][ky]-H[jy][kx]))/4
    return M
def analytic_levi(w):
    t=math.log(abs(w)**2); a=cmath.exp(1j*t); b=cmath.exp(2j*t)
    return [[2,-b,1j*a.conjugate()/w.conjugate()],[-b.conjugate(),1,0],[-1j*a/w,0,0]]
ok=True
def check(name,cond,info=""):
    global ok
    print(("PASS " if cond else "FAIL ")+name+(" | "+str(info) if info else ""))
    if not cond: ok=False
print("== (i) M subset bW: rho(0,0,w)==phi(t)==0 ==")
for t0 in [0.0,2.0,-5.0,10.99,-10.99]:
    for th in [0.0,2.0]:
        w=cmath.exp(t0/2+1j*th)
        check(f"rho(0,0,w)=0 t0={t0}", abs(rho(0,0,w))<1e-12 and phi(t0)==0.0, rho(0,0,w))
        v=toR(0,0,w); g=gradR(v)
        t=math.log(abs(w)**2); a=cmath.exp(1j*t)
        cg=[complex((g[0]-1j*g[1])/2),complex((g[2]-1j*g[3])/2),complex((g[4]-1j*g[5])/2)]
        check(f"grad=(-abar,0,0) t0={t0}", abs(cg[0]+a.conjugate())<1e-6 and abs(cg[1])<1e-6 and abs(cg[2])<1e-6, [round(abs(c),2) for c in cg])
print("== (ii) Levi matrix + kernel X1=(0,0,1) ==")
for t0 in [0.0,2.0,-5.0,10.5]:
    for th in [0.0,2.0]:
        w=cmath.exp(t0/2+1j*th); v=toR(0,0,w)
        Mv=leviM(v); Av=analytic_levi(w)
        err=max(abs(Mv[j][k]-Av[j][k]) for j in range(3) for k in range(3))
        check(f"Levi closed form t0={t0} th={th}", err<5e-6, f"maxerr={err:.1e}")
        R=[[Mv[1][1],Mv[1][2]],[Mv[2][1],Mv[2][2]]]
        check(f"restricted block=diag(1,0)", abs(R[0][0]-1)<1e-4 and abs(R[0][1])<1e-4 and abs(R[1][0])<1e-4 and abs(R[1][1])<1e-4, [[f'{c:.2e}' for c in row] for row in R])
        g=gradR(v); cg3=complex((g[4]-1j*g[5])/2)
        RX1=[R[0][0]*0+R[0][1]*1, R[1][0]*0+R[1][1]*1]
        check(f"X1 tangential+restricted-kernel", abs(cg3)<1e-6 and abs(RX1[0])<1e-4 and abs(RX1[1])<1e-4, f"rho3={abs(cg3):.1e} R.X1={[f'{c:.1e}' for c in RX1]}")
print("== (iii) winding bidegree (1,2) ==")
N=20000; run1=0.0; run2=0.0; prev1=cmath.exp(1j*(-L)); prev2=cmath.exp(2j*(-L))
for k in range(1,N+1):
    t=-L+2*L*k/N; c1=cmath.exp(1j*t); c2=cmath.exp(2j*t)
    run1+=math.atan2((c1/prev1).imag,(c1/prev1).real); run2+=math.atan2((c2/prev2).imag,(c2/prev2).real)
    prev1,prev2=c1,c2
I1=run1/(2*L); I2=run2/(2*L)
check("rate integrals (1,2)", abs(I1-1)<1e-9 and abs(I2-2)<1e-9, f"I1={I1:.12f} I2={I2:.12f}; runs/2pi={[run1/(2*math.pi),run2/(2*math.pi)]}")
print("== (iv) coupled-system coupling coefficients: exact complex equalities ==")
for t0 in [0.0,2.0,-5.0,10.5]:
    for th in [0.0,0.7,2.0]:
        w=cmath.exp(t0/2+1j*th); t=math.log(abs(w)**2); a=cmath.exp(1j*t); b=cmath.exp(2j*t)
        Av=analytic_levi(w)
        c1=-a*Av[0][2]  # Hess(N0,X1), N0=-a d1, X1=d3
        c2=-a*Av[0][1]  # Hess(N0,X2), X2=d2
        e1=-1j/w.conjugate(); e2=a*b
        od=c1*e2.conjugate()
        check(f"exact c1=-i/conj(w), c2=a*b, off-diag nonzero t0={t0} th={th}",
              abs(c1-e1)<1e-9 and abs(c2-e2)<1e-9 and abs(od)>1e-12,
              f"|c1-e1|={abs(c1-e1):.1e} |c2-e2|={abs(c2-e2):.1e} |c1 conj(c2)|={abs(od):.4f}")
print("ALL VERIFY_OK" if ok else "VERIFY_FAILED")
