# Scientific review

## Correctness
PASS. Direct Itô moment closure proves the exact integral-current equation without Gaussian initial conditions, provided raw second moments are finite. Positive definiteness of the drift ensures a unique pre-quench stationary state. The strictly positive exponential convolution kernel proves the minimum-first-reversal bound, and constant saturated temperature difference attains it. The additional result that a bath swap takes exactly \(\log2/(a+b)\) assumes the potential remains fixed. Reproducible diagnostics: `checker.py`, 2,100 comparisons. There is no extrapolation of finite numerical tests to the theorem.

## Originality
PASS on the compared evidence, with explicit historical-priority limits. Filliger–Reimann's full 2007 paper provides the stationary gyrator torque but not the arbitrary-bath-time scalar response or fastest reversal theorem. Dotsenko et al. derive stationary angular velocity, which is a distinct radius-weighted observable. The full text of Baldassarri–Puglisi–Sesta has finite-time controls of potential parameters rather than the fixed-potential bath-difference control posed here. The 2020 Cerasoli et al. paper studies time dependence with fixed unequal temperatures. A later closely named minimum-time study by Patrón et al. uses potential controls according to its accessible abstract, but its complete manuscript remained unavailable for decisive comparison. Standard Ornstein–Uhlenbeck moment equations are not claimed new. Public-result searches for the exact response, swap reversal, alternate formulations and broader control laws did not identify the same full implication. Search non-return is not priority proof.

## Value
PASS. A physical transport observable that usually appears to require three coupled covariances has an exact autonomous kinetic mode for all positive definite stiffnesses and arbitrary bath drives. This yields a sharp universal first-reversal deadline and an attainable optimal bath-control protocol; the dependence only on the trace of stiffness can guide temperature-swapping experiments and provides a diagnostic distinct from full equilibration. These are structural and constrained-control statements, not a small numerical improvement or an arbitrary parameter slice.

## Limitations and priority
The result does not govern mean unweighted angular velocity, all currents, full-system state-transfer time, or nonconfining/time-dependent potential matrices. A 2024 potential-control paper remains an abstract-level historical risk. A general covariance-semigroup formula could make the central eigenmode derivable retrospectively; independent priority certification is not claimed.

Self-review: passed. Independent audit: not yet performed.
