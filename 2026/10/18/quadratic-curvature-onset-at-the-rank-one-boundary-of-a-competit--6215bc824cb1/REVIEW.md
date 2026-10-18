# Scientific review: quadratic separatrix curvature onset

## Correctness — PASS

The exact rank-collapse calculation gives \(x_1y_1=bd\). The resulting scalar map has exactly one positive fixed point for \(b>A\), and the sign of its displacement yields the entire line of convergent initial points and the two escape regions. The equilibrium Jacobian has stable eigenvalue zero and unstable eigenvalue \((2b-A)/b>1\). Smooth hyperbolic stable-manifold dependence, followed by the implicit-function theorem applied to its one-step preimage, constructs the stable graph uniformly on each compact interval. The exact graph invariance equation determines the two displayed Taylor coefficients uniquely. Symbolic differentiation yields the strictly negative quadratic curvature coefficient; the standalone checker verifies all polynomial/rational identities and additional sample shooting tests. These computations do not replace the smooth-manifold argument; no global-in-\(y\) remainder is asserted.

## Originality — PASS, with residual priority uncertainty

The principal source is Camouzis–Kulenović–Ladas–Merino (2009), DOI `10.1080/10236190802125264`. Garić-Demirović–Kulenović–Nurkanović (2009), DOI `10.1155/2009/153058`, gives the general global-basin theorem for the nondegenerate case and **explicitly states the degenerate scalar reduction in Remark 2.4**. Neither inspected source states the parameter-Taylor expansion of the stable curve or the quadratic negative curvature formula. The cited competitive-map invariant-manifold theory ensures qualitative existence of a monotone curve but does not supply its parameter response. The claim is therefore the explicit second-order unfolding, not a new reduction or a new proof of the known qualitative trichotomy. Targeted equivalence, domination, and coefficient searches did not identify a previously published formula. An unindexed exact calculation remains possible; lack of a search hit is not proof of absolute priority.

## Mathematical value — PASS

The degenerate surface separates noninvertible one-step collapse from invertible competitive dynamics, for which the 2009 global theorem supplies a curved but implicitly defined basin separator. The derived expansion measures *how* that separator emerges from a straight line: affine first-order motion hides an unavoidable second-order concavity of the same sign under both positive and negative detuning. This is a natural, quantitatively sharp geometric invariant of the published dynamical family, not an arbitrary finite instance or a routine restatement of the existence theorem. Its scope is compact segments and small detunings; global curvature behavior is not decided.

## Source comparison and limits

The 2009 qualitative stable-manifold and scalar reduction are credited in full. The perturbation result assumes fixed positive \(A,d\), \(b>A\), state coordinates as printed, and a small parameter preserving positivity. It relies on standard smooth stable-manifold theory but its rational coefficients are worked out and verified here. The derivative calculation is not independent review and absolute historical priority remains uncertain.

Self-review: passed. Independent audit: not yet performed.
