# The Wagner graph matching complex and its two edge-orbit splittings

## Finding
Let \(W\) be the Wagner graph, also called the eight-vertex Möbius ladder: its vertex set is \(\mathbb Z/8\mathbb Z\), with undirected edges \(\{i,i+1\}\) for all \(i\) and \(\{i,i+4\}\) for \(i=0,1,2,3\), interpreted modulo eight. Let \(\mathcal M(H)\) be the ordinary matching complex of a graph \(H\): its vertices are the edges of \(H\), and its simplices are *all* sets of pairwise endpoint-disjoint edges, including the empty face.

**Theorem (complete edge-orbit matching-complex homotopy classification).** The integral homotopy type of the full complex is
\[
\mathcal M(W)\simeq\bigvee^{6}S^{2}.
\]
The graph's edges form an orbit of eight cycle edges and an orbit of four opposite-vertex edges. For *every* cycle edge \(e\),
\[
\mathcal M(W-e)\simeq\bigvee^{3}S^{2},\qquad
\mathcal M(W-V(e))\simeq\bigvee^{3}S^{1};
\]
for *every* opposite-vertex edge \(e\),
\[
\mathcal M(W-e)\simeq\bigvee^{4}S^{2},\qquad
\mathcal M(W-V(e))\simeq\bigvee^{2}S^{1}.
\]
Here \(W-e\) deletes an edge but retains vertices, whereas \(W-V(e)\) deletes both endpoints and incident edges. For either kind of edge, the natural deletion-link cofibration splits:
\[
\mathcal M(W)\simeq \mathcal M(W-e)\vee \Sigma\mathcal M(W-V(e)).
\]
Thus both edge orbits independently recover the same six two-spheres: \(3+3=6\) and \(4+2=6\).

## Assumptions and scope
Graphs are finite, undirected, simple, and without loops. All homotopy equivalences refer to geometric realizations, and spheres and wedge sums have their standard, *integral* homotopy meanings. Unlike a perfect matching complex, \(\mathcal M(W)\) includes matchings that do not extend to perfect matchings. In particular, the result is not about \(\operatorname{Ind}(W)\); rather, it concerns the equivalent complex \(\operatorname{Ind}(L(W))\), where \(L(W)\) is the line graph. The theorem is restricted to the eight-vertex ladder and its two edge-orbit deletions and links.

## Proof
**1. Finite model.** Sort the twelve undirected edges lexicographically. Represent a nonempty matching by a nonzero twelve-bit mask, retaining a mask precisely when its selected edges have pairwise distinct endpoints. For a deletion or link, first sort the retained graph edges and use bit masks indexed by this shorter list. This exhaustively enumerates the following nonempty faces; entries are the numbers of simplices in increasing dimension:

| Complex | Face vector | Faces | Matched pairs | Critical cell dimensions | Hasse incidences checked |
|---|---|---:|---:|---|---:|
| \(\mathcal M(W)\) | \((12,42,44,7)\) | 105 | 49 | one \(0\), six \(2\) | 244 |
| \(\mathcal M(W-e)\), \(e=\{0,1\}\) | \((11,35,33,5)\) | 84 | 40 | one \(0\), three \(2\) | 189 |
| \(\mathcal M(W-V(\{0,1\}))\) | \((7,11,2)\) | 20 | 8 | one \(0\), three \(1\) | 28 |
| \(\mathcal M(W-e)\), \(e=\{0,4\}\) | \((11,35,33,4)\) | 83 | 39 | one \(0\), four \(2\) | 185 |
| \(\mathcal M(W-V(\{0,4\}))\) | \((7,11,3)\) | 21 | 9 | one \(0\), two \(1\) | 31 |

**2. Explicit acyclic matchings.** The executable certificate `verify_wagner_morse.py` specifies five permutations of local edge indices. In each case start with all nonempty simplices unmatched. For each pivot \(j\) in that order, pair every currently unmatched simplex \(\sigma\) omitting \(j\), whenever \(\sigma\cup\{j\}\) remains unmatched, with \(\sigma\cup\{j\}\). Neither member is used again. The exact permutations, in table order, are:

```
whole:          [11,10,9,8,7,6,5,4,3,2,1,0]
cycle_delete:   [4,2,9,7,5,0,10,8,1,6,3]
cycle_link:     [0,1,2,3,4,5,6]
rung_delete:    [0,1,2,3,4,5,6,7,8,9,10]
rung_link:      [0,1,2,3,4,5,6]
```

