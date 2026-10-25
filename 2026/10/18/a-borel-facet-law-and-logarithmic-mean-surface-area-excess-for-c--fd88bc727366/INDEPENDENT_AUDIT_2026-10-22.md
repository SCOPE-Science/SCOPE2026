# Independent mathematical audit

## correctness

PASS

Under exactly the standard Euclidean segment embedding sum[e_i,e_j] and uniform Cayley labeled trees, each tree has independent n-1 incidence columns, Gram determinant n, and intrinsic volume sqrt n. Deleting edge e splits the tree into sizes k and n-k, and Cauchy–Binet tree-incidence minors yield each of its TWO facet Gram determinants k(n-k). Therefore S(T)=2 sum_e sqrt(k(n-k)). Cayley counting gives exact q_nk=binom(n,k) k^(k-1)(n-k)^(n-k-1)/n^(n-2), with half factor k=n/2. Independently recomputed rational cut expectations for n=3,4,5, verifying their counts sum n-1 and the corresponding intrinsic area expectations. Uniform Stirling cancellation yields q_nk=n^(5/2)/[sqrt(2pi)(k(n-k))^(3/2)]*(1+O(1/k+1/(n-k))); identity sum_{k≤n/2} w/[k(n-k)]=H_(n-1)/n gives sqrt(2/pi)n^(3/2)log n+O(n^(3/2)). Uniform random facet has P(K_n=k)=E N_k/(n-1) tending to Borel(1), whose k^(-3/2) tail gives E sqrt B infinity; normalization E(A_n/sqrt n)~log n/sqrt(2pi). No concentration claimed and area-weighted facet selection would differ. Actual package check.py enumerates all Prüfer n3..6 with Gram minors and compares expectations.

## originality

PASS

The exact Cayley-averaged intrinsic boundary area, its logarithmic coefficient, and uniform random facet Borel limit are distinct from known graphical-zonotope geometry, general i.i.d. random zonotopes, deterministic tree edge-division extremizers, and previously published width-variance formulas.

## value

PASS

All tree graphical zonotopes have the same intrinsic volume sqrt n and cube face lattice, so the changing Euclidean surface across the natural uniform Cayley ensemble is a motivated geometric statistic. The exact critical n^(3/2) log n scale and Borel(1) uniform-facet distribution with infinite mean expose a genuine heavy-tail/non-uniform-integrability mechanism distinguishing typical geometry from mean geometry. This is a natural all-size stochastic-geometric theorem independent of a downstream application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
