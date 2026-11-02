# The Fano induced-matching exchange graph: a tripartite triangle geometry with diameter five

## Finding

Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane \(\operatorname{PG}(2,2)\). A *maximum induced matching* is a largest set of edges whose endpoints induce a disjoint union of edges. Form the *one-edge exchange graph* \(\mathcal E\): its vertices are maximum induced matchings of \(H\); distinct matchings are adjacent precisely when one of their three edges can be replaced by another edge, with the result again maximum and induced.

**Theorem (exact exchange geometry).** The graph \(\mathcal E\) has \(84\) vertices and \(252\) edges and is connected, tripartite, and six-regular. Its three natural parts have \(28\) vertices each; every vertex has three neighbours in each of the other two parts. Exactly \(84\) triangles occur, and every exchange edge belongs to exactly one triangle. The diameter is \(5\) and the radius is \(4\); precisely \(28\) vertices are central. The unordered-pair distance distribution at distances \(1,2,3,4,5\) is

\[
(252,840,1442,840,112).
\]

For any two maximum induced matchings \(M,N\), set \(\delta(M,N)=3-|M\cap N|\), the number of edges that must be replaced if all intermediate matchings were unrestricted. Then

\[
\delta(M,N)\leq d_{\mathcal E}(M,N)\leq\delta(M,N)+2.
\]

Among the \(\binom{84}{2}=3486\) unordered pairs, the excesses \(d_{\mathcal E}-\delta\) are \(0,1,2\) for respectively \(2492,882,112\) pairs. Every two-extra-move pair is diametral: its two matchings are disjoint and have exchange distance \(5\). All \(28\) central vertices are those matchings whose three chosen points are collinear **and** whose three chosen lines are concurrent.

The cardinality bound \(\nu_s(H)=3\), the equivalence with strong representative systems, and the separate count of \(84\) maximum triples are **not claimed as original contributions**. The claim assessed here is the exact exchange graph, its triangle/part geometry, and its complete metric.

## Assumptions and scope

A Fano flag is an incident point–line pair \((p,L)\). The \(21\) flags are exactly the edges of \(H\). Two flags \((p,L),(q,M)\) are compatible in an induced matching if and only if \(p\notin M\) and \(q\notin L\). In particular the chosen points and lines are distinct. All sets and matchings are unlabelled; a move replaces exactly one flag, not an entire strong edge-colouring or a collection of colour classes. This is a fixed-graph theorem; no assertion is made for projective planes of larger order.

For independent reproduction, one may label the seven points by the nonzero vectors of \(\mathbb F_2^3\), represented as integers \(1,\ldots,7\), and use the seven lines \(\{a,b,a\oplus b\}\) for distinct nonzero \(a,b\), where \(\oplus\) denotes coordinatewise binary addition. An independent cyclic model labels points by \(\mathbb Z/7\mathbb Z\) and uses lines \(L_j=\{j,j+1,j+3\}\) modulo \(7\).

## Proof

**Maximum size and the \(84\) configurations.** The selected point set of an induced matching has a tangent line at each selected point: a line containing that point and no other selected point. No four-point subset of the Fano plane has a tangent at every point. Indeed, if four points contain a collinear triple, then the fourth point has its three joining lines occupied; if no three are collinear, then each of the three other selected points lies on a different line through each selected point. Therefore an induced matching has at most three edges. For example, in the cyclic presentation below, the flags \((0,L_4),(1,L_5),(2,L_2)\) form a three-edge induced matching.

For three noncollinear points, each has exactly one tangent among its three lines. There are \(\binom73-7=28\) such point triples, hence \(28\) matchings. For three collinear points, the common line is not tangent, while each point has exactly two choices of tangent. The seven collinear point triples therefore give \(7\cdot2^3=56\) further matchings. Thus there are \(84\) maxima.

**Three natural types.** Classify a maximum matching by whether its selected three points are collinear and its selected three lines concurrent. The three possible types are: \(A\), noncollinear points and concurrent lines; \(B\), collinear points and nonconcurrent lines; and \(C\), collinear points and concurrent lines. The impossible fourth type has noncollinear points and nonconcurrent lines. For noncollinear points the uniquely selected tangents meet in the fourth point of their complementary affine configuration, yielding \(28\) type-\(A\) matchings. For each of the seven possible common point-lines, the \(2^3\) choices of three tangents split into four concurrent and four nonconcurrent configurations, yielding \(28\) of each of types \(B,C\).

**Every compatible pair has exactly three completions.** Fix two compatible flags \((p,L)\) and \((q,M)\). The lines \(L,M\) intersect at a point other than \(p,q\), and their union has five points. Thus the third selected point must be one of the two points outside \(L\cup M\). One is the third point \(t\) of the line \(pq\); at \(t\) there are exactly two tangent-line choices avoiding \(p,q\). For the other outside point there is exactly one tangent line avoiding \(p,q\). The resulting three maximum matchings have types \(A,B,C\), one of each.

