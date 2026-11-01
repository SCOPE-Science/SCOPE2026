# Scientific review

## Correctness — PASS

The statement fixes the unit sphere, the exact-degree-four nine-dimensional complex harmonic space, probability-area basis normalization, equal unweighted sample rows, and the full integer domain \(N\ge9\). Distinct azimuthal orders modulo \(N\) make the Gram matrix diagonal, with eigenvalues \(9Na_j(t)\) and multiplicities \(1,2,2,2,2\). Differentiated Legendre polynomials give the five quartic factors without approximation. The exact proof reduces the global condition-number problem to a cubic crossing and five explicit polynomial lower bounds on complementary intervals. All five inequalities have complete rational Bernstein-positivity certificates, and the unique squared optimum is isolated rationally. At that root, rational interval arithmetic verifies the precise eigenvalue ordering required for attainment. The standalone checker passed all exact identities and 1215 independent numerical Gram entries; numerics are expressly not used to infer the all-height theorem. Endpoint ranks, exceptional modal zeros, initial-longitude invariance, and both height signs are handled by the statement.

## Originality — PASS under bounded comparison

The nearest mathematical construction is the harmonic-index-four polygon lift of Bannai–Okuda–Tagami (2013), but a zero harmonic *average* at a Gegenbauer root is not the invertibility or sharp condition number of an exact-degree-four evaluation matrix. The later work of Zhu and collaborators (2015) concerns harmonic-index existence and tightness, not latitude-frame singular values. The 2014 Khalid–Kennedy–McEwen spherical-sampling paper works with entire degree-bounded spherical harmonic spaces and several latitude circles, and minimizes condition numbers for different matrices using a numerical placement procedure. The present closed-form global optimum for one ring and one exact degree is not a corollary of those statements. Bounded indexed-record and literature searches revealed no identical formula, equivalent single-ring formulation, or stronger theorem directly covering it. Search absence alone is not a uniqueness or novelty proof; earlier specialized ring-frame optimization remains a residual risk.

## Mathematical value — PASS

A regular latitude ring with exactly nine nodes is a minimally sized unisolvent configuration for degree-four spherical harmonics whenever all five amplitude sectors are nonzero. This result solves its sharp robustness/conditioning design problem simultaneously for every larger regular sample count. Unlike degree-two ring conditioning, five distinct modal levels compete, their minimax is governed by a cubic crossing, and global optimality requires a nontrivial exact certificate excluding disconnected near-degenerate latitude regions. It supplies a reproducible algebraic sensor-placement rule rather than a numerical optimum, and explains why the latitude of a harmonic-index-four design is not appropriate for invertible degree-four reconstruction.

## Sources and limitations

Primary materials inspected: the harmonic-index construction and basis argument in Bannai–Okuda–Tagami, arXiv:1308.5101; the iso-latitude transform/conditioning Sections II–III of Khalid–Kennedy–McEwen, arXiv:1403.4661; and the harmonic-index classification material of Zhu et al., arXiv:1507.05373. Exact rational certificates and the executable checker support correctness. Bounded searching does not rule out older uncatalogued equivalent formulations. This is a local geometry-class optimum, not an optimum among all nine-point spherical sets. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
