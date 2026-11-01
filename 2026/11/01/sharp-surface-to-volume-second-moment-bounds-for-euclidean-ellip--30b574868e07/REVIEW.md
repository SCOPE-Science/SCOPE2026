# Scientific review: ellipsoid surface and volume second moments

## Correctness
**PASS.** The area Jacobian converts uniform Euclidean surface measure on an ellipsoid to a sphere distribution weighted by the inverse-axis norm. Gaussian linearization and the exact spherical \(|\langle z,u\rangle|\)-weighted second-moment identity yield the positive-definite covariance formula. A symmetric strictly convex log-Gaussian norm functional orders the auxiliary weights oppositely to the squared semiaxes, giving the sharp trace upper bound and the ball equality case; positivity gives the strict lower bound. A controlled flattening limit proves optimality of the lower scalar and Loewner constants. The standalone code verifies two independently derived deterministic integral representations, exact angular normalizations, and representative boundary cases. Numerical checks are corroboration rather than a proof in all dimensions.

## Originality
**PASS, with residual priority risk.** The motivating distance-comparison work of Lotnikov (arXiv:2608.14848) addresses general convex bodies, planar symmetric cases and higher-dimensional counterexamples, but its inspected statements do not give the all-dimensional ellipsoid covariance representation or sharp ratio. Tokmachev (arXiv:2607.08869) provides a convex-order comparison only under planar matching-centroid or special circumscribed-polytope assumptions; its abstract does not imply the higher-dimensional result, nor the sharp ellipsoidal constants. The published triangle second-moment gap is for another class; Rivin and Poelaert–Schniewind–Janssens treat ellipsoid surface areas and curvature, not this covariance/ratio classification. The relevant full sources, title-level alternatives, equivalent ratio formulations and published mathematical summaries were compared. One relevant 2026 full text was unavailable, leaving a documented historical risk; search absence is not treated as uniqueness proof.

## Mathematical value
**PASS.** The surface and interior sampling problem is a natural quantitative special case of a recent boundary-versus-interior distance program, which has counterexamples for general high-dimensional convex bodies. The theorem distinguishes ellipsoids from those counterexamples, supplies dimension-optimal nontrivial constants, proves a strict matrix inequality, and classifies equality and degenerating sharpness cases. Its proof identifies a reusable Gaussian-mixture representation and an order-reversing axis-weight principle, rather than merely computing a single shape.

## Scope and independent validation
Applies only to squared Euclidean distances and full-dimensional ellipsoids sampled from Euclidean surface area and normalized volume. The strict lower constant is an infimum, not a minimum. Definitive historical priority and independent validation are not established.

Self-review: passed. Independent audit: not yet performed.
