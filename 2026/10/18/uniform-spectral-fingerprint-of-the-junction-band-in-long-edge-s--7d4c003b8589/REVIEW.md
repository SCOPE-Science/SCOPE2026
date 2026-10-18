# Scientific review — uniform junction-band spectral fingerprint

## Correctness (C): PASS

The proof explicitly defines the parent graph, path-length convention, unit-hopping spectral normalization, quantifiers, and limiting regime. Dirichlet recurrence along each inserted path gives the exact Chebyshev secular equation; the change of variables \(\lambda=u+u^{-1}\) makes the high-junction root a uniformly controlled perturbation of \(u=\sqrt{d-1}\). Its expansion has a graph-size-independent error, and Cauchy interlacing excludes any extra eigenvalues above \(2\). The monotone scalar branch gives the sharp bandwidth. Direct full-matrix spectral computations agree with all secular roots in six graph families; finite checks supplement rather than replace proof.

## Originality (O): PASS, subject to residual risk

Berkovits (arXiv:2604.12759) identifies junction localization, its limiting energy and qualitative exponentially small band broadening, while Kumar–Mohar–Pragada–Zhan (arXiv:2303.10488) establish asymptotic limits of subdivision eigenvalues and bounds on their count. Neither inspected presentation supplies the full graph-size-uniform first-order spectral map, sharp coefficient, or induced parent-spectrum fingerprint. Searches on subdivision/Chebyshev equivalents and comparable high-energy quantum-graph band effects did not identify a direct covering result; this does not prove novelty. The general possibility of an existing exact subdivision transform or asymptotic perturbation result subsuming the statement remains the principal risk. See `AUDIT.json` for four claim-level comparisons and source inspections.

## Value (V): PASS

Junction localization makes very narrow bands experimentally and mathematically natural, but a suppression rate alone does not determine their spectral organization. The quantified first-order map determines which inherited parent adjacency levels remain encoded in the narrow band, uniformly over arbitrary network size and geometry at a fixed degree. Its exact bandwidth also detects parent bipartiteness through a sharp extremal case. This connects a physically motivated one-particle tight-binding localization mechanism with concrete recoverable network spectral information rather than a small numerical coefficient improvement.

## Limits and review status

The result does not address disordered or irregular bond inflation, or infinite-volume Bloch bands. The exact spectral transform itself may be implicitly known elsewhere. Numerical replay and the present review are not independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
