# Five integral homotopy types of Möbius-ladder two-independence complexes

## Finding
For the Möbius ladder \(M_{2n}\), let \(\operatorname{Ind}_2(M_{2n})\) denote the simplicial complex of vertex sets inducing connected components of size at most two. The first five cases after the degenerate complete-bipartite instance are:

\[
\begin{aligned}
\operatorname{Ind}_2(M_8)&\simeq S^2,\\
\operatorname{Ind}_2(M_{10})&\simeq\bigvee^{9}S^3,\\
\operatorname{Ind}_2(M_{12})&\simeq\bigvee^{6}S^3,\\
\operatorname{Ind}_2(M_{14})&\simeq S^4,\\
\operatorname{Ind}_2(M_{16})&\simeq\bigvee^{31}S^5.
\end{aligned}
\]

All equivalences are integral homotopy equivalences, not merely field-homology agreements. Each is established by an explicit finite acyclic face-poset matching. No statement about all larger Möbius ladders is claimed.

## Assumptions and scope
For \(n\geq 4\), the simple graph \(M_{2n}\) has vertex set \(\{0,1,\ldots,2n-1\}\), edges \(\{i,i+1\}\) modulo \(2n\), and edges \(\{i,i+n\}\), all modulo \(2n\). A face \(F\) is admitted exactly when every connected component of the induced graph \(M_{2n}[F]\) has no more than two vertices. Equivalently, no vertex of \(F\) has more than one neighbor within \(F\). The latter equivalence holds because an induced component on at least three vertices contains a vertex with at least two selected neighbors. The empty face is included, although the verification models the nonempty face poset.

The cases \(n=4,5,6,7,8\) give the smallest five Möbius ladders strictly beyond \(M_6\cong K_{3,3}\). This is a finite exact classification and a benchmark for the transition from the published ordinary independence-complex periodicity to higher independence.

## Proof
An explicit, terminating algorithm constructs an acyclic partial matching on the face poset of each complex. Every face is represented by a nonzero bitmask \(F\) on \(2n\) vertices. Enumerate *all* masks from \(1\) through \(2^{2n}-1\), accepting a mask precisely when all of its set bits \(v\) satisfy
\[
\#\bigl(F\cap\{v-1,v+1,v+n\}\bigr)\leq 1,
\]
with vertex indices modulo \(2n\). This enumerates exactly the nonempty faces by the preceding equivalence.

Initially mark every nonempty face as available. For the integer pivot sequence recorded below, process each pivot \(v\) by visiting available faces in increasing order of (cardinality, integer mask). For each available face \(F\) with \(v\notin F\), pair \(F\) with \(F\cup\{v\}\) if that larger face is available, and remove both from the available set. Every pair is a codimension-one face/coface pair, and no face is used twice. The exact pivot orders are:

| \(n\) | Pivot sequence (vertices numbered from zero) |
|---|---|
| 4 | 4,5,0,1,6,7,2,3 |
| 5 | 0,3,4,2,5,9,7,1,8,6 |
| 6 | 8,3,9,1,11,5,0,4,7,10,6,2 |
| 7 | 5,13,11,1,12,9,3,7,4,6,0,2,10,8 |
| 8 | 2,14,13,3,4,6,8,7,1,11,0,15,5,10,9,12 |

For every covering relation \(F\subset F\cup\{v\}\) in the nonempty face poset, orient its Hasse edge from the larger to the smaller face unless it belongs to the matching, in which case orient it upward. The program `verify.py`, included with this result, explicitly constructs every such arrow and performs a complete topological sort. In all five cases all Hasse vertices are sorted, proving the directed graph acyclic. This is a finite exhaustive check of the entire relevant Hasse diagram, not a sampling argument.

The numbers of nonempty faces, matching pairs, oriented covering relations, and unmatched cells are:

| \(n\) | Faces | Pairs | Hasse arrows | Critical cells |
|---|---:|---:|---:|---|
| 4 | 78 | 38 | 192 | one \(0\)-cell, one \(2\)-cell |
| 5 | 232 | 111 | 720 | one \(0\)-cell, nine \(3\)-cells |
| 6 | 685 | 339 | 2,556 | one \(0\)-cell, six \(3\)-cells |
| 7 | 2,046 | 1,022 | 8,946 | one \(0\)-cell, one \(4\)-cell |
| 8 | 6,078 | 3,023 | 30,384 | one \(0\)-cell, thirty-one \(5\)-cells |

By the acyclic-matching theorem of discrete Morse theory, each simplicial complex is homotopy equivalent to a CW complex with exactly its listed critical cells. Since it has one \(0\)-cell, no \(1\)-cells and no intermediate-dimensional critical cells, every critical cell of the unique positive dimension \(d\geq 2\) attaches by the unique map \(S^{d-1}\to\{*\}\); the result is a wedge of the stated number of \(d\)-spheres. Thus these are integral homotopy types; no assumption about torsion or attaching maps is needed.

## Verification
Execute `python3 verify.py` in a directory containing the included standalone checker. It uses only the standard Python library. For each specified \(n\), the checker constructs the graph, tests the component-size criterion a second way using breadth-first search on every vertex subset, executes the stated pivot matching, checks all critical dimensions and counts, and checks acyclicity by topologically sorting every directed Hasse edge. It terminates with `VERIFY_OK`; the archived exact output is `verification_output.txt`. The two independent membership predicates agree for all \(87,291\) nonempty subsets across the five graphs. The checker enumerates \(9,119\) accepted nonempty faces and tests \(42,798\) Hasse covering relations. The Euler-characteristic checks based on independent face counts give reduced Euler characteristics \(1,-9,-6,1,-31\), consistent with the homotopy classification.

These finite computer calculations are exhaustive *for the five named graphs* and certify an acyclic matching that yields the integral homotopy conclusion. They are not used to extrapolate to larger graphs.

## Relationship to prior work
Agarwal and Basak (first public preprint August 31, 2026, subsequently revised) determine the homotopy types of the **ordinary** independence complexes and the **perfect matching** complexes of Möbius ladders, obtaining periodic families of sphere wedges. Their full text concerns vertex-independent sets and edge matchings and does not determine the two-independence complexes classified here. Sawant (May 24, 2026) establishes vertex decomposability of higher independence complexes for **trees**; Möbius ladders contain cycles and are not trees. General higher-independence results and other previously studied graph-associated complexes do not imply the five numerical integral homotopy types without additional computation or proof. Ordinary matching complexes are edge-indexed; two-independence complexes are vertex-indexed with a different face criterion. Likewise, cut and total-cut complexes of the original Möbius ladder are not the Alexander dual complex of the present claim. Published numerical table and equivalent-formulation searches identified no prior record of these five exact classifications; residual bibliographic uncertainty remains.

## Limitations
This is a finite classification of exactly five graphs, not a formula for \(n\geq 9\), a new structural result about all Möbius ladders, or a statement that these complexes are vertex decomposable or shellable. The general principle used after constructing the matchings is standard discrete Morse theory. Priority rests on bounded literature searches and examination of the closest primary results, not an exhaustive guarantee that no unpublished or unindexed calculation exists. Independent assessment of the computational proof has not been performed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first version August 31, 2026; https://arxiv.org/abs/2608.30601.
2. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, May 24, 2026; https://arxiv.org/abs/2605.25150.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145; standard acyclic matching theorem.
