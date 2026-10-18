# The Frucht-graph matching complex is a wedge of twenty three-spheres

## Finding
Let \(F\) be the twelve-vertex, eighteen-edge Frucht graph, in the explicitly labeled representation below. Its **ordinary matching complex** \(\mathcal M(F)\) has one vertex for each edge of \(F\), and a simplex for each set of pairwise vertex-disjoint edges. Then the complete **integral homotopy type** is
\[
\boxed{\mathcal M(F)\simeq\bigvee^{20}S^3.}
\]
Consequently its only nonzero reduced integral homology is \(\widetilde H_3(\mathcal M(F);\mathbb Z)\cong\mathbb Z^{20}\). This is not the independence complex of \(F\), nor its perfect-matching subcomplex.

## Assumptions and scope
The graph is the simple undirected graph on \(\{0,\ldots,11\}\) with edges indexed in this exact order:

```python
EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
```

This is a standard Frucht-graph presentation: the independent verifier reconstructs the published LCF presentation `[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]` and exhibits the explicit vertex relabeling. No higher-dimensional family or arbitrary cubic-graph statement is claimed. Homotopy equivalence concerns geometric realizations of finite abstract simplicial complexes.

## Proof
Represent a nonempty matching by a nonzero 18-bit integer \(b\), with its set bits naming disjoint graph edges. The exhaustive face predicate independently checks all \(2^{18}-1\) nonzero bitmasks against the given vertex incidences. Exactly 1,025 are valid, with face counts by simplicial dimension \(0\) through \(5\) equal to
\[
(18,117,333,397,152,8).
\]

Now fix the edge-index order

```
(15,11,1,2,7,17,8,16,3,4,9,5,0,6,14,13,10,12)
```

and start with all nonempty faces unmatched. At each index \(i\) in this order, pair every currently unmatched face \(\sigma\) not containing edge \(i\) with \(\sigma\cup\{i\}\), provided both faces are still unmatched; then remove both from subsequent stages. Different pairs in one stage are disjoint because the lower member does not contain \(i\), while the upper member does. This constructs exactly 502 face/coface pairs. The 21 remaining critical faces consist of one vertex and twenty three-dimensional simplices. In the 18-bit notation, the unique critical vertex is `32768` and the critical three-cells are

```
(4417,4420,5188,8513,8528,8961,8976,9281,9296,16706,
 17153,17442,17474,25632,65810,66081,66084,66578,69665,69668)
```

To establish acyclicity without relying on an unproved toggle lemma, enumerate **all 3,629 covers** in the Hasse diagram of nonempty faces. Orient a matched cover from its lower-dimensional face to its upper-dimensional face, and every unmatched cover in the opposite direction. The supplied verifier performs a complete directed topological sort of this finite graph, visiting all 1,025 face vertices; thus there is no closed gradient path. Every matching pair is checked to be a genuine codimension-one face inclusion, with no face appearing twice. Hence this is a valid acyclic discrete-Morse matching on the entire face poset, rather than only a numerical chain computation.

Forman's discrete-Morse theorem gives a CW complex homotopy equivalent to \(\mathcal M(F)\) with exactly one 0-cell, twenty 3-cells, and no other cells. Every 3-cell is necessarily attached by a constant map to the unique 0-cell, so the resulting CW complex is precisely \(\bigvee^{20}S^3\). This proves the **integral** homotopy type, not merely its homology ranks. No homology over a field is used to infer an integral attaching map.

## Verification
Run `python3 verify_frucht_matching.py` and `python3 verify_frucht_homology.py` using only the Python standard library. The first rebuilds all face masks, reproduces the matching, and topologically sorts the complete 3,629-cover directed face poset. It asserts the unique critical vertex, twenty critical 3-cells, 502 pairs and the entire face vector. The second reconstructs the same graph *independently* from the LCF cycle-and-chords presentation and verifies the explicit isomorphism, then computes all six unsigned mod-two boundary ranks. The latter are \((0,17,100,233,144,8)\) for boundaries originating in dimensions \(0,1,2,3,4,5\), and produce Betti vector \((1,0,0,20,0,0)\). Its chain calculation independently checks the reduced Euler characteristic \(-20\). Both programs' actual output is embedded in the package.

## Relationship to prior work
Agarwal and Basak's August 2026 paper develops the homotopy theory of independence and **perfect-matching** complexes of the highly symmetric Möbius ladders. Its definitions and Theorem 18 were inspected. The present complex instead contains *all* matchings in the **asymmetric Frucht graph**, and its theorem is neither an instance nor a consequence of theirs. The matching complex is an independence complex of the **line graph**, not of the underlying Frucht graph.

A published homotopy classification of \(\operatorname{Ind}(F)\) finds \(\bigvee^3S^2\); this does not determine \(\operatorname{Ind}(L(F))=\mathcal M(F)\). A published Franklin-graph calculation determines \(\mathcal M(\mathrm{Franklin})\simeq\bigvee^{12}S^3\), again for a different twelve-vertex cubic graph. A separately published five-graph classification computes Vietoris–Rips filtrations of asymmetric cubic graph vertex metrics, not their edge-matching complexes. Engström's general claw-free independence-complex connectivity theorem provides bounds and techniques, but not this exact integral homotopy multiplicity. The value here is the **complete matching-complex homotopy classification of the canonical smallest asymmetric cubic graph**, complementing calculations for symmetric cubic graphs. These distinctions were checked at the level of objects, constructions, assumptions and conclusions—not titles alone.

## Limitations
This is a finite named-graph result, not an assertion about every cubic, planar, or asymmetric graph. It is an exhaustive computer-assisted mathematical proof: trust requires executing or independently inspecting the finite face enumeration, matching, and complete directed acyclicity check. A mod-two homology verification alone would not prove the integral claim. The source searches and inspected public results found no dominating theorem for this exact Frucht matching complex, but unindexed or differently named prior work could exist. No independent scientific audit or certification is claimed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601v1, first public August 31, 2026; especially Section 2, Section 4, Theorem 18. https://arxiv.org/abs/2608.30601
2. E. W. Weisstein, *Frucht Graph*, MathWorld. https://mathworld.wolfram.com/FruchtGraph.html
3. *The Frucht graph independence complex and its complete vertex-deletion classification*, publicly available mathematical result (the Frucht complex and explicit graph data). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-frucht-graph-independence-complex-and-its-complete-vertex-de--8b7d9b2243c2
4. *Edge-orbit matching-complex splitting for the Franklin graph*, publicly available mathematical result (ordinary matching complex for a distinct twelve-vertex cubic graph). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-edge-orbit-matching-complex-splitting-for-the-franklin-graph--be4888fadcca
5. *Complete graph-metric Vietoris–Rips filtrations of the five asymmetric cubic Hamiltonian graphs on twelve vertices*, publicly available mathematical result (Rips rather than matching complexes). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtrations-of-the-five-asym--417fbc0c618b
6. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1 (2005), abstract and theorem scope. https://arxiv.org/abs/math/0512420
7. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
