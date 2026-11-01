# The two-independence complex of the Frucht graph is a three-sphere

## Finding

For the standard twelve-vertex Frucht graph \(F\), the two-independence complex is homotopy equivalent to a single three-sphere:
\[
\operatorname{Ind}_{2}(F)\simeq S^{3}.
\]
In particular, its reduced integral homology is \(\mathbb Z\) in degree three and zero otherwise. This is an integral homotopy statement, not merely an equality of field homology ranks.

## Assumptions and scope

The graph has vertices \(\{0,1,\ldots,11\}\) and exactly the following eighteen undirected edges, whose vertex labels are zero-based:

```
(0,1) (0,6) (0,7) (1,2) (1,7) (2,3) (2,8) (3,4) (3,9)
(4,5) (4,9) (5,6) (5,10) (6,10) (7,11) (8,9) (8,11) (10,11)
```

This is the customary Frucht graph, a connected cubic graph with trivial automorphism group. A nonempty vertex subset \(\sigma\) is a simplex of \(\operatorname{Ind}_{2}(F)\) exactly when every connected component of the induced subgraph \(F[\sigma]\) has one or two vertices; equivalently, every selected vertex has at most one selected neighbor. All face-poset calculations below exclude the empty face.

## Proof

1. Exhaustive enumeration of the twelve-bit nonempty masks against the displayed edge set produces exactly 824 simplices, with face vector (degrees zero through six)
\[
(12,66,190,293,209,53,1).
\]
The included checker implements two independent membership predicates: induced maximum degree at most one, and direct breadth-first exploration of all induced connected components. It verifies they agree for every one of the 4095 nonempty masks.

2. Order the graph vertices as
```
9 0 1 7 8 10 4 11 2 3 5 6
```
Start with the set \(P\) of all nonempty simplices. At each vertex \(v\) in this order, traverse remaining masks in increasing integer order. Whenever \(\sigma\in P\), \(v\notin\sigma\), and \(\sigma\cup\{v\}\in P\), match those two faces and remove them from \(P\). This gives exactly 411 distinct pairs \((\sigma,\sigma\cup\{v\})\), with exactly two unmatched masks: `512` and `338`. The first has one bit and is a zero-cell; the second has four bits and is a three-cell.

3. To prove acyclicity rather than assume it, the checker explicitly lists all 3244 face-cover incidences in the nonempty face poset. Direct each incidence from the higher-dimensional face to its codimension-one face, except reverse precisely the 411 matched incidences. Kahn's topological sorting visits all 824 vertices of this directed Hasse graph. Thus it has no directed cycle, so the matching is acyclic.

4. By the discrete Morse theorem for finite simplicial complexes, the face poset matching yields a CW complex homotopy equivalent to \(\operatorname{Ind}_{2}(F)\), with one zero-cell and one three-cell and no other cells. The three-cell has its attaching map into a single point, hence the CW complex is \(S^3\). This proves the claimed integral homotopy equivalence.

## Verification

Run `python3 verify.py` using Python 3's standard library. The checker reconstructs the graph and all faces, compares two independent simplex membership tests, regenerates every matching pair, checks the complete directed Hasse graph for acyclicity, and separately computes all reduced mod-two Betti numbers by exact bitset Gaussian elimination. Expected boundary ranks in degrees one through six are (11,55,135,157,52,1), and the only nonzero reduced mod-two Betti number is one in degree three. These finite checks verify the entire finite complex; the homotopy conclusion additionally follows from the stated discrete Morse theorem.

## Relationship to prior work

Deshpande and Singh introduced and computed higher-independence complexes for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect branching trees [1]. The Frucht graph is not among these families: it is connected cubic and neither a cycle nor a tree; it has no leaves, is not complete multipartite, and is not chordal. The distance-domination and chordal results in [2,3] do not supply its exact homotopy type. A separately available calculation of the *ordinary* independence complex of the Frucht graph gives \(\operatorname{Ind}_{1}(F)\simeq\bigvee^{3}S^{2}\); it uses a different simplicial complex and does not imply the first higher-cutoff classification. The present result identifies an exact change from three two-dimensional sphere summands to one three-sphere.

## Limitations

The theorem applies to the graph and cutoff specified above; no formula for all asymmetric cubic graphs or for higher cutoffs is inferred. The numerical complex has dimension six even though its homotopy type has dimension three. Searches and inspected sources do not establish absolute bibliographic novelty; an unindexed or inaccessible equivalent computation could exist. The executable finite checks are not an independent audit.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first submitted January 15, 2020, Sections 3–5; https://arxiv.org/abs/2001.05448.
2. P. Deshpande, S. Shukla, and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775, submitted January 19, 2020; https://arxiv.org/abs/2001.06775.
3. F. M. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, submitted June 21, 2021; https://arxiv.org/abs/2106.10863.
4. *The Frucht graph independence complex and its complete vertex-deletion classification*, public mathematical research record `2026/10/11/SCOPE-the-frucht-graph-independence-complex-and-its-complete-vertex-de--8b7d9b2243c2` (ordinary independence only).
