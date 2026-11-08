# Independent mathematical audit

## correctness

PASS

For fixed distinct anchors A,B distance d>0 with midpoint O, Poincaré normalization puts them at (±a,0), a=tanh(d/4), and a sampled third point at Euclidean radius u=tanh(t/2), angle θ. Its Euclidean circumcircle center (0,(u²−a²)/(2u sinθ)) lies wholly inside the disk exactly when |sinθ|>|u²−a²|/[u(1−a²)], valid away from probability-zero collinearity. Thus shell probability is zero u<=a² and otherwise 2/π arccos of this ratio, maximal 1 at u=a (T=d/2). Intrinsic area density is 4u/(1−u²)^2 and radial normalization yields weighted integral F(R). The manuscript integrates by parts using a displayed exact antiderivative J, derives closed disk formula and derivative F´=2(f−F)/[R(1−R²)]; because f increases then decreases, a single crossing exists after a, with every crossing downward. Boundary expansion 1−tanh(T/2)~2e^(−T) gives shell constant (4/π)sqrt(cosh(d/2)) and intrinsic-area integration doubles it for the disk. Independently evaluated integral by SciPy quadrature for a=.15,.4,.8 at four R values each, including inner/outer transition, agreeing closed F to <1e−8. The source verify.py was inspected, finite checks do not prove uniqueness or tails.

## originality

PASS

Beardon 2022 full accessible primary article states the historical exact hyperbolic circumcycle existence criterion (circle/horocycle/hypercycle) including equivalent side-length inequality; this is correctly recognized as PRIOR. The paper does not derive the explicit probability under a midpoint-centered uniform hyperbolic arc/disk third point, unique disk-radius optimizer or distinct e^(−T/2) constants. Glasgow educational two-horocycle locus is also prior geometry. Primary and Resultary searches found adjacent geometric or Euclidean-random-triangle results but no dominating exact sampling distribution; older unindexed random hyperbolic triangle work remains a documented risk.

## value

PASS

For a natural sampling protocol fixed by two anchors, existence of a genuine hyperbolic circumcircle is not automatic, and the complete radius-dependent probabilities are natural geometric-probability invariants. The inner forbidden disk, different circle/disk optimal radii and sharp half-exponential rare-event law with a factor two distinguish intrinsic area from arclength sampling beyond the already known deterministic criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
