# Scientific review: general-position polynomials of sunlets

## Correctness — PASS

The argument is an all-orders counting bijection. A general-position set of cardinality at least three contains no two vertices from one root–leaf site. Its selected leaves are never geodesic interiors, and a selected root is a geodesic interior exactly when the two adjacent occupied-site gaps sum to at most half the cycle length. These statements include all shortest-path tie cases. The resulting independent local choices give the cyclic-gap formula. Marking one eligible root, one adjacent eligible pair, and (only for triples of supported sites) three eligible roots gives the three finite-sum correction terms. Nonadjacent eligible roots are impossible when at least four sites are selected. The direct BFS verifier tests every subset for sunlets with \(3\le n\le9\), and all compared coefficients agree; the infinite claim is supported by the proof rather than inferred from finite samples.

## Originality — PASS, with explicit limits

Iršič–Klavžar–Rus–Tuite (arXiv:2401.05696, 2024) introduced the invariant, established general inclusion–exclusion and formulas for other graph families, and raised the corona-unimodality question. Rather (arXiv:2603.06930, 2026, Section 7) already computed the specific \(C_6\circ K_1\) polynomial and used it as a log-concavity counterexample. Neither inspected primary text gives the cycle-corona gap criterion or all-\(n\) coefficients. The 2026 version of the general-position survey treats the invariant but does not give an all-sunlet enumerator. The published adjacent general-position polynomial result for windmill graphs concerns the join family \(K_1\vee mK_r\), not sunlets. The finite \(n=6\) coefficient vector, the existing scalar general-position theory, and the generic inclusion–exclusion formula are not claimed as new. Residual risk: an implicit or differently indexed all-\(n\) formula has not been categorically excluded.

## Value — PASS

The graph family is the natural cycle analogue of the path coronas in the initiating literature, and an exact enumeration across all cardinalities answers a mathematically motivated question more informative than a single scalar or isolated case. The theorem provides a necessary-and-sufficient cyclic-geodesic characterization and a polynomial-time integer formula that determines the complete size distribution for arbitrary cycle length. This supplies exact test data for the corona-unimodality problem without claiming to solve that separate problem.

## Scientific limits

The result concerns exactly one leaf per cycle vertex, with \(n\ge3\). No general coefficient unimodality or log-concavity theorem is asserted. Independent proof checking is not represented by the reproducibility experiments.

Self-review: passed. Independent audit: not yet performed.
