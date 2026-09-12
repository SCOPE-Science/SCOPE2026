import numpy as np
def run(N=4000,T=4000.0,dt=0.05,mu_ext=28.0,sig=5.0,Jpsp=-0.15,Dmean=4.0,sigD=0.0,taus=2.0,seed=3):
    rng=np.random.default_rng(seed)
    tau_m=20.0; Vth=20.0; Vr=10.0; tref=2.0
    nT=int(T/dt)
    V=rng.uniform(Vr,Vth,N); I=np.zeros(N); ref=np.zeros(N)
    maxD=Dmean+10*max(sigD,0.01)+5; nbuf=int(maxD/dt)+2
    buf=[[] for _ in range(nbuf)]; step=0
    k=Dmean**2/max(sigD,1e-9)**2 if sigD>1e-9 else None
    th=sigD**2/Dmean if sigD>1e-9 else None
    pop=np.zeros(nT); sq=sig/np.sqrt(tau_m)*np.sqrt(dt)
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
            if sigD<=1e-9: buf[(step+int(round(Dmean/dt)))%nbuf].extend([1]*len(spk))
            else:
                ds=rng.gamma(k,th,len(spk))
                for d in ds: buf[(step+int(round(d/dt)))%nbuf].append(1)
        step+=1
    return pop,dt
def spec(pop,dt):
    x=pop-np.mean(pop); w=np.hanning(len(x))
    X=np.fft.rfft(x*w); f=np.fft.rfftfreq(len(x),dt/1000.0)
    return f,np.abs(X)**2
import sys
ss=[float(s) for s in sys.argv[1:]] or [1.1]
for sigD in ss:
    pop,dt=run(sigD=sigD,seed=31)
    rate=np.sum(pop)/4.0/4000.0
    f,P=spec(pop[int(1000/0.05):],dt)
    med=np.median(P[(f>=30)&(f<=160)])
    m=(f>=55)&(f<=100); fpk=f[m][np.argmax(P[m])]
    # no-peak test: max in 30-120 vs high-f background 150-200? use median-based; also compare to 30-50 base
    base=np.median(P[(f>=30)&(f<=50)])
    print(f"sigD={sigD} rate={rate:.2f}Hz peak={fpk:.1f}Hz xMed={np.max(P[m])/med:.1f} xBase30-50={np.max(P[m])/base:.1f}",flush=True)
    # save spectrum
    np.savetxt(f"output/artifacts/spec_sig{int(sigD*100):d}.txt",np.column_stack([f,P]),header="freq_Hz power")
