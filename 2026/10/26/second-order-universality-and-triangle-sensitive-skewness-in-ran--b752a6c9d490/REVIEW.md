# Review of the orientation-score moment theorem

## Correctness — PASS

The fixed-host random orientation measure is a product of independent fair edge signs. Expanding centered squared vertex scores into pairwise products of incident edge signs gives a distinct quadratic monomial for each wedge of the simple host. Pairwise orthogonality fixes the variance; every surviving third-order product is exactly a three-cycle of the host's line graph. Common-vertex triples contribute positively and actual host triangles negatively because the incidence signs reverse at the edge endpoints. There are exactly six orderings of each triple. This proves all claimed identities for every finite simple host, including disconnected hosts. Separately, exact conditional enumeration across a shared edge gives the regular-host histogram covariance formula; binomial orthogonality gives its projection spectrum.

`check.py` independently enumerates all orientations of every graph through four vertices and larger contrasting regular hosts, with 444 exact arithmetic assertions. The finite tests corroborate, rather than establish, the arbitrary-size proof. All necessary proof steps and checker code are included.

## Originality — PASS (bounded to the inspected literature)

The complete primary paper of Sanchez and Kolesnik (arXiv:2009.09322, 2020) characterizes feasible and mean score sequences using graphical zonotopes, but does not provide these second/third moments or the exact regular-host covariance projection. Claesson et al. (arXiv:2209.03925, 2022) count possible score sequences rather than study uniform random orientations and higher moments. Lin and Reinert (arXiv:0912.4812, 2009) study joint degrees of random undirected graphs, which does not directly imply the fixed-host orientation-score statement. Published published-finding corpus similarity comparisons and the accessible previously recorded claims were checked for the exact formulas and stronger equivalents. No inspected result covers the combined claim. In particular, an earlier result about cyclic triangles versus an additive score functional on *complete* random tournaments is a distinct cross-covariance identity, not the third centered moment across arbitrary host graphs.

The identity is expressed using classical independent-sign moment expansion, so a general theorem about quadratic Rademacher forms or random graphical zonotopes might imply it. Priority and independent assessment remain open; the search result is not a proof of uniqueness.

## Value — PASS

Degree-sequence invariance of all histogram covariances contrasts sharply with the degree-insensitive third-moment change \(\tfrac34 t(H)\): the third cumulant gives an exact observable fingerprint for a structural graph invariant. The triangular prism and \(K_{3,3}\) furnish explicit connected equal-size, equal-degree examples for which **the complete second-order histogram covariance coincides** yet skewness of a natural quadratic score statistic differs. The result is an exact all-graph identification and a natural full-covariance classification, not a chosen-parameter table or a textbook asymptotic. This has a plausible role in score-based inference and in distinguishing uniform orientation models.

## Limits and residual risks

Uniformly fair, independent orientations and a simple fixed host are essential. The degree sequence is needed to infer triangle count; the first three moments do not determine the full law. Primary-paper comparison does not exhaust historical probability and Rademacher-chaos sources. No external independent scientific validation has been performed.

Self-review: passed. Independent audit: not yet performed.
