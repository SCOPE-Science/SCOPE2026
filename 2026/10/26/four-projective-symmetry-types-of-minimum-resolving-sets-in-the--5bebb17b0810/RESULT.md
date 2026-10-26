# Four projective symmetry types of minimum resolving sets in the ternary projective plane

## Finding

Let \(G\) be the point–line incidence graph of \(\operatorname{PG}(2,3)\). A *resolving set* is a subset \(S\) of its vertices such that the vectors of graph distances to \(S\) distinguish all vertices. The previously determined metric dimension is \(\dim(G)=8\). The new exact classification is that there are **9,828** resolving sets of cardinality eight, all containing **four points and four lines**, and precisely **four orbits** under the full incidence-graph automorphism group.

| Selected point–line incidence graph | Number of bases | Full symmetry-orbit size | Stabilizer order | Collinear point triples / concurrent line triples |
| --- | ---: | ---: | ---: | --- |
| One edge, six isolated vertices | 936 | 936 | 12 | 0 / 0 |
| Two disjoint edges, four isolated vertices | 1,404 | 1,404 | 8 | 0 / 0 |
| Three disjoint edges, two isolated vertices | 1,872 | 1,872 | 6 | 1 / 1 |
| Three-edge path, four isolated vertices | 5,616 | 5,616 | 2 | 0 / 0 |

The four orbits together account for every basis: \(936+1404+1872+5616=9828\). The orbit sizes refer to **sets of eight graph vertices**, not to individual point/line vertices.

## Assumptions and scope

Take the finite field \(\mathbb F_3=\{0,1,2\}\). The 13 points are the one-dimensional subspaces of \(\mathbb F_3^3\): represent each by the unique nonzero triple \((a,b,c)\) whose first nonzero coordinate is one. The 13 lines are the same normalized coefficient triples \([u,v,w]\); a point lies on a line precisely when \(au+bv+cw=0\) in \(\mathbb F_3\). Thus \(G\) has 26 vertices and is a connected, four-regular bipartite graph. All graph edges have unit length. An incidence among selected vertices means an edge between one of the four selected points and one of the four selected lines.

The full automorphism group acts by projective collineations and correlations. Its order is \(2|\mathrm{PGL}(3,3)|=11232\); no field automorphisms occur over \(\mathbb F_3\). The result is specifically for this 26-vertex graph; it is not a claim about larger projective planes or minimal-but-not-minimum resolving sets.

## Proof

**(1) Exact distance test.** For two distinct points or two distinct lines, the distance is two. The distance between a point and a line is one if incident and three otherwise. Distances to a selected vertex itself are zero. These rules follow directly from the projective-plane axioms: two distinct points determine one line, and two distinct lines meet in one point.

For any two different vertices \(x,y\), form the 26-bit mask of landmarks at different distances from them:
\[
W(x,y)=\{s\in V(G):d(x,s)\ne d(y,s)\}.
\]
A subset \(S\) resolves \(G\) if and only if it intersects every such mask. This is a direct reformulation of metric resolution, with no probabilistic or asymptotic step.

**(2) Exhaustive finite lower bound and count.** Generate all 13 normalized point triples and 13 normalized line triples, construct the 26-by-26 distance array by the displayed rule, and test every seven-element vertex subset against the \(\binom{26}{2}=325\) separating masks. Exactly zero of the \(\binom{26}{7}=657800\) candidates resolve. By upward closure of the resolving-set property, no smaller set resolves either. Test all \(\binom{26}{8}=1562275\) eight-element subsets. Exactly 9,828 pass, and all passers have four points and four lines. The included C++17 program implements the complete two-size enumeration and prints its checked totals.

**(3) Independent incidence test.** A selected point or line resolves itself from every other vertex of its own type by the zero distance. Among *unselected* lines, their distance profiles are identical precisely when their incidence signatures on the selected points coincide. Dually, among unselected points, equality is equivalent to identical incidence signatures on selected lines. Point–line pairs cannot have equal distance profiles to a nonempty landmark set because the incidence graph is bipartite and opposite types have distances of opposite parity to every landmark. Thus these two incidence-signature tests are necessary and sufficient. The separate Python program examines every one of \(\binom{13}{4}^2=511225\) four-point/four-line candidate, independently reproduces 9,828 winners, and splits them by the number of selected incidences and projective collinear/concurrent triples as shown in the table. It separately checks that a one-sided semi-resolving set needs at least six points (or six lines), consistent with the existing literature.

