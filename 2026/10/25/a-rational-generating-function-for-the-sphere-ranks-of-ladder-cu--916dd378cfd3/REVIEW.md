# Scientific review: ladder ordinary cut-complex ranks

## Correctness: PASS
The theorem quantifies over all integers \(n\ge3\), \(3\le k\le2n-3\). The complete codimension-two skeleton follows from an induced vertex of degree at most two at an extreme occupied rung. Missing next-to-top faces are exactly complements of deletion-robust \((k+1)\)-sets, proved to be consecutive fully occupied rung blocks. Their count, the exact finite-state rational enumerator of connected \(k\)-sets, and the reduced Euler identity give the claimed sphere rank. Top-dimensional wedge homotopy follows from the independently published two-row shellability theorem [2], Theorem 5.6. The separate executable checker verifies 21 parameter pairs by direct induced-subgraph enumeration, with Euler-face enumeration for all allowable \(k\) on \(n\le5\). Finite tests do not substitute for the all-parameter reasoning.

## Originality: PASS
The closest primary prior work [1], Section 5 and Table 3, supplies the first four five-cut values \(13,85,270,636\), and the three- and four-cut formulas. Prior work [2], Theorem 5.6, proves shellability over the full range but does not supply the rational bivariate rank formula. Those are substantive prerequisites, not the precise rank classification. Focused searches compared rational connected-set enumerators, the ordinary grid cut complex, and indexed total/circular-ladder claims, including aliases. They found no directly dominating formula; this is a best-knowledge conclusion, not a uniqueness certificate. A potential residual risk is an independently known enumerator for connected induced sets on ladders, and two related project full texts were not accessible beyond summaries.

## Value: PASS
A complete all-parameter formula replaces partial small-cut tables and provides an explicit integer sphere-wedge rank for every allowed two-row-grid cut complex. The rational series explains uniform parameter recurrence and yields a new symbolic five-cut formula, rather than merely recomputing existing finite entries. The result fills a natural quantitative gap between previously known low-parameter calculations and general shellability. It does not prove shellability afresh or settle wider-grid or equivariant questions.

## Sources and scientific limitations
[1] Bayer et al., *Topology of Cut Complexes II*, arXiv:2407.08158v1, Sections 2 and 5, Table 3.

[2] Chandrakar et al., *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646v3, Theorem 5.6. Its original v1 first appeared 2024-08-14, while the cited v3 theorem was read in the January 2026 revision.

The verification script is not an independent mathematical audit; no independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
