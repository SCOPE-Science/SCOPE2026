# Independent mathematical audit

## correctness

PASS

Aggregating the two fine Euler steps gives multiplier a² and forcing sigma sqrt(h) S, S=a xi_1+xi_2. Both candidates are normalized Gaussians independent across blocks, so both preserve each entire Euler-grid marginal, without needing the same Brownian realization. The deterministic terminal mean difference does not affect the variance. With k remaining blocks, the fine and coarse weights are a^{2k} and b^k; independence makes the terminal variance additive. In each block the covariance of S and zeta is at most sqrt(1+a²), with equality only at S/sqrt(1+a²) almost surely. The weights multiplying the covariance in the variance formula are strictly negative because a,b>0 and sigma is nonzero, so simultaneous equality is necessary and sufficient for the unique optimum. Expanding the squares gives the gap as 2 sigma² h times [sqrt(2(1+a²))-(1+a)] times sum (a²b)^k; the bracket is positive since the difference of the two squared arguments is (1-a)². Rationalization gives the leading gap bracket lambda²h²/4. For t=2kh the uniform expansions give a^{2k}-b^k=e^{-lambda t}lambda²t h/2+O(h²) and sqrt(1+a²)=sqrt(2)[1-lambda h/2+O(h²)]. Their Riemann limit for V_*/h² is sigma²lambda²/4 times the integral of e^{-2lambda t}(1-lambda t)², while the gap gives sigma²lambda(1-e^{-2lambda T})/8. Integration gives the stated constants, and subtracting three aligned brackets from the shared bracket gives 4U(U-1)e^{-2U}. An independent 40-digit forward covariance recursion at U=0.2,1,3 (4000 blocks each) respectively yielded ratios 2.21163, 2.99985, 3.06065, consistent with the fixed-horizon limits; no uniform claim was inferred from those samples. Replay: python3 /workspace/branches/audit_finite_reproduction.py.

## originality

PASS

Cauchy–Schwarz maximal covariance is classical and receives no originality credit, nor does aggregating fine increments in MLMC. The overlooked difference addressed here is the exactly normalized drift-aligned innovation under the two prescribed explicit-Euler marginals in the independent-block class, with exact positive gap and the nonconstant fixed-horizon ratio crossing three. Closest weighted couplings use other grid marginals; inspected exact statements do not provide this comparison. Literature priority is qualified, particularly for related finite-dimensional Langevin couplings.

## value

PASS

When a linear terminal observable only requires the separate Euler marginal laws, a local Gaussian rescaling without extra samples produces a quantifiable variance reduction with an exact optimum for that implementable class. The strict finite-step gain and the limiting horizon-dependent factor, which can exceed three, make it a useful calibrated comparison rather than a tiny numerical improvement or a general Cauchy–Schwarz example. It is not an improved power of h or a general complexity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
