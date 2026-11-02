# Scientific assessment

## Correctness — PASS

The enumeration from three-leaf insertion has a unique deletion inverse and generates exactly \(945\) binary unrooted seven-leaf trees. Both the edge-split predicate and the independent four-point distance predicate produce the same complete set of \(945\) binary vectors on \(105\) quartet queries. The explicit six-query witness table realizes every one of \(64\) patterns. Fixing one query for the seven-query upper search is valid because label permutations act transitively on all resolved quartet queries; exhaustive monotone extension rejects all candidate supports after \(206{,}992\) search nodes. The depth-nine online certificate gives \(512\) distinct compatible leaves, and a depth-ten certificate is impossible because \(1024>945\). The extracted artifacts were replayed.

## Originality — PASS under the accessible comparisons

The 2018 Hirai–Iwamasa quartet-compatibility paper studies reconstruction for multipartite systems rather than exact binary shattering. The 2023 Avdiukhin et al. tree-learning paper analyzes Natarajan and multiclass Littlestone dimensions asymptotically for hierarchical labels, including constant tuple sizes; its results do not numerically determine the one-versus-rest seven-leaf problem. The 2026 Arvanitakis et al. quartet-reconstruction paper proves \(\Theta(n)\) Natarajan dimension (including a \(10n\) upper bound), not the claimed finite Boolean dimensions. Indexed searches for quartet displays, VC shattering, online tree shattering, aliases and the particular \(945/6/9\) parameters did not locate a statement that logically covers both equalities. Historical-priority uncertainty persists for alternate encodings or unindexed work. No negative result is inferred solely from a search failure.

## Mathematical value — PASS

A fully specified, classical phylogenetic hypothesis family has a large and mathematically motivated finite query domain, and exact static and online dimensions govern two different learning regimes. The six-query fixed shattering limit differs by three from the adaptive depth nine, which saturates the sharp concept-count bound. The result supplies a reproducible exact calibration instance for a one-versus-rest binary projection of quartet reconstruction, not merely a relabeling of rooted-triplet learning. The finite cutoff is natural because it is the entire class of seven-leaf resolved phylogenies, not an arbitrarily selected slice. It makes no unsupported extrapolation to larger orders.

## Closest sources and limits

The main source comparisons are Hirai–Iwamasa (ISAAC 2018, doi:10.4230/LIPIcs.ISAAC.2018.57), Avdiukhin et al. (arXiv:2302.04492), and Arvanitakis et al. (arXiv:2604.17461). Relevant source sections were materially inspected in HTML or PDF; the 2018 work's expanded full-text manuscript was inspected in HTML. The claim concerns only exact displayed-quartet membership on seven fully resolved, unrooted trees. Remaining risk: other historical work may express the same finite invariant through quartet compatibility or one-vs-rest tree classification.

Self-review: passed. Independent audit: not yet performed.
