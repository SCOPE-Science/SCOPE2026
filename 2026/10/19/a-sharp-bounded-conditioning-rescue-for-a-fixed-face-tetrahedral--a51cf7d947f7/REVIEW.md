# Self-review

## Correctness — PASS

The claim is a fixed-face, one-parameter, positive-weight theorem. The face boundary relation gives an exact three-coordinate SPD reduction; no asymptotic norm equivalence is assumed. Direct rank-one diagonalization proves the inherited condition number. The reweighted characteristic polynomial has three distinct positive limiting roots. A scale-invariant correlation lower bound on a principal two-dimensional block, followed by eigenvalue interlacing, applies to **every** positive diagonal weight choice. Hence the constructive upper bound and the universal lower bound match to first order, including the sharp improvement coefficient. The accompanying checker passes 74 rational or numerical assertions, independently constructing the oriented six-edge incidence matrix; the infinite and optimizing statements are proved analytically.

## Originality — PASS, with limits

The closest motivating paper is Savostianov--Tudisco--Guglielmi (arXiv:2401.15492v1), specifically the fixed-subcomplex weight approximation discussion in Section 6.1 and their conditioning formula in Theorem 18. It studies the same Hodge object, but the norm-difference weight objective is not the spectral-condition-number minimization studied here; its spectral statement does not supply the new sharp asymptotic diagonal-reweighting constant. Qu--Gao--Hinder--Ye--Zhou (arXiv:2209.00809v2) give general diagonal scaling optimization and SDP methods; they do not state the tetrahedral weight family, its simple additive rule, or the sharp explicit limiting optimum in the inspected sections. Searches for equivalent face-removal, Hodge preconditioning, tetrahedral diagonal scaling, and rank-one-plus-diagonal formulas found no dominating specialized statement. Earlier generic diagonal-preconditioning theory remains a residual priority risk. Separate mathematical-record comparisons and accessible previous claims revealed no equivalent implication.

## Value — PASS, with limits

This is a motivated spectral-conditioning problem raised by the fixed-subcomplex setup of the motivating paper: face subsets may be externally fixed, and face weights may be strongly graded. The theorem demonstrates an unbounded conditioning penalty for blindly carrying the sampled weights, while a computable local correction is provably asymptotically optimal against **all** positive reweightings of those same retained faces. The constant is a genuine optimal-conditioning invariant, rather than a selected error statistic, and the proof explains its two-face correlation obstruction. The limitation is significant: another omitted face, chosen by a heavy-face algorithm, can avoid the adverse regime; no guarantee is claimed for that algorithm or for larger meshes.

## Closest literature and residual risks

The general diagonal-preconditioning problem has prior algorithmic solutions, and the special-case asymptotic might exist in specialized unpublished computations. The tetrahedral family is intentionally small; broader discretization effects and runtime benefits remain open. A separate independent priority check is needed before claims about publication priority.

Self-review: passed. Independent audit: not yet performed.
