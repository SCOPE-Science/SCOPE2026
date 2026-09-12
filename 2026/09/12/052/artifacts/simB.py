import numpy as np
# Balanced-style: mu_ext large, Jeff large (per-spike J*N), hold nu 5-15Hz. Brunel-like: N=5000 all-to-all impossible; use mean-field-matched single-pop with effective coupling.
# Use N=4000, J_psp=-0.15mV, Jeff=N*J=-600mV; mu_ext ~ 25-35.
def run(N=4000,T=1500.0,dt=0.05,mu_ext=28.0,sig=5.0,Jpsp=-0.15,Dmean=4.0,sigD=0.0,taus=2.0,seed=0):
    rng=np.random.default_rng(seed)
    tau_m=20.0; Vth=20.0; Vr=10.0; tref=2.0
    nT=int(T/dt)
    V=rng.uniform(Vr,Vth,N)
    I=np.zeros(N)
    ref=np.zeros(N)
    maxD=Dmean+10*max(sigD,0.01)+5
    nbuf=int(maxD/dt)+2
    buf=[[] for _ in range(nbuf)]
    step=0
    k=Dmean**2/max(sigD,1e-9)**2 if sigD>1e-9 else None
    th=sigD**2/Dmean if sigD>1e-9 else None
    pop=np.zeros(nT)
    sq=sig/np.sqrt(tau_m)*np.sqrt(dt)
    for t in range(nT):
        arr=buf[step%nbuf]
        if arr: I+=Jpsp*len(arr); buf[step%nbuf]=[]
        ref-=dt; ref[ref<0]=0
        active=ref<=0
        noise=rng.normal(size=N)*sq
        V[active]+= ((-(V[active])+mu_ext+I[active])/tau_m)*dt+noise[active]
        I-=I/taus*dt
        spk=np.where(active&(V>=Vth))[0]
        if len(spk)>0:
            pop[t]=len(spk); V[spk]=Vr; ref[spk]=tref
            if sigD<=1e-9:
                buf[(step+int(round(Dmean/dt)))%nbuf].extend([1]*len(spk))
            else:
                ds=rng.gamma(k,th,len(spk))
                for d in ds: buf[(step+int(round(d/dt)))%nbuf].append(1)
        step+=1
    return pop,dt
def spectrum(pop,dt):
    x=pop-np.mean(pop); w=np.hanning(len(x))
    X=np.fft.rfft(x*w); f=np.fft.rfftfreq(len(x),dt/1000.0)
    return f,np.abs(X)**2
import sys
mu_ext=float(sys.argv[1]) if len(sys.argv)>1 else 28.0
Jpsp=float(sys.argv[2]) if len(sys.argv)>2 else -0.15
sigDs=[float(s) for s in sys.argv[3:]] or [0.0,1.0,2.0,3.0]
for sigD in sigDs:
    pop,dt=run(mu_ext=mu_ext,Jpsp=Jpsp,sigD=sigD,T=1500.0,seed=2)
    rate=np.sum(pop)/(1.5)/4000.0
    f,P=spectrum(pop[int(300/0.05):],dt)
    base=np.median(P[(f>=30)&(f<=160)])
    for lo,hi in [(55,100),(30,50)]:
        m=(f>=lo)&(f<=hi); fpk=f[m][np.argmax(P[m])]
        print(f"sigD={sigD} rate={rate:.1f}Hz band[{lo},{hi}] peak={fpk:.1f}Hz xMed={np.max(P[m])/base:.2f}",flush=True)
    print("---",flush=True)
