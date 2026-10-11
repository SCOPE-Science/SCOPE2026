# Complete local graph-degree spectrum of the fourth consecutive-pattern polytope

## Finding
Let \(\mathcal P_4\subseteq\mathbb R^{24}\) be the feasible region of limiting frequencies of **consecutive permutation patterns of length four**, without a pattern-avoidance restriction. Its affine dimension is \(18\). Its one-skeleton has exactly \(160\) vertices and \(2667\) edges, and the **complete graph-degree distribution** is
\[
\begin{array}{c|rrrrrrrrrr}
\text{degree}&18&22&26&43&59&61&71&81&111&159\\\hline
\text{number of vertices}&72&34&4&16&16&2&8&4&2&2.
\end{array}
\]

More precisely, a vertex corresponds to a directed simple cycle in the permutation overlap graph \(\mathrm{Ov}(4)\). Conditioning on the length of that cycle gives the entire joint cycle-length/vertex-degree distribution:

| Cycle length | Degree : number of vertices |
|:--:|:--|
| \(1\) | \(159:2\) |
| \(2\) | \(81:4,\ 111:2\) |
| \(3\) | \(59:16,\ 61:2,\ 71:8\) |
| \(4\) | \(26:4,\ 43:16\) |
| \(5\) | \(22:34\) |
| \(6\) | \(18:72\) |

A vertex is **simple** (has degree equal to the affine dimension \(18\)) **if and only if** its overlap-graph cycle is Hamiltonian (has length six); there are exactly \(72\) such vertices. This is a structural simplicity classification, not just a degree total.

The only two universal vertices are the length-one cycles labeled by the monotone patterns \(1234\) and \(4321\). Hence the one-skeleton has diameter \(2\), vertex eccentricities \(1\) for exactly two vertices and \(2\) for the other \(158\), with \(2667\) unordered vertex pairs at distance \(1\) and \(10053\) at distance \(2\).

## Assumptions and scope
For a tuple of distinct real numbers, its *standardization* is its relative-order permutation. Form a directed multigraph \(\mathrm{Ov}(4)\) whose vertex set is the six permutations of \(\{1,2,3\}\). Each permutation \(\pi\) of \(\{1,2,3,4\}\) labels one separately distinguished directed edge from the standardization of its first three entries to that of its last three entries. Parallel labeled edges are distinct; loops are retained. There are exactly \(24\) labeled edges.

For every directed simple cycle \(C\) (no repeated vertices, except closure, and permitting a one-edge loop) put \(v_C=\mathbf1_{E(C)}/|E(C)|\in\mathbb R^{24}\). Define
\[
\mathcal P_4=\operatorname{conv}\{v_C:C\text{ is a directed simple cycle of }\mathrm{Ov}(4)\}.
\]
By Borga and Penaguiao [1], this cycle polytope is precisely the limiting-consecutive-pattern feasible region. Our claim concerns combinatorial edges of this polytope, not distances between Euclidean embedded vectors, and does not impose any restriction to pattern avoidance. Both cycle vertices and polytope edges are counted without quotienting by graph or permutation symmetries.

## Proof
**1. Flow representation and vertices.** Let \(B\) be the signed vertex–arc incidence matrix of \(\mathrm{Ov}(4)\). The flow polytope is
\[
\mathcal P_4=\left\{z\in\mathbb R^{24}:z_e\ge0,\ Bz=0,\ \sum_e z_e=1\right\}.
\]
Every nonnegative circulation decomposes into nonnegative directed cycle flows. Intersecting with total mass one gives exactly the convex hull of the normalized simple-cycle incidence vectors. Each such normalized cycle is a vertex: its support contains no other directed simple cycle, so any decomposition into nonnegative normalized cycles supported there must repeat that cycle. Conversely no vertex arises otherwise. The ambient graph is strongly connected, and \(\operatorname{rank}B=5\), giving affine dimension \(24-5-1=18\).

**2. An exact adjacency test.** For two distinct simple cycles \(C,D\), write \(U=E(C)\cup E(D)\), and let \(V(U)\) be all vertices incident to arcs of \(U\). Let \(c(U)\) count connected components of the *underlying undirected multigraph* induced by \(U\) on \(V(U)\). Nonnegativity coordinates outside \(U\) vanish at both \(v_C\) and \(v_D\); their midpoint is strictly positive on every arc in \(U\). Therefore the smallest face containing these two vertices is precisely the normalized circulation polytope supported on \(U\), of dimension
\[
\dim F_U=|U|-\bigl(|V(U)|-c(U)\bigr)-1.
\]
Indeed, the middle term is exactly the rank of the restricted signed incidence matrix, and the midpoint is a relative-interior positive circulation in the restricted affine space. Thus **the two vertices are adjacent if and only if**
\[
|U|-|V(U)|+c(U)=2.
\]
Equivalently, precisely two directed simple cycles have edge sets contained in \(U\), namely \(C\) and \(D\), because these are exactly the vertices of the common face. This equivalence permits two independently implemented exhaustive adjacency tests.

