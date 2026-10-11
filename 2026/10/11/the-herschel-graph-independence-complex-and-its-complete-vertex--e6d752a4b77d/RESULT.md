# The Herschel graph independence complex and its complete vertex-deletion profile

## Finding

For the eleven-vertex Herschel graph \(G\), the ordinary independence complex \(K=\operatorname{Ind}(G)\) has integral homotopy type

\[
K\simeq S^2\vee S^2.
\]

Its complete vertex-deletion and link profiles, for the vertex labels defined below, are

| Vertices \(v\) | \(\operatorname{Ind}(G-v)\) | \(\operatorname{lk}_{K}(v)\) |
|---|---|---|
| \(\{3,4\}\) | Simplicially collapsible | \(S^1\vee S^1\) |
| \(\{0,1,2,5,6,7,8,9,10\}\) | \(S^2\) | \(S^1\) |

All eleven vertex deletions therefore change the integral homotopy type. Precisely two deletions collapse the complex to a point; each of the other nine decreases the number of two-sphere summands from two to one. This is a classification of homotopy types, not a claim merely about field homology.

## Assumptions and scope

The graph is simple, undirected, and has labeled vertex set \(\{0,1,\ldots,10\}\) and exactly the following eighteen edges (each unordered pair is written in increasing order):

```
(0,5) (0,6) (0,9) (0,10)
(1,5) (1,6) (1,7) (1,8)
(2,7) (2,8) (2,9) (2,10)
(3,5) (3,7) (3,9)
(4,6) (4,8) (4,10)
```

This is an explicit labeling of the Herschel graph; it is isomorphic to the published eleven-vertex eighteen-edge representation and has the characteristic polynomial \(t^3(t^2-11)(t^2-3)(t^2-2)^2\), consistent with the published spectrum. No graph-labeling convention is assumed from the literature. The bipartition is \(\{0,1,2,3,4\}\) versus \(\{5,6,7,8,9,10\}\).

For a finite simple graph \(H\), \(\operatorname{Ind}(H)\) is the abstract simplicial complex of all independent vertex subsets, including the empty simplex. A deletion \(K-v\) is the subcomplex omitting \(v\), equal to \(\operatorname{Ind}(G-v)\). Its link is the subcomplex of faces \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\in K\), equivalently \(\operatorname{Ind}(G-N_G[v])\), with the closed neighborhood \(N_G[v]\). All homotopy equivalences are of geometric realizations with integral homotopy meaning.

## Proof

Both programs supplied alongside this statement reconstruct every simplicial face from the displayed edge list rather than using a precalculated table. The first program enumerates all nonempty faces for \(K\), for each of its eleven deletions, and for each of its eleven links. Each face is encoded by its vertex-subset bitmask.

For any of these twenty-three simplicial complexes, the program pairs available faces \(\sigma\subset\tau\) whenever \(\tau=\sigma\cup\{v\}\) for a selected toggle vertex \(v\), working through a deterministic ordering of toggles. The matching algorithm never reuses a face. In the directed Hasse graph of *all* nonempty faces, it reverses the matched cover incidences and orients all unmatched cover incidences from higher to lower dimension. A complete Kahn topological sort verifies that this digraph is acyclic. Thus the collection is an acyclic simplicial matching and the discrete-Morse reduction theorem applies to the associated ordinary CW complex. The empty face is excluded from this ordinary reduction; therefore a remaining vertex is a genuine critical zero-cell.

The full complex has face vector \((11,37,45,22,7,1)\). Its 123 nonempty faces admit 60 matched pairs, leaving exactly one critical zero-cell and two critical two-cells. All 338 directed nonempty cover incidences are enumerated and the acyclicity sort visits all 123 faces. A reduced CW model has one zero-cell and two two-cells and no positive-dimensional one-cells. Its two attaching maps have target a point, and the realization is therefore \(S^2\vee S^2\).

