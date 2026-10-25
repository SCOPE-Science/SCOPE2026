# Review of the phase–frequency covariance classification

## Correctness

**PASS.** The complex-parameter Fourier transform uses a valid half-plane analytic continuation of the absolutely integrable radial exponential, with an explicit \(c_d\) normalization. The argument \(\theta(\rho)\) is continuous, monotone and ranges from \(-2\phi\) to \(0\); the spectral-phase interval has fixed width \((d+1)\phi\). Bochner positivity gives exactly the two phase endpoint inequalities. The \(d=3\) witness was independently simplified symbolically, and a radial Hankel quadrature cross-check was executed at several frequencies/dimensions. No discrete grid is used to certify an infinite statement.

## Originality

**PASS, within bounded literature review.** The closest exact special case is the known positive-definiteness condition for pure damped cosine (the section \(\beta=0\)), which does not imply the nonzero-sine admissible region or its unique high-frequency extremizer. The general radial Schoenberg treatment in Gneiting (arXiv:1111.7077v1, Section 2) supplies a characterization but not the parameter classification. Schubert–Korte–Brockmann–Schuh (DOI 10.3390/math8040591, Sections 3 and 8) treat stationary time-series oscillators, not positive definiteness of isotropic extensions on all \(\mathbb R^d\). Searches for phased damped sinusoidal radial covariances and semantic published-result matches did not retrieve the complete cone. Strongest residual risk is an unindexed equivalent phase criterion or a more general spectral-positivity theorem whose corollary already implies the result.

## Value

**PASS.** Oscillatory stationary covariances can model negative correlations at positive spatial separation, but a one-dimensional autocorrelation formula need not remain positive definite on spatial point sets. The theorem supplies a complete, sharp multi-dimensional admissibility region, an explicit frequency ceiling, and the unique boundary phase at that ceiling. The spatially valid \(d=3\) witness is disallowed by the standard cosine-only family at the same oscillation frequency. This is a structurally motivated parameter classification, not an arbitrary finite computation.

## Limitations

The result excludes geodesic spherical distances, multidimensional mixtures of frequencies, and improper damping. The literature search is bounded, and the 1999 Chilès–Delfiner book cited by the cosine-model documentation was not materially inspected. The numerical checks are illustrative, not exhaustive proofs, and no independently commissioned validation is claimed.

Self-review: passed. Independent audit: not yet performed.
