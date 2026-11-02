# Review: minimal connected domination of rook graphs

## Correctness — PASS
The necessary-and-sufficient classification follows from the line-graph correspondence, exact domination support condition, cycle-edge deletion, and leaf-edge deletion. Conversely every selected bipartite tree spanning exactly one shore with all occupied vertices on the other shore having degree at least two is deletion-minimal for connected domination. The conversion between one-deletion and full inclusion minimality is proved by a spanning-tree pruning argument. Bipartite Prüfer encodings give \(m^{c-1}\,c!\bigl\{{m-1\atop c}\bigr\}\) trees on a fixed occupied column set; the two alternatives are disjoint. Support, smallest/largest sizes, and endpoint multiplicities follow without numerical extrapolation. An independently programmed graph-level verifier checked 1,444,991 nonempty subsets over 17 ordered graph orders, and verified direct surjection counts through length six.

## Originality — PASS (publication-priority uncertainty remains)
The 2016 paper of Lokshtanov, Pilipczuk, and Saurabh, and the 2022 enumeration work of Abu-Khzam et al., concern general algorithms/bounds; their inspected full texts do not state this all-parameter rook polynomial. The 2021 connected-domination polynomial literature concerns all connected dominating sets, not the inclusion-minimal subfamily. The 2022 topological formulation likewise concerns all connected dominating sets. Individual small-graph polynomial tables are not equivalent to a uniform two-parameter Stirling formula. Exact graph-family/alias/line-graph searches, comparisons with earlier mathematically related findings, and primary paper inspection found no equivalent or dominating prior formula. Unindexed literature, private symbolic tables, and unexamined general frameworks remain explicit risks; originality is a provisional self-review, not a priority certificate.

## Mathematical value — PASS
This is a complete classification and coefficientwise enumeration of a nonmonotone minimality property for a natural two-parameter graph family. It improves substantially on knowledge of only the scalar connected domination number: a sharp upper connected domination number, exact numbers of minimum and maximum sets, and a distinct forbidden cardinality interval appear as consequences. The support gap for sufficiently skew rectangles is a structural outcome, not an arbitrary small-instance coefficient.

## Boundaries and checks
All arguments assume \(m,n\ge2\), use labeled graph vertices, and require inclusion-minimality. The proof treats squares and rectangles and establishes a precise boundary at \(n=2m\) after symmetry. The checker is finite verification only. Full publication priority and independent validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
