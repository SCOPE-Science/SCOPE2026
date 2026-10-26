# Two-hole crown matching slides: exact eccentricity geometry through eight columns

## Finding

Let \(n\ge3\), and let \(\operatorname{Cr}_n\) be the crown graph with vertex classes \(X=\{x_1,\ldots,x_n\}\) and \(Y=\{y_1,\ldots,y_n\}\), and edges \(x_i y_j\) exactly when \(i\ne j\). Let \(\mathcal T_n\) be the reconfiguration graph of its matchings of cardinality \(n-1\): two states are adjacent exactly when one matching edge is replaced by an edge sharing one endpoint with it, and the result is another matching of cardinality \(n-1\). Thus every state leaves exactly one vertex unmatched on each side, and a step moves one of those two holes.

The finite **exact metric classification**, for every \(3\le n\le8\), is
\[
\operatorname{diam}(\mathcal T_n)=n+\lfloor n/2\rfloor-1.
\]
If \(n\) is odd, every state has this eccentricity. If \(n\) is even, a state has eccentricity exactly one less than this diameter if and only if its two unmatched vertices have the same subscript; every other state has eccentricity equal to the diameter. Equivalently, for even \(n\in\{4,6,8\}\), the center consists of precisely \(nD_{n-1}\) states of degree \(2n-2\), where \(D_j\) denotes the number of derangements of \(j\) elements. These statements are **finite assertions through \(n=8\)**, not claims for larger orders.

The complete size, edge, orbit, radius, diameter and center census is:

| \(n\) | vertices | edges | marked-cycle orbits | radius | diameter | center size |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 9 | 12 | 2 | 3 | 3 | 9 |
| 4 | 44 | 96 | 3 | 4 | 5 | 8 |
| 5 | 265 | 840 | 5 | 6 | 6 | 265 |
| 6 | 1,854 | 7,680 | 7 | 7 | 8 | 264 |
| 7 | 14,833 | 76,020 | 11 | 9 | 9 | 14,833 |
| 8 | 133,496 | 815,808 | 15 | 10 | 11 | 14,832 |

At \(n=8\), exactly \(118{,}664\) states have eccentricity \(11\), and exactly \(14{,}832\) have eccentricity \(10\). There are exactly **\(2{,}593{,}920\) unordered diameter-eleven pairs**. The complete unordered distance count at distances one through eleven is
\[
(815808,6734112,41646864,196630980,697472160,1755796784,2817050544,2375025136,895716192,121041760,2593920).
\]

Further, for **every** \(n\ge3\), independently of the finite distance computation, \(\mathcal T_n\) has \(D_{n+1}\) vertices, degree \(2n-2\) at exactly \(nD_{n-1}\) vertices and degree \(2n-4\) elsewhere, hence exactly
\[
(n-2)D_{n+1}+nD_{n-1}
\]
edges. The graph is bipartite with bipartition sizes differing by exactly \(n\), and therefore has no spanning Hamilton path. The count of derangements and the standard sign-imbalance identity are classical ingredients, not asserted as newly discovered results.

## Assumptions and scope

All indices are fixed labels. A graph state is a matching with \(n-1\) edges, sometimes called a *deficiency-two* or *one-edge-short-of-perfect* matching; it is not a near-perfect matching in the usual sense of covering all but one vertex. A legal move has exactly one edge removed and one edge added; these two edges must share a vertex, and both endpoints of the new edge must be free after removal. Vertex relabelings are used only to reduce verification, never to identify distinct states. There are no edge weights, no parallel edges, and no transitions through matchings of other cardinalities.

For \(n\ge3\), set \(D_m=m!\sum_{j=0}^{m}(-1)^j/j!\). The automorphism action used below consists of simultaneous permutations of the indices on both bipartition classes; swapping the two classes is not needed for the argument. Radius and eccentricity always refer to the connected graph \(\mathcal T_n\). Connectivity for the finite orders follows directly from exhaustive breadth-first search; for arbitrary \(n\) it also follows from the previously published nonmaximum independent-set theorem for connected claw-free line graphs.