**(4) Full symmetry classification.** Act on point triples by four invertible linear maps: interchange the first two coordinates, add the second coordinate to the first, multiply the first coordinate by two, and cyclically shift coordinates. Act on line coefficients by inverse transpose, and add the polarity that exchanges point \((a,b,c)\) with line \([a,b,c]\). These five incidence-preserving generators produce exactly 11,232 permutations of the 26 vertices. This is the full group by the fundamental theorem of projective geometry (over \(\mathbb F_3\), a point/line-preserving automorphism is projective linear; an exchanging automorphism composes with the displayed polarity to become one). The C++17 verifier explicitly constructs the generators, checks preservation of all distances, enumerates the generated group and computes orbits of **all 9,828** accepted subsets. There are exactly four, of sizes \(936,1404,1872,5616\). Orbit–stabilizer gives \(12,8,6,2\) as the respective stabilizer orders. For each orbit the selected incidence structure and the point/line triple counts agree with the table. Since these induced incidence structures are different, the four classes cannot merge under an automorphism.

For fully explicit witnesses, the four orbit representatives can be read from the `orbit classes` output of the C++17 program. The displayed normalized triples specify both selected point coordinates and selected line coefficients and permit direct reconstruction of every orbit by the five generators.

## Verification

Run `g++ -O3 -std=c++17 pg3_resolving.cpp -o pg3_resolving && ./pg3_resolving` and `python3 pg3_independent.py` with standard C++17 and Python 3. The first program prints `VERIFY_OK` after verifying the seven- and eight-subset enumerations, the 11,232-element group, all four basis orbits, and their stabilizer sizes. The second independently checks the 9,828 count and the four geometric profiles using incidence signatures rather than graph-distance masks. Both programs finish by exhaustive finite computation, not by sampling. The exact tested source files are embedded alongside this document.

## Relationship to prior work

Héger and Takáts (first public preprint July 23, 2012) already state that the metric dimension of \(\operatorname{PG}(2,3)\)'s incidence graph is eight, prove the general upper bound, and classify minimum resolving sets for sufficiently large orders \(q\ge23\). They also analyze split/semi-resolving sets. In particular, their small-order semi-resolving bound highlights that the optimal eight landmarks here necessarily rely on a joint point–line selection rather than a split construction. The value eight is therefore **not** claimed to be new. Bailey (2013 preprint; 2015 article), Table 4, independently tabulates the same dimension eight, but does not give a census of the optimum bases. The present contribution is exactly the size-eight count, forced balance, four full-group orbits, and their geometric distinction; none is an implication of merely knowing the minimum size or the large-order classification.

## Limitations

This is a complete **finite** classification for the single projective plane of order three, not an infinite-family result or an independent human audit. It relies on reproducible exhaustive enumeration of 657,800 seven-sets and 1,562,275 eight-sets. The origin of the group description is standard finite projective geometry; the explicit group closure, however, is also checked computationally. Unindexed tables, informal computational notes, or supplementary data could contain overlapping classifications not found by the targeted searches; the absence of a database hit does not prove absolute priority.

## References

1. T. Héger and M. Takáts, *Resolving Sets and Semi-Resolving Sets in Finite Projective Planes*, Electronic Journal of Combinatorics 19(4), P30 (2012), first public preprint July 23, 2012. `arxiv:1207.5469`; DOI `10.37236/2582`. Full journal PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i4p30/pdf/ .
2. R. F. Bailey, *The Metric Dimension of Small Distance-Regular and Strongly Regular Graphs*, Australasian Journal of Combinatorics 62 (2015), 18–34, preprint December 17, 2013. `arxiv:1312.4973`. Full text: https://www.math.mun.ca/rbailey00/papers/small.pdf .
3. R. F. Bailey and P. J. Cameron, *Base Size, Metric Dimension and Other Invariants of Groups and Graphs*, Bulletin of the London Mathematical Society 43 (2011), 209–242. DOI `10.1112/blms/bdq096`.
