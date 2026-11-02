# Self-review

## Correctness — PASS
With full-sphere area normalization, azimuthal and equatorial parity reduce the problem **exactly** to beta-weighted polynomial Rayleigh quotients. The local monic orthogonal-polynomial argument calculates the least eigenvalue of every invariant block, with the exact Jacobi norm and uniform fixed-bandwidth first correction. A finite strict binomial comparison determines the unique azimuthal sector or conjugate pair; the two-point evaluation kernel determines the largest eigenvalue. A separate 85-digit generalized-Gram checker tests six bandwidths and two asymptotic coefficients. The proof, not finite computation, covers every fixed integer bandwidth.

## Originality — PASS (subject to historical-priority risk)
Simons and Dahlen (2006) analyze precisely the same double-cap concentration operator, its parity blocks and a commuting numerical tridiagonal operator. That earlier work is foundational and *does* encompass exact numerical computation for any parameters, so the present result does **not** claim discovery of the double-cap spectral problem. Its new statement is a sharp fixed-bandwidth shrinking-cap law across **all azimuthal sectors**, including exact least-eigenspace parity, central-binomial leading constant and inverse condition number; these are not stated by the inspected earlier sections or the checked nearby results. The spherical design paper (2023) motivates the fixed-band spherical sampling setting but does not assert this cap condition theorem. A relevant old paper on concentrated polynomials was seen at abstract level only. Novelty remains provisional until more historical sources are scrutinized independently.

## Value — PASS
The smallest concentration eigenvalue is the worst-case observable energy when a bandlimited spherical signal is measured only on two polar patches. Its exact leading constant dictates sharp inverse stability and reveals an even/odd change in the worst recoverable angular mode. This is a motivated finite-bandwidth endpoint regime distinct from the extensively studied high-bandwidth/shrinking-region planar limit and is not merely a numerical fit or a reparametrized known spectral formula.

## Scope and risk
The result has no joint limit in angular radius and bandwidth and does not address nonsymmetric caps. Historical priority is not established definitively. Numerical checking is finite and supplementary.

Self-review: passed. Independent audit: not yet performed.
