# Scientific review: The exact price transition for fastest mixing on a five-cycle

## Correctness — PASS

The claim covers every positive real exceptional edge price and every **unrestricted** nonnegative five-edge allocation satisfying the stated budget. The five-cycle reflection decomposition is checked in both sectors, and the proposed interior rates produce two linearly independent centered gap eigenvectors. The remaining two eigenvalues are strictly larger, by explicit positive rational expressions and Bernstein sign certificates. Parameter uniqueness follows from a strictly negative rational derivative whose polynomial sign has an exact Bernstein certificate. A rank-two positive-semidefinite matrix, with edge Gram distances equal to the prices, proves a global upper bound by the Rayleigh trace inequality; this does not presume symmetry of competing allocations. Equality determines all five rates and proves interior uniqueness. An independent centered-path Rayleigh witness proves the sharp high-price threshold and the full optimal segment at equality. The attached checker verifies all crucial symbolic identities, but the global conclusion comes from the written proof, not finitely many numerical trials.

## Originality — PASS, with limits

The mathematical framework and its graph-Laplacian SDP dual are established by Sun–Boyd–Xiao–Diaconis (2006); the arbitrary-cost path formula and **equal-priced** cycle formula are also theirs. Their inspected section 5.3 gives a two-dimensional bound for the general cycle, but no exact heterogeneous five-cycle optimizer, transition price \(16\), full boundary optimizer segment, or uniqueness result. Boyd–Diaconis–Parrilo–Xiao (2009) optimizes the different discrete-time SLEM, treating edge-transitive unpriced cycles. Current searches in published mathematical records and online primary literature did not locate equivalent five-cycle coverage. Residual risk: earlier or differently phrased special-cycle optimality work may exist, including less accessible pre-2006 papers. Search failure is not a proof of novelty.

## Value — PASS

The first odd cycle beyond the triangle provides a natural small nonbipartite test graph where the standard symmetry method leaves a nontrivial even cubic-plus-odd quadratic decomposition. The result converts a general semidefinite optimization into an exact single-parameter formula and proves a qualitative change in the full optimizer set at price \(16\). In particular, a **nontrivial continuum** of optimal conductance allocations exists exactly at the transition, whereas the interior double-gap solution and the deleted-edge solution are unique. This is a complete natural classification useful as a benchmark for heterogeneous graph diffusion and as a proof-level test of SDP-dual methods. It is not a routine re-expression of equal-price or path results: the certificate and optimizer-face analysis are explicit and topology-dependent. It does not generalize to arbitrary price patterns or cycle lengths.

## Sources and residual limitations

Primary full-text sections compared: Sun et al., *SIAM Review* 48 (2006), sections 1, 4–5.3 and references, DOI 10.1137/S0036144504443821; Boyd et al., *SIAM Journal on Optimization* 20 (2009), sections 2–3.1.1, DOI 10.1137/070689413. Published-record overlap checks found only general or different-network approaches, with the closest mathematical comparison being a different cycle size. The novelty determination is a self-review with explicitly limited literature coverage; it does not constitute independent validation.

Self-review: passed. Independent audit: not yet performed.
