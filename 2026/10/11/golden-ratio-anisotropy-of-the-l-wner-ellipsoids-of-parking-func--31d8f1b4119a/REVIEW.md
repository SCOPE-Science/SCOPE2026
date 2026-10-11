# Review of the parking-function Löwner ellipsoid limit

## Correctness — PASS
The claimed object is the **unique minimum-volume enclosing ellipsoid** of the classical parking-function polytope in ordinary Euclidean coordinates. The proof does not confuse an enclosing sphere, a John inscribed ellipsoid, or an affine-unimodular model with the present Euclidean Löwner ellipsoid. It reduces the global ellipsoid problem to the log-determinant of a vertex covariance distribution by deriving both the ellipsoid contact condition and the determinant–trace lower bound. Symmetrization justifies restricting the maximizing distribution to permutation-orbit masses. The orbit covariance formulas and their \(n^3\) normalizations are exact.

The critical nonstandard step is the factorization
\[
 v_*-v(s)-\tfrac53(h(s)-h_*)^2
 =\tfrac16s(s-u)^2(\sqrt5-1-s),
\]
which is nonnegative on \([0,1]\), with precisely two zeros. The proof derives a two-orbit determinant lower benchmark and a matching sharp upper bound using finite-polynomial perturbation estimates and a concentration argument. The sharp bound forces the **axial** shape limit rather than merely the transverse limit. With both limits established, the contact-layer conclusion follows from equality in the limiting orbital inequality. The coefficient identity is checked exactly in \(\mathbb Q(\sqrt5)[s]\). The included finite verifications establish 27 orbit covariance formulas, exact contact certificates for dimensions 2, 3, and 4, and six larger-dimensional dual benchmark values. These experiments are not relied on as infinite proof.

Residual correctness risk: the perturbative estimates in Step 4 require the stated uniform neighborhood split; the proof supplies the nondegenerate local curvature and explicit expansion needed to justify each estimate, but an independent proof reading has not been performed. No exact finite-dimensional formula beyond the tested cases is claimed.

## Originality — PASS
Primary objects, vertex data, and volume/combinatorial formulas were checked against Amanbayeva–Wang (arXiv:2104.08454), Hanada–Lentfer–Vindas-Meléndez (arXiv:2212.06885, open-access article), and Bayer et al. (arXiv:2403.07387, accessible full HTML). None of the inspected relevant results evaluates the minimum-volume enclosing ellipsoid's separate axial/transverse semiaxes, their limiting ratio \(3/5\), or the limiting contact-layer dichotomy. A classical Löwner contact theorem supplies a general criterion but does not imply the special polynomial factorization or constants without further input. A minimum enclosing *sphere* calculation would optimize a constrained one-radius subclass and does not fix the two independent radii of the true Löwner ellipsoid.

The checked published mathematical records contained related ellipsoid theorems for different convex bodies and parking-function positivity/combinatorics, not a statement covering this asymptotic result. The comparison is between mathematical implications, not just titles or dimensions. Residual originality risk: an equivalent asymptotic optimal-design/covariance statement may exist under different terminology; absence from the indexed searches is not proof of absolute novelty.

## Value — PASS
This is a natural metric question for an established \(n\)-dimensional polytope family with a rich known face/volume theory. The theorem identifies an explicit golden-ratio-scaled center, two **different** leading semiaxis constants, the strict asymptotic anisotropy \(\sqrt{3/5}\), and the only two possible contact-layer accumulation proportions. The sharp quartic deficit explains simultaneously the center, anisotropy and contact localization. These are connected structural facts about optimal containment, not an arbitrary finite index, a table recomputation, or a renaming of a sphere result. Its significance is bounded to the asymptotic classical parking-function family, not an asserted finite-dimensional complete classification or a general theorem for all generalized parking-function polytopes.

Same-model review: passed. Independent audit: not yet performed.
