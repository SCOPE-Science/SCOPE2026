# Scientific review

## Correctness
**PASS.** The covariance–derivative identity is exact for the finite Mallows exponential tilt. Uniform-bias covariance is obtained by conditioning on individual fixed points and summing inversion indicators. At either extreme of bias, the first nontrivial permutation layer is a single adjacent transposition. A uniform bound on all deeper layers, using the inversion-sequence product and a two-point Lipschitz estimate, proves strict signs for the displayed cutoffs at every sample size. The standard-library checker passed 393 exact finite assertions, including inversion-weighted moment formulas and sign checks. Finite checks are not used as an infinite proof.

## Originality
**PASS (best-knowledge, residual historical-priority risk).** He (2021) and He–Müller–Verstraaten (2022) give fixed-parameter large-size cycle limits, including odd/even effects, but no all-finite-size covariance derivative sign with the displayed bias cutoff. A February 2024 discussion on fixed points versus inversions specifically poses the monotonic relationship that this result refutes. Nearby published uniform-permutation covariance formulas do not imply the tilted finite-size statement. Exact historical priority is not formally established.

## Value
**PASS.** The result answers a motivated monotonicity question negatively using infinitely many odd sizes, identifies a quantitative region where the reversal is guaranteed, and completely resolves the first odd size by an exact rational covariance and threshold. The even-size high-bias contrast distinguishes a real parity boundary, not a single isolated computation.

## Limits and closest literature
The all-parameter covariance sign remains open in this package except at the specified regimes and for the full three-symbol formula. The sufficient cutoff need not be sharp; odd-size zero uniqueness is not asserted beyond three symbols. The cited research on Mallows cycle laws addresses different limits. Independent validation and exhaustive historical priority review have not been performed.

Self-review: passed. Independent audit: not yet performed.
