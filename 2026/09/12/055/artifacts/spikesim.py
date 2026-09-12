"""Bruno-style LIF spiking sim (delayed exponential PSCs), vectorized per-pop.
 Current-based synapses, dt=0.1ms. Reports pop rates, PSD peak of total rate,
 E-I cross-correlation lag/phase. Safe to import (sim only under __main__).
"""
import numpy as np

def run_net(NE=4000, NI=1000, T=3000.0, dt=0.1,
            tau_mE=20.0, tau_mI=10.0, Vth=20.0, Vreset=10.0, Vrest=0.0,
            refE=2.0, refI=1.0,
            tauE=3.0, tauI=2.0, tauX=2.0,
            JEE=0.3, JIE=0.35, JEI=-1.2, JII=-1.0, JX=0.7,
            KEE=80, KIE=80, KEI=40, KII=40, KX=25, rateX_Hz=18.0, loop=1.0, r=1.0, Tstar=4.0, seed=0,
            burn=500.0):
    rng = np.random.default_rng(seed)
    JEIp = JEI*loop; JIEp = JIE*loop
    dEI = r*Tstar/(1+r); dIE = Tstar/(1+r)
    n = int(T/dt); nb = int(burn/dt)
    nE, nI = NE, NI
    connEE = rng.integers(0, nE, size=(nE, KEE))   # per E cell: KEE presyn E idx
    connEI = rng.integers(0, nI, size=(nE, KEI))   # per E cell: KEI presyn I idx
    connIE = rng.integers(0, nE, size=(nI, KIE))   # per I cell: KIE presyn E idx
    connII = rng.integers(0, nI, size=(nI, KII))   # per I cell: KII presyn I idx
    VE = rng.uniform(Vreset, Vth, nE); VI = rng.uniform(Vreset, Vth, nI)
    refcE = np.zeros(nE); refcI = np.zeros(nI)
    IE = np.zeros(nE); II = np.zeros(nI)
    lamX = rateX_Hz/1000.0*dt*KX
    dE = int(round(1.0/dt)); dI = int(round(1.0/dt))  # intra/EXT ~1ms
    bEI = int(round(dEI/dt)); bIE = int(round(dIE/dt))
    bufE = max(dE, bIE)+2; bufI = max(dI, bEI)+2
    qE = np.zeros((bufE, nE), dtype=np.bool_); qI = np.zeros((bufI, nI), dtype=np.bool_)
    axE = 1.0-np.exp(-dt/tauX); axI = axE
    aE = 1.0-np.exp(-dt/tauE); aI = 1.0-np.exp(-dt/tauI)
    # Conductance-like state s with <s> = tau * (total presyn rate): update
    #   s += a*(k*tau/dt - s), where k = spikes this step across the K inputs.
    # Then current I = J*s matches mean-field mu = C*J*tau*nu exactly (C=K).
    gX_E = tauX/dt; gX_I = tauX/dt; gE = tauE/dt; gI = tauI/dt
    sX = np.zeros(nE); sXI = np.zeros(nI); sEE = np.zeros(nE); sIE = np.zeros(nI)
    sEI = np.zeros(nE); sII = np.zeros(nI)
    e_busE = np.zeros(nE); e_busI = np.zeros(nE)
    rE = np.zeros(n, dtype=np.float32); rI = np.zeros(n, dtype=np.float32)
    decE = np.exp(-dt/tau_mE); decI = np.exp(-dt/tau_mI)
    for t in range(n):
        # external Poisson: counts across KX inputs per cell
        nXE = rng.poisson(lamX, nE); nXI = rng.poisson(lamX, nI)
        sX += axE*(nXE*gX_E - sX); sXI += axE*(nXI*gX_I - sXI)
        # delayed recurrent arrivals
        spE_EE = qE[(t-dE) % bufE]; spE_IE = qE[(t-bIE) % bufE]
        spI_EI = qI[(t-bEI) % bufI]; spI_II = qI[(t-dI) % bufI]
        e_busE[:] = 0.0; e_busI[:] = 0.0
        if spE_EE.any(): np.add.at(e_busE, connEE[spE_EE].ravel(), 1.0)
        # I->E: for each E cell, count how many of its presyn I cells fired
        if spI_EI.any():
            F = np.where(spI_EI)[0]
            hit = np.isin(connEI, F)
            e_busI[:] = hit.sum(axis=1)
        eb = np.zeros(nI); ib = np.zeros(nI)
        if spE_IE.any():
            F = np.where(spE_IE)[0]
            eb[:] = np.isin(connIE, F).sum(axis=1)
        if spI_II.any():
            F = np.where(spI_II)[0]
            ib[:] = np.isin(connII, F).sum(axis=1)
        sEE += aE*(e_busE*gE - sEE); sEI += aI*(e_busI*gI - sEI)
        sIE += aE*(eb*gE - sIE); sII += aI*(ib*gI - sII)
        IE = JX*sX + JEE*sEE + JEIp*sEI
        IIc = JX*sXI + JIEp*sIE + JII*sII
        VE = Vrest + (VE-Vrest)*decE + (IE)*(1.0-decE)
        VI = Vrest + (VI-Vrest)*decI + (IIc)*(1.0-decI)
        VE[refcE > 0] = Vreset; VI[refcI > 0] = Vreset
        refcE = np.maximum(0, refcE-dt); refcI = np.maximum(0, refcI-dt)
        fE = (VE >= Vth) & (refcE <= 0); fI = (VI >= Vth) & (refcI <= 0)
        VE[fE] = Vreset; VI[fI] = Vreset
        refcE[fE] = refE; refcI[fI] = refI
        qE[t % bufE] = fE; qI[t % bufI] = fI
        rE[t] = fE.sum(); rI[t] = fI.sum()
    return rE, rI, dt, nb, nE, nI