For each nonempty face-poset cover \(\sigma\subset\tau\) with one new vertex, orient the cover *upwards* if it is a matched pair and *downwards* otherwise. The certificate builds every such directed cover and uses a complete topological sort to check the graph has no directed cycles. The counted directed cover incidences are given in the table. This independently verifies the precise acyclicity hypothesis of Forman's discrete Morse theorem, rather than inferring acyclicity from matching size or from a partial traversal.

**3. Homotopy types from critical cells.** The discrete Morse theorem supplies a CW model with one cell for each critical face, of corresponding dimension. The full complex and both edge-deletion complexes have just one zero-cell and only dimension-two positive cells, hence are wedges of two-spheres with the listed multiplicities. Both endpoint-deletion complexes have just one zero-cell and only dimension-one cells, hence are wedges of circles. No unknown attaching maps remain in any of these five CW models.

**4. Both edge orbits.** Translation and reflection of the index set, \(i\mapsto i+t\) and \(i\mapsto-i+t\) modulo eight, preserve both kinds of graph edges. They act transitively on all eight cycle edges and separately on all four opposite-vertex edges. Therefore the representative computations at \(\{0,1\}\) and \(\{0,4\}\) apply to every edge in their respective orbits.

**5. The splitting.** For any edge \(e\) of \(W\), the link and deletion of the matching-complex vertex indexed by \(e\) are respectively \(\mathcal M(W-V(e))\) and \(\mathcal M(W-e)\). Thus the matching complex is the union of its deletion and the cone on its link. The link is in both cases a wedge of circles, while the deletion is a simply connected wedge of two-spheres. Every map from a wedge of circles to a simply connected space is null-homotopic. The inclusion of the link therefore vanishes up to homotopy, so the mapping-cone splitting yields the stated wedge decompositions. This completes the proof.

## Verification
Run `python3 verify_wagner_morse.py` with Python 3 and no third-party dependencies to reconstruct all five complexes, test every matched face-pair, verify every face-vector/critical-cell count, check the two edge orbits under all sixteen dihedral automorphisms, and confirm acyclicity via a full directed Hasse-graph topological sort. It prints `VERIFY_OK` if all assertions pass. Independently run `python3 verify_wagner_homology.py`; it reconstructs the graph by cyclic vertex distance, enumerates compatible tuples of edges without reusing the mask generator, computes all simplicial boundaries over the fields of characteristics \(2,3,5,101\), and checks the reduced Betti numbers of the five complexes. The second computation corroborates, but does not replace, the integral discrete-Morse homotopy proof. Both programs were replayed successfully in their complete standalone form.

## Relationship to prior work
Barmak's archived star-cluster framework for independence complexes of claw-free graphs, including line graphs, gives general connectivity bounds for matching complexes (Theorem 5.5 and Corollary 5.10 of [1]); it does not determine the five stated homotopy types. Bayer, Jelić Milutinović and Vega [2] prove an exact wedge-of-spheres *form* for matching complexes of **outerplanar** graphs, a class excluding the nonplanar Wagner graph; moreover their statement does not supply these precise sphere counts and edge-orbit splittings. Agarwal and Basak [3, Definition 3 and Main Theorem 1] determine homotopy types of the *independence complex* and the *perfect matching complex* of Möbius ladders, not the ordinary matching complex considered here. Their Problem 26 explicitly proposes investigating ordinary matching complexes of Möbius ladders, confirming that these are separate constructions. The full graph \(W\) is an important named cubic nonplanar graph, so this exact smaller-rank instance and its two deletion-link calculations serve as a natural benchmark for that proposed direction.

## Limitations
The result does not classify ordinary matching complexes of all Möbius ladders, nor imply a periodic formula for arbitrary ladder size. Exhaustiveness is finite and relies on the fully specified eight-vertex graph; it supplies no assertion about an infinite graph family. The computational proof uses standard discrete Morse theory; secondary finite-field homology agreement alone is not an integral homotopy certificate. While relevant primary texts and indexed comparisons were inspected, an equivalent result in unindexed or unpublished material cannot be absolutely ruled out.

## References
[1] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first posted 2010-07-02; especially Section 5, Theorem 5.5, Corollary 5.10. https://arxiv.org/abs/1007.0418

[2] M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first posted 2024-11-07; especially Definition 1, Theorem 2, and the deletion/link preliminaries. https://arxiv.org/abs/2411.04601

[3] A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, 2026-09-14; especially Definition 3, Main Theorem 1, and Problem 26. https://arxiv.org/abs/2608.30601

[4] Wagner graph, eight-vertex Möbius ladder, standard graph identification: https://mathworld.wolfram.com/WagnerGraph.html
