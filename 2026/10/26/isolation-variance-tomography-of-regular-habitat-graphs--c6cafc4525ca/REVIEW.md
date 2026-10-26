# Scientific review: Isolation-variance tomography of regular habitat graphs

## Correctness (PASS)
The paper gives an exact site-isolation covariance calculation, an algebraic polynomial-coefficient inversion, an independent wedge-counting identity for triangle multiplicity, and a low-density expansion. All degrees, normalizations, nonadjacency restrictions, and quantifiers are explicit. The standalone exact-rational checker verifies 27 first-and-second-moment comparisons (10,968 weighted configurations) across nine graphs and three probabilities each; nine independently expanded cubic coefficients agree with the analytic formula. This finite experiment does not establish the infinite theorem; the proof is combinatorial and symbolic.

## Originality (PASS with stated search limits)
The relevant ecological literature includes With (1995) (metadata/abstract only) and the fully inspected paper by Neel, McGarigal and Cushman (2004), whose metric-versus-landscape investigations do not give the inverse variance theorem. Diskin and Krivelevich (2023) study asymptotic site-percolation components and isolated vertices on pseudorandom graphs, not recovery of nonedge-codegree statistics from the regular graph's isolation variance polynomial. Semantic searches of published mathematical records identified a bond-percolation component/triangle covariance theorem and separate co-degree reconstruction for complete multipartite graphs; neither statement covers the present all-regular-graph inverse result. General graph-polynomial and reliability-equivalence risk remains; this is not independent bibliographic certification.

## Value (PASS)
For an independent vertex-retention model, the expected count of isolated surviving habitat patches is simply \(np(1-p)^r\) and erases network structure in a fixed-degree family. The variance instead recovers the full positive nonedge shared-neighborhood histogram and triangle count, at only finitely many retention levels, providing an exact boundary of what an interpretable ecological sampling statistic detects. The decagon-versus-two-pentagons construction shows that graph topology is not fully recoverable. Theorem scope excludes estimation noise, heterogeneous survival, and correlated ecological losses.

Self-review: passed. Independent audit: not yet performed.
