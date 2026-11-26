# Exact metric-basis reconfiguration of the Tutte–Coxeter graph under token jumping and sliding

## Finding

Let \(T\) be the Tutte–Coxeter graph, the cubic incidence graph of duads and synthemes on a six-element set. A *metric basis* is a minimum-cardinality set of vertices whose distance vectors distinguish every vertex. Bailey [1] gives the minimum cardinality \(6\). The exhaustive census of \(32{,}460\) bases and their bipartition counts were already published [2]; here they specify the state space, not a new enumeration claim.

**Theorem.** The two graphs of single-landmark relocations between metric bases have the following invariants:

| Invariant | Token jumping | Token sliding |
| --- | ---: | ---: |
| Undirected edges | 403,020 | 55,440 |
| Connected components | 1 | 1 |
| Radius | 7 | 17 |
| Diameter | 8 | 20 |

For jumping, there are \(31{,}740\) bases of eccentricity \(7\) and \(720\) of eccentricity \(8\). The \(720\) bases of eccentricity \(8\) form a single orbit under the natural \(S_6\) action. For sliding, the numbers at eccentricities \(17,18,19,20\) are \(3780,11040,10440,7200\), respectively.

## Assumptions and scope

A duad is a two-element subset of \(\{0,1,2,3,4,5\}\); a syntheme is a partition of this set into three duads. Adjacency in \(T\) is membership of a duad in a syntheme. Resolution uses ordinary, unweighted graph distances. Two bases are adjacent in the jump graph precisely when their symmetric difference consists of two vertices. A jump is a slide if the outgoing and incoming vertices are adjacent in \(T\). Every state must remain a minimum resolving set; no nonresolving intermediate configuration or seventh landmark is allowed.

## Proof

The supplied exact enumerations give a finite proof. In `verify_metric_A.py` construct the fifteen duads, fifteen synthemes, and all incidences. Compute all distances by breadth-first search. For each landmark, mark every unordered pair it distinguishes; a set resolves exactly when its marked pairs cover all \(435\) pairs. Exhaustively test the subsets of sizes one through six, recovering the known state census. To enumerate jumps, for each basis delete each of its six vertices and try each of the twenty-four vertices outside the original basis; retain exactly the resulting sets in the basis list. Each undirected edge is counted in both directions. The slide graph keeps precisely the retained substitutions that traverse an incidence in \(T\). The exact edge counts are those in the table.

Permutations of the six underlying symbols preserve incidence, then distances, resolution, and both kinds of moves. Thus eccentricity is constant on each orbit. Apply the five adjacent transpositions until closure to partition the known basis list under \(S_6\): the computation finds 62 orbits (orbit sizes and multiplicities \(720:32,360:24,180:2,120:2,90:2\)). These are the classes used for the breadth-first searches; this auxiliary count is not needed as a separate novelty claim. From one representative per orbit, breadth-first search in each relocation graph reaches every state. Weighting its greatest distance by its orbit size gives the stated eccentricity distributions. Their least and greatest values give the radii and diameters. Exactly one representative in the jump calculation has greatest distance eight; its orbit has size 720. In the script's lexicographic duad and generated syntheme indexing, the representative is \((0,1,12,15,21,22)\).

The supplied `verify_metric_B.py` cross-checks the figures using the symplectic point–line model over \(\mathbb F_2^4\), direct distance signatures, grouping by common five-element subsets for jumps, incident replacements for slides, and symplectic transvections for breadth-first-search reduction. The natural \(S_6\) claim is certified directly by the duad–syntheme calculation above.

## Reproducibility

The frozen certificate files `verify_metric_A.py` and `verify_metric_B.py` use only Python's standard library; their captured outputs are supplied as `verify_metric_A.out` and `verify_metric_B.out`. They certify a finite classification on this graph and do not imply reconfiguration results for any other graph or landmark budget. The previously known census is recomputed as input to the dynamic classification.

## Relationship to prior work and limits

The full automorphism-group census in [2] supplies the same basis count and bipartition profile and classifies bases into 34 orbits under a group of order 1,440. It is not a classification of distances or connectedness under the two relocation rules. Restriction to the natural part-preserving \(S_6\) action gives an orbit refinement used here for the searches. The contribution is the exact reconfiguration analysis, including the identification of a whole exceptional jump-eccentricity orbit, not the number of bases or a standalone symmetry census.

Bailey [1] studies minimum resolving-set cardinality and Bartoli et al. [3] give bounds for generalized quadrangles. Public material on metric-basis reconfiguration [4] discusses the general problem. The full text of the associated thesis was not available for comparison; cage-specific overlap there or in unindexed work remains possible.

## References

1. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, https://arxiv.org/abs/1312.4973v1, Table 3.
2. *All 32,460 metric bases of Tutte's eight-cage in 34 symmetry classes*, https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-all-32-460-metric-bases-of-tutte-s-eight-cage-in-34-symmetry-cla--b94e989474bf, Finding and orbit census.
3. D. Bartoli, T. Héger, G. Kiss and M. Takáts, *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, https://arxiv.org/abs/1706.06583v1, §4.
4. J. Morentin, *The Reconfigurations of Metric Bases*, public presentation abstract, https://www.cpp.edu/sci/mathematics-statistics/docs/colloquium/2021_2022_jimmy_morentin.pdf.
