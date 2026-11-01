# Mixed-dimensional integral homotopy of the four-cube two-independence complex

## Finding

For the four-dimensional binary hypercube graph \(Q_4\), the two-independence complex has the integral homotopy type

\[
\operatorname{Ind}_2(Q_4)\simeq\bigvee^{16}S^3\vee S^4.
\]

The precise reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z^{16}\), \(\widetilde H_4\cong\mathbb Z\), and zero in every other degree. The statement is an integral *homotopy* classification: it includes the vanishing of the unique possible higher-cell attaching map and is not deduced merely from Betti numbers.

## Assumptions and scope

Let \(Q_4\) have vertex set \(V=\{0,1,\dots,15\}\), with each integer interpreted in binary. Two vertices are adjacent exactly when their bitwise XOR has Hamming weight one. Thus \(Q_4\) has 16 vertices and 32 undirected edges. For an arbitrary simple graph \(G\), its two-independence complex \(\operatorname{Ind}_2(G)\) consists of all vertex subsets \(U\) for which every connected component of the induced graph \(G[U]\) has at most two vertices. For a simple graph this is equivalent to every vertex of \(G[U]\) having degree at most one.

The result concerns this exact graph and simplicial construction. It does not assert an all-dimensional hypercube formula, the homotopy type of ordinary independence complexes, or the homotopy type of other graph-complex functors.

Faces are represented by integers \(m\in\{0,\ldots,65535\}\) with bit \(v\) set when vertex \(v\) is included. The empty face is present and corresponds to zero. Face orientations always use increasing vertex order; the oriented simplicial boundary is

\[
\partial[v_0,\ldots,v_k]=\sum_{j=0}^{k}(-1)^j[v_0,\ldots,\widehat{v_j},\ldots,v_k].
\]

## Proof

**1. Exhaustive simplicial model.** Enumerate all \(2^{16}=65536\) vertex subsets and retain exactly those for which no selected vertex has two selected neighbors. This gives 3055 faces including the empty face, with face numbers indexed by *cardinality* \(0,1,\ldots,8\):

\[
(1,16,120,464,964,960,440,80,10).
\]

There are 186 facets, in dimensions three (16 facets), five (160 facets), and seven (10 facets). The complex is therefore nonpure and seven-dimensional. This enumeration is complete because every subset occurs once and the degree predicate is equivalent to the defining component condition. The accompanying program independently checks the component condition by breadth-first search for each of the 65536 subsets.

**2. A complete acyclic partial matching.** Process the following vertex labels, in exactly this order:

```
15,0,4,3,8,11,10,13,9,14,2,7,6,1,5,12
```

At each label \(v\), take the presently unmatched faces \(a\) not containing \(v\), in increasing integer order; whenever \(b=a\cup\{v\}\) is also unmatched, pair \((a,b)\) and remove both from subsequent stages. This is a sequential element matching. By the standard element-matching proposition (Deshpande–Singh, Proposition 2.10), its union is acyclic. More importantly, the certificate independently checks acyclicity without invoking that proposition: orient every Hasse edge from larger face to smaller face, except that matched Hasse edges are reversed. A topological ordering exists for all 3055 vertices and 13,584 cover incidences of this directed graph.

The matching contains exactly 1519 pairs. The empty simplex belongs to a pair. The only unmatched faces are 16 faces with cardinality four (critical dimension three):

```
408,960,1440,2328,2640,3120,4488,6168,
8772,9252,10260,12300,16962,17442,18450,20490
```

and the single face with cardinality five (critical dimension four):

```
6800
```

Ordinary discrete Morse theory therefore gives a CW model consisting of one zero-cell, 16 three-cells, and one four-cell. There are no one-cells or two-cells, and no higher cells. The characteristic map of the sole four-cell is the only remaining possible nontrivial attaching map.

**3. Exact integral attaching calculation.** For faces \(a\subset b\) of codimension one, write \([b:a]\in\{-1,+1\}\) for the oriented simplicial incidence. For each matched pair \((f,b)\) with \(f\) three-dimensional and \(b\) four-dimensional, eliminate an occurrence of \(f\) in a boundary chain by replacing its coefficient \(c(f)\) and propagating to each other facet \(a\subset b\) the increment

