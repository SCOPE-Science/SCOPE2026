# Same-model review

## Correctness

**Assessment: PASS.**

The proof uses four statements proved in Niu, arXiv:2609.20790v1: the exact volume-form preservation of \(g e^{tA}\) for trace-free \(A\); the uniform quadratic fixed-set perimeter expansion; compactness with strict \(BV_g\) convergence for isoperimetric regions under smooth metric convergence; and weak-* continuity and rigidity of the boundary stress.

For the right derivative, the upper bound is obtained by freezing a base-metric minimizer with maximal stress pairing. The lower bound uses minimizers for the perturbed metrics. Compactness gives a strict-\(BV_g\) subsequential limit in \(\mathcal I(g,m)\); the quadratic remainder divided by \(t\) vanishes uniformly, and stress pairings converge. These inequalities meet at the negative maximal stress pairing. Allowing \(A_j\to A\) in the argument proves the stated Hadamard stability rather than only a fixed-direction derivative. The left derivative follows from the right formula applied to \(-A\), with the sign checked explicitly.

The differentiability criterion is exact: equality of the left and right derivatives in every direction forces all minimizing stresses to have identical pairings against every smooth trace-free field. Such fields separate trace-free tensor-valued Radon measures, and Niu's Proposition 3.5 then identifies the corresponding regions up to complement. Conversely, complementation reverses the normal but leaves the stress unchanged. At half volume this correctly permits the unavoidable pair \(E,E^c\).

The global exponential estimate follows directly from the exact integrand \(|e^{-A/2}\nu|_g\) and the operator-norm spectral bounds. Since the volume form is exactly fixed, the same admissible class is used on both sides.

Potential failure modes checked include singular reduced boundaries, the moving choice of perturbed minimizers, varying perturbation directions, half-volume complementation, and the distinction between one-sided and two-sided derivatives.

## Originality

**Assessment: PASS, to the best of our knowledge.**

The closest source is Niu, arXiv:2609.20790v1, submitted 17 September 2026. The full text was inspected at the statements of Lemma 3.3, Proposition 3.5, Proposition 3.9, and Appendix Propositions A.1--A.2. It develops boundary stresses and metric perturbations to prove generic uniqueness, but no statement of a one-sided derivative of the optimized profile value \(I_g(m)\), no Hadamard directional formula, and no equivalence between metric differentiability and uniqueness up to complement was found.

The general envelope-theorem mechanism is not claimed as new. Milgrom--Segal (2002) gives broad value-function derivative results for arbitrary choice sets. The claimed contribution is limited to the geometric support-function formula for Niu's finite-perimeter boundary stresses, its Hadamard-stable proof in arbitrary dimension, and the converse kink/uniqueness criterion obtained from stress rigidity.

Targeted searches covered combinations and synonymous formulations involving: isoperimetric profile plus Riemannian metric variation; metric derivative or Gâteaux/Hadamard derivative; perimeter sensitivity; boundary stress; shape/envelope derivatives; and the source arXiv identifier. The readily found Riemannian isoperimetric-profile derivative literature concerns variation in the enclosed volume (typically through mean curvature), rather than variation of the ambient metric at fixed volume form. No prior statement matching the theorem was found, and current SCOPE records were searched by source identifier, boundary stress, directional derivative, and isoperimetric-profile terminology without a collision.

No specific inaccessible paper with a closely matching statement was identified. The main residual risk is recency: the motivating preprint is newly released, so parallel or not-yet-indexed work could exist.

## Value

**Assessment: PASS.**

The result turns the boundary-stress device from a minimizer-selection tool into a complete first-order sensitivity formula for the optimized isoperimetric value. It also provides an exact analytic diagnostic for phase coexistence: noncomplementary minimizers are equivalent to a strict first-order kink in some volume-preserving metric direction. The support-function formulation packages all minimizing stresses into the profile's directional response, while the exponential bound supplies a global stability estimate on the same metric slice.

## Scientific limitations

The result treats only trace-free, volume-form-preserving metric directions. It is first-order only and does not establish Fréchet differentiability, a Hessian, or rates of convergence for perturbed minimizers. The generic differentiability corollary is inherited from Niu's generic uniqueness theorem and is not a separate genericity theorem.

Same-model review: passed. Independent audit: not yet performed.
