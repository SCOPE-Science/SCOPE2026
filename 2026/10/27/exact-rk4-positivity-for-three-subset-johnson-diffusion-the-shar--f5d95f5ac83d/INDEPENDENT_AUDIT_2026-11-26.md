# Independent mathematical audit

## correctness

PASS

The three-subset exchange graph is simple, unit weight, degree 3(n−3) and diameter three for every n≥6. For a vertex at distance j from a fixed vertex, replacing a common element by an outside element has b_j=(3−j)(n−3−j) choices; replacing a noncommon element by a missing common element has c_j=j². Iterating these transitions with the negative degree stay reproduces the normalized entries per pair. Independently propagated one sparse basis row through integer powers Q^0,…,Q^4 on the explicit exchange graphs for n=6,7,10,33,34,40; every off-diagonal coefficient matched. As a crossover check, 24(3n−4)^4 t_1(n,2/(3n−4)) from the explicit rows is 5616 at n=33 and −78720 at n=34. For all n the diagonal is strictly positive by the spectral scalar-square identity, and the distance-two discriminant is negative with a positive leading coefficient. The edge cubic is strictly decreasing because 3AC−B² has positive coefficients in n−6; the positive constant and negative leading cubic give one positive root. The distance-three bracket has single root 2/(3n−4). At this point the edge sign is opposite F(n); the certificate in z=(n−6)/27 is strictly negative for 6≤n≤33 and the expansion in n−34 is strictly positive for n≥34, ruling out boundary ties and reentry. At forward Euler's endpoint h=1/[3(n−3)] the edge entry is positive from the (A/d)/3 term of the convex decomposition and the distance-three bracket is still positive since n≥6. This proves the strict improvement. Read VERIFICATION.md and verify.py; their finite and symbolic results are recorded, not represented as re-execution.

## originality

PASS

The supported distinct claim is the exact range and its unique integer switch on J(n,3). The diffusion model and intersection-number algebra are established; the located SSP statements and other exact graph families do not supply these signs or sharp Johnson triple thresholds.

## value

PASS

Three-subset diffusion is a natural Bernoulli–Laplace exchange model and provides a fixed diameter-three test of endpoint positivity distinct from strong stability or absolute stability. The determination that the limiting entry changes from maximal-distance to adjacent pairs precisely between n=33 and n=34 is not supplied by forward Euler or orbit algebra alone. A user selecting a maximum positivity-preserving time step needs both the exact endpoint and nonreentry, not merely the smaller Euler guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
