# Scientific review

## Correctness — PASS

The claimed stationary iteration, its preconditioner and its error matrix are explicitly defined. Exact right-block multiplication and similarity give the spectral reduction to the real generalized eigenvalues of \((\alpha I-WT^{-1}W,T+\alpha I)\), independently of the off-diagonal parameter \(\gamma\). Every associated Rayleigh quotient has strictly positive derivative for every nonzero direction, since \(T+WT^{-1}W\) is SPD. Uniform compactness establishes strict monotonicity of *both* spectral extrema, including multiple-eigenvalue cases. Opposite endpoint signs and strict monotonicity produce exactly one balancing root. The exact stability boundary and two-dimensional closed form follow by direct quadratic-form and trace identities. All quantified hypotheses and strict boundary inequalities are retained. The included checker tests the full block matrix, the noncommuting example, the nilpotent example, and 80 additional finite systems, but the analytic proof supplies the all-dimension conclusion.

## Originality — PASS (qualified)

Makhdomi and Khojasteh Salkuyeh, arXiv:2608.29985, Sections 2–4, provide the VBP factorization, quotient structure and sufficient convergence tests, and their Section 4 selects the shift by Frobenius-distance matching. They do not give the global unique exact asymptotic stationary spectral-radius minimizer, the universal balancing rule without commutativity, or the sharp noncommuting two-dimensional formula. Huang–Chen (2018) analyze a different relaxed block-splitting factorization and cannot imply this result by direct specialization. published-finding corpus searches on VBP, extreme generalized eigenvalues, shift balancing and analogous preconditioners returned other algorithms, not this claim. The classical minimax balancing idea is acknowledged rather than claimed as a novel abstract principle. A 2024 PMBP optimal-parameter article could not be inspected beyond the abstract, leaving a residual cross-family equivalence risk; its known family is different and there is no evidence of dominating coverage. A failed search is not a uniqueness proof.

## Value — PASS

The theorem supplies the previously unspecified rate-optimal VBP shift for all SPD–indefinite symmetric matrix pairs, including noncommuting cases, by one monotone scalar equation requiring only extreme symmetric generalized eigenvalues. It also gives the exact global stationary stability boundary and a coupling-insensitive two-dimensional optimizer. This matters because the source's Frobenius-distance choice, when used for the stationary iteration, can yield spectral radius approximately \(15.999728\) while the exact optimal shift makes the error nilpotent; no such assertion is made against the source's outer FGMRES experiments. This is a substantive global algorithmic tuning result, not an arbitrary tabular computation or unmotivated parameter slice.

## Closest literature and limitations

The primary VBP source arXiv:2608.29985 was materially read in its theoretical sections and parameter-selection section; Huang and Chen (2018), DOI 10.1515/math-2018-0051, was also compared by block formula and convergence analysis. Zhang–Dai (2017), DOI 10.1007/s11075-016-0175-y, was available through abstract and citations. Xie et al. (2024), DOI 10.1007/s40314-024-02643-4, remains a partial-access originality risk, not an asserted negative full-text finding. Finite simulations cannot establish mathematical novelty or prove the theorem; the proof is analytic. No independent audit or validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
