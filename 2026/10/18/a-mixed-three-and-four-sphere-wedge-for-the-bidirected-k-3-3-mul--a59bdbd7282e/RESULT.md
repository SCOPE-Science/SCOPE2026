# A mixed three- and four-sphere wedge for the bidirected \(K_{3,3}\) multipath complex

## Finding
Let \(G=\overleftrightarrow{K}_{3,3}\) denote the directed graph with vertex partition \(A=\{0,1,2\}\) and \(B=\{3,4,5\}\) and both oppositely oriented arcs between every \(a\in A\) and \(b\in B\). Its multipath complex \(X(G)\) is the simplicial complex on its eighteen arcs whose faces are directed subgraphs with indegree and outdegree at most one at every vertex and no directed cycles. Then

\[
X(G)\simeq\bigvee^{19}S^3\ \vee\ \bigvee^{12}S^4.
\]

In particular its reduced integral homology is free of rank \(19\) in dimension \(3\), rank \(12\) in dimension \(4\), and zero in all other degrees. The full automorphism group is \((S_3\times S_3)\rtimes C_2\), of order \(72\). The rational homology characters in degrees \(3\) and \(4\), respectively, have the following complete values on its nine conjugacy classes. In the partition-preserving rows, the labels list the unordered cycle types of the permutations on \(A\) and \(B\); in the swapping rows, the label is the cycle type of the product of the two cross-part bijections.

| Conjugacy class | Size | Degree-three trace | Degree-four trace |
|---|---:|---:|---:|
| \((111,111)\) | 1 | 19 | 12 |
| \((111,21)\) | 6 | 1 | 0 |
| \((111,3)\) | 4 | 1 | 0 |
| \((21,21)\) | 9 | 3 | 0 |
| \((21,3)\) | 12 | 1 | 0 |
| \((3,3)\) | 4 | 1 | 6 |
| swapping, product type \(111\) | 6 | -1 | -2 |
| swapping, product type \(21\) | 18 | 1 | 0 |
| swapping, product type \(3\) | 12 | -1 | -2 |

Averaging these characters over the group gives \(\dim_{\mathbb Q}\widetilde H_3(X(G);\mathbb Q)^{\operatorname{Aut}(G)}=1\) and \(\dim_{\mathbb Q}\widetilde H_4(X(G);\mathbb Q)^{\operatorname{Aut}(G)}=0\).

## Assumptions and scope
All complexes are finite abstract simplicial complexes; all homotopy equivalences refer to geometric realizations. A face corresponds to a selected subset of *oriented* arcs, not to an undirected matching. An isolated vertex is allowed in a multipath. Arc sets containing a two-cycle, a four-cycle, or any other directed cycle are excluded. The nine rows above use the full graph automorphism group including interchange of the two vertex partitions. There are no variable parameters in this classification: it concerns exactly the bidirected complete bipartite graph with three vertices in each part.

The eighteen arcs are numbered in this canonical order:

```
(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),
(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2).
```

Each nonempty face is represented by its eighteen-bit incidence integer. The exact verifiers `verify_bidirected_k33.py` and `verify_symmetry.py` use only the Python standard library and SymPy, respectively.

## Proof
**Complete finite face description.** Enumerate all nonzero eighteen-bit integers and retain a mask if selected arcs have pairwise distinct sources, pairwise distinct targets, and no directed cycle. This is exactly the definition of a directed vertex-disjoint union of paths. The resulting face counts by dimension \(0,1,2,3,4\) are \((18,108,264,252,72)\), totaling \(714\) nonempty faces. In particular there are no faces in dimension greater than four. The full face poset contains \(2376\) codimension-one cover relations.

**Acyclic matching.** Apply the elementary matching algorithm to the entire set of nonempty faces, considering prospective arc indices in this fixed order:

```
12,0,17,11,16,14,10,13,5,15,7,4,8,9,3,6,2,1.
```

At pivot \(i\), pair each as-yet-unmatched nonempty face \(\sigma\) not containing arc \(i\) with \(\sigma\cup\{i\}\) whenever both belong to the still-unmatched set, and remove both from that set. Never pair the empty face. This produces exactly \(341\) pairs and leaves one critical zero-simplex, nineteen critical three-simplices and twelve critical four-simplices. Reverse the directed cover arrow for each paired incidence; orient all other face-poset incidences from coface toward facet. A complete topological sort on this explicitly determined directed graph visits all \(714\) face-poset nodes, with \(2376\) directed edges. Thus this is an acyclic Forman matching and yields a Morse CW complex with precisely the listed critical cell dimensions.

**Integral attaching degrees.** Orient each simplex by the increasing numerical order of its selected arcs. For a matched lower face \(\sigma\) and upper face \(\tau\), let \([\tau:\sigma]\in\{+1,-1\}\) be their ordinary simplicial incidence. Recursively project a face to critical faces of the same dimension: a critical face projects to itself; a matched upper face projects to zero; and a matched lower face satisfies