\[
-c(f)\,[b:f]\,[b:a].
\]

The sign is correct because \([b:f]^{-1}=[b:f]\). Process these eliminations in a topological order of the directed gradient graph on three-faces. Such an ordering exists by the acyclicity already verified. Starting with the oriented ordinary simplicial boundary of critical four-face 6800, exact integer propagation yields the complete Morse boundary column

```
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
```

in the order of the 16 critical three-faces above. This is a computation of the *integral* Morse differential, not just its reduction modulo two. Every intermediate signed coefficient is calculated directly from the code's enumerated face incidences.

**4. Conclude the homotopy type.** The Morse three-skeleton is a wedge \(\bigvee^{16}S^3\). By the Hurewicz theorem its third homotopy group is isomorphic to its third integral homology, \(\mathbb Z^{16}\), with the critical three-cell classes as basis. The signed Morse boundary column is exactly the Hurewicz image of the attaching map of the four-cell. Since the column is zero, the attaching map is nullhomotopic. Attaching the four-cell consequently contributes a free four-sphere. This proves the displayed integral homotopy equivalence.

## Verification

Run the complete standard-library-only certificate:

```
python3 verify_q4_two_ind.py
```

The certificate checks both independent face predicates for every subset, all 3055 faces, all 13,584 Hasse incidences, the 1519 matching pairs and their complete directed acyclicity, the exact signed sixteen-entry Morse differential, and independently computes homology over \(\mathbb F_2\) using Gaussian elimination on the *original* simplicial chain complex. It also verifies the reduced Euler characteristic \(-15\), equal to \(-16+1\) from the claimed wedge.

The result marker is `Q4_TWO_INDEPENDENCE_INTEGRAL_MORSE_OK`. The executable and one complete execution output are supplied as separate files. All tests are exhaustive for this finite graph; no extrapolation from sampled dimensions is used in the theorem.

## Relationship to prior work

Deshpande and Singh, *Higher independence complexes of graphs and their homotopy types* (arXiv:2001.05448, first public version January 15, 2020), define the same complexes and prove formulas for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees. The four-cube has induced squares, is not a tree or cycle, and is not any of the treated graph families; their general element-matching method is used here with a new exact certificate for the four-cube.

Carnero Bravo, *The Forest Filtration of a Graph* (arXiv:2307.13271), identifies the first forest-filtration stage \(\mathcal F_1(G)\) with \(\operatorname{Ind}_2(G)\). This is an **equivalent formulation** of the object, not a second invariant. The paper's graph-product calculations treat the top forest-filtration stage of two-row Cartesian ladders and the first stage of *categorical* products of complete graphs. Neither proposition determines \(\mathcal F_1(Q_4)\), where \(Q_4\) is a fourfold *Cartesian* product of two-vertex graphs.

Abdelmalek, Deshpande, Goyal, Roy, and Singh, *Chordal graphs, higher independence and vertex decomposable complexes* (arXiv:2106.10863), study chordal graph classes, especially trees and caterpillars. The four-cube is not chordal because it contains induced four-cycles. Separately indexed calculations for the *ordinary* independence complex of \(Q_4\), its cut complexes, and its neighborhood complex concern different simplicial constructions, and none of their stated claims implies this two-independence homotopy equivalence.

## Limitations

This is a complete, exact classification for one canonical finite graph, not for all hypercubes. No assertion is made about the full automorphism representation on homology. Source searching and inspection can miss equivalent unpublished or unindexed results; novelty is assessed relative to explicitly checked evidence, not independently certified. The finite computation is part of the proof, with a self-contained checker; it does not constitute an independent external audit.

## References

1. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first submitted 2020-01-15), especially Sections 2–5 and Proposition 2.10. https://arxiv.org/abs/2001.05448
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first submitted 2023-07-25), especially the introduction and Section 4.2.2. https://arxiv.org/abs/2307.13271
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (first submitted 2021-06-21). https://arxiv.org/abs/2106.10863
