# Independent mathematical audit

## correctness

PASS

The candidate reconstructs a nearest-neighbor renewal walk of actual reset/diffusion path: each completed site-to-site passage time T has stated rational hyperbolic Laplace transform obtained from Brownian killed Green kernel; site increments are symmetric ±ℓ independent of T. Actual position remains within ℓ of embedded site walk so the renewal equation M(k,t)=h_k(t)+cosh(kℓ)∫M(k,t−s)P(T∈ds) gives the same long-time logarithmic exponential rate, with exponentially light T and nonlattice pole ensuring local analyticity. Differentiating φ at zero yields m=2sinh²α/(r coshα) and v=[4sinh²α cosh²α−2α sinhα(sinh²α+2)]/(r²cosh²α). Expanding logφ(ψ)+logcosh(kℓ)=0 gives ψ^(4)(0)=ℓ⁴(3v−2m²)/m³. The remaining H(α) inequality is proved analytically: 2H=Σ_{n≥2}3[9^n+3−(2n+1)4^n] α^(2n+1)/(2n+1)!>0 by base n=2 and induction; the CV²<1 inequality follows from another positive coefficient series, with endpoints 2/3 and 1. Independent symbolic differentiation and 60 numerical parameter checks reproduced exact moments and signs (CASE5_OK), not an infinite substitute. The weak-reset expansion matches H(α)=α⁵/20+O(α⁷). No finite-time cumulant sign or CLT non-Gaussian limit claimed.

## originality

PASS

Alston–Bertrand 2024/2025 already introduced nearest-site reset model, the first-passage transform and effective diffusion (main Eq.12/17). Their inspected full primary preprint including first-passage appendix does not give a model-specific strict fourth scaled cumulant inequality or open CV corridor. Pacheco-Pozo–Sokolov 2020/2021 supply general renewal/CTRW large deviation machinery and implicit SCGF style, expressly prior. Another 2024 asymmetric ratchet resetting article has different return mechanism and is a residual comparison risk. The new claim is the sharp all-rate sign and CV inequality, not renewal theory or effective diffusivity.

## value

PASS

The fourth-cumulant growth measures non-Gaussian finite-time fluctuations in a common periodic resetting model even though Brownian motion has zero fourth scaled cumulant; the strict positivity and sharp (2/3,1) corridor expose a structural waiting-time mechanism. The exact model-specific sign is independently useful beyond known second-moment effective diffusivity; normalized excess kurtosis still decays as t^-1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
