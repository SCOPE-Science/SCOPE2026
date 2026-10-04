# Review of Far-field boundary layer for centered maximal averages of a ball

## Correctness

PASS. The claim reduces the centered maximal average of the unit ball at \(Re_1\) to a one-parameter intersection-volume optimization. The missed region for radius \(R+1-\delta\) is analyzed by exact axial cross-sections. Its leading volume is the spherical-cap term
\[
\frac{2^{(n+1)/2}\omega_{n-1}}{n+1}\delta^{(n+1)/2},
\]
while the partial-cross-section transition has relative order \(O(R^{-1})\). Expanding the denominator gives the competing gain \(n\delta/(R+1)\). Balancing these terms forces the scale \(\delta\asymp(R+1)^{-2/(n-1)}\). After rescaling, the objective converges uniformly on compact scaled intervals to a strictly concave profile with a unique positive maximizer. Elementary cap lower bounds exclude scaled maximizers escaping to zero or infinity. This proves the optimizer asymptotic for every maximizing radius and the stated second term of the maximal value.

The calculation was independently stress-tested by direct numerical quadrature in dimensions \(2\) through \(5\); those finite checks were not used to infer the theorem.

## Originality

PASS with a recorded access risk. The motivating preprint's public metadata states that it gives an explicit formula for the unit-ball maximal function only in dimension three and, separately, a general incomplete-beta formula for two-ball intersection volume. The accepted claim deliberately starts at \(n=4\) and solves a different problem: the far-field radius optimization in arbitrary higher dimension, with exact scaling and leading constants.

Multiple published-finding corpus searches were made for centered maximal unit-ball asymptotics, maximizing radii, far-field optimizer laws, and incomplete-beta formulations. The closest records concern one-dimensional sharp centered maximal norms and near-eigenfunction rigidity, not the unit-ball radius optimization. Broad web searches likewise found no statement of the \(2/(n-1)\) boundary-layer exponent or the constants \(c_n,\kappa_n\).

The full text of arXiv:2609.27687v1 could not be retrieved despite bounded attempts through the preprint endpoint, open-access mirrors, and institutional retrieval; the primary abstract/metadata and a detailed public review were inspected. This is an access risk, not a claim that the unseen text is noncovering.

## Value

PASS. The source introduces explicit higher-dimensional ball-intersection geometry specifically to study the centered maximal operator, while singling out dimension three as the case where the full unit-ball maximal function becomes elementary. The new result extracts a dimension-uniform higher-dimensional consequence that the source's abstract does not provide: the optimizer approaches the containing radius through a nontrivial boundary layer, and both the boundary-layer exponent and the first correction to the maximal value are explicit.

This is mathematically motivated because maximizing-radius geometry is central to the source's noninjectivity constructions. The result identifies the precise far-field scale on which the optimizer can respond to small geometric perturbations. It is not a generic Taylor expansion at a fixed radius: the maximizing radius itself moves on a dimension-dependent singular scale.

Same-model review: passed. Independent audit: not yet performed.
