# Review: The annealed metric law of spherical Voronoi interfaces

## Correctness — PASS

The claim is about the expected arclength measure of pairwise Voronoi interfaces, not about normalization by a random realization's total length. The proof gives an exact coarea expression on the pair bisector, including its intrinsic-gradient Jacobian. For independent uniform sites, the site-height density is constant on \([-1,1]\); the remaining sites satisfy the strict empty-cap condition independently with probability \(((1+c)/2)^{n-2}\). After integrating the relative azimuth and transforming the common height, the resulting measure factorizes into two explicitly normalized beta laws. The total-length, all-moment, and exponential-limit assertions follow by exact beta and gamma identities. The case of two sites is included, with one great-circle interface; higher-order ties are arclength-null almost surely. A separate algorithm reconstructing actual random spherical diagrams agrees numerically; it is auxiliary rather than the proof.

## Originality — PASS, with historical priority risk

Hug–Reichenbacher (original 2017 arXiv text, spherical Poisson–Voronoi section) addresses large-cell shape inequalities and Poisson-driven models, not the finite-binomial metric mark at a length-biased interface. Kabluchko–Thäle (2019 preprint, 2021 full open-access text, inspected main theorems) proves exact *counts* of faces of the binomial spherical Voronoi tessellation and duality with inscribed polytopes, but neither the expected total interface arclength nor the joint arclength-weighted generator geometry follows from those statements. The closest accessible previously recorded findings concern great-circle hyperplane tessellations or a three-site spherical Voronoi *area* distribution, not this arbitrary-site metric law. Muche's Euclidean Poisson–Voronoi edge relations are for a distinct underlying model. A plausible historical source, Miles (1971), could not be examined in complete original full text; it remains an explicit priority risk. The novelty conclusion is best-knowledge, not independently certified.

## Mathematical value — PASS

The exact joint beta factorization determines the distribution of two natural metric marks at a randomly encountered interface, all generator-distance moments, and a meaningful rare-scale limit. The expected total arclength is an exact finite-sample function of the number of sites, with a curvature-sensitive correction to the planar \(\sqrt n\) limit. These facts describe metric information not supplied by a deterministic face-count census, and can serve as finite-size benchmarks for spherical nearest-site tessellations.

## Scope and remaining limitations

Uniform independent sites, curvature-one two-sphere, and annealed arclength weighting are essential to the stated proof. Individual edge-length distributions and quenched interface statistics are not asserted. Complete inspection of Miles's 1971 source and external mathematical verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
