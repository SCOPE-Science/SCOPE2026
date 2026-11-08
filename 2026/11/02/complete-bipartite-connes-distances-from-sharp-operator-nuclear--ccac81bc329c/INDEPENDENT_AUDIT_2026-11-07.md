# Independent mathematical audit

## correctness

PASS

For unweighted adjacency D of K_{p,q}, integers p,q>=2, directly derived the commutator off-diagonal block M=a 1_q^T-1_p b^T and ||[D,diag(f)]||=||M||_op. Row-difference bound and rank-one equality witness give sqrt(2/q) within p-part and sqrt(2/p) within q-part. For cross pairs, the explicit rank-two partial isometry gives (sqrt(p-1)+sqrt(q-1))/sqrt(pq); the displayed Y has both exact e1 marginals, and its 2x2 nuclear norm equals this witness by the Frobenius-plus-determinant identity. The inequality is sharp in all p,q including p=q=2. Five fresh floating-point SVD certificate checks corroborate identities; analytic matrix duality proves the full infinite family, not sampling.

## originality

PASS

Clare–Li–Poon–Swartz (2024) define the same adjacency-Dirac spectral distance and solve paths, not K_{p,q}. Besnard (2021) proves universal geodesic/degree estimates and pruning comparisons, not exact biclique distances. Classical finite-space results cover small vertex totals but do not provide the all-biclique three-pair-type formula. No equivalent family result found in the targeted published records; alternate matrix-norm formulas remain a plausible priority risk.

## value

PASS

Connes distance with an adjacency Dirac operator is not shortest-path distance and is difficult beyond tiny graphs because edges couple in the spectral norm. The first explicit all-size bipartite exact three-type classification with attaining primal-dual nuclear certificates supplies a natural benchmark and quantifies dependence on both shore sizes, rather than a numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
