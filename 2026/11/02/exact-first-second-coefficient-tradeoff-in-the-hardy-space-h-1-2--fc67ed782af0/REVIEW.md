# Review of the first--second Hardy coefficient tradeoff

## Correctness — PASS

The extremal is known to exist by normal-family compactness, and the general outer-extremal theorem of Brevig--Søvik (arXiv:2610.21788, Theorem 1) applies because the mixed Taylor coefficient functional is nonzero and bounded on \(H^{1/2}\). Every extremal therefore has an analytic fourth root of unit \(H^2\) norm. Directly expanding its first three coefficients reduces the maximization to an explicit homogeneous quartic on the nonnegative unit sphere. All global maximizers lie in the positive interior. Two stationary equations reduce to a univariate quartic; Descartes' rule gives exactly one positive root. A zero-free homotopy verifies that the explicit candidate is an admissible outer function. Equality phases prove uniqueness up to unimodular multiples, and convex geometry proves strict convexity of the sharp support curve. The symbolic and numerical supplementary checker reports `CHECK_OK 92`. The universal statements rely on the proof, not on those numerical tests.

## Originality — PASS relative to inspected evidence

The closest full-text papers are: Brevig--Søvik (arXiv:2610.21788), which establishes outer extremals but does not evaluate the mixed coefficient functional; Brevig--Saksman (arXiv:1905.09547), which calculates individual coefficient maxima and the general extremal structure, but not the continuum of sharp mixed \(a_1+\lambda a_2\) norms; and Brevig--Grepstad--Instanes (doi:10.1007/s40315-022-00469-x), which fixes the constant coefficient while maximizing another coefficient. General structural results do not supply the explicit quartic root, sharp support profile and uniqueness at every positive weight. A published research note on the \(a_0+\tau a_2\) functional treats different coefficient indices and does not, by rotation or degree shift, imply the present \(a_1+\lambda a_2\) norm. Querying published mathematical research records for mixed first--second coefficient norms and equivalent Taylor-jet formulations identified no decisive covering statement. An equivalent unindexed earlier calculation remains possible.

## Value — PASS

The first and second Taylor coefficients have separately known sharp Hardy quasi-norms, but their joint tradeoff is not obtained by adding those scalar bounds. The result determines an entire, intrinsically motivated positive-support boundary for simultaneous coefficients, including a unique zero-free extremal, a strict convexity law, and explicit endpoint profiles. The quartic uniqueness and phase rigidity make the conclusion more than a single routine evaluation. No classification beyond positive weights or the exponent \(1/2\) is claimed.

## Scope, sources, residual risks

Source material inspected: the complete available arXiv HTML text of arXiv:2610.21788 (Theorem 1 and proof); the Introduction, finite-degree extremal structure (Lemma 4), proof of the single-coefficient theorems, and concluding remarks of arXiv:1905.09547; and the abstract, introduction, stated fixed-constant coefficient problem, and applicable structural sections of the open-access Springer article doi:10.1007/s40315-022-00469-x. General Carathéodory--Fejér and Khavinson/Kabaila structural theory may include equivalent untabulated special cases. Numerical checker comparisons establish neither an infinite-dimensional theorem nor originality. Independent external mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