**3. Exact finite census.** Enumerate the six vertex permutations and all \(24\) separately labeled arcs lexicographically. Enumerate all simple directed cycles by depth-first search, starting each cycle at its smallest vertex and forbidding intermediate vertices smaller than that start. This produces \(160\) cycles, distributed by lengths \(1,2,3,4,5,6\) as \(2,6,26,20,34,72\). A second enumeration, fixing instead each cycle's smallest *edge* and forbidding smaller subsequent edges, produces the same \(160\) cyclically normalized edge words.

For each of the \(\binom{160}{2}=12720\) unordered pairs of cycles, apply the incidence-rank criterion. A disjoint-set computation gives \(c(U)\) and hence the face dimension. Independently count all simple cycles entirely contained in \(U\), and confirm adjacency exactly when that number is two. The two tests agree for all pairs. Counting incidences of these adjacencies yields the joint length-degree table and the displayed degree spectrum. Its handshake sum is \(5334=2\cdot2667\), proving the edge total. In a \(18\)-dimensional polytope a vertex is simple precisely when its graph degree is \(18\); in the table those and only those entries have cycle length six, which exhausts the overlap graph's six vertices. This is a finite **exhaustive proof**, since the two cycle generators cover all simple cycles of a six-vertex directed multigraph and every unordered pair is examined; it is not an inference from sampled instances.

**4. Diameter and universal vertices.** The only one-edge loops are labeled by \(1234\) and \(4321\): equality of the consecutive length-three standardizations forces the three adjacent comparisons to have identical sign. A simple directed cycle containing a loop must be that loop. The union of the loop with any other simple cycle therefore contains exactly those two cycles, and they give adjacent vertices by Step 2. Hence the two loops are universal. All other vertices have degree strictly below \(159\) in the exhaustive table, and all nonadjacent pairs have graph distance exactly two via either loop. The count of distance-two pairs is \(\binom{160}{2}-2667=10053\), as asserted.

## Verification
The accompanying standalone `verify.py` needs only Python's standard library. Running `python3 verify.py` prints the exact confirmation line

`VERIFY_OK pattern-four cycle-polytope: vertices=160 edges=2667 dimension=18 diameter=2 independent_cycle_enumerations=yes two_independent_adjacency_tests=yes all_12720_pairs=yes full_degree_profile=yes`

It reconstructs all labeled arcs from permutations; cross-compares independent vertex-minimum and edge-minimum simple-cycle enumerators; tests both incidence rank and contained-cycle number for every unordered cycle pair; computes the joint length-degree spectrum and handshake identity; and recomputes all eccentricities by breadth-first search. All operations used in the proof are exact integers, sets, and permutations. The reported values are reproducible by the supplied code rather than by a stored table alone.

## Relationship to prior work
Borga and Penaguiao [1], especially Proposition 2.6 and Theorem 2.7, prove the general circulation description and face–full-subgraph correspondence for cycle polytopes. Their Theorem 1.6 identifies consecutive-pattern frequency polytopes with overlap-graph cycle polytopes, so the dimension and the basic face method used here are **established background**, not new discoveries. They treat the small \(k=3\) example explicitly. Their full text does not tabulate the fourth-order adjacency count, full degree spectrum, or the joint length-degree table given here.

Asplund and Fox [2] study enumerating cycles in permutation overlap graphs; their cycle-counting perspective is close to Step 3, but does not give the complete skeleton degree distribution of this 18-dimensional cycle polytope. Borga and Penaguiao [3] treat pattern-avoiding feasible regions and explicitly recall [1] as the treatment of the unrestricted case; their main statements do not determine the unrestricted fourth-order degree census. The new contribution is the **exact fully resolved first nontrivial fourth-order local adjacency profile, including the Hamiltonian/simple equivalence**, not a new general face theorem or a general cycle-enumeration algorithm.

## Limitations
This is an exact computation for one canonical, unquotiented fourth-order polytope, not a closed formula for all pattern lengths, not a census of higher-dimensional faces, and not an independent validation. The diameter-two assertion is a straightforward consequence of the established full-subgraph face criterion and the existence of monotone loops; the substantive additional calculation is the complete local degree profile. Although direct searches and full-text inspections located no publication of that profile, an absent match is not a proof that it has never appeared in a broader database or unpublished computation. The verifier's two descriptions independently cross-check a complete finite object, but both use the same mathematical definition of the overlap graph.

## References
[1] J. Borga and R. Penaguiao, *The feasible region for consecutive patterns of permutations is a cycle polytope*, arXiv:1910.02233 (first publicly posted 2019-10-05), Algebraic Combinatorics **3** (2020), 1259–1281, DOI:10.5802/alco.135. See Theorem 1.6, Proposition 2.6, Theorem 2.7, and Remark 2.9.

[2] J. Asplund and J. Fox, *Enumerating cycles in the graph of overlapping permutations*, arXiv:1609.02210 (2016); background on the cycle structure of permutation overlap graphs.

[3] J. Borga and R. Penaguiao, *The feasible regions for consecutive patterns of pattern-avoiding permutations*, arXiv:2010.06273 (2020; revised 2022), sections 1.2–1.3; the unrestricted-case definitions and results are cited back to [1].
