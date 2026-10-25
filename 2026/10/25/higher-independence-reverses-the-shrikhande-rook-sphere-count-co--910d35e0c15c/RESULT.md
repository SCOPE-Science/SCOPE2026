# Higher independence reverses the Shrikhande–rook sphere-count comparison

## Finding
Let \(\mathrm{Sh}\) be the Shrikhande graph and \(R=K_4\mathbin{\square}K_4\) the four-by-four rook graph, the two nonisomorphic strongly regular graphs with parameters \((16,6,2,2)\). For a finite graph \(G\), let \(\operatorname{Ind}_r(G)\) be the simplicial complex whose faces are vertex subsets for which each connected component of the induced graph has at most \(r\) vertices. Then
\[
\operatorname{Ind}_2(\mathrm{Sh})\simeq\bigvee^{57}S^3,\qquad
\operatorname{Ind}_2(R)\simeq\bigvee^{105}S^3.
\]
These are homotopy equivalences over the integers, not simply rational or modular homology calculations. They reverse the relative sphere counts of the ordinary independence complexes:
\[
\operatorname{Ind}_1(\mathrm{Sh})\simeq\bigvee^{23}S^2,\qquad
\operatorname{Ind}_1(R)\simeq\bigvee^{15}S^2.
\]
The ordinary cases are a previously indexed result and are independently checked here only to make the reversal precise. For the new degree-two cases the only nonzero reduced integral homology is \(\mathbb Z^{57}\), respectively \(\mathbb Z^{105}\), in dimension \(3\).

## Assumptions and scope
All graphs are finite, simple, and undirected. Label the common vertex set by pairs \((a,b)\in(\mathbb Z/4\mathbb Z)^2\), represented by the integer \(4a+b\) for \(a,b\in\{0,1,2,3\}\). In \(\mathrm{Sh}\), distinct vertices \(x,y\) are adjacent when
\[
y-x\in\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}
\]
with coordinates modulo \(4\). In \(R\), distinct \((a,b),(c,d)\) are adjacent precisely when \(a=c\) or \(b=d\). These models are the classical pair of strongly regular graphs with the same parameters and spectrum. In particular, every vertex has six neighbors and every pair of distinct vertices has exactly two common neighbors.

The property defining \(\operatorname{Ind}_2(G)\) is equivalent to requiring that the graph induced by a face have maximum degree at most one (isolated points and disjoint isolated edges). Equivalently it contains no three-vertex path as a **subgraph**; an *induced* path exclusion by itself would not suffice, because a triangle also violates the degree condition. The complex is often called the dissociation complex. No additional assumptions on embeddings, orientations, or coefficient fields are made.

## Proof
For a subset \(S\subseteq\{0,\ldots,15\}\), encode its incidence vector by the integer \(m=\sum_{v\in S}2^v\). Enumerate all \(2^{16}=65{,}536\) masks. For the ordinary complex, accept a mask if it contains no adjacent pair. For \(\operatorname{Ind}_2\), accept it if no chosen vertex has two chosen neighbors. Both predicates are verified independently by checking respectively forbidden edges and forbidden center-neighbor-neighbor triples. The resulting counts, **including the empty simplex**, grouped by simplex cardinality, are:

| Graph | \(r\) | Cardinalities \(0,1,\ldots\) | Total including empty |
| --- | ---: | --- | ---: |
| \(\mathrm{Sh}\) | 1 | \(1,16,72,96,16\) | 201 |
| \(R\) | 1 | \(1,16,72,96,24\) | 209 |
| \(\mathrm{Sh}\) | 2 | \(1,16,120,384,544,240,32\) | 1,337 |
| \(R\) | 2 | \(1,16,120,384,528,144\) | 1,193 |

Construct a partial matching of each **nonempty** face poset as follows. Use the common vertex order
\[
(9,2,13,7,12,6,15,14,8,3,0,10,4,1,11,5).
\]
At each vertex \(v\), scan all faces in ascending integer-mask order. Whenever both \(m\) and \(m+2^v\) are as-yet unmatched faces, with \(v\notin m\), match them and remove both from subsequent stages. Each matching edge joins faces differing in exactly one vertex.

Orient every codimension-one incidence in the nonempty face poset **downward**, except for a matched edge, which is oriented upward. The supplied standalone program enumerates *every* such incidence and checks that the resulting finite directed graph is acyclic by a complete Kahn topological sort. The complete verified matching certificate is:

