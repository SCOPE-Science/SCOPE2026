# Ten symmetric simplicial collapses between Petersen odd-cycle and forest complexes

## Finding
For the Petersen graph \(P=\operatorname{KG}(5,2)\), let \(\mathcal B(P)\) be the abstract simplicial complex of vertex subsets inducing bipartite graphs (odd-cycle-independent sets), and let \(\mathcal F(P)\) be the subcomplex of subsets inducing forests (cycle-independent sets). There are exactly ten extra six-vertex faces and ten extra seven-vertex faces in \(\mathcal B(P)\setminus\mathcal F(P)\). Each extra six-vertex face induces a six-cycle, belongs to exactly one extra seven-vertex face, and is a free codimension-one face. Deleting these ten free-face/cofacet pairs gives precisely \(\mathcal F(P)\), with the entire matching invariant under \(\operatorname{Aut}(P)\cong\mathfrak S_5\). Thus

\[
\mathcal B(P)\searrow\mathcal F(P)\simeq\bigvee^{6}S^{5}.
\]

The inclusion induces an isomorphism of \(\mathfrak S_5\)-modules on fifth rational reduced homology, both identified with \(\bigwedge^2 V\cong S^{(3,1,1)}\), where \(V\) is the four-dimensional standard rational permutation-augmentation representation. This module is irreducible and has no nonzero global invariant.

## Assumptions and scope
The graph is the simple ten-vertex Kneser graph with vertices the two-subsets of \(\{0,1,2,3,4\}\), adjacent precisely when disjoint. No graph weights or subdivision are involved. Both complexes include the empty face; geometric realizations use their nonempty faces. All homotopy conclusions are integral, while the representation assertion is over \(\mathbb Q\). The assertion concerns this graph and this particular inclusion only, not arbitrary graph families.

## Proof
1. **Exhaustive classification of allowed faces.** Encode each of the ten graph vertices by a bit. Inspect every mask in \(\{0,\ldots,1023\}\). A two-color traversal decides membership in \(\mathcal B(P)\), and union-find decides membership in \(\mathcal F(P)\), independently cross-checked by the edge-count/connected-component forest criterion. The resulting face counts by cardinalities zero through seven are respectively \((1,10,45,120,210,240,150,30)\) for \(\mathcal B(P)\), and \((1,10,45,120,210,240,140,20)\) for \(\mathcal F(P)\); there are no larger faces. The twelve minimal nonfaces of \(\mathcal B(P)\) all have cardinality five and are induced pentagons. The difference consists of precisely ten six-sets and ten seven-sets.

2. **Free-face certificate.** For each of the ten six-sets in the difference, the induced graph has degree two at every vertex; it is therefore an induced six-cycle because enumeration confirms the induced graph is cyclic and connected. A complete proper-superset scan of \(\mathcal B(P)\) finds precisely one coface, of size seven, for each six-set. Those ten seven-set cofaces are pairwise different, and the twenty paired faces exhaust the difference. Therefore one may remove each free face together with its unique maximal coface by elementary simplicial collapse, in any order. The final complex is exactly \(\mathcal F(P)\). Under every permutation of the five ground-set labels, the complete ten-pair set is mapped to itself; hence the collapse pairs form an invariant orbit collection and the inclusion is compatible with the \(\mathfrak S_5\) action.

3. **Integral homotopy of the forest subcomplex.** The included exact verifier constructs a complete acyclic discrete-Morse matching on all 785 nonempty faces of \(\mathcal F(P)\): 389 matched pairs and seven critical cells, namely one vertex and six cells of dimension five. It explicitly orients all 3,470 codimension-one incidences down except the matched incidences, which are oriented up; a complete topological sort terminates on every face, proving no closed gradient path. Forman's discrete Morse theorem gives a CW complex with precisely those critical cells. Since its only zero-cell supports the six five-cells and there are no intermediate cells, every attaching map is constant and its homotopy type is \(\bigvee^{6}S^{5}\).

4. **Symmetry character.** For every one of the 120 permutations of the five symbols, the verifier checks graph adjacency preservation and pair equivariance. It calculates the alternating signed trace on simplicial chains fixed setwise by that permutation, including orientation inversion parity. By the Lefschetz trace identity and concentration in fifth homology, the resulting fifth-homology character agrees on all 120 elements with

\[
\chi(g)=\tfrac12\bigl((f(g)-1)^2-(f(g^2)-1)\bigr),
\]

where \(f(g)\) counts fixed points of \(g\) on the five-symbol set. This is the exterior-square character of the standard four-dimensional module. The character values have frequencies \((-2:15,\;0:80,\;1:24,\;6:1)\), and their squares sum to 120. Hence the rational representation is irreducible. The sum of character values is zero, so it has no invariant vectors. The collapse gives the asserted identification of the two complexes' rational homology representations.

## Verification
Run `python3 verify.py` from the extracted package using Python standard library only. It independently tests forests via two distinct finite criteria, checks all 1,024 masks, reconstructs every free pair and its unique coface, exhaustively tests acyclicity of the Morse matching, and verifies each of the 120 signed character traces. The recorded output is provided as `verification_output.txt` and ends in `VERIFY_OK`. Exhaustion is possible because the graph has exactly ten vertices. The finite certificate proves precisely the finite classification and the requisite Morse acyclicity; the infinite-level topological consequences use the cited general simplicial-collapse and discrete-Morse theorems, not an inference from approximate numerical experiments.

## Relationship to prior work
Grady, Knoll, Laskar and Lipman (2015, Definitions 2.1 and 2.7) introduced the cycle-independent and odd-cycle-independent hereditary vertex-set conditions, and studied their extremal parameters. This claim instead concerns the elementary-collapse relation between the associated simplicial complexes. Carnero Bravo (2023, Section 4) studies induced-forest complexes for other graph families, without providing the present odd-cycle comparison. The integral homotopy type and \(\mathfrak S_5\) top-homology character of \(\mathcal F(P)\) were independently recorded before this result; they are used as known comparands here, not presented as novel discoveries. A previously indexed Petersen three-cut complex has the same irreducible top-homology representation but is a different complex and gives no inclusion map or collapse of \(\mathcal B(P)\) onto \(\mathcal F(P)\). The distinctive result is the **ten-pair, symmetry-invariant simple-homotopy bridge** between two naturally motivated complex constructions.

## Limitations
The result is special to the ten-vertex Petersen graph; it does not establish such a collapse for general nonbipartite graphs. Its symmetries preserve the *collection* of free pairs, rather than the individual sequential deletion order; no claim is made that every individual elementary collapse is fixed by the full group. The 10 induced six-cycles are a known structural feature of Petersen's graph, and their number alone is not claimed original. Equivalence to earlier unindexed terminology (odd-cycle hitting-set duals, signed Petersen graph literature, or historical computational tables) remains a literature risk. No independent mathematical audit has been performed.

## References
1. Grady, Knoll, Laskar and Lipman, Cycle Domination, Independence, and Irredundance in Graphs, arXiv:1505.02268v1, posted 2015-05-09. https://arxiv.org/pdf/1505.02268
2. Carnero Bravo, The Forest Filtration of a Graph, arXiv:2307.13271, initially posted 2023-07-25. https://arxiv.org/pdf/2307.13271
3. Zaslavsky, Six signed Petersen graphs, and their automorphisms, Discrete Mathematics 312 (2012), DOI:10.1016/j.disc.2011.12.010; abstract and secondary indexing inspected only.
4. Forman, Morse theory for cell complexes, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
