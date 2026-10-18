# Review of the parity-constrained linear-ordering ellipsoid theorem

## Correctness — PASS
The exact edge-comparison covariance, signed parity-correction matrices, and complete spectra are derived in RESULT.md. The uniform even rank orbit has constant covariance-normalized squared norm, so its covariance ellipsoid contains and contacts every generating point. Averaging plus the trace–determinant inequality proves global minimum volume and uniqueness for arbitrary ellipsoid orientation and center. The separate exact-arithmetic path in `CHECKER.py` exhaustively validates the exceptional dimensions using rational arithmetic and checks the six-label threshold; the all-\(n\) theorem rests on the two-unused-label parity involution, not finite extrapolation.

## Originality — PASS (qualified)
The literature inspection compared the full linear-ordering representation (Katthän, arXiv:1109.5040), the Löwner–John ellipsoids of the metric polytope (Gartsman–Linial, arXiv:2305.02113), and the even permutation-matrix polytope (Cunningham–Wang, DOI 10.1016/j.laa.2004.03.016). These concern known representation structure or other polytopes, not the parity-selected pairwise-comparison hull and its precise exceptional determinant ratios. Further mathematical-result searches under rank-comparison, alternating-group, transitive tournament and extremal ellipsoid aliases found no stronger covering theorem. The full Cunningham–Wang paper was not inspected and an unindexed equivalent covariance result remains a risk. Novelty is a qualified source-based conclusion, not a proof from negative search.

## Value — PASS
This is an exact canonical-ellipsoid classification for a natural family of parity-restricted preference polytopes. It identifies a sharp stabilization at six labels and a surprising identical strict volume reduction in ambient dimensions six and ten, with the enclosing sphere unable to detect any parity difference. The eigenvalue spectra, all-vertex contacts and volume ratios give usable intrinsic geometry beyond generic Löwner existence.

## Scope and limitations
Only enclosing ellipsoids in the Euclidean pairwise-sign representation are classified. The result does not compute John ellipsoids, volumes of the polytopes themselves, or facial structures. The algebra for n=4,5 is finite exact; the infinite-range proof uses a parity cancellation. No independent human mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
