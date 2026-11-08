# Independent mathematical audit

## correctness

PASS

For the 20-vertex cubic GP(10,2), after deleting k vertices with e(S) internal edges the 20−k complement has 30−3k+e(S) edges. Forest inequality <=19−k implies 11+e(S)<=2k, so every FVS has k>=6. Exact enumeration of all C(20,6)=38,760 six-subsets finds 2,520 valid minima, with 660 e(S)=0 and 1,860 e(S)=1. For each state, the complete token-slide adjacency list is obtained by exchanging a selected vertex for an adjacent unselected vertex and retaining the move exactly when the new mask is in the enumerated optimal set. A fully independent Python reconstruction performed the complete search (not a sample) and all 2,520 BFS distance sweeps: one connected graph, 8,880 edges, stratum edges 1,620/4,140 and crossing 3,120, eccentricities exactly 120 at distance 8, 2,340 at 9, 60 at 10. Therefore radius 8 and sharp diameter 10; stratum connectivity follows the supplied component search. The original two independent programs use DSU vs leaf-pruning and transition detection by moves vs pairwise symmetric differences. Such a complete finite exhaust does prove this one finite statement, but not a general graph-family theorem.

## originality

PASS

The known 2,520-state dodecahedral minimum FVS census and unrestricted token-jump graph (23,940 edges, diameter six) are prior information and explicitly excluded from novelty. The locally adjacent token-slide relation is strictly more restrictive; unrestricted FVS reconfiguration results for planar subcubic graphs do not imply its connectivity or its diameter ten. The exact slide graph profile is qualified as original for this single natural graph.

## value

PASS

The dodecahedron is a canonical cubic large-girth object and the minimum-feedback-set space is a natural optimization landscape. Connectivity and sharp distances under physically local token slides are mathematically different from known arbitrary-jump connectivity; the full radius/eccentricity/stratum profile is a complete motivated finite classification, not an arbitrary isolated count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
