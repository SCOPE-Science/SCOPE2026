# Independent mathematical audit

## correctness

PASS

Reconstructed degree-pair interpolation: any 16-edge graph with one degree >=8 or two degrees on the same side summing >=8 has an 8-edge induced bipartite subgraph; any degree submultiset summing 8 works by taking all opposite vertices. If no such split, integer partitions on either side are necessarily P=(4,3,3,3,3) or Q=(3,3,3,3,3,1). This is an order-independent argument despite unbounded isolated vertices. Independently wrote, compiled and executed a different column-mask exhaustive C++ generator, not the supplied row-mask code, over ALL four residual fixed degree-sequence matrices: 906, 6720, 6720, 43440, total 57,786; every single matrix admits a row+column subset containing exactly eight ones. Smaller dyadic half-splits 2,4,8 follow stars and pair interpolation. Recursive binary query split of a 2^r-edge subfamily constructs a depth-r shattered tree. Any arbitrary m in [1,31] contains 2^floor(log2 m) edges, and adding hypotheses cannot decrease Ldim; info bound 2^r<=m supplies equality. Upper bound valid for all finite hypothesis classes. Finite exhaustive program alone is not a proof for arbitrary orders: the explicit prior degree-partition reduction provides the needed unbounded-vertex link. No claim at 32 or more edges.

## originality

PASS

Best-of-knowledge PASS: compared an exact bipartite induced-half-edge statement, unrestricted in vertex order, against published interpolation results and online-dimension closure bounds. The inspected Alon-Krivelevich-Sudakov Lemma 4.1 bounds a shorter interval by partition-side size and does not imply eight for residual P,Q; general Boolean closure bounds likewise do not force exact edge-conjunction Ldim. Specific 16-edge priority remains qualified by limited indexing of combinatorial finite cases.

## value

PASS

The 16-edge case is a small but intrinsically motivated dyadic threshold within the long-standing induced-half-edge problem: the exact finite cutoff is universal over bipartite graphs of arbitrary order, not a bounded-vertex computation. Its consequence is a complete sharp online mistake-dimension law through 31 edge hypotheses. This is a natural classification of the binary query capability, not an unmotivated arbitrary slice; larger dyadic thresholds remain open or unclaimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
