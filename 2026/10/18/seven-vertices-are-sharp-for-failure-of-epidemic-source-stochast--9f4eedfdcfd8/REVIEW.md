# Independent mathematical audit

## correctness

PASS

The independent-bond percolation tail at threshold k is the exact Bernstein sum over open edge subsets grouped by size j; one uniform coefficient sign for every k,j proves a common stochastic ordering for all 0<p<1. Prüfer words enumerate every labeled tree for n=2..6, and every root pair, edge subset, threshold and j is checked. Separate independent exact BFS/union-root implementation covered 1441 labeled trees, 20796 unordered source pairs and 609408 coefficient differences, with ZERO conflicting signs. On the seven-vertex (3,2,1) spider, exact open-subset calculations give root 2 versus leaf 6 tails: +p(1-p) at k2, 0 at k3, -p^4(1-p) at k4, +p^4(1-p)^2 at k5, +p^5(1-p) at k6, 0 at k7. The opposite signs persist for every interior p; summing gives positive expected difference p(1-p). No extrapolation to larger trees or dependent SIR is made.

## originality

PASS

Best-of-knowledge no covering exact stochastic-tail ranking result found. Kenah and Robins define independent bond versus correlated SIR epidemic representations; Holme and Bucur-Holme analyze small-graph node importance/mean outbreak and estimators, not the universal pairwise first-order stochastic dominance theorem on all at-most-six trees. The new small sharp threshold and all-p counterexample answer a different distributional question. Rooted reliability/tree-branching polynomial terminology remains a priority risk.

## value

PASS

Smallest-possible counterexample delineates when choosing a fixed source by mean influence can disagree with strict-majority outbreak risk, uniformly in bond probability. The complete six-vertex lower bound makes the boundary exact rather than anecdotal numerical graph simulation; relevant to risk-based selection of seed nodes and stochastic-order graph invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
