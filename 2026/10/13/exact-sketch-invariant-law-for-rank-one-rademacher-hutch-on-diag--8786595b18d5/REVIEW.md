# Research review

## Correctness — PASS

The sign sketch produces a coordinate-sign conjugate of one fixed rank-one projector. Because independent residual signs are invariant under this conjugation, the entire conditional output law is independent of the sketch. Expanding the fixed residual matrix gives the two-weighted-sign-sum law. The off-diagonal Rademacher variance identity proves the spectral variance expression; choosing a maximal eigenvalue proves strict positivity. The isotropic random-walk fourth moment proves the exact finite distribution and variance. Exhaustive rational enumerations guard the algebra but do not replace its all-dimensions proof.

Limits: strictly positive diagonal spectra, one sign-sketch column, exact arithmetic. Further residual probes reuse the same rank-one sketch; non-diagonal or Gaussian-sketch cases are not asserted.

## Originality — PASS

The 2020 Hutch++ original provides the sign sketch but only generic variance bounds, and its later explicit-variance analysis uses a Gaussian sketch. The 2021 improved-Hutch++ paper describes the sign option and adaptive allocation but not the all-spectrum rank-one conditional distribution. The 2016 Gambhir–Stathopoulos–Orginos paper already proves variance can increase under spectral deflation, so that phenomenon is prior; it does not yield the data-dependent sign-sketch law. Practitioner material also notes diagonal Hutchinson exactness, which is not claimed as new. Focused indexed searches and primary-literature comparisons found no implication-equivalent conditional law, though an unindexed treatment remains possible.

## Value — PASS

The three-query case is the smallest complete Hutch++ run, and diagonal positive matrices are the natural exactness class for sign-probe trace estimation. The complete distribution and nonrandom sketch-conditional variance quantify failure of variance reduction in the finite-matvec regime for every diagonal spectrum, not just a hand-picked point. A bivariate weighted-Rademacher representation enables exact discrete risk calculations and an explicit two-point worst-case error at the smallest nontrivial dimension. The centered chi-square limiting error remains nondegenerate as dimension grows at fixed residual-sample count, making the warning relevant beyond the smallest illustrative matrix. This gives an exact quantitative calibration for budgeting a rank-one control-variate sketch.

Self-review: passed. Independent audit: not yet performed.
