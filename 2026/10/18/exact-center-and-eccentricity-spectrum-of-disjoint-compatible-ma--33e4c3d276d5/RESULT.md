# Exact center and eccentricity spectrum of disjoint-compatible matchings on eighteen convex points

## Finding

Let \(G\) be the disjoint compatibility graph \(\mathrm{DCM}_9\) of noncrossing perfect matchings on eighteen labeled points in strictly convex position. Let \(B\) be its unique component of order \(4070\). Then
\[
\operatorname{rad}(B)=10,\qquad \operatorname{diam}(B)=15.
\]
The center of \(B\) consists **exactly** of the two perfect matchings formed by alternating boundary edges of the eighteen-gon. Its entire eccentricity distribution is

| Eccentricity | Number of matchings in \(B\) |
|---|---:|
| \(10\) | 2 |
| \(11\) | 480 |
| \(12\) | 483 |
| \(13\) | 1,377 |
| \(14\) | 1,368 |
| \(15\) | 360 |

There are \(4862\) noncrossing perfect matchings in total, and the full graph has \(8677\) edges, \(612\) isolated vertices, \(36\) components isomorphic to \(K_{1,4}\), and the single big component \(B\). These totals and component sizes are consequences of the earlier component-count and edge-enumeration results of Aichholzer, Asinowski and Miltzow; **they are included as independent checks, not as new claims**. The new finite result is the exact metric profile and unique center of the big component.

## Assumptions and scope

The eighteen points are labeled \(0,1,\ldots,17\) in strict cyclic order; their precise coordinates do not matter. A configuration consists of nine straight chords forming a perfect matching, with no two chords crossing in their interiors. The edge between configurations \(M\) and \(N\) exists precisely when \(M\cap N=\varnothing\) and no chord of \(M\) crosses a chord of \(N\) in its interior. Shared endpoints of distinct chords are permitted. All graph distances and eccentricities in the finding are computed **within the connected component** \(B\); no finite distance is asserted between different components. Eccentricity is maximum shortest-path distance to another vertex in the same component; radius and diameter are the minimum and maximum eccentricities, respectively.

Write
\[
R_0=\{\{0,1\},\{2,3\},\ldots,\{16,17\}\},\qquad
R_1=\{\{0,17\},\{1,2\},\{3,4\},\ldots,\{15,16\}\}.
\]
Then \(\operatorname{Center}(B)=\{R_0,R_1\}\).

## Proof

This is an exhaustive finite proof with two independent constructions of the graph. The algorithms are supplied in full in `verify_chord_masks.py` and `verify_dyck_dp.py`, use only the Python standard library, have no external data dependencies, and assert all final numerical conclusions. The completeness and shortest-path correctness of the computations follow from the following elementary reductions.

**Exhaustive vertex enumeration.** Every noncrossing perfect matching on consecutively labeled points \(a,\ldots,b\) pairs \(a\) with a point \(j\) of opposite parity. Its remaining chords divide uniquely into a noncrossing perfect matching on \(a+1,\ldots,j-1\) and one on \(j+1,\ldots,b\). Conversely, any such pairing and two such submatchings are noncrossing. Induction proves that the interval recursion in `verify_chord_masks.py` enumerates every configuration exactly once. Independently, marking every lower chord endpoint with an opening parenthesis and the higher endpoint with a closing parenthesis gives a balanced parenthesis word, and the stack matching of the word recovers the chords. This is a bijection with Dyck words of semilength nine; `verify_dyck_dp.py` enumerates all \(\binom{18}{9}\) choices of opening positions and retains exactly the balanced ones. Both constructions obtain the Catalan number \(\frac1{10}\binom{18}{9}=4862\).

**Exact adjacency.** For distinct normalized chords \(\{a,b\}\) and \(\{c,d\}\), where \(a<b\) and \(c<d\), their relative interiors cross if and only if \(a<c<b<d\) or \(c<a<d<b\). In the first program, a bit mask excludes each chord equal to or crossing a chord of the starting matching; the test against another matching's chord mask is therefore equivalent to disjoint compatibility. The program tests every unordered pair of distinct configurations. The second program constructs instead, for every starting matching, its set of allowed replacement chords and uses independent interval recursion to generate **all** noncrossing perfect matchings from those allowed chords. That is also exactly its adjacency list, with neither omitted nor extra neighbors.

