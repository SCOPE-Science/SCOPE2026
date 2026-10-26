# Five-landmark resolving bases and maximally separated codes in the two-token Petersen graph

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph and let \(T=F_2(P)\) be its two-token graph. The exact metric dimension is \(\dim(T)=5\). It has **189540 metric bases**, partitioned into **1627 orbits** under the natural action of \(S_5\). The orbit-size histogram is \(1534\) orbits of size \(120\), \(90\) orbits of size \(60\), and one orbit of each size \(30,24,6\).

A five-element subset \(S\) of the configuration vertices is **three-separated** when \(d_T(x,y)\ge3\) for every distinct \(x,y\in S\). Exactly **30** three-separated five-sets exist; they are all metric bases, they are all pairwise equidistant with distance exactly \(3\), and they form two \(S_5\)-orbits of sizes \(6\) and \(24\). No three-separated set has six elements. Hence the maximum three-separated packing number is exactly \(5\).

## Assumptions and scope
The ten vertices of \(P\) are all two-element subsets of \(\{0,1,2,3,4\}\), with adjacency exactly when disjoint. The 45 vertices of \(T\) are all unordered pairs of *distinct vertices of* \(P\). Two such pairs are adjacent exactly when they differ by moving one token along one edge of \(P\) to an unoccupied vertex. Thus there are \(15\) base edges and \(15(10-2)=120\) token edges. All graph distances are unweighted shortest-path distances. A set \(S\subseteq V(T)\) resolves \(T\) precisely if the vector of distances to \(S\) differs for every pair of vertices of \(T\). The group action mentioned in this finding is the **induced natural \(S_5\)-action**, not an unproved assertion about the full automorphism group of \(T\).

## Proof
The following exhaustive finite procedure is implemented without external dependencies in `verify_resolving_petersen.py`. It provides a complete certificate for the stated finite claim, not an inference from samples.

1. Enumerate the ten underlying Petersen vertices in lexicographic order, then its 15 disjoint-pair edges. Enumerate all 45 unordered pairs of distinct underlying vertices. For every base edge and every third vertex, connect the two corresponding token states. This constructs every token edge exactly once. Breadth-first search from each of the 45 states gives the entire integer distance matrix \(D\), with diameter \(4\).
2. Index the \(\binom{45}{2}=990\) unordered pairs of distinct token states. For each prospective landmark \(s\), form the 990-bit set \(B_s=\{\{u,v\}:D_{s,u}\ne D_{s,v}\}\). By the definition of resolving, a five-set \(S\) is a metric basis candidate precisely when the bitwise union \(\bigcup_{s\in S}B_s\) includes every one of the 990 pairs.
3. Exhaust all \(\binom{45}{4}=148995\) four-subsets and find none resolving. Any smaller resolving set would extend to a resolving four-set, so no resolving set of size at most four exists. Exhaust all \(\binom{45}{5}=1221759\) five-subsets and find exactly \(189540\) resolving sets. This proves the minimum and complete basis count.
4. For each of the \(5!=120\) permutations of the five original labels, compute its induced permutation of the 45 token states and check that it preserves all token adjacencies. Form the orbit of each still-unclassified five-element basis under these 120 maps, and delete the whole orbit. The resulting counts are \(1534,90,1,1,1\) for orbit sizes \(120,60,30,24,6\); their weighted sum is \(189540\).
5. In the graph on 45 token states joining pairs of distance at least \(3\), enumerate every increasing clique using recursive common-neighbor intersections. The clique numbers by size \(1,2,3,4,5\) are \(45,480,1220,570,30\), and there are no larger cliques. Direct checks show all 30 five-cliques have all pairwise distances exactly \(3\), all resolve the 45 states, and the same induced group action partitions them into two orbits of sizes \(6\) and \(24\).

The executable verifier constructs the objects from these definitions and uses explicit assertions for all numerical statements. The finite search space is fully enumerated rather than sampled; no probabilistic or floating-point step is used.

## Verification
Run `python3 verify_resolving_petersen.py` with the Python standard library. A complete execution prints `VERIFY_OK; 45 states; 120 moves; metric dimension 5; 189540 bases; 1627 S5-orbits; 30 optimal distance-separated bases`. The code additionally checks every potential pairwise landmark distinction, every listed group map, and direct distance signatures for all 30 maximally separated bases. The count of 30 is for distinct unlabeled **five-subsets** of configurations, not for ordered five-tuples.

## Relationship to prior work
Audenaert, Godsil, Royle and Rudolph (2005 preprint) define the symmetric-square configuration graph and investigate spectral properties, but do not provide this resolving-set classification. Fabila-Monroy et al. (2009 preprint) study token-graph connectivity, diameter, cliques, colorings and Hamiltonicity, without computing resolving-basis counts for \(F_2(P)\). Bailey and Cameron (2011) determine metric dimension of the underlying Petersen graph, \(\dim(P)=3\), and discuss Johnson and Kneser graphs; this does not imply the metric dimension of the *two-token graph* of \(P\). Baskoro et al. (2025) treat a different, collision-allowing **supertoken** construction and general bounds; their theorem does not give this 45-state census. Previously computed spectral, resistance or chip-firing invariants of \(F_2(P)\) likewise do not entail the stated metric-basis count or separated-packing orbits.

## Limitations
The result is a complete finite classification on this one canonical graph, not a general formula for arbitrary token graphs. The numerical proof requires execution or independent reimplementation of the finite verifier; the output line alone is not a proof. Published and research-record overlap searches found no equivalent result but do not establish priority against unpublished or unindexed computations. The orbit assertions concern the action induced by \(S_5\) only. No independent audit has been performed.

## References
1. K. Audenaert, C. Godsil, G. Royle, T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251 (first public 2005-07-12).
2. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, D. R. Wood, *Token Graphs*, arXiv:0910.4774 (first public 2009-10-25).
3. R. F. Bailey, P. J. Cameron, *Base size, metric dimension and other invariants of groups and graphs*, Bulletin of the London Mathematical Society 43 (2011), 209–242. DOI: 10.1112/blms/bdq096.
4. E. T. Baskoro, C. Dalfó, M. A. Fiol, R. Simanjuntak, *On some metric properties of supertoken graphs*, Utilitas Mathematica 123 (2025), 19–33. DOI: 10.61091/um123-02.
