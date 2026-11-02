# Independent mathematical audit

## correctness

PASS

For t_j=d+1+j(2d+2), retain the independent fresh refresh bit U_j at vertex u, expose all other update randomness. The source event A_j uses only exposed variables: u refreshes at t_j and at t_j±d, all members of closed N[u] refresh at t_j+1, and the two lag endpoint bits equal. P(A_j)≥ε^{Δ+4}/2 (with a redundant requirement at d=1). The closed-neighborhood refresh barrier prevents U_j propagating past t_j+1, leaving precisely two Q_T indicators, both 1{U_j=b_j}, whose combined conditional variance is 1. Disjoint time windows make these bits independent; hence conditional variance equals the number of successful events, and total variance proves the bound. Derivation covers arbitrary locally finite graphs independent of finite-state mixing. Existing published Lemma 2.3 and Theorem 2.7 are explicitly imported only for existence of σ² and unthinned CLT. Independent exact Markov transition/counter moment computations on the two-vertex edge for d=1,2 and six horizons verified the bound.

## originality

PASS

Comparisons of actual mathematical implications support a best-of-knowledge original contribution beyond cited prior facts, with explicit overlap credit and residual priority risks; not a universal guarantee.

## value

PASS

Closes a concrete open logarithmic-vs-linear variance alternative for temporal local observations of noisy voter dynamics, with an explicit degree-and-noise constant valid on infinite locally finite graphs. The local refresh barrier also establishes the published CLT variance condition without time thinning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
