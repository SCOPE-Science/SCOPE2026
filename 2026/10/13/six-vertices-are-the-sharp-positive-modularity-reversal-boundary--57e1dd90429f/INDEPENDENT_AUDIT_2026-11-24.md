# Independent mathematical audit

## correctness

PASS

For one bipartition the internal edge fraction is (m−c)/m and its null term is (a^2+b^2)/(4m^2), with a+b=2m. Thus Q=(ab−2mc)/(2m^2) and Ncut=2mc/(ab), proving the stated identity, positivity equivalence, and opposite numeric monotonicity at fixed ab. Independently exhausted connected graph orbits through six, all partitions by smaller-side representatives (lexicographic on equal halves), and all unordered partition pairs. Used the integer signs of the difference of ab−2mc and the cross-product comparison of c/(ab), requiring Q>0 for both splits. Orbit-weighted labeled counts are zero strict reversals through five and 420 at six. Explicit relabelings of both decorated witnesses yield disjoint orbits of sizes 360 and 60 that exhaust the 420; the exact Q, Ncut and cut/volume statistics also match. The positivity restriction is substantive: with no positivity requirement the independent census finds 180 labeled strict reversals at order five, including pairs with both Q negative. Replay: python /workspace/replay_frozen_graphs.py 3, output /workspace/replay_3.log.

## originality

PASS

The supported distinct result is the exact sharp positive-modularity reversal boundary at six and the complete two-class decorated first layer. The standard objective definitions, their elementary balance identity, and the spectral algorithm connection do not by themselves constitute novelty. The strongest checked connection concerns the relaxation and does not cover discrete rankings.

## value

PASS

These are standard but differently balanced discrete community scores. The positive-modularity filter keeps both splits above the null baseline, so the disagreements are not merely artifacts of comparing two poor partitions. The two minimal decorated graph types and exact objective values provide diagnostic cases for whether an objective or code really responds to volume balance as intended, despite a connection between spectral relaxations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