| Graph | \(r\) | Nonempty faces | Matched pairs | Critical cells | Directed incidences |
| --- | ---: | ---: | ---: | --- | ---: |
| \(\mathrm{Sh}\) | 1 | 200 | 88 | one \(0\)-cell, 23 \(2\)-cells | 496 |
| \(R\) | 1 | 208 | 96 | one \(0\)-cell, 15 \(2\)-cells | 528 |
| \(\mathrm{Sh}\) | 2 | 1,336 | 639 | one \(0\)-cell, 57 \(3\)-cells | 4,960 |
| \(R\) | 2 | 1,192 | 543 | one \(0\)-cell, 105 \(3\)-cells | 4,224 |

By Forman's discrete Morse theorem, each complex is homotopy equivalent to a CW complex with exactly the listed critical cells. Because each has only one zero-cell and all remaining critical cells have the *same* dimension, either two or three, the attaching maps of those higher cells land in a point. The CW complex is consequently a wedge of exactly the stated spheres. In particular this proves the **integral homotopy type**, without any inference from finite-field Betti numbers or unverified attaching-degree computations. Since \(23>15\) whereas \(57<105\), the claimed reversal follows.

The higher complexes are nonpure: the maximal-simplex dimensions for \(\mathrm{Sh}\) are \(3,4,5\) with counts \(64,48,32\); those for \(R\) are \(3,4\) with counts \(96,144\). These counts are verified directly and do not serve as substitutes for the Morse proof.

## Verification
Run `python3 verify_higher_independence.py` with Python 3.10 or newer (the standard-library implementation uses `int.bit_count`). It uses only the standard library and finishes with `VERIFY_OK`. The accompanying `verification_output.txt` records its exact expected output.

The verifier reconstructs both adjacency matrices, checks the common-neighbor condition of the strongly regular parameters, checks both independent face predicates against each other on all masks, validates each face vector and maximal-face distribution, regenerates all matching pairs, checks the critical-cell multiset and Euler characteristic, and topologically sorts the entire oriented Hasse diagram. All four matching verifications and the common permutation use only data contained in the attached script. They require no other code or data files.

## Relationship to prior work
Shrikhande's 1959 association-scheme work establishes the exceptional parameter pair. Paolini and Salvetti initiated systematic work on higher independence complexes, and Deshpande and Singh classified their homotopy types for complete multipartite, fully whiskered, path, cycle and perfect rooted-tree families. Their classification does not include either of the present two graphs. Deshpande, Shukla and Singh also proved a wedge-of-spheres result for **chordal** graphs, which does not apply here: for example, the vertices \((0,1,2,3)\) form an induced four-cycle in \(\mathrm{Sh}\) with the chosen labeling, and \((0,1,4,5)\) do so in \(R\).

A previously indexed calculation already gives the ordinary \(r=1\) homotopy types \(\bigvee^{23}S^2\) and \(\bigvee^{15}S^2\); those are credited, not presented as new. Neither those conclusions nor the spectral parameters determine the \(r=2\) homotopy type. The new result is the **complete two-independence homotopy comparison**, including the reversal of sphere-count order. Searches for equivalent dissociation-complex terminology, degree-one induced-subgraph complexes and complete stronger classifications did not identify a result containing this pair of assertions. This negative search outcome is not an absolute guarantee of novelty.

## Limitations
The theorem treats exactly the two graphs on sixteen vertices and the indicated two values of \(r\). It gives no formula for arbitrary strongly regular graphs, no integral equivariant decomposition under the automorphism groups, and no classification for larger values of \(r\). The proof depends on finite, fully exhaustive combinatorial checks; it is not a general symbolic family theorem. Independent mathematical audit has not been performed. Equivalent work may exist in unindexed sources or in literature that was not fully accessible.

## References
1. S. S. Shrikhande, *The uniqueness of the \(L_2\) association scheme*, Annals of Mathematical Statistics **30** (1959), 781–798, DOI: `10.1214/aoms/1177706207`.
2. G. Paolini and M. Salvetti, *Weighted sheaves and homology of Artin groups*, Algebraic & Geometric Topology **18** (2018), 3943–4000, preprint `arXiv:1703.02586`, Section 3.
3. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, J. Ramanujan Math. Soc. **36** (2021), 53–71, preprint `arXiv:2001.05448` (initial public submission January 15, 2020).
4. P. Deshpande, S. Shukla and A. Singh, *Distance \(r\)-domination number and \(r\)-independence complexes of graphs*, preprint `arXiv:2001.06775`, January 19, 2020.
5. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, previously indexed public mathematical result (ordinary independence comparison).
