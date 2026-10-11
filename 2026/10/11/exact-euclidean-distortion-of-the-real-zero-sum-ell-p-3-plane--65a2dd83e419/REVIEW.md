# Same-model scientific review

**Correctness — PASS.** Symmetrizing an arbitrary comparison ellipsoid produces the Euclidean quadratic form without enlarging distortion. The projective unit circle reduces to \((1,r,-1-r)\) for \(0\le r\le1\). An explicit logarithmic-derivative numerator is strictly convex in \(p-1\) and vanishes exactly at \(p=2,4\); it determines the complete radial extrema. The proof separately treats \(p=1\) and \(p=\infty\). The standalone program corroborates the real quartic identity and endpoint inequalities with 22,307 finite checks. None of these finite checks is being used as an infinite proof.

**Originality — PASS, with residual risk.** Passer's approximate Jordan--von Neumann theorem (arXiv:1305.3546, Theorem 3.4) gives general near-Hilbert distortion estimates, not this sharp global formula. Zhang--Meng--Wu (arXiv:2207.05499, Theorem 2) address the full real \(\ell_p^3\)-to-cube comparison, not the two-dimensional zero-sum subspace-to-Euclidean one. The known real quartic hyperplane case already implies the special value at \(p=4\); the all-exponent formula and two transitions are the new asserted statement. Searches under type-\(A_2\), three-atom, and trace-zero aliases did not identify a dominating result. Historical equivalence remains possible and is not ruled out by failed searches.

**Value — PASS.** The formula classifies a natural Banach--Mazur invariant of the canonical three-atom mean-zero \(\ell_p\) family, specifies optimal Hilbert position and all extremal directions, and detects two exceptional Hilbertian exponents and their symmetry-orbit reversals. The result is not claimed beyond real three-atom spaces.

**Verification and limitations.** Run `python3 verification/check.py`. The printed finite counts can be reproduced from this package. The proof uses continuum strict convexity for all exponents; it has not received an independent review.

Same-model review: passed. Independent audit: not yet performed.
