# Independent mathematical audit

## correctness

PASS

Reconstructed both 16-vertex graphs, confirmed 48 edges, degree 6 and exactly two common neighbors on every distinct pair, and used Floyd–Warshall vertex distances followed by exact vertex-to-edge minima. A fresh program exhausts all landmark subsets from zero through the claimed minimum, testing resolution by refining partitions of the edge set with each landmark. The minimum families have sizes 736 at size six (Shrikhande) and 576 at size five (rook), with no smaller resolving set. An unrestricted adjacency/nonadjacency-preserving bijection search independently gives the full groups of orders 192 and 1152, hence all stated orbit sizes and least hexadecimal representatives. The published stabilizer bounds also work: each local graph is the stated cycle or pair of triangles, and each nonneighbor of the fixed vertex has a different neighborhood within that local graph. Tested every pair of bases by symmetric difference of size two, obtaining one component for each graph, 4128 and 3744 edges, and degree distributions respectively {6:64,10:192,11:192,13:192,14:96} and {13:576}. Replay: python3 /workspace/reproductions/metric_review.py. The proof is exhaustive for these two labeled graphs with vertex landmarks and exactly one replacement, and does not infer a general strongly regular graph theorem.

## originality

PASS

The established graph parameters, group orders and edge resolution definition are background, not the contribution. The census and exchange results concern minimum vertex sets resolving adjacent endpoint pairs. The strongest available same-graph literature/records instead resolve all small vertex sets, ordinary vertex pairs with failure tolerance, or ordinary vertex pairs with multiple witnesses. None of their inspected claims supplies the two exact minima together with the minimum-basis orbits and exchange geometry.

## value

PASS

These are the natural two same-parameter strongly regular graphs on which to ask whether those parameters determine edge localization. Different minimum sensor counts already provide an exact counterexample. The census further determines whether optimum placements are symmetry-equivalent and whether one-at-a-time replacements maintain resolution, showing contrasting orbit structure and exchange regularity rather than just tabulating a graph order. These finite answers can be used without a general graph-family extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