**Exact distances.** Both programs perform graph search to enumerate all connected components, identify the sole component of size \(4070\), and run breadth-first search from **every** vertex of that component. Breadth-first search computes the minimum number of edges on any path from a given source, by induction on its successive distance layers. Its maximum finite distance is precisely the source eccentricity. Thus tabulating the \(4070\) maxima yields the stated eccentricity multiplicities, radius and diameter, not a sampled estimate. Both programs independently obtain the same canonical graph-edge digest, and each verifies that the two sources of eccentricity \(10\) are precisely \(R_0\) and \(R_1\). At least one source attains eccentricity \(15\), and the complete enumeration shows none exceeds \(15\).

These three complete reductions prove the finding for the **specific** finite graph \(\mathrm{DCM}_9\), independently of asymptotic assumptions.

## Verification

Run `python3 verify_chord_masks.py` and `python3 verify_dyck_dp.py` from a directory containing the extracted files. The recorded outputs are `verify_chord_masks.stdout` and `verify_dyck_dp.stdout`. Both produce `VERIFY_OK`, enumerate \(4862\) vertices and \(8677\) edges, and recover component sizes \(1^{612}\), \(5^{36}\) and \(4070^{1}\); both then agree on every eccentricity class, the two center matchings and the graph-edge SHA-256 fingerprint

`81631930f2db82172b1509c4f558f1933749e4b263323c00c58fdcae6eed97cb`.

The fingerprint is computed from the lexicographically indexed unordered adjacency pairs, one ASCII line `i,j` per edge, and therefore checks that the two implementations reconstructed the **identical** labeled graph, not merely the same counts. The programs have no randomized steps. The second uses a different Dyck-word enumeration and chord-filtering construction from the first chord-mask pair scan.

## Relationship to prior work

Aichholzer, Asinowski and Miltzow introduced and classified the connected-component types of \(\mathrm{DCM}_k\), including the threshold \(k=9\) for exactly three component isomorphism classes, formulas for the isolated and star components, the order of the single big component, and a generating function for the graph's edge counts [1]. Their Proposition 40 also identifies the alternating boundary matchings (rings) as the **unique maximum-degree** vertices. Neither the component-size result nor the maximum-degree result implies that these rings minimize eccentricity or determines the radius, diameter or eccentricity distribution of the big component. This new finite calculation isolates those exact metric facts at the **first** parameter where the structural three-class regime starts.

Hernando, Hurtado and Noy consider an operation that changes **two** matched chords in one step and obtain a different connected flip graph [2]; that graph's diameter does not determine distances for disjoint-compatible whole-matching transitions. Ishaque, Souvaine and Tóth prove the existence of disjoint-compatible matchings in even size [3], not shortest transformation lengths. Aichholzer and collaborators later consider a different adjacency defined by a common disjoint-compatible auxiliary spanning tree, caterpillar or path [4]; their distance results do not apply to the direct matching-matching compatibility graph here.

## Limitations

The theorem is **only for nine matched pairs**, equivalently eighteen convexly positioned points. No general formula, monotonicity, bound or conjecture for larger \(k\) is proved. The proof is a reproducible exhaustive finite computation supported by elementary completeness lemmas, not a symbolic formula for all orders. The previously published vertex, component and edge totals are not asserted to be novel. Priority relative to unindexed or inaccessible literature has not been independently established.

## References

[1] O. Aichholzer, A. Asinowski, and T. Miltzow, “Disjoint compatibility graph of non-crossing matchings of points in convex position,” *Electronic Journal of Combinatorics* 22(1), P1.65 (2015), DOI: 10.37236/4403; first preprint arXiv:1403.5546 (2014-03-21).

[2] C. Hernando, F. Hurtado, and M. Noy, “Graphs of non-crossing perfect matchings,” *Graphs and Combinatorics* 18 (2002), 517–532, DOI: 10.1007/s003730200038.

[3] M. Ishaque, D. L. Souvaine, and C. D. Tóth, “Disjoint compatible geometric matchings,” *Discrete & Computational Geometry* 49 (2013), 89–131, DOI: 10.1007/s00454-012-9466-9.

[4] O. Aichholzer, J. Obmann, P. Paták, D. Perz, J. Tkadlec, and B. Vogtenhuber, “Disjoint Compatibility via Graph Classes,” arXiv:2409.03579 (2024).
