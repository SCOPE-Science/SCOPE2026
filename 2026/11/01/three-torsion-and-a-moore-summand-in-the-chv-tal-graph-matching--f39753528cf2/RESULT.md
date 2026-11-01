# Three-torsion and a Moore summand in the Chvátal graph matching complex

## Finding

For the twelve-vertex Chvátal graph \(C\), the **ordinary matching complex** has integral homotopy type
\[
\mathcal M(C)\simeq\bigvee^{28}S^3\vee M(\mathbb Z/3,3),
\]
where \(M(\mathbb Z/3,3)\) is the Moore space with one three-cell and one four-cell attached by degree three. Thus \(\widetilde H_3(\mathcal M(C);\mathbb Z)\cong\mathbb Z^{28}\oplus\mathbb Z/3\), with all other reduced integral homology groups zero. In particular, it is not a wedge of spheres. No claim about a family of graphs is made.

## Assumptions and scope

The graph has vertex set \(\{0,1,\ldots,11\}\) and edges, with endpoints in increasing order:

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

Every vertex has degree four and there are no triangles. The complex \(\mathcal M(C)\) is the simplicial complex with the graph's 24 edges as vertices, and a set of those edges is a face if and only if the edges are pairwise vertex-disjoint. This is equally \(\operatorname{Ind}(L(C))\), with \(L(C)\) the line graph. The source definition excludes a distinct *perfect-matching complex*, and excludes induced-component-bounded independence complexes on graph vertices.

## Proof

Enumerate all nonempty edge subsets satisfying pairwise vertex-disjointness. The exact face count is \(2835\), with dimensions zero through five and face counts \(24,204,752,1175,628,52\). Encode a matching by its 24-bit edge-index mask, using the lexicographically ordered edge list above.

Execute successive elementary acyclic partial matchings indexed by the ordered edge indices

```text
1,2,22,11,5,9,8,6,23,18,10,21,16,13,20,17,19,4,3,14,12,0,7,15
```

At a stage indexed by \(i\), pair every still-present face omitting bit \(i\) with its bit-\(i\) extension, when both are still present. The executable `verify_chvatal.py` constructs the complete matching (1396 pairs) and, crucially, **checks acyclicity** by orienting the entire face-poset Hasse diagram: paired cover relations go upward, all other cover relations downward. The topological-sort check visits all \(2835\) simplices across \(10816\) incidences, proving no closed gradient paths. Exactly one critical vertex, 35 critical three-simplices, and seven critical four-simplices remain.

For each of the seven critical four-simplices, compute its signed integral Morse boundary against the 35 critical three-simplices. The checker implements the standard algebraic elimination along gradient arrows, recursively expanding paired three-faces through their matched four-cofaces, with alternating simplicial boundary signs. The resulting exact integer \(35\times7\) boundary matrix has Smith diagonal

\[
(1,1,1,1,1,1,3).
\]

There are no critical cells in dimensions one or two. The Morse CW complex is therefore a wedge of 35 three-spheres over a common base vertex with seven four-cells attached. By the Hurewicz theorem, the attaching maps lie in \(\pi_3(\bigvee^{35}S^3)\cong\mathbb Z^{35}\) and are fully determined by the signed degree matrix. Unimodular changes of bases are realizable by homotopy equivalences and cell slides. Smith reduction cancels six degree-one three-/four-cell pairs and leaves exactly one degree-three attaching map; 28 three-spheres remain freely wedged. This proves the displayed integral homotopy decomposition.

## Verification

Run `python verify_chvatal.py` using Python 3 with `networkx` and `sympy`. The script rebuilds the graph, independently enumerates every matching, recomputes the discrete-Morse pairings, checks the entire oriented Hasse graph, reconstructs each signed boundary entry and determines its integer Smith normal form. It separately constructs the original simplicial boundary matrices and reduces them modulo \(2\), \(3\) and \(5\), verifying that the characteristic-three dimensions jump to \(29\) and \(1\) in homological degrees three and four respectively, whereas the other tested characteristics give \(28\) and \(0\). These field checks corroborate, but do not by themselves establish, the integral torsion assertion; the exact integral Smith factors do that. The complete standard output is in `verification_output.txt`.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega, arXiv:2211.12559 (first public 2022-11-22), treat matching complexes of polygonal-line tilings and show sphere-wedge behavior there. Their inspected full text defines polygonal-line graphs by a chain of cycles with internal degree-two vertices; the four-regular Chvátal graph does not satisfy those hypotheses. The 2024 outerplanar extension, arXiv:2411.04601, likewise cannot cover \(C\), which has 24 edges and exceeds the outerplanar bound \(2\cdot12-3=21\).

Jonsson's degree-bounded graph-complex work (DOI:10.4153/CJM-2013-008-4) and the classical theory of complete-graph matching complexes establish earlier examples of three-torsion, but do not give this restricted graph's full integral homotopy type. A separate published record on the icosahedral matching complex likewise exhibits a degree-three Moore summand for a different, five-regular graph; the *presence of torsion per se is not claimed as novel*. The contribution here is the exact decomposition and sphere multiplicity for this canonical smallest triangle-free four-regular four-chromatic graph.

## Limitations

The proof applies only to the specified labeled graph, not to all regular, triangle-free, or four-chromatic graphs. The finite certificate is exhaustive for this one graph; it is not evidence for an infinite-family theorem. Results compared through abstracts and research-record summaries do not substitute for uninspected full text; an equivalent unindexed calculation remains a bibliographic risk. Independent human verification has not been performed.

## References

- M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559 (first posted November 22, 2022), DOI:10.1016/j.disc.2023.113428.
- M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (first posted November 7, 2024).
- J. Jonsson, *3-torsion in the homology of complexes of graphs of bounded degree*, Canadian Journal of Mathematics 65 (2013), 843–862, DOI:10.4153/CJM-2013-008-4.
- Earlier graph-specific record: *Three-torsion in the icosahedral matching complex: a planar counterexample*, public published-finding corpus record 2026/10/11/SCOPE-three-torsion-in-the-icosahedral-matching-complex-a-planar-count--28565ad1ea1a.
