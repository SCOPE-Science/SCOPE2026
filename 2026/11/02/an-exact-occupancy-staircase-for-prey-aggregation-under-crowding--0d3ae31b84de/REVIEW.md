# Independent mathematical audit

## correctness

PASS

For n≥2, B,r,K,c,h>0, maximize Σf(x_i) with Σx=B and f(t)=rt−rt²/K−ct/(1+ht). f''(t)=−2r/K+2ch/(1+ht)^3 is strictly convex (its second derivative positive). If a maximizer has 0<a<b, first stationarity under pair transfer gives ∫_a^b f''(t)dt=0; strict upper Hermite–Hadamard yields f''(a)+f''(b)>0, a forbidden positive second variation. Thus every positive entry equals B/k. G_k=kf(B/k) and G_k−G_{k+1}=B²/[k(k+1)]·[ch/((1+hB/k)(1+hB/(k+1)))−r/K]; zeros c_k=r/(Kh)(1+hB/k)(1+hB/(k+1)) strictly decrease with k. Strict signs on either side show only k wins for c_k<c<c_{k−1}, with exactly k,k+1 tied at c_k, no skipped support or unequal maxima. Verified Step3 and all boundaries from actual RESULT.md; independent exact rational threshold and G_k calculations for n=2–5 and multiple pressures matched; finite checks do not substitute for Hermite–Hadamard proof.

## originality

PASS

Qualified PASS: the closest full primary ecological papers analyze evolving preferences and spatial-moment model scaling, not this fixed-sum global instantaneous optimizer. The same structure may be a specialization of general separable resource-allocation theorem; that risk is recorded, and basic Hermite–Hadamard inequality itself receives no novelty credit.

## value

PASS

The distribution of fixed biomass under opposing density-dependent crowding and predator satiation is a natural explicit constrained nonlinear allocation problem. All global optimizers and all n−1 exact monotone critical pressures are classified for every n, rather than an isolated numerical example; only instantaneous model optimality is claimed, not observed prey behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
