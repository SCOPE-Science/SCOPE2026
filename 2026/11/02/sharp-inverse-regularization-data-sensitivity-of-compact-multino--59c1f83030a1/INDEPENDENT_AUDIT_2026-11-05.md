# Independent mathematical audit

## correctness

PASS

For fixed unisolvent stencils, indicator sites and support weights, perturbing bounded data f by delta changes each residual indicator at rate at most Hx delta. The log of the positive unnormalized weight differentiates almost everywhere with rate at most tHx delta/epsilon. The normalized-weight covariance identity, weighted Cauchy-Schwarz and |Pj|<=Lx B give |K[f]-K[g]|<=Lx(1+tBHx/epsilon)delta, with no smoothness assumption on the data. In the actual six nodes (0,1/4,1,2,11/4,3), at x=3/2 exactly two equal geometric weights are active; first active branch 0, second 1, and the first residual changes to delta. Independently checked geometric support and exact formula K(delta)=(epsilon+delta)^t/[epsilon^t+(epsilon+delta)^t], giving derivative t/(4epsilon) and an O(1) output gap for delta=c epsilon. The bound is sharp in exponent, not in its prefactor; fixed stencils need not be selected by a particular implementation.

## originality

PASS

Best-of-knowledge originality of the precisely scoped sharp theorem survives comparisons to primary antecedents; generic tools, original model/method and known broad phenomena are explicitly credited. Detailed four implications below distinguish genuinely new claimed conclusions from prior theory; remaining literature-access/priority risk is material but not in itself a known covering theorem.

## value

PASS

For a newly specified data-dependent scattered-data interpolation operator, the sharp sensitivity to small regularization epsilon is a mathematically and numerically motivated stability obstruction. The explicit admissible geometry and fixed-noise-scale output jump diagnose how local adaptation trades off data perturbation robustness. The calculation is more than the generic derivative of inverse weights because geometry/indicator-only point and sharp uniform data bound must coexist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
