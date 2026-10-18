# Mathematical review: perfect-square resonance of inball contacts

## Correctness — PASS

Bayer et al. (arXiv:2403.07387, Theorem 2.3(c)) show that for positive integral parameters with \(b_1\ge 2\), exactly the lower coordinate inequalities and all nonempty upper subset-sum inequalities are facets. Their Euclidean distances from the uniform candidate incenter give the already-known baseline \(r=\min_k A_k/(k+\sqrt k)\); all lower facets touch, and the upper facets of size \(k\) touch exactly when the ratio is minimized. Uniform-center uniqueness follows by simultaneous sharp inequalities on every subset of any active size.

The new necessity uses the integrality of the \(A_k\). A rational ratio of two expressions \(k+\sqrt k\) with distinct positive integer indices forces both indices to be perfect squares, by squaring and comparing rational and irrational terms. The new converse constructs integer data \(A_k\) a bounded distance from \(100n^4(k+\sqrt k)\), with zero normalized excess exactly at any chosen square indices, or uniquely smallest excess at an arbitrary nonsquare singleton. The explicit second-difference lower bound dominates all perturbations, hence the data give a positive integral \(\mathbf b\) by reversed first differences. Telescoping recovers the target \(A_k\) exactly. Every binomial facet orbit is positive, so the maximum is obtained by activating all square-index orbits.

The standalone integer checker verifies 431 constructive patterns for dimensions 2–24, 9,605 exact interval comparisons, strict concavity, positivity and telescoping, plus the explicit dimension-four witness. The checker is finite corroboration, not a proof of the universal theorem.

## Originality — PASS, with bibliographic uncertainty

Behrend et al., *Partial permutohedra* (arXiv:2207.14253), examine the related classical/partial permutohedral construction, faces, volumes and Ehrhart theory. Hanada et al., *Generalized parking function polytopes* (arXiv:2212.06885), study the two-parameter subclass and its face structure and volume. Bayer et al., *Combinatorics of generalized parking-function polytopes* (arXiv:2403.07387), prove the unrestricted facet and generalized-permutahedron descriptions. Those results do not state the integral perfect-square resonance criterion or its universal constructive converse.

The closest earlier metric statements already give the scalar inradius, tangent-orbit test and individual singleton realizations, which are explicitly treated as prior work. The new claim classifies **all possible sets of simultaneously active cardinalities**, and derives a sharp maximum of the total facet-contact count. A short accessible index record for a related two-parameter inball theorem does not permit whole-document exclusion of uninspected statements, so an older equivalent formulation remains possible.

## Mathematical value — PASS

The central mathematical question is which simultaneous facet-orbit contact patterns can occur in an integral family whose face structure remains unchanged as parameters vary. The answer is a surprising arithmetic rigidity law, not merely an evaluation of a distance formula: nonsquare cardinalities are completely isolated, arbitrary collections of square cardinalities are realizable, and the maximum number of tangent facets follows exactly. Both obstruction and realization are needed; neither follows solely from knowing the inradius and each individually achievable orbit. This supplies a complete classification of natural contact degeneracies for an infinite family of simple lattice polytopes.

## Limits

Real parameters and the \(b_1=1\) facet-degeneracy regime are outside the claim. No claim is made for John ellipsoids, affine-invariant contacts, or exhaustive prior-literature absence. Code corroboration is not independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
