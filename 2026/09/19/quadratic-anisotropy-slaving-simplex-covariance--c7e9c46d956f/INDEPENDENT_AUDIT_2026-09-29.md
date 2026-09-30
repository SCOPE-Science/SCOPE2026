# Independent audit — 2026-09-30

## Disposition: PASSED

Record: `2026/09/19/quadratic-anisotropy-slaving-simplex-covariance--c7e9c46d956f`

### Correctness
PASS. The second-order covariance asymptotics check symbolically and dynamically. Linearizing the eigenvalue ODE at λ* gives the stated traceless and isotropic rates. The exact pairwise-gap formula yields a nonzero limit e^{α_perp t}A_t→Q for anisotropic data because the exponent error is integrable. The centered elementary-symmetric expansion has quadratic term -1/2 C(d-2,n-2)λ*^{n-2}||A||_F². Averaging the ODE therefore gives a positive quadratic forcing of the scalar mode. Direct binomial simplification gives α_parallel-2α_perp=4c_n C(d-2,n-2)λ*^{n-1}[d(n-2)+n]/(n-1)>0, and variation of constants yields exactly the filed recoil and interaction-energy constants.

### Originality
PASS, qualified to the inspected evidence. The current Kim–Park–Shim preprint is still indexed as v1. Its public description and the filed source comparison cover covariance reduction, equilibria, and explicit first-order convergence rates, not the nonzero quadratic mean-recoil coefficient, its universal sign, or the exact interaction-energy tail. Searches for the source identifier together with second-order/anisotropy/mean-covariance terms did not locate a prior statement of these source-specific formulas.

### Scientific value
PASS. The result explains how the faster isotropic mode is slaved to the slower anisotropic mode and turns a big-O remainder into a universal signed asymptotic law. The positive approach-from-above statement and energy-tail coefficient add interpretable nonlinear information beyond the source's linear rates.

### Independent findings
- The rate gap α_parallel>2α_perp is strict for every 2≤n<d.
- The recoil ratio simplifies to n(n-1)/(2d λ*[d(n-2)+n]).
- The interaction-energy ratio simplifies to C(d-2,n-2)λ*^{n-2}(d-n)/[d(n-2)+n], hence is positive.
- The supplied d=5,n=4 integration converges numerically to both predicted constants.

### Independent checks
- Independently linearized the covariance eigenvalue system into scalar and traceless modes.
- Recomputed the binomial identities and both coefficient simplifications symbolically.
- Verified the centered elementary-symmetric expansion and the variation-of-constants denominator.
- Inspected the supplied verification artifact and its numerical convergence data.

### Literature evidence
- https://arxiv.org/abs/2609.16978 — Kim–Park–Shim diffusive simplex model; current public version indexed as v1.
- https://arxiv.org/abs/2606.21918 — Nondiffusive predecessor; different asymptotic regime.

### Limitations
- The theorem is covariance-level only and does not imply a full second-order Wasserstein expansion.
- It excludes isotropic data, n=1, and the critical regime n=d.
- Priority remains qualified against unindexed contemporaneous notes on this very recent preprint.
