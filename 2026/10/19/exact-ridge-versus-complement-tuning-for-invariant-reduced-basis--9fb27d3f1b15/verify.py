"""Independent finite arithmetic checks for invariant-space spectral tuning."""
import numpy as np

rng = np.random.default_rng(20260910)
count = 0
for j in range(3000):
    k = int(rng.integers(1, 6))
    m = int(rng.integers(1, 6))
    selected = np.exp(rng.uniform(-4, 4, size=k))
    omitted = np.exp(rng.uniform(-4, 4, size=m))
    if j % 5 == 0:
        selected[:] = selected[0]
    if j % 7 == 0:
        omitted[:] = omitted[0]
    a, b = min(selected), max(selected)
    c, d = min(omitted), max(omitted)
    A = np.diag(np.r_[selected, omitted])
    S = np.diag(np.r_[1 / selected, np.zeros(m)])
    PP = np.diag(np.r_[np.ones(k), np.zeros(m)])
    candidate_s = [1e-12, 1e12, max(c-a, 1e-12), max(d-b, 1e-12)]
    candidate_s += [float(np.exp(rng.uniform(-9, 9))) for _ in range(8)]
    optimal = max(b,d)/c if c <= a else max(d,b+c-a)/c
    for s in candidate_s:
        alpha = 1/s
        BI = S + alpha*np.eye(k+m)
        BII = S + alpha*(np.eye(k+m)-PP)
        eigenI = np.linalg.eigvalsh((np.sqrt(BI)@A@np.sqrt(BI)))
        eigenII = np.linalg.eigvalsh((np.sqrt(BII)@A@np.sqrt(BII)))
        kI = eigenI[-1]/eigenI[0]
        kII = eigenII[-1]/eigenII[0]
        fI = max(b+s, d)/min(a+s,c)
        fII = max(1,alpha*d)/min(1,alpha*c)
        assert np.isclose(kI,fI,atol=1e-6,rtol=5e-8), (kI,fI)
        assert np.isclose(kII,fII,atol=1e-6,rtol=5e-8), (kII,fII)
        assert fI >= optimal - 1e-7*max(1,optimal), (fI,optimal)
        assert fII >= d/c - 1e-7*max(1,d/c)
        count += 4
    if c > a:
        sstar = c-a
        assert np.isclose(max(b+sstar,d)/min(a+sstar,c),optimal)
    for alpha in [1/d,1/c]:
        val = max(1,alpha*d)/min(1,alpha*c)
        assert np.isclose(val,d/c)
    count += 3
for K in [2,5,10,100,10000]:
    for alpha in [0.001,0.1,1,10,1000]:
        assert (1+alpha*K)/alpha > K
    assert np.isclose(max(1,1)/min(1,1),1)
    count += 6
print(f"PASS {count} deterministic comparisons")
