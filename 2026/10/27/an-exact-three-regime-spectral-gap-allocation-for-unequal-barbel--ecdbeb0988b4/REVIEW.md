# Scientific review

## Correctness
**PASS (self-review).** The centered simplex-plus-path embedding has every allowed squared edge length at most one, and its squared norm is the exact concave quadratic \(D(t)\). The Rayleigh/trace upper bound holds for every feasible rate allocation. The exhibited rates attain it: the scalar and simplex columns have eigenvalue \(B/D_*\); the irreducible tridiagonal quotient has that eigenvalue as its smallest positive eigenvalue by a positive edge-gradient eigenvector; the remaining transverse spectra lie above it. Complementary slackness and the full simplex span prove uniqueness, including at both thresholds. The boundary \(p=q=2\), class-absence cases and strict/weak inequalities were individually checked. The finite numerical replay checks 1225 graph sizes but does not certify the infinite theorem by itself.

## Originality
**PASS (self-review; residual bibliographic uncertainty).** The first two phases reduce to the weighted double-broom tree and are not claimed as independently new. The third regime is structurally different: after \(p(p-1)>2(2q-1)^2\), extra clique edges become strictly positive and improve the spectral gap beyond the double-broom optimum. For \(p=9,q=3,B=1\), the tree value is \(1/17\), whereas the complete barbell reaches \(12/203\). Published work on general continuous-time fastest mixing provides the dual framework, not this allocation. The effective-resistance optimal barbell has a different objective, and an asynchronous-communication paper studies a different rate. A potentially relevant 2024 barbell paper could only be checked at abstract level; that access gap is a residual risk rather than proof of novelty.

## Mathematical value
**PASS (self-review).** The result completely determines the optimal design for a natural class of two-community networks, including explicit allocations, a nontrivial three-regime phase diagram, unique optimizers and an exact boundary at which a previously unused family of allowed edges turns active. The third regime is a quantitative structural phenomenon not obtainable by merely relabeling a known tree case.

## Closest literature and limits
Sun–Boyd–Xiao–Diaconis (2006): general convex fastest-mixing dual. Richter–Rocha (2014): exact double-broom tree optimization; this covers sparse regimes but not the dense regime. Ghosh–Boyd–Saberi (2006): total effective resistance (different spectral objective). Nabli–Oyallon (2025): accelerated asynchronous communication (different objective). Song et al. (2024): abstract inspected; full paper not available. This review is not a substitute for an independent literature audit.

Self-review: passed. Independent audit: not yet performed.
