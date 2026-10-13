# Scientific review

## Correctness — PASS

The theorem has exact quantified hypotheses and a complete matching-bounds proof. The upper bound is an explicitly reproduced known forcing sequence (Abiad et al., arXiv:2610.03892v1, Proposition 9). For the lower bound, distinct path eigenvalues yield independent eigenspaces of dimension at least \(m-1\) each. For \(\ell\ge2k-1\), positivity of the first \(k-1\) roots and parity of tree walks preclude cancellation of off-diagonal polynomial entries; for the only shorter arm lengths in the \(k=3\) and \(k=4\) cases, explicit coefficients and degree-sum walk identities prove exact graph support. Hence the constructed real symmetric matrix has nullity at least \(k(m-1)\), and the standard maximum-nullity inequality closes the bounds. Verification reproduces 108 numerical support/witness tests and 91,793 exhaustively tested smaller seed sets; these are checks, not substitutes for the all-parameter proof.

## Originality — PASS, with residual literature risk

The motivating primary source [1] poses exactly the sought equality as Conjecture 10 and supplies only the upper bound (Proposition 9). Its Theorem 20 establishes a *conditional* polynomial-eigenvalue method, so we do not claim invention of that method. The present application establishes the nonvanishing support condition symbolically throughout two complete power indices and a further infinite long-arm region; this is not implied merely by the source's conditional bound. Its examples do not cover these parameters. Older complete primary treatments [2] and [3] cover paths, strict powers and squares of general trees, not this higher-power theorem. Searches for zero forcing and maximum nullity of cubic/fourth spider powers, spectral polynomial alternatives, and comparable research records found no implication dominating the present statement. Residual risk: equivalent or stronger results could exist in unindexed or uninspected literature, and the conditional spectral framework is closely related.

## Value — PASS

The result settles an expressly formulated recent conjecture in all admissible cube and fourth-power cases and every higher power with sufficiently long equal legs. The proof gives a structured family of extremal symmetric matrices and exact minimum rank, beyond a small numerical case or a routine substitution into a general inequality. The unresolved shorter-arm region for higher powers provides a precise boundary for subsequent work.

## Scope and limitations

The theorem is restricted to equal-leg spiders with \(m\ge3\), \(k\ge3\), and either \(k\in\{3,4\}\) or \(\ell\ge2k-1\). It is not a solution of the complete all-parameter conjecture. Independent external review is absent. Primary comparison sources: A. Abiad et al., arXiv:2610.03892v1; L. M. DeAlba et al., Electronic Journal of Linear Algebra 23 (2012); G. J. Chang and J. C.-H. Lin, *Minimum rank of powers of cycles and trees*.

Self-review: passed. Independent audit: not yet performed.