def axX_sub(cnt, a, s):
    # add Poisson-driven jumps: s += a*(cnt - s)? No: jump process: s += a*cnt then decay handled by s+=a*(bus-s) form.
    # Here handle as direct increments a*cnt.
    return a*cnt - 0.0*s

def analyze_trace(rE, rI, dt, nb, nE, nI, fmax=150.0):
    xE = (rE[nb:].astype(float)/nE/dt*1000.0); xI = (rI[nb:].astype(float)/nI/dt*1000.0)
    mE, mI = xE.mean(), xI.mean()
    xE -= mE; xI -= mI
    N = len(xE)
    dt_s = dt/1000.0
    S = np.abs(np.fft.rfft(xE+xI))**2
    f = np.fft.rfftfreq(N, dt_s)
    m = (f >= 15.0) & (f <= fmax)
    k = int(np.argmax(S[m])); idx = np.where(m)[0][k]
    fpk = float(f[idx])
    # band power ratio: peak bin vs median
    pr = float(S[idx]/np.median(S[m]))
    # E-I lag: cross-correlation
    xe = xE/np.std(xE); xi = xI/np.std(xI)
    cc = np.correlate(xi, xe, mode="full")
    lags = (np.arange(len(cc))-len(xe)+1)*dt
    ml = np.abs(lags) <= 50.0
    k2 = int(np.argmax(cc[ml])); lag = float(lags[ml][k2])
    # phase at fpk via FFT
    FE = np.fft.rfft(xE); FI = np.fft.rfft(xI)
    kk = int(np.argmin(np.abs(f-fpk)))
    ph = float(np.angle(FE[kk]/FI[kk]))
    return dict(rateE=mE, rateI=mI, fpk=fpk, peak_ratio=pr, lag_ms=lag, phase=ph)

if __name__ == "__main__":
    import sys, time
    t0 = time.time()
    loop = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    r = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    nue = float(sys.argv[4]) if len(sys.argv) > 4 else 18.0
    rE, rI, dt, nb, nE, nI = run_net(loop=loop, r=r, seed=seed, rateX_Hz=nue)
    a = analyze_trace(rE, rI, dt, nb, nE, nI)
    print(f"SIM loop={loop} r={r} seed={seed} nue={nue}: rateE={a['rateE']:.2f}Hz rateI={a['rateI']:.2f}Hz "
          f"fpk={a['fpk']:.1f}Hz peakratio={a['peak_ratio']:.1f} lag(E-I)={a['lag_ms']:+.2f}ms phase={a['phase']:+.3f}rad "
          f"t={time.time()-t0:.0f}s", flush=True)
