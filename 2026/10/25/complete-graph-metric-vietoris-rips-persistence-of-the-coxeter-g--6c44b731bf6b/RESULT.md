# Complete graph-metric Vietoris–Rips persistence of the Coxeter graph

## Finding
Let \(G\) be the 28-vertex Coxeter cubic graph, with shortest-path distance \(d_G\). For \(r\ge0\), put \(K_r=\operatorname{VR}_{\le r}(V(G),d_G)\), where a finite vertex set spans a simplex if every pair is at distance at most \(r\). Then for **every real scale** \(r\ge0\),
\[
K_r\simeq\begin{cases}
\bigvee^{27}S^0,&0\le r<1,\\
\bigvee^{15}S^1,&1\le r<3,\\
\bigvee^{87}S^4,&3\le r<4,\\
\ast,&r\ge4.
\end{cases}
\]
The inclusion \(K_1\hookrightarrow K_2\) is a homotopy equivalence. Consequently, over \(\mathbb Z\) or any field, the complete **reduced** persistence barcode has 27 degree-zero intervals \([0,1)\), 15 degree-one intervals \([1,3)\), and 87 degree-four intervals \([3,4)\); all other reduced persistence groups vanish.

## Assumptions and scope
Use the cyclic Fano-plane presentation with ground set \(\mathbb Z/7\mathbb Z\) and seven lines
\[
\mathcal L=\bigl\{\{i,i+1,i+3\}:i\in\mathbb Z/7\mathbb Z\bigr\}.
\]
Take the 28 vertices to be all three-subsets not in \(\mathcal L\), in lexicographic order, and join two distinct vertices precisely when the represented triples are disjoint. This is the standard Coxeter graph (Foster census F28A), **not** the 30-vertex Tutte–Coxeter graph or a Coxeter-complex construction. The metric is intrinsic *graph distance*, not Euclidean distance in a polyhedral embedding. All simplicial complexes are finite, and all homotopy groups, attaching maps, and homology are understood integrally unless a coefficient ring is displayed. Integer thresholds are inclusive. No statement about other cubic graphs, general Fano modifications, or Euclidean embeddings is made.

## Proof
**1. Reconstruction and distance layers.** The seven cyclic triples form the Fano lines. Enumerating the other 28 triples, inserting disjointness edges, and performing breadth-first search from every vertex gives 42 edges and the same distance shell cardinalities \((1,3,6,12,6)\) at distances \(0,1,2,3,4\). Thus \(G\) is connected, cubic, and has diameter four. The supplied checker independently verifies each edge and every distance, with exact integer operations. The original graph has no triangle: any three pairwise disjoint triples would require nine elements of a seven-element ground set. Hence \(K_1\) is the graph itself, homotopy equivalent to a wedge of \(42-28+1=15\) circles. The threshold-zero complex is 28 points; the diameter-four threshold is a simplex and is contractible.

**2. An inclusion-preserving scale-two collapse.** Every vertex \(v\) has three neighbors \(a,b,c\). The radius-two complex contains the tetrahedron on \(\{v,a,b,c\}\). Enumerating all threshold-two cliques gives face vector \((28,126,112,28)\). First collapse the 28 tetrahedra along the opposite triangular faces \(\{a,b,c\}\), one per vertex. Then, for every vertex \(v\) and unordered pair \(\{a,b\}\) of its three neighbors, collapse the triangle \(\{v,a,b\}\) along the edge \(\{a,b\}\). There are 84 such additional pairs. At every step the indicated lower-dimensional face is contained in precisely one remaining coface, a fact verified exhaustively in the checker for the exact enumerated complex. The 112 collapses leave **precisely** the 28 vertices and 42 original graph edges, untouched by any step. Accordingly \(K_2\searrow K_1\) as a simplicial collapse that fixes \(K_1\), so \(K_1\hookrightarrow K_2\) is a homotopy equivalence, including on all integral homology.

**3. Complete scale-three certificate.** Enumerate the threshold-three flag complex exactly by extending a face only by later lexicographic vertices adjacent to every member. Its face vector in dimensions zero through six is
\[
(28,294,1456,3514,3864,1596,144),
\]
comprising 10,896 nonempty faces. Represent a face by a 28-bit mask. Process vertex indices, in the **fixed order**
```
15,22,3,12,13,17,9,27,25,7,5,14,11,24,
20,18,1,26,21,2,23,6,4,8,0,19,16,10
```
At a pivot \(v\), pair every currently unmatched nonempty face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), whenever the latter is a face and is also unmatched. All such pairs at a given pivot are disjoint. Remove each paired face from subsequent consideration. The deterministic algorithm matches 5,404 pairs, leaving **one critical zero-cell and 87 critical four-cells**, with no other critical cells.

