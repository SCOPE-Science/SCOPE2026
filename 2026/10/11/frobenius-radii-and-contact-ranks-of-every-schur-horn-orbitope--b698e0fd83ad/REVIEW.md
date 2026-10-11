# Same-model review

## Correctness
PASS. The proof uses the exact Schur-Horn majorization inequalities and the Ky Fan variational principle to replace each partial-eigenvalue bound by all rank-\(k\) projection supports. In the intrinsic trace hyperplane, the support normal is \(P_L-(k/d)I\), whose squared Frobenius norm is exactly \(k(d-k)/d\). This gives the exact radius-\(r\) center inequalities, not just a bound. Orthogonal averaging proves that the scalar matrix \(\bar a I\) realizes the largest possible \(r\), and equality identifies the contact ranks. The circumradius proof separately uses the equal-norm orthogonal orbit, uniqueness and symmetry of the minimum enclosing Euclidean ball, and strict convexity to identify its complete contact set. Repeated eigenvalues are allowed.

## Originality
PASS. Three highly relevant sources were compared by statement and implication. The middle-period source *Spectral Polyhedra* defines the spectral lift, records the Schur-Horn/permutahedron relation, majorization inequalities, and the support-function transfer. The foundational *Orbitopes* paper gives the rank-\(k\) spectrahedral and supporting-subspace descriptions. Jeong--Gowda gives a broad spectral-set transfer principle. None of the inspected material states the Frobenius inradius, complete incenter locus, contact-rank profile, circumradius, and outer contact set. Direct and alias searches under Chebyshev-center, largest-inscribed-ball, minimum-enclosing-ball, majorization-radius, and exact-formula language found no covering result. Residual risk remains for older matrix-nearness theory under different terminology.

## Value
PASS. The result supplies a metric classification for every nontrivial Schur-Horn orbitope in its canonical Frobenius realization. It converts the full inball problem into a finite minimum over normalized majorization slacks, identifies exactly which rank orbits touch the centered maximal ball, and gives the complete incenter set and minimum-enclosing sphere. For the standard family it yields the closed forms
\[
r_{\mathrm{in}}=\sqrt{d(d-1)},
\qquad
R_{\mathrm{out}}=\sqrt{\frac{d(d^2-1)}3}.
\]

## Closest literature and limitations
The closest sources provide structural descriptions powerful enough to make the present proof short, but no inspected theorem was found that already states or directly packages these Euclidean invariants and equality cases. A general distance-transfer result elsewhere could shorten part of the argument and is retained as a literature risk. The theorem is tied to the canonical Frobenius metric and is not affine invariant.

Same-model review: passed. Independent audit: not yet performed.
