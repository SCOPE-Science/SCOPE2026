# Independent mathematical audit

## correctness

PASS

At a stationary observation time, the Poisson age and successive preceding gaps are independent Exp(r). Conditional on them, displacements on the disjoint Brownian intervals are independent; each unconditioned displacement has transform r/(r−μs−Ds²)=H(s) and is U−V with independent rates λ_+, λ_−. Applying the resets gives the series with scales (−b)^j, absolutely summable by finite first moments. This construction is stationary; coupling with the same noise yields difference (−b)^{N_t} times the initial difference and proves uniqueness. An interior moment parameter s can be enlarged to qs (q>1) still in the open interval; convergence of the positive products at qs by geometric scales gives uniform integrability for the transform at s. At either endpoint or outside, an independent constituent already has infinite exponential moment, hence so does the sum. The slowest positive term is U_0, while on the negative side only V_0 and bU_1 can be slowest; all other rates are separated strictly for fixed b. Isolating one slow exponential gives its rate times the tilted moment of the remainder as leading density coefficient by monotone convergence. At the tie the two slow terms are independent exponentials of the same rate; the Gamma(2) density gives the coefficient λ_−²E exp(−λ_−R_c) and the linear factor t, with the needed moment margin because the remainder rates are strictly faster. The companion exponential moments produce all four printed products; e.g. the critical multiplier is λ_−²(λ_+/Σ)(λ_−/Σ). This is a density asymptotic, not a claim equating density and cumulative-tail coefficients. Frozen supporting files were read, and the frozen script was not executed. An independent SymPy reproduction checked 24 rational pole and coefficient identities for finite truncations of depths 2–5; the infinite-limit conclusion rests on the convolution proof.

## originality

PASS

The closest primary works cover drift with a positive proportional factor and sign reversal with zero drift, respectively. They supply the constituent frameworks but neither contains the crossing of two distinct negative rates in the stated drifted signed model. The distinct indexed comparisons address temporal moments, positive weak resets, or different coefficient laws. The supported separate result is the stationary density transition with the exact critical and noncritical coefficients and finite-moment domain, not the stationary product framework itself.

## value

PASS

Even though each reset contracts the position magnitude, reversing sign can turn a typical direction of rare excursions into the dominant source of unusually negative positions. The exact switching boundary, the linear prefactor missed by a single-rate approximation, and the matching exponential-moment interval characterize that mechanism in a natural minimal model. The density asymptotics give more information than the transform identity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