There are \(21\) possible first flags and each is compatible with eight others (four points outside its line, with two eligible lines through each point), hence \(21\cdot8/2=84\) unordered compatible pairs. In the exchange graph, the three extensions of any such pair form a triangle. Each maximum matching has three contained compatible pairs, each with exactly two alternate completions, so it has six neighbours: three in each other type. Each edge of \(\mathcal E\) fixes a unique two-flag pair, giving a unique such triangle. To see there are no additional triangles, observe that three pairwise adjacent triples with no common two-flag pair would use four flags, every two of which occur together in one triple, creating a forbidden four-edge induced matching. Hence the listed \(84\) triangles are all triangles, and \(\mathcal E\) is tripartite.

**Exact distances and central vertices.** The remaining metric assertions have a finite exhaustive certificate. With the seven lines specified above, construct all \(\binom{21}{3}=1330\) flag triples and retain those whose three pairs are compatible. Construct an adjacency between two retained triples exactly when their intersection contains two flags. Breadth-first search from each of the \(84\) triples visits the entire graph and yields the stated distance and excess distributions. The program `verify_direct.py` implements precisely these finite loops and checks the forbidden four-flag possibilities among all \(\binom{21}{4}=5985\) subsets.

An independent certificate `verify_cyclic.py` begins instead with the \(84\) compatible *pairs* in the cyclic model, generates their three completions, builds the exchange edges as the three sides of each completion triangle, and enumerates the \(168\) collineations preserving the seven lines. Those collineations have exactly three orbits, the classes \(A,B,C\), each of size \(28\). Breadth-first search from one representative of each orbit gives the following distance profiles at distances \(0,1,2,3,4,5\):

\[
\mathrm{prof}(A)=\mathrm{prof}(B)=(1,6,21,34,18,4),\qquad \mathrm{prof}(C)=(1,6,18,35,24,0).
\]

The full point-line duality swaps the first two classes and preserves the third. Since collineations preserve all exchange distances and are transitive on each class, multiplying these profiles by the class sizes and dividing the nonzero-distance totals by two proves the complete pair-distance distribution, centrality and diameter. Computing \(3-|M\cap N|\) for each unordered pair establishes the exact excess counts. Both certificates have independent Fano constructions and independent adjacency-generation procedures.

## Verification

Run each embedded standalone program with Python 3, using only the standard library:

```sh
python3 verify_direct.py
python3 verify_cyclic.py
```

The expected terminal markers are `DIRECT_FANO_FLAG_EXCHANGE_PASS` and `CYCLIC_FLAG_PAIR_AND_AUTOMORPHISM_PASS`. Both programs were executed from the packaged files successfully. The direct program checks every possible three- and four-flag subset, all \(252\) exchange edges, the \(84\) triangles, all \(84\) breadth-first searches, and all \(3486\) unordered-pair distances. The second constructs all \(84\) compatible pairs, verifies three completions for each, enumerates all \(168\) collineations, and checks three orbit-representative breadth-first searches. These are finite exhaustive arguments, not inferences from random sampling.

## Relationship to prior work

Illés, Szőnyi and Wettl introduced strong representative systems in finite projective planes and established general size bounds; their concept is the flag formulation of induced matchings used here. Basavaraju and collaborators proved upper bounds and enumeration algorithms for maximal induced matchings in triangle-free graphs. Those results do not state the distance geometry of single-flag exchanges among the maximum Heawood systems. The Heawood count of \(84\) compatible triples already appears as intermediate data in a separate strong-edge-colouring partition census; that work studies swaps of whole colour classes in complete partitions, not the present graph whose vertices are individual induced triples. These configurations and move relations must not be conflated. Dejter studied a different Fano-derived \(84\)-vertex graph, explicitly four-regular, rather than this six-regular exchange graph. No absolute claim of historical priority is made.

## Limitations

The result concerns only the Fano incidence graph and one-flag exchanges. It does not generalize the diameter bound to larger projective planes or characterize strong-edge-colouring partition trades. The metric component is proved by exact finite search, with source code supplied and its full finite search space specified. An equivalent description under strong-representative-system, tangency-set, or finite-geometry terminology may have escaped the inspected sources; the historical comparison is not exhaustive.

## References

1. T. Illés, T. Szőnyi and F. Wettl, *Blocking sets and maximal strong representative systems in finite projective planes*, Mitt. Math. Sem. Giessen 201 (1991), 97–107. Author-posted text: https://www.researchgate.net/publication/255720223_Blocking_sets_and_maximal_strong_representative_systems_in_finite_projective_planes
2. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei and Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180v1 (first public version 18 December 2013). https://arxiv.org/abs/1312.5180
3. I. J. Dejter, *On a \(\{K_4,K_{2,2,2}\}\)-ultrahomogeneous graph*, Australas. J. Combin. 44 (2009), 63–75. https://ajc.maths.uq.edu.au/pdf/44/ajc_v44_p063.pdf
4. T. Hibi, A. Higashitani, K. Kimura and A. Tsuchiya, *Dominating induced matchings of finite graphs and regularity of edge ideals*, arXiv:1412.3881 (2014). https://arxiv.org/abs/1412.3881