For each \(v\in\{3,4\}\), the deletion has 97 nonempty faces, 48 matched pairs, and just one critical zero-cell. In addition, the program independently constructs 48 actual elementary simplicial collapse pairs, each checked to consist of a free face and its unique codimension-one coface, ending at a single vertex. The corresponding link has 25 nonempty faces, eleven matched pairs, one critical zero-cell, and two critical one-cells, so it has the homotopy type \(S^1\vee S^1\).

For each of the nine remaining vertices, the deletion matching leaves precisely one critical zero-cell and one critical two-cell. The link matching leaves one critical zero-cell and one critical one-cell. The possible lower-dimensional attaching maps are again constant, giving \(S^2\) and \(S^1\), respectively. For the deletion of vertex 2 the deterministic toggle ordering is the permutation embedded in the verifier; every other case uses the natural increasing order. The verifier checks each complex separately; no claim is inferred solely by symmetry.

All 23 separate acyclicity verifications together cover 1,465 nonempty face occurrences, 3,644 cover incidences, and 709 matched pairs. The exact enumeration covers every vertex subset of every complex, so these are exhaustive finite certificates rather than statistical experiments.

## Verification

Run the included Python 3 standard-library programs from a directory containing both files:

```
python3 verify_herschel_morse.py
python3 verify_herschel_homology.py
```

The first emits `HERSCHEL_MORSE_OK 23 faces 1465 incidences 3644 pairs 709` after checking all matching incidences, acyclic topological sorts, critical-cell counts, and simplicial collapse sequences. The second reconstructs the graph independently from an adjacency dictionary, recomputes the characteristic polynomial using integral traces, generates each complex by recursive independent-set branching, and checks every mod-two simplicial boundary rank. It ends with `HERSCHEL_HOMOLOGY_OK 23`. For \(K\), it returns augmented boundary ranks \((1,10,27,16,6,1,0)\), giving reduced Betti number two in degree two only. The latter check cross-validates face enumeration but does not by itself establish the integral homotopy claims; the acyclic-matching argument above does.

## Relationship to prior work

Barmak, *Star clusters in independence complexes of graphs* (arXiv:1007.0418v1, originally public July 2, 2010), Theorems 3.4 and 3.5, proves that the independence complex of a graph with a vertex in no triangle is homotopy equivalent to a suspension. The Herschel graph is bipartite, so this applies. It does not determine the number and dimensions of sphere summands for this exact graph or the twenty-two associated deletion/link complexes. Engström, *Complexes of Directed Trees and Independence Complexes* (arXiv:math/0508148v1, August 8, 2005), develops graph-deletion and independence-complex gluing methods but likewise does not give the present graph-specific profile. General graph-family calculations for cycles, forests, categorical products and generalized Mycielskians do not directly identify the given graph with any classified family. The exact profile is obtained here from explicit finite acyclic matchings.

The term *Herschel graph* is used for the canonical smallest non-Hamiltonian polyhedral graph, and the published adjacency-spectrum fingerprint matches the graph defined above. This is a motivation for computing its full local topology: each of eleven deletions removes a sphere summand, with two vertices destroying both, even though the graph has only two degree values and the two exceptional vertices have the same degree as six nonexceptional ones.

## Limitations

The theorem is specifically about the displayed eleven-vertex graph and its vertex deletions and links. It makes no assertion about a general family of non-Hamiltonian polyhedral graphs, a relationship between graph Hamiltonicity and topological deletion-criticality, or the homotopy types of arbitrary induced subgraphs. The mod-two ranks are consistency checks, not substitutes for the integral proof. Literature comparisons cannot rule out every unindexed or unpublished equivalent calculation.

## References

- Jonathan A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, primary MSC 57M15. https://arxiv.org/html/1007.0418v1
- Alexander Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148v1, first public 2005-08-08. https://arxiv.org/html/math/0508148v1
- Eric W. Weisstein, *Herschel Graph*, MathWorld, https://mathworld.wolfram.com/HerschelGraph.html
- *adagio* reference manual, the `H11_edges` representation of the Herschel graph, https://www.stat.ethz.ch/CRAN/web/packages/adagio/refman/adagio.html
