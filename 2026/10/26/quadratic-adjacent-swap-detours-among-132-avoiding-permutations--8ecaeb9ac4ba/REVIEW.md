# Scientific review

**Correctness — PASS.** A local necessary-and-sufficient swap criterion follows by checking the only newly changed relative order. It proves connectivity, supplies a pairwise-crossing lower bound of \((n-1)^2\), and certifies an attaining two-phase path. A maximum-element Catalan decomposition independently derives the complete edge-enumeration recurrence and closed form. The included executable exhaustively checks the entire relevant graph for each \(2\le n\le10\); small cases use a separate brute-force avoider predicate.

**Originality — PASS, subject to literature risk.** Reifegerste (2002) supplies Catalan diagram descriptions rather than the adjacent-swap distance. Aisbett (2015) analyzes a nonadjacent insertion move and pattern popularity. The 2018 sorting-network analysis addresses minimal monotone paths to the reverse permutation, whereas this result is a nonmonotone shortest route to a different target. Ehrenborg–Kitaev–Steingrímsson (2015) study a distinct overlap graph. Targeted research-record and literature searches did not identify a statement implying the exact \((n-1)^2\) distance, but an unindexed sorting-reconfiguration analysis remains possible. The Catalan vertex count itself is prior work and is not presented as new.

**Value — PASS.** The ordinary Kendall-tau distance for the canonical pair is \(n-1\), but imposing a natural classical-pattern restriction multiplies it by \(n-1\). The sharp quadratic distortion is a structural limitation on sorting while maintaining pattern avoidance, rather than a small finite correction. Connectedness and the explicit edge count describe the ambient Catalan reconfiguration graph and make the metric phenomenon well-defined.

No full diameter formula is claimed, and the program's finite horizon is not used as an infinite proof. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
