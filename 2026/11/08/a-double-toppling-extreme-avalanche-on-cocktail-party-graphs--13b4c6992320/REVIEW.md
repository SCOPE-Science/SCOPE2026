# Scientific review: a double-toppling extreme avalanche on cocktail-party graphs

## Correctness — PASS

The result treats all integers \(m\ge2\), with a unique sink, a prescribed nonadjacent drive site, uniform recurrent initial heights, and individual-toppling counts. The comparison odometer \((2,1,\ldots,1)\) has reduced-Laplacian image \((2m-2)\mathbf e_u\), providing a valid least-action upper bound even when the comparison terminal height is negative at the drive. An explicit burning-order equivalence characterizes equality by recurrent states of the vertex-deleted graph. The Laplacian eigenspaces give the exact two determinants; stationarity gives the mean. The exponential limit follows from two standard binomial limits. Two structurally different programs independently passed complete recurrent enumeration through \(m=4\), exact symbolic determinant/Green-function checks through \(m=10\), and the deletion-bijection checks.

## Originality — PASS on examined evidence, with residual risk

Austin et al., *The Avalanche Polynomial of a Graph* (arXiv:1605.02713), sections 2, 5 and 6, give the relevant foundation, including the adjacent-drive single-toppling bound and the complete-graph and wheel polynomial calculations; they do not give a formula for an antipodal drive on \(K_{2m}\) minus a matching. Dukes–Selig (2016) analyze edge duplication and cut-vertex decomposition of recurrent configurations; these do not give the proposed event count on the two-connected cocktail-party graph. The complete-bipartite recurrence results of Aval et al. (arXiv:1307.7740) concern a different graph and do not imply the single nonadjacent-drive double-toppling event. Examined mathematical research index searches did not return an equivalent statement; one relatively close record concerns acyclic-orientation signatures on complete graphs minus matchings, not sandpile avalanches. The result requires its own burning characterization and exact asymptotic contribution, rather than merely replacing parameters in the complete-graph result. Unindexed or inaccessible stronger statements remain a historical-priority risk; a negative search is not a priority certificate.

## Mathematical value — PASS

Removing a perfect matching from a complete graph creates a unique sink-nonadjacent drive, changing the maximal avalanche odometer from a square-free one to a sharp double-toppling event. The extreme-event probability has a closed product law, its number is a natural smaller-graph spanning-tree determinant, and system-spanning events of vanishing probability nevertheless account for exactly an asymptotic \(1/e\) share of the mean toppling activity. This is an infinite-family structural and physical statement, not an arbitrary fixed-size census.

## Limitations and closest sources

The exact result does not cover other drive sites, arbitrary edge weights, complete multi-partite graphs with different part sizes, or the entire avalanche histogram. Primary references are Austin et al. (2016), https://arxiv.org/abs/1605.02713, and Dukes–Selig (2016), https://doi.org/10.1016/j.endm.2016.09.018; further comparison includes Aval et al. (2013), https://arxiv.org/abs/1307.7740. The included computational checks verify finite examples but do not independently certify the infinite proof. The novelty comparison is provisional with respect to unindexed literature.

Self-review: passed. Independent audit: not yet performed.