## Proof

**1. Exact state bijection.** Adjoin a distinguished symbol \(0\) to the indices \(1,\ldots,n\). If matching \(M\) leaves \(x_r\) and \(y_c\) unmatched, define a permutation \(p\) of \(\{0,1,\ldots,n\}\) by \(p(0)=c\), \(p(r)=0\), and \(p(i)=j\) whenever \(x_i y_j\in M\). Every image and every preimage occurs once, and there are no fixed points: forbidden diagonal edges exclude \(p(i)=i\) for nonzero matched indices, while \(p(0)\ne0\) and \(p(r)=0\ne r\). Conversely, a derangement recovers the missing row \(r=p^{-1}(0)\), missing column \(c=p(0)\), and all matching edges. This is a bijection and proves \(|V(\mathcal T_n)|=D_{n+1}\). The derangement count itself is classical.

**2. Exact adjacency.** Write \(r=p^{-1}(0)\). A slide that replaces \(x_i y_j\) by \(x_r y_j\) swaps the images in positions \(i,r\) in \(p\). A slide replacing \(x_i y_j\) by \(x_i y_c\) swaps the images in positions \(0,i\). Conversely, each such swap is a legal slide precisely when its resulting permutation is still fixed-point-free. Both swaps are genuine transpositions, and no other slides exist. In particular, the parity of \(p\) changes on every step.

**3. All-order degree, symmetry and parity assertions.** If \(r=c\), all \(2(n-1)\) endpoint slides are legal. If \(r\ne c\), there are two and only two forbidden diagonal slides: into row \(r\) from the matched column \(r\), and into column \(c\) from the matched row \(c\). Thus the two degrees are \(2n-2\) and \(2n-4\). The case \(r=c\) is equivalent to the cycle containing \(0\) in \(p\) having length \(2\). Choosing \(r\) and a derangement on the remaining \(n-1\) labels gives exactly \(nD_{n-1}\) such states. Summing degrees gives the edge formula.

Every move swaps two permutation images, so even and odd permutation signs give a bipartition. Inclusion-exclusion over fixed points, noting that the signed sum of permutations of at least two free symbols is zero, gives
\[
\sum_{\substack{p\in S_m\\p(i)\ne i\ (0\le i<m)}}\operatorname{sgn}(p)=(-1)^{m-1}(m-1).
\]
For \(m=n+1\), the bipartition-size difference is \(n\). Any Hamilton path in a bipartite graph alternates between the sides and requires their sizes to differ by at most one; therefore no such path exists here.

**4. Exact finite shortest-path certificate.** Simultaneous relabeling of the nonzero indices conjugates \(p\) by a permutation fixing \(0\), and preserves adjacency. Its orbits are exactly classified by \((k,\lambda)\), where \(k\ge2\) is the length of the cycle containing \(0\) and \(\lambda\) is a partition of \(n+1-k\) with no parts equal to one. If \(\lambda\) has \(a_j\) parts of size \(j\), the orbit has size
\[
\frac{n!}{\prod_{j\ge2} j^{a_j}a_j!}.
\]
The reason is that fixing \(0\) prevents rotation of its cycle, while the other cycles can be rotated and permuted among equal lengths. Consequently, one exhaustive shortest-path search from one representative of **each** \((k,\lambda)\) orbit gives all eccentricities and all pairwise distance counts for the entire graph: conjugation is an automorphism sending any source to its orbit representative.

The executable `verify_permutations.py` enumerates every derangement of \(n+1\) symbols, constructs all and only legal transposition neighbors by the criterion in Step 2, identifies every orbit, and runs breadth-first search (BFS) from one member per orbit. BFS explores the whole connected component and yields exact shortest-path distances, since every edge has unit length. Reachability of every vertex and edge reciprocity are asserted. For each distance, multiplying each representative's BFS sphere count by its orbit size and halving the nonzero-distance total gives the exact unordered-pair census. The complete, machine-readable sphere and pair census is in `permutation_output.jsonl`.

