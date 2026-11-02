# Scientific assessment

## Correctness

**PASS.** The universal induced-two-edge-matching tail follows by a complete same-edge/shared-endpoint/disjoint-edge analysis. If a pair of disjoint edges has any cross-adjacency, its distance cannot exceed \(5/2\); if not, diameter two forces every cross-endpoint distance to equal two. The conditional tail is an elementary triangle-area calculation. The finite pair comparison defines both graphs explicitly, enumerates every one of their \(1128\) unordered distinct-edge pairs using exact integer distances, and reduces the difference of distance laws to convex-polygon areas. The polygon vertices move affinely between half-integer thresholds, so three exact rational evaluations certify each quadratic branch. The packaged standalone verifier performed these checks with exact rational arithmetic and passed.

## Originality

**PASS, subject to historical-priority risk.** The nearest existing general result is Wei–Walteros–Batta's full forward framework for calculating random-edge-location distance distributions on arbitrary networks; such a framework can evaluate either graph but does not present the structural inverse recovery of induced two-edge matchings or the exact Shrikhande/rook cancellation and squared-tent difference. Gamble et al. study distinguishability of strongly regular graphs via quantum walks instead of the arclength-intrinsic metric statistic. Published geometric-topology comparisons distinguish this graph pair by different homotopy invariants. Published records and the present source comparisons did not reveal the stated sharp distance-law identity. A sufficiently explicit but uninspected historical distance-table result could subsume it, and a general distance-law algorithm supplies an indirect route to the finite calculation; this residual coverage risk is acknowledged rather than asserted away.

## Mathematical value

**PASS.** The Shrikhande/rook pair is a canonical obstruction to reconstruction from degree, vertex distances, and adjacency spectrum. An exact observable that is provably blind on a whole interval and then sharply discriminating is a natural inverse metric-geometric fact, not an arbitrary numerical instance. The universal diameter-two tail identifies what the new observable measures structurally: the exact induced-two-edge-matching count. Its square-tail formula applies to an entire graph class and supplies a reproducible diagnostic threshold.

## Limitations

All graph edges must have equal metric length, and the universal identity requires vertex diameter at most two. The pair comparison does not imply graph reconstruction for arbitrary strongly regular graphs. Some general published distance algorithms can compute this case by specialization, so an older explicit simplification remains possible; no independent historical-priority audit is claimed.

Self-review: passed. Independent audit: not yet performed.
