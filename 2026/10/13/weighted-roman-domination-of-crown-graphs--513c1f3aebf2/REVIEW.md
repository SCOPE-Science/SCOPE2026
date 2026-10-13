# Self-review

## Correctness
PASS. The proof exhausts all possible locations of label \(2\) after showing that an optimum has at most two such vertices on each shore. For each support pattern, positivity uniquely determines the cheapest remaining labels. The three discarded support patterns are dominated by explicit feasible alternatives, so the six displayed costs are exhaustive. The theorem is analytic; finite enumeration only stress-tests the boundary cases.

## Originality
PASS. The closest primary source is the defining weighted-Roman paper, which proves an exact formula for weighted complete bipartite graphs but does not treat crowns or perfect-matching deletion. Targeted searches under crown, \(K_{n,n}-M_n\), matching-deleted biclique, and weighted-Roman aliases found no equivalent exact statement. Older weighted \((a,b)\)-Roman algorithms on strongly chordal graphs do not cover crowns, which contain an induced \(C_6\).

## Value
PASS. The result solves the arbitrary-cost problem on the canonical one-factor perturbation of \(K_{n,n}\). It identifies a six-regime optimizer structure absent from the complete-bipartite formula and directly addresses the weighted setting's motivating issue: heterogeneous costs can change which defense topology is optimal.

## Closest literature and limitations
The 2025 preprint arXiv:2512.22622v1 is the closest same-invariant source and supplies the complete-bipartite baseline. The result here is restricted to positive vertex weights on crowns; no claim is made for arbitrary matching-deleted unbalanced bicliques or other Roman variants. A poorly indexed equivalent crown result remains the principal residual originality risk.

Self-review: passed. Independent audit: not yet performed.