A second independently organized exhaustive checker, `verify_matchings.py`, instead enumerates the \(n-1\)-edge partial injections directly, constructs the matching-edge slides directly using the two unmatched vertices, and calculates the same orbit spectra and BFS distances. It does not use derangements as its graph states. Its output in `matchings_output.jsonl` agrees byte-for-byte with the first checker at each of the six orders. For \(n\in\{3,4,5,6,7,8\}\), these exhaustive finite verifications yield precisely the displayed diameter, radius, center and pair-census data. In particular, the only \(n=8\) source-orbit profiles of eccentricity \(10\) have \(k=2\); all profiles with \(k>2\) have eccentricity \(11\). For odd tested orders all source-orbit profiles have the same eccentricity.

## Verification

Reproduce using a standard Python 3 interpreter with no third-party dependencies:

```sh
python3 verify_permutations.py > permutation_replayed.jsonl
python3 verify_matchings.py > matchings_replayed.jsonl
cmp permutation_replayed.jsonl matchings_replayed.jsonl
cmp permutation_output.jsonl permutation_replayed.jsonl
cmp matchings_output.jsonl matchings_replayed.jsonl
```

The scripts enumerate \(D_{n+1}\) states for each \(3\le n\le8\), and the largest case has \(133{,}496\) vertices. The two outputs give every marked-cycle orbit, its size, every BFS sphere size, each orbit eccentricity, and every distance multiplicity. The verification checks every state and every legal neighbor, rather than randomly sampling state pairs. The finite computation does not prove any diameter formula for \(n\ge9\).

## Relationship to prior work

Bonsma, Kamiński and Wrochna (first public arXiv version, March 3, 2014) prove general reachability theorems for token sliding on connected claw-free graphs. Applied to line graphs of connected crown graphs and to matchings smaller than maximum size, their theorem supplies connectivity, but no exact labeled crown-family diameter or eccentricity census. This established connectivity is **not** claimed as new. Bousquet, Hatanaka, Ito and Mühlenthaler (2018) study shortest reconfiguration of matchings mainly under token **jumping**, with general complexity results; those are not exact numerical slide distances for the crown family. Avis and Hoang (2022) study structure of token-slide graphs and cite generic polynomial bounds for claw-free instances, but not the crown-specific metric. The classical sequence of derangement counts is OEIS A000166, and the matching interpretation of crown graphs was previously recorded; the vertex-count identity is not a novelty claim.

The potential new assertion here is the **full finite token-slide distance classification through eight crown sizes**, especially the parity-dependent exact eccentricity split and the \(133{,}496\)-vertex order-eight distance census. Other mathematical descriptions of derangements and earlier classifications of other matching-exchange graphs have different adjacency or different underlying matchings and do not automatically imply the distances computed here. No general closed form for all-order diameter is asserted.

## Limitations

The metric classification is only verified for the six finite sizes \(3\le n\le8\), by exhaustive programs with a symmetry-reduction proof. Agreement of independent implementations is evidence for the finite assertions; it does not replace all-order proof or establish any conjectured continuation. The all-order cardinality, degree, orbit and parity statements do have short proofs above. A previously unindexed crown-specific computational table or a more general distance theorem might subsume the finite distance result; publication priority has not been independently audited. No independent external review is asserted. The token-slide rule must not be confused with unrestricted token jumps, even though reachability may coincide in the relevant general theorem.

## References

1. P. Bonsma, M. Kamiński and M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, first posted March 3, 2014, arXiv:1403.0359v1, https://arxiv.org/html/1403.0359v1 .
2. N. Bousquet, T. Hatanaka, T. Ito and M. Mühlenthaler, *Shortest Reconfiguration of Matchings*, first posted December 13, 2018, arXiv:1812.05419, https://arxiv.org/abs/1812.05419 .
3. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, first posted March 31, 2022, arXiv:2203.16861, https://arxiv.org/abs/2203.16861 .
4. OEIS Foundation, *A000166 — Subfactorials or derangements*, https://oeis.org/A000166 ; contains the classical derangement counts and a crown-graph matching interpretation.