A collection of pairs is not alone an acyclicity proof. For every codimension-one incidence of *all* 10,896 nonempty faces, orient the Hasse edge coface-to-face if unmatched, and face-to-coface if matched. Apply Kahn's topological-sort algorithm to this entire directed graph; the independent checker exhausts all 10,896 Hasse vertices. Therefore there is **no directed cycle**, verifying an acyclic Forman matching on the whole nonempty face poset. The finite matching and exhaustive directed-graph verification together form an exact reproducible certificate, not statistical sampling. By discrete Morse theory, \(K_3\) is homotopy equivalent to a CW complex consisting of one zero-cell and 87 four-cells only. Every three-sphere attaching map into a point is null, giving
\[
K_3\simeq\bigvee^{87}S^4.
\]
In particular this determines integral homotopy type, not just ranks of homology groups.

**4. Persistence maps.** Between consecutive integer thresholds the complex is constant. The scale-one to scale-two inclusion is a homotopy equivalence by Step 2. The scale-three complex has vanishing positive-degree homology except free fourth homology of rank 87 by Step 3, so the 15 degree-one bars die exactly at threshold three, when the degree-four bars are born. At threshold four the diameter-four graph yields the full simplex and kills those 87 classes. Connectivity at threshold one kills the 27 reduced degree-zero bars. This proves the displayed complete barcode.

## Verification
Run `python3 check_coxeter.py` alongside this file, using only the standard Python library. It reconstructs the Fano nonlines, every graph edge, all-pairs shortest paths, both nontrivial flag complexes, the 112 individual simplicial collapses, the 5,404 scale-three matching pairs, the full directed Hasse graph, and the distance-four diameter condition. The exact observed output is:
```
radius 2: 112 certified collapses onto original 28-vertex 42-edge graph
radius 3: 10896 faces, 5404 disjoint matched pairs,
          Hasse DAG verified, one critical vertex and 87 critical four-cells
radius 4: full simplex; integral wedge and persistence classification PASS
```
A full topological sort, not merely face counts or finite-field rank computations, verifies the matching acyclicity. The general inference from an acyclic matching to a CW homotopy model invokes the standard finite discrete-Morse theorem.

## Relationship to prior work
Saleh, Titz Mite and Witzel [1] study Vietoris–Rips complexes of **Platonic-solid vertex sets**, not graph-metric Rips filtration of the Coxeter graph. Dejter [2] studies the 28-vertex Coxeter graph and its 7-cycle/Klein graph geometry, without computing these Vietoris–Rips homotopy types. A prior published exact computation [3] determines \(\operatorname{Ind}(G)\simeq\bigvee^7S^6\) on the **ordinary cubic graph**. In contrast, our scale-three complex is \(\operatorname{Ind}(D_4(G))\), where \(D_4(G)\) is the different **six-regular graph joining vertices at distance exactly four**. The prior independence-complex theorem has a different set of faces and does not imply our result. Another published Rips computation [4] treats the **30-vertex Tutte–Coxeter incidence graph** and obtains 256 three-spheres at threshold three, not the Coxeter graph of this paper. Searches of accessible indexed literature and comparison with the full texts cited below did not identify any result implying the 87 four-sphere classification or the integral barcode. Such absence is evidence-limited and is not a mathematical uniqueness proof.

## Limitations
The theorem concerns exactly the 28-vertex Coxeter graph with its intrinsic graph metric and all nonnegative real thresholds. The 87-sphere stage is proved by a complete finite executable acyclic-matching certificate; it does not assert a uniform theorem for all distance-regular graphs, all graph metrics, or a formula for equivariant homology representations. The class of graphs joining vertices at distance exactly four is used only as an equivalent description of the scale-three complex, not as a claim that its ordinary independence complex was previously unstudied. An equivalent result in unindexed or inaccessible prior work cannot be excluded by the searches performed. Independent external validation has not been performed.

## References
[1] N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, publicly posted 2023-02-28; https://arxiv.org/pdf/2302.14388.

[2] I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960, https://arxiv.org/pdf/1002.1960 (Fano/Coxeter model and cycle structure).

[3] *The Coxeter graph independence complex is* \(\bigvee^7S^6\), publicly accessible result and complete proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-coxeter-graph-independence-complex-is-bigvee-7-s-6--8a1bdfa47e09/RESULT.md.

[4] *The scale-three Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres*, publicly accessible result and complete proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-scale-3-rips-complex-of-the-tutte-coxeter-graph-is-a-wedge-o--9454ecd0bd54/RESULT.md.

[5] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic discrete-Morse matching theorem).