\[
P(\sigma)=-[\tau:\sigma]\!\sum_{\rho\subset\tau,\,\rho\ne\sigma,\,|\rho|=|\sigma|}\![\tau:\rho]P(\rho).
\]

The acyclic matching makes this recursion well-founded. Projecting the oriented simplicial boundaries of all twelve critical four-simplices yields *identically zero* in the free abelian group on the nineteen critical three-simplices. This computes the exact integral cellular Morse differential \(\partial_4=0\), not just its reduction modulo two.

The Morse CW complex has a point, nineteen three-cells, and twelve four-cells. Its three-skeleton is \(\bigvee^{19}S^3\), which is two-connected. The Hurewicz map \(\pi_3\rightarrow H_3\) is an isomorphism for this skeleton. Therefore the vanishing integral cellular boundary of each four-cell means that the corresponding attaching map from its boundary three-sphere is nullhomotopic. Attaching all twelve four-cells yields the claimed wedge of nineteen three-spheres and twelve four-spheres. This establishes the **integral homotopy** classification, not merely Betti numbers.

**Automorphism character.** Every graph automorphism is a permutation within each part, optionally composed with a swap of the parts, giving exactly \(72\) permutations of the six graph vertices. Each permutes the eighteen arcs and therefore gives a signed action on oriented simplicial chains. Construct the full integral simplicial boundary \(\partial_4:C_4\to C_3\) of size \(252\) by \(72\). Rational row reduction gives rank \(60\), hence the top homology is \(\ker\partial_4\) of dimension \(12\). A basis is obtained by taking free positions \(21,23,29,31,41,43,49,51,61,63,69,71\) in the ordered list of four-simplices and solving the pivot equations. For each of the \(72\) automorphisms, trace its action on these twelve explicit cycles, obtaining the degree-four character. Independently sum the signed traces on every simplicial chain group to obtain the Lefschetz number \(L(g)\). Since the only nontrivial rational homology groups are in degrees \(0,3,4\), the degree-three character is \(\operatorname{tr}(g|H_3)=1+\operatorname{tr}(g|H_4)-L(g)\). All exact traces agree within the nine asserted conjugacy classes. Character averaging proves the invariant-dimension statements.

## Verification
Run both complete verifiers together in a directory containing all files:

```
python3 verify_bidirected_k33.py
python3 verify_symmetry.py
```

The first script tests all \(714\) allowed faces, every one of the \(2376\) face-poset covers, all \(341\) matching pairs, the directed topological sort, and all signed Morse critical four-to-three incidences. It also independently computes all mod-two simplicial boundary ranks \((17,91,173,60)\), giving ordinary Betti numbers \((1,0,0,19,12)\). These mod-two ranks are a corroboration, *not* the integral proof.

The second script computes the signed integral fourth simplicial boundary, its exact rank \(60\), explicit rational kernel vectors with coefficients \(0,\pm1\), all \(72\) graph-automorphism actions on simplices, the nine character rows, and both invariant dimensions. Its output is saved in `symmetry_check.txt`; the first script's output is in `multipath_check.txt`. Both outputs were reproduced from the supplied script files.

## Relationship to prior work
Caputi, Collari, and Smith (2026, arXiv:2601.05670v1) study multipath complexes of bidirectional linear and polygonal digraphs, notably their high connectivity and homology. Their graph families do not include the bidirected complete bipartite graph \(K_{3,3}\), whose underlying undirected graph has nine rather than six edges.

Caputi, Collari, Di Trani, and Smith (2022 preprint; 2024 publication, arXiv:2208.04656) examine directed bipartite graphs with all arcs pointing from one part to the other in their generating-function results. Such one-way digraphs have no directed cycles and give ordinary chessboard matching complexes; this does not determine the bidirected example.

Vrećica and Živaljević (2007 preprint, arXiv:0710.5252) introduce generalized cycle-free chessboard complexes, a definition encompassing the present restricted board, and establish connectivity bounds for the **complete** directed graph (the full square board). The present complex is the proper induced subcomplex obtained by allowing only arcs between two fixed triples. Their results for the full complex do not determine this restricted subcomplex's exact homotopy or its automorphism character. Existing classifications for bidirected \(K_{2,n}\) similarly do not settle the first balanced thicker bipartition \(K_{3,3}\).

## Limitations
The theorem establishes the stated single-graph homotopy type and its *rational* homology character, not an integral decomposition into irreducible automorphism modules and not a formula for all \(K_{m,n}\). The finite enumeration is exhaustive because there are exactly eighteen arc vertices and the program examines all possible nonempty masks; it does not constitute a classification for arbitrary parameter sizes. The proof relies on exact computer-assisted checks with complete supplied algorithms, rather than a short closed-form hand matching. The literature comparison cannot rule out unindexed or otherwise inaccessible equivalent results. Independent external mathematical validation has not been performed.

## References
1. L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first public version January 9, 2026), https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, C. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, https://arxiv.org/abs/2208.04656.
3. S. T. Vrećica and R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252, https://arxiv.org/abs/0710.5252.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
