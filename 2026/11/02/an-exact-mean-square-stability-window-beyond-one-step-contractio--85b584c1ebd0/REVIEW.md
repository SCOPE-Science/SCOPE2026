# Scientific review

## Correctness — PASS

Rotating two unit row normals to symmetric coordinates gives an exact two-coordinate second-moment recursion. Each fixed batch has zero-mean signed imbalance and second moment \(1/\eta\). The symmetric nonnegative moment matrix has an irreducible positive off-diagonal and an explicit Perron eigenvalue; strict convexity establishes a unique positive unit crossing and the unique fastest relaxation. The one-step conditional-energy operator has independently computed eigenvalues. Exact-rational exhaustive path checks in `verify.py` confirm 1,116 finite identities and 114 numerical comparisons, but the infinite-horizon conclusions are analytic.

## Originality — PASS (subject to independent priority verification)

Moorman–Tu–Molitor–Needell establish randomized Kaczmarz averaging and conditional one-step bounds; Tondji–Lorenz give block-sparse averaged variants and optimum for a general upper bound. Neither inspected argument implies the exact annealed two-row matrix, its positive strict gap between one-step and eventual mean-square stability, or its simple optimal-rate characterization. Agaskar–Wang–Lu supply a general exact-MSE lifting precedent for *single-row* random Kaczmarz, so the matrix method alone is not original. Published research-record comparisons addressed related cyclic Kaczmarz, maximal-distance row selection and smoothed-momentum Kaczmarz; their iteration rules do not cover independent within-batch averaging. A potentially covering calculation in earlier theses or uninspected appendices cannot be ruled out.

## Value — PASS

One-step expected energy decrease is a common convenient sufficient stability certificate for randomized solvers. This result proves, quantitatively and sharply, that such a certificate can be genuinely conservative: a strictly nonempty open relaxation interval produces temporary mean-square amplification along some directions while retaining global asymptotic mean-square contraction. It also gives a rare exact fixed-relaxation tuning criterion and demonstrates that averaging individually norm-preserving reflections can create contraction.

## Scope and risks

The result addresses exactly two nonparallel unit rows, equal independent draws with replacement and consistent noiseless data. The full Agaskar–Wang–Lu paper and the complete journal version of Moorman et al. were not fully read in this run; terminology and special-case priority remain residual risks. No claim of independent validation is made.

Self-review: passed. Independent audit: not yet performed.
