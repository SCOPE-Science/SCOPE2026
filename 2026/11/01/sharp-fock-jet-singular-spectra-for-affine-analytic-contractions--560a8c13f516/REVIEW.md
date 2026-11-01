# Scientific review — sharp Fock-jet singular spectra

## Correctness: PASS

The mathematical claim is for a fixed positive singular-value index and a strict nonzero affine contraction on the explicitly normalized one-variable analytic Fock space. The proof identifies the Taylor expansion of the corrected composition as an absolutely trace-norm convergent series of rank-one derivative-jet maps. Its exterior powers have a unique lowest nonzero Taylor order, and consecutive exterior-power norm asymptotics produce the singular-value constants. Direct orthogonal projection onto truncated reproducing kernels gives the exact Fock-jet Gram pivots. The Weyl translation supplies the dual pivots without an unproved symmetry assumption. The packaged pure-Python checker passed 456 exact rational assertions for determinant ratios, the algebraic Taylor identity and coefficient domination. Finite tests corroborate, but do not establish, the infinite-dimensional result.

## Originality: PASS, subject to historical-priority limitations

The closest inspected primary paper is Chalendar–Partington, arXiv:2106.00427, Theorem 2.2: operator-norm convergence to the fixed-point evaluation map, without its full fixed-rank approximation-error spectrum. Bayart–Tapia-García, arXiv:2205.11066, Theorem 7.3 computes singular values of an *uncorrected* compact affine composition operator, not its subtraction by the limiting generally nonorthogonal projection. The source statements do not imply the new constants by equality or straightforward restriction, and they give no singular-vector information that permits subtracting singular values. Semantic published-finding corpus searches for fixed-point composition, jet filtrations and corrected approximation spectra returned no matching claim; this is negative search evidence, not a proof of priority. Older results of Doan–Hu–Khoi–Queffélec concern uncorrected composition approximation numbers; only bibliographic and abstract information was available for that source, so it is a residual historical risk rather than a full-text exclusion.

## Mathematical value: PASS

This resolves a natural quantitative gap left by a qualitative norm-convergence theorem: it determines, simultaneously at every fixed rank, the optimal finite-rank approximation cost of the asymptotic error. The exponential hierarchy and the explicit coefficients describe how fixed-point location affects each independently observable Taylor-jet direction. They are not the already-known geometric singular values of the uncorrected operator: at the first level, for example, the nonorthogonality factor is \(1+|c|^2\). This is a structural spectral law for a canonical analytic contraction, not a change of notation or an isolated computational example.

## Scope and remaining risks

The asymptotics are for fixed rank and fixed parameters; there is no uniform growing-rank estimate or higher-dimensional statement. Relevant source searches cannot establish historical uniqueness, and a 2017 entire-function composition paper was not obtained in full. The comparison specifically targets corrected differences rather than the simpler full composition operators. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
