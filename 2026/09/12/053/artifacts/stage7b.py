"""Stage 7b: refined spiking sims, dt=0.01ms, overshoot-carry reset, windowed PSD."""
import numpy as np, json
P = dict(tau=5.0, tauSE=2.0, tauSI=4.0, JEE=6.0, JII=-6.0, JEI=-20.0, JIE=8.0, etaE=1.0, etaI=-2.0)
S=2.0
def d_of(r): return S*r/(1+r), S/(1+r)

def sim(rho, NE=6000, NI=1500, T=2000.0, dt=0.01, seed=1, vp=100.0, vr=-100.0):
    rng = np.random.default_rng(seed)
    DE,DI = d_of(rho)
    etaE = np.clip(P['etaE'] + DE*np.tan(np.pi*(rng.random(NE)-0.5)),-150,150)
    etaI = np.clip(P['etaI'] + DI*np.tan(np.pi*(rng.random(NI)-0.5)),-150,150)
    VE = -10+rng.random(NE)*20; VI=-10+rng.random(NI)*20
    sE=0.035; sI=0.026
    tau=P['tau']
    nb=int(1.0/dt)  # 1ms bins
    n=int(T/dt)
    fr=[]; frI=[]
    ce=0; ci=0
    for i in range(n):
        IE = tau*(P['JEE']*sE+P['JEI']*sI); II = tau*(P['JIE']*sE+P['JII']*sI)
        VE += dt*(VE**2+etaE+IE)/tau
        VI += dt*(VI**2+etaI+II)/tau
        spE = VE>=vp; spI = VI>=vp
        VE[spE]=vr+(VE[spE]-vp); VI[spI]=vr+(VI[spI]-vp)
        ce += int(spE.sum()); ci += int(spI.sum())
        sE += dt*(-sE + spE.sum()/(NE*dt))/P['tauSE']
        sI += dt*(-sI + spI.sum()/(NI*dt))/P['tauSI']
        if (i+1)%nb==0:
            fr.append(ce/(NE*1e-3)); frI.append(ci/(NI*1e-3)); ce=0; ci=0
    fr=np.array(fr); frI=np.array(frI)
    cut=int(len(fr)*0.5)
    x=fr[cut:]-fr[cut:].mean(); xi=frI[cut:]-frI[cut:].mean()
    # windowed PSD: 500ms Hann segments, 50% overlap
    L=500; step=250; wins=[]
    for s in range(0,len(x)-L,step):
        w=np.hanning(L)
        wins.append(np.abs(np.fft.rfft((x[s:s+L]-x[s:s+L].mean())*w))**2)
    Ps=np.mean(wins,axis=0); fq=np.fft.rfftfreq(L,1e-3)
    winsI=[]
    for s in range(0,len(xi)-L,step):
        w=np.hanning(L)
        winsI.append(np.abs(np.fft.rfft((xi[s:s+L]-xi[s:s+L].mean())*w))**2)
    PsI=np.mean(winsI,axis=0)
    m=(fq>=5)&(fq<=150)
    fq=fq[m]; Ps=Ps[m]; PsI=PsI[m]
    g=(fq>=30)&(fq<=100); base=(fq>=5)&(fq<=15)
    return dict(rho=rho, meanE=float(fr[cut:].mean()), meanI=float(frI[cut:].mean()),
      stdE=float(x.std()), stdI=float(xi.std()),
      fE=float(fq[g][np.argmax(Ps[g])]),
      peakE=float(Ps[g].max()/Ps[base].max()), peakI=float(PsI[g].max()/PsI[base].max()),
      fq=fq.tolist(), psdE=Ps.tolist(), psdI=PsI.tolist())

for rho in [1.0, 4.0]:
    r=sim(rho)
    print(f"rho={rho} meanE={r['meanE']:.1f} meanI={r['meanI']:.1f} fE={r['fE']:.1f} peakE={r['peakRatioE'] if 'peakRatioE' in r else r['peakE']:.2f} peakI={r['peakI']:.2f} stdE={r['stdE']:.1f} stdI={r['stdI']:.1f}")
    json.dump(r, open(f"output/artifacts/spikeB_rho{rho:.1f}.json","w"))
