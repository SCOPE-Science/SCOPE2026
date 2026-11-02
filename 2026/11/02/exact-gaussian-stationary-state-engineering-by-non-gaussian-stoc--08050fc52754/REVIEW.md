# Scientific review: Gaussian stationary-state design via resetting

## Correctness — PASS
The stationary distributional identity uniquely forces the reset density. Direct Gaussian differentiation yields the displayed quadratic tilt. Matrix positive semidefiniteness, a range constraint, and completion of squares yield **necessary and sufficient** positivity; the normalization is automatic. A last-reset resolvent and a first-reset coupling prove existence and uniqueness. Isotropic optimization is differentiated and every boundary, including an unattained infimum at rate \(dk\), is treated. The standalone reproducibility program passed 71 independent deterministic calculations (Gaussian quadrature and exact rational symbolic checks); the proof of all-dimensional sufficiency is analytic.

## Originality — PASS, with qualification
Olsen, *Steady-state moments under resetting to a distribution* (arXiv:2310.04840), provides the forward source-to-moment theory and master equation. Trajanovski et al. (arXiv:2301.12304) derive OU resetting densities and moments for fixed return sites and comb geometry. Neither inspected primary source states the multivariate Gaussian **inverse source positivity** conditions, the unique admissible quadratic tilt, or the sharp bounded-to-unbounded displacement-reachability transition. The nearest accessible historical findings treat distinct covariance-twin, fractional-diffusion, and harmonic-gas problems. Research-record searches used Gaussian source-design aliases, Lyapunov matrix comparisons, pseudoinverse feasibility, and stationary inverse-law parameters; no decisive equivalent result emerged. Standard Fokker–Planck inversion and OU resetting itself are not claimed as new. A broader inverse-process synthesis result could still subsume the theorem; publication priority is not independently established.

## Mathematical value — PASS
The theorem completely answers a physically motivated distribution-engineering problem for stable OU dynamics under random refreshing. It reveals that non-Gaussian resets can generate exactly Gaussian one-time statistics, and identifies a sharp dimension-dependent rate barrier for producing arbitrarily displaced Gaussian stationary means. This is a natural exact reachable-set classification with a concrete feasibility discontinuity, not merely numerical fluctuation data. It does not address resetting work, noisy experiments, nonlinear dynamics, or non-Poisson reset clocks.

## Closest literature and limitations
- K. Stølevik Olsen, arXiv:2310.04840 (2023): forward resetting distribution to OU moments, not inverse Gaussian attainable set.
- P. Trajanovski et al., arXiv:2301.12304 (2023): fixed-site OU resetting and constrained comb diffusion.
- Standard OU/Fokker–Planck identities are reused explicitly; residual risk of an unlocated general inverse-source theorem remains.
- The claim assumes independent whole-vector Poisson resets, stable drift, positive diffusion, and strictly positive-definite Gaussian target covariance.

Self-review: passed. Independent audit: not yet performed.
