# Same-model review

## Correctness
PASS. The proof reduces the finite-group problem to two real coefficients using the standard Fourier characterization of positive definiteness. The even and odd-multiple-of-three cases have one-line sharp certificates. In the remaining odd cases, two active constraints give the exact upper bound, and the proposed extremizer factors as a cubic whose only negative interval contains no sampled cosine. This proves the all-\(N\) claim analytically. The numerical verifier is corroborative only.

## Originality
PASS. Targeted searches covered Turán constants, positive-definite functions on cyclic groups, the sampled polynomial \(1+2a\cos t+2b\cos3t\), and equivalent sparse-support language. The closest primary source is Kolountzakis–Révész, arXiv:math/0312218v1: it defines the problem, treats finite groups, and gives a different exact five-point example on \(\mathbb Z\), but not this finite-cyclic support or its residue-class formula. Révész, arXiv:0904.1824v1, provides broader LCA-group structure and packing bounds without the exact value found here. The closest own-ledger harmonic result has a different linear objective and does not imply this theorem. Residual risk remains that an elementary sparse cyclic calculation is buried under alternate terminology in unindexed literature.

## Value
PASS. The five-point set \(\{0,\pm1,\pm3\}\) is a natural minimal two-frequency test case for finite cyclic Turán theory. The formula is structurally informative: it identifies exactly how parity and divisibility by \(3\) change the optimum and supplies explicit extremizers and supporting certificates. It is not a routine numerical recomputation.

Same-model review: passed. Independent audit: not yet performed.
