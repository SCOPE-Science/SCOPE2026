# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The top-mode theorem follows directly from the exact symmetric AR(1) secular equation. Rewriting it with \(x_N=N\omega_N\) gives an exact equation whose finite-\(\kappa\) limit is \(x\tan(x/2)=\kappa\); monotonicity gives uniqueness, while divergence of \(N(1-\rho_N)\) forces \(x_N\to\pi\). The exact finite trigonometric sums for the centered-cosine eigenvector yield the stated overlap. The iff claim was checked against the only two possible nonzero subsequential regimes, finite positive \(\kappa\) and \(\kappa=\infty\).

The correction-factor corollary uses only orthogonal invariance of the spectral norm and the fact that matrix operator norm dominates any corresponding-row difference. It is deliberately stated as a non-uniformity result and necessary condition, not as a full-transform sufficiency theorem.

For fixed mode index, the source phase equation converges to \(x+2\arctan(x/\kappa)=m\pi\); the normalized sinusoidal eigenvector then converges by elementary Riemann sums to the displayed Robin profile. Substitution into the exact AR(1) eigenvalue formula gives \(\lambda_{m,N}/N\to2\kappa/(\kappa^2+x_m^2)\). The DCT-DC Rayleigh quotient follows from the double Riemann sum of \(e^{-\kappa|s-t|}\).

The standalone numerical artifact separately solves the exact finite-\(N\) frequency equation and directly diagonalizes moderate covariance matrices. The observed overlaps, top eigenvalues, and Rayleigh efficiencies converge to the analytic formulas.

## Originality — PASS, to the best of our knowledge

The motivating 2026 source proves an exact DCT-II/DCT-IV-core factorization with orthogonal corrections and states that, for fixed transform size, the corrections tend to identity as \(\rho\to1\). It also develops large-size correction algorithms. The inspected source does not state a joint \(N\to\infty\), \(\rho\to1\) transition, an \(N(1-\rho)\) threshold, or an operator lower bound showing failure of uniformity.

Classical literature already contains the AR(1) sinusoidal eigenstructure, the DCT endpoint, DCT/KLT performance comparisons, asymptotic performance equivalence, and continuum exponential-kernel/Robin spectral problems. Those facts are excluded from the novelty claim. The claimed contribution is restricted to their combination into the exact local-to-unity boundary-layer classification, the quantitative correction-factor non-uniformity consequence, and the explicit basis-angle versus leading-energy-efficiency comparison.

Repository overlap searches using the source identifier, AR(1)/KLT/DCT terminology, Kac--Murdock--Szegő terminology, Karhunen--Loève/cosine synonyms, and the principal claim family returned no matching SCOPE record. External searches for joint forms such as \(N(1-\rho)\), \(\rho=1-c/N\), local-to-unity KLT/DCT limits, and boundary-layer formulations found the recent source and classical endpoint/performance references but no matching theorem.

### Residual literature risk

The following are the most plausible sources of unobserved overlap:

- A. K. Jain, “A sinusoidal family of unitary transforms,” IEEE PAMI, 1979, DOI 10.1109/TPAMI.1979.4766944. Its accessible abstract and later textbook exposition were inspected; they emphasize a common sinusoidal transform family and asymptotic performance, but the full article was not inspected.
- M. Unser, “On the approximation of the discrete Karhunen–Loève transform for stationary processes,” *Signal Processing* 7(3), 1984, DOI 10.1016/0165-1684(84)90002-1. Its accessible abstract states asymptotic equivalence in performance for stationary processes; the full article was not inspected.
- R. J. Clarke, “Relation between the Karhunen–Loève and cosine transforms,” 1981, DOI 10.1049/ip-f-1.1981.0061. It is cited for the fixed-size high-correlation endpoint; the full short paper was not inspected.
- P. J. Sherman, “On the eigenstructure of the AR(1) covariance,” IEEE SSP 2023, DOI 10.1109/SSP53291.2023.10208005. A detailed accessible secondary exposition of its exact finite-size formulas was inspected, but the full conference paper was not.

These access gaps leave a real residual originality risk, especially because older transform-coding literature is broad. No accessible statement located in this review materially indicates that the specific joint \(N(1-\rho)\) theorem is already covered. The motivating preprint is also recent, so simultaneous follow-up work cannot be excluded.

## Value — PASS

The result identifies the precise scale at which a widely used fixed-size KLT→DCT statement ceases to be uniform. The consequence is directly algorithmic for the new exact factorization: even while \(\rho_N\to1\), the correction matrices can remain a fixed operator distance away from identity unless correlation approaches one faster than \(1/N\). This distinguishes a regime in which dropping the correction factors is not justified by basis/operator convergence.

The fixed-mode Robin description gives a simple structural explanation for the scale, while the leading-energy calculation explains why classical coding-performance comparisons can nevertheless remain favorable. The result therefore sharpens both the numerical-linear-algebra interpretation of the factorization and the approximation-theoretic interpretation of DCT as a KLT surrogate.

## Limitations checked

The review does not infer whole-transform convergence from a single row, does not claim a sufficient joint scale for all correction modes, does not extend fixed-index asymptotics to mode indices growing with \(N\), and does not equate leading-component energy efficiency with total coding gain. Continuum Robin eigenfunctions are treated as classical background rather than a new theorem.
