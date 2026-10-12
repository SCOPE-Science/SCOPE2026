# Scientific review: exact shared-clock grid mixing

## Correctness — PASS

The theorem is exact for adjacency-matrix quantum walks on the unweighted twelve-vertex \(P_3\square P_4\), with one nonnegative observation time used for both factors. The seven explicit spectral idempotents and the two Fourier-density moment constraints yield the uniform \(3\times3\) and \(4\times4\) averages by exact algebra. The frequencies \(\sqrt2,(1+\sqrt5)/2,(1-\sqrt5)/2\) are rationally independent, so the time orbit is dense in their phase torus. The joint density is bounded strictly away from zero, placing the target in the relative interior of the phase-image convex hull; this is the critical step upgrading approximation to **exact finite physical-time realization**. The coefficient-space dimension and stochastic constraint justify the support bound fifteen. Direct exact computations are reproducible with `verify.py`; the separate numerical LP does not prove exactness.

## Originality — PASS, with residual risk

Baptista–Coutinho–Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1, Sections 3.2 and 4.3 already give uniform randomized averages for the two factor paths, and this contribution does **not** claim those discoveries. Their Section 5 explicitly warns that one shared sampling time does not generally tensorize factor averages; it supplies covariance and trace relations, not exact uniformity on their Cartesian product. Coutinho–Guo, arXiv:2404.02236, surveys generalized averages without the stated shared-clock twelve-vertex theorem. Lo et al., quant-ph/0509059, use a different Cesàro notion on circulant bunkbeds, not this path grid. The searches for equivalent graphs, Cartesian-product implications, and table entries did not identify the same claim. A stronger undetected graph-product theorem remains a residual originality risk: negative search results do not prove novelty.

## Value — PASS

This exact twelve-vertex graph is a naturally motivated test of the synchronization problem: averaging each factor uniformly is not enough by itself to obtain uniform mixing when observation time is shared. An exact law on at most fifteen physical observation times provides a positive test case for a nontrivial product, with an explicit independent-phase density explaining how synchronized trajectories can simulate the required joint average. The limit of the contribution is this graph and support bound; no general product theorem, closed-form list of exact observation times, or instantaneous result is claimed.

## Scientific limitations

The proof is analytical but existential for the precise times and weights. Numerical finite sampling is merely a corroborating check. The close 2023 source has been read in relevant sections; general indexing incompleteness and undiscovered stronger results remain possible. External independent review has not occurred.

Self-review: passed. Independent audit: not yet performed.
