# Same-model review

## Correctness — PASS

For the ideal-gas mathematical entropy used in arXiv:2609.19838v1, direct differentiation gives a positive-definite Hessian on \(\rho,p>0\), while \(\partial_p\eta<0\). Restricting to the maximal-pressure edge yields a one-dimensional strictly convex function whose stationary point is \(e^{-1}p_+^{1/\gamma}\); clipping this value to the density interval gives the unique rectangle minimizer. This directly disproves the implication that convexity permits minimization by checking only rectangle corners. The numerical example in the verification artifact reproduces the strict corner gap.

The gauge statement follows from mass conservation. Adding \(c\rho\) to an Euler entropy density and \(c\rho u\) to its entropy flux adds \(c\) times the mass conservation law, leaves the Hessian unchanged, and therefore leaves the entropy inequality and convexity class unchanged. Candidate scores are affine functions \(\eta_i+c\rho_i\), so distinct candidate densities necessarily permit reference-dependent rankings. The explicit two-state example and the continuous minimizer formula verify this effect quantitatively. Harten–Lax–Levermore–Morokoff independently confirms that Euler specific entropy is determined only up to an additive constant and that \(\rho f(\sigma)\) forms a generalized entropy family.

## Originality — PASS, to the best of our knowledge

The elementary convex-analysis fact, entropy-reference freedom, generalized Euler entropy families, and minimum principles for specific entropy are prior art and are excluded from the novelty claim. The accepted contribution is limited to the new ELCD construction of arXiv:2609.19838v1: its stated continuous rectangle minimization is not equivalent to its four-corner rule; the exact rectangle minimizer has the closed form given in RESULT.md; and its absolute entropy-density ranking is not invariant under the admissible mass-affine entropy gauge and can switch the selected characteristic state.

Searches covered the motivating title and arXiv identifier, combinations of entropy-based LCD with convex/corner minimization, entropy gauge/reference constants, generalized Euler entropy pairs, and specific-entropy minimum principles. No public correction or equivalent source-specific theorem was located, and no overlapping SCOPE record was found. The Harten–Lax–Levermore–Morokoff paper was inspected directly. Tadmor's 1986 minimum-entropy work and Berthon–Dubroca–Sangam 2012 were inspected through accessible abstract/full bibliographic material rather than rederived end-to-end; they are the older references most plausibly relevant to the distinction between entropy density and specific entropy, but neither available statement addresses this 2026 ELCD selection rule. Because the motivating preprint is extremely recent, an unindexed contemporaneous comment or later revision remains the principal residual originality risk.

## Value — PASS

The result identifies two independent structural issues in a newly proposed numerical linearization rule. The first is constructive: the continuous entropy minimizer claimed in the paper has an explicit constant-cost formula. The second is invariant-theoretic: equivalent entropy normalizations can change the discrete characteristic state, so reported behavior is tied to a convention that does not alter the underlying Euler entropy admissibility. The specific-entropy normalization \(\eta/\rho\) supplies a simple gauge-invariant diagnostic without asserting that it is the best numerical replacement.

## Limitations

The finding is a correction and invariance analysis, not an instability theorem. It does not show that the published ELCD benchmarks lose accuracy, fail to converge, or violate entropy stability. Algorithm 1 remains a well-defined four-candidate heuristic once a particular entropy normalization is fixed. The gauge-invariant alternative score has not been benchmarked and is not claimed to improve resolution.

Same-model review: passed. Independent audit: not yet performed.
