# Scientific review: distant period-two orbits for a bounded Halley correction

## Correctness — PASS

The correction, its positive denominators, and its large-positive-argument expansion are explicitly derived from the formula in arXiv:2609.08110v1. Oddness reduces every two-cycle to the scalar equation \(Q(c)=2\). On every sufficiently distant prescribed interval, the left endpoint has \(Q>2\) and the right endpoint has \(Q<2\); the derivative \(Q'\) is eventually strictly negative, establishing exactly one root per interval. Expansion at the right endpoint gives the stated displacement coefficient. The mean-value theorem independently gives the Newton global-contraction comparison. All quantifiers, eventual thresholds, and the difference between exact periods and stability are explicit. A standard-library test program corroborates sample intervals and finite calculations, but is not used to prove the infinite statement.

## Originality — PASS under accessible-source comparison

The source construction and early theoretical sections of Mukasa (arXiv:2609.08110v1) were inspected and show the method's positivity, boundedness and sufficient convergence framework, but not this specific near-linear analytic nonconvergence family in the inspected material. Access to the rest of that manuscript failed; this is a material residual source risk, not evidence that the remainder does not cover the result. Martin (arXiv:2312.12305v1) was inspected in full and exhibits cycles for Newton and a different positive correction, not the claim that the new bounded correction cycles infinitely often while Newton is globally contractive on the same strictly increasing function. The independently indexed Newton derivative-sector theorem concerns undamped or constant-relaxed Newton, so its statement does not imply the bounded-curvature-dependent correction's behavior. Actual claim-level searches in mathematical research records and general literature returned no directly dominating theorem, which is limited negative evidence rather than proof of absolute novelty.

## Mathematical value — PASS

The construction answers a method-specific global-reliability question: bounded, positive, third-order local correction does not preserve even the strong derivative-sector guarantee enjoyed by undamped Newton. The failure persists for arbitrarily small \(\|f'-1\|_\infty\), and repeats in infinitely many distinct distant intervals with a sharp location asymptotic. This is a natural robustness boundary, not an arbitrary isolated numerical counterexample. It isolates the role of the dimensionless curvature ratio, which can be large far from the zero even when the first derivative varies very little.

## Relationship to literature and limitations

Main source: H. Mukasa, *Third-order Halley-type iterative method with positive and bounded correction function* (2026), arXiv:2609.08110v1. Full accessible historical predecessor: R. J. Martin, *Root-finding: from Newton to Halley and beyond* (2023), arXiv:2312.12305v1. Closest comparison record: *Sharp minimax relaxation frontier for scalar Newton under derivative-sector bounds*, public record `46b773bf52ed` (its statement concerns Newton, not the new correction). The exact period-two orbits need not attract nearby initial conditions; the claim does not establish positive-measure divergence or invalidate stronger sufficient hypotheses. Complete historical-priority review and independent mathematical review have not occurred.

Self-review: passed. Independent audit: not yet performed.
