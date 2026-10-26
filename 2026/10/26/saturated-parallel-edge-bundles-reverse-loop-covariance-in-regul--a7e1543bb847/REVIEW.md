# Mathematical review

## Correctness

PASS. A fixed elementary parallel-bundle event specifies exactly \(r\) disjoint half-edge pairs and therefore has probability \(p_r\). Summing those events gives \(\mathbb E P_r=B_rp_r\). Conditional on one event, exactly \(r\) stubs at each endpoint have been consumed and the remaining stubs pair uniformly; the eligible same-vertex stub-pair count is \(n\binom d2-r(2d-r-1)\). The resulting exact conditional loop mean yields the displayed covariance identity on subtracting the unconditional mean. Positive denominators and the bracket inequality prove strict sign reversal precisely at \(r=d\). Fixed-degree asymptotics follow by expansion. The standalone exact enumerator independently agrees in 24 small test cases, with additional parameter sign tests. The proof does not rely on these finite cases.

## Originality

PASS on the inspected record, subject to historical-priority uncertainty. Angel–van der Hofstad–Holmgren (arXiv:1603.07172), especially (1.2), (1.6), (3.1), introduce the loop and double-edge pair statistics and their asymptotic limits; these are credited. Janson (arXiv:1901.09744) gives exact probabilities of prescribed disjoint half-edge pairs and analyzes switching defects. The exact covariance of the loop total against *every* \(r\)-fold parallel-edge bundle count, the strict positive-only-at-saturation sign classification, and the two different decay scales are not statements found in the relevant inspected sections. A generic counting kernel can be used to derive the new identity after identifying the two competing effects; the kernel itself is not claimed as new. Chodrow (arXiv:1909.09037) treats a different, uniform-multigraph sampling law and only its abstract was inspected. This is a finite source search, not certification of historical priority.

## Mathematical value

PASS. Loops and multiple edges are the canonical defect variables controlling simplicity of the configuration model. The result shows that the direction of their finite-size dependence changes sharply only when a parallel bundle exhausts its endpoint degrees, and that this positive dependence decays faster than the negative unsaturated covariance. This is a natural complete classification by multiplicity rather than an arbitrary numerical slice. The reversal is not visible from the leading asymptotic independent-Poisson laws.

## Boundaries and residual risk

The claim concerns \(n\ge3\); at \(n=2,r=d\), loop and saturated bundle events are mutually exclusive. The conclusion does not address arbitrary irregular degree sequences or other multigraph sampling measures. Exact rational finite enumeration does not prove universal correctness; that follows from the written conditional-expectation derivation. Earlier broad factorial-moment analyses may contain an equivalent specialized corollary not identified by the search.

Self-review: passed. Independent audit: not yet performed.
