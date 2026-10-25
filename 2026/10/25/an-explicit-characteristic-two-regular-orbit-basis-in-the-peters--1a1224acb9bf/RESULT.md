# An explicit characteristic-two regular-orbit basis in the Petersen forest complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its ten vertices are two-element subsets of \(\{0,1,2,3,4\}\), adjacent precisely when disjoint. Let \(\mathcal F(P)\) be its forest complex, with one simplicial vertex for each of the fifteen graph edges and one face for each acyclic edge subset. Under the natural relabeling action of \(S_5\), the top modular homology is a **free rank-two group-algebra module**:
\[
\boxed{\widetilde H_8(\mathcal F(P);\mathbb F_2)\cong_{\mathbb F_2[S_5]}\mathbb F_2[S_5]^{\oplus2}.}
\]
Two explicit eight-cycles over \(\mathbb F_2\), specified in `verify_mod2.py` by complete 2,000-bit facet-coefficient vectors, have 120 translates apiece which together form a basis. The top homology has dimension 240 over \(\mathbb F_2\). This statement is stronger than the previously known characteristic-zero identification: reduction modulo two of a rationally regular representation need not be regular or free.

## Assumptions and scope
The simplicial complex is the **graphic-matroid independence complex** of the Petersen graph, not its ordinary vertex independence complex, matching complex, or graph-Morse complex. The fifteen graph edges are ordered lexicographically by their indices in the lexicographically ordered ten two-subsets. Top simplices are precisely the 2,000 nine-edge spanning trees ordered by their 15-bit masks. A coefficient bit in either supplied seed is the coefficient of that indexed top simplex in the field \(\mathbb F_2\). Every label permutation induces a permutation of the graph edges and of the spanning-tree facets; no orientation signs are needed in characteristic two. The theorem concerns \(\mathbb F_2[S_5]\)-modules only. It does not assert an integral \(\mathbb Z[S_5]\)-lattice splitting or a characteristic-three or characteristic-five version.

## Proof
**(1) The top chain complex.** Construct the ten graph vertices and fifteen graph edges from disjoint two-subsets of a five-element set. For each 15-bit edge mask, the disjoint-set union algorithm tests whether the selected edges form a forest. This yields exactly 2,000 nine-edge forests and 4,680 eight-edge forests. Since the Petersen graph is connected, every nine-edge forest is a spanning tree; no forest has ten or more edges. Hence the top augmented chain group is \(C_8\cong\mathbb F_2^{2000}\), with zero incoming boundary, and its differential \(\partial_8:C_8\longrightarrow C_7\cong\mathbb F_2^{4680}\) has matrix with entry one whenever the lower forest is obtained by deleting one edge from the upper forest.

**(2) The exact kernel dimension.** The deterministic bitwise Gaussian elimination in `verify_mod2.py` constructs **all** 4,680 rows of this complete boundary matrix. Their rank over \(\mathbb F_2\) is exactly 1,760, so
\[
\dim_{\mathbb F_2}\widetilde H_8(\mathcal F(P);\mathbb F_2)=\dim\ker\partial_8=2000-1760=240.
\]
This is a complete finite-field proof of the top dimension, not an extrapolation from samples. The classical matroid independence-complex shellability theorem also identifies the integral homotopy type as a wedge of degree-eight spheres, but that known theorem is not needed to prove the modular representation.

**(3) Two explicit cycles.** The source file `verify_mod2.py` contains two hexadecimal strings in `SEED_HEX`. Interpret each as a nonnegative binary integer; bit \(j\), with the least significant bit numbered zero, is the coefficient of the \(j\)-th nine-edge forest in ascending mask order. The first seed has 972 nonzero facet coefficients; the second has 992. The verifier checks each of the 4,680 boundary equations for both seeds, and every equation vanishes modulo two. Thus each is a genuine mod-two top-dimensional cycle.

**(4) An exact 240-column orbit-basis certificate.** For each seed and for each of all 120 permutations of the five graph labels, transport every supported facet to the image graph-edge mask, and use its index in the same ascending list of spanning trees. The verifier explicitly constructs all 240 such transported 2,000-bit coefficient columns, checks that all 240 are cycles, and performs binary Gaussian elimination on the columns. Their rank is **240**, equal to the full top-homology dimension. There is no boundary group in degree eight from above, since the forest complex has dimension eight. The 240 orbit classes are therefore a basis, and the action permutes the 120 translates of each seed freely and regularly. This gives the stated two-summand group-algebra isomorphism, including in nonsemisimple characteristic two.

## Verification
From the standalone supplied source, execute `python3 verify_mod2.py`. It uses only the Python standard library, with exact integer masks and binary elimination. It prints `TOP_BOUNDARY_RANK_MOD2 1760 H8_DIM_MOD2 240`, `EXPLICIT_SEED_SUPPORT_SIZES 972 992`, `TWO_120_ELEMENT_SYMMETRY_ORBITS_RANK_MOD2 240`, and the terminal marker `VERIFY_OK_PETERSEN_FOREST_COMPLEX_MOD2_REGULAR_ORBIT_BASIS`. The explicit seeds are in the source, not in an external path. The verifier constructs every graph edge, forest, boundary row and group orbit from definitions.

## Relationship to prior work
Graphic-matroid topology and sphere-wedge shellability are classical; see Swartz's exposition (arXiv:math/0208157, sections 2–3). General characteristic-zero representations of matroid automorphism groups are studied by Moci–Pezzoli (arXiv:2001.03760, Theorem 19 and sections 6–7). A prior Petersen forest-complex calculation already determined that its characteristic-zero top homology is two regular \(S_5\)-representations. That determination does **not** imply an isomorphism over \(\mathbb F_2[S_5]\), since the modular group algebra is not semisimple. The 240 explicitly independent binary orbit vectors provide the additional mathematical content and distinguish this theorem from any character-only calculation. Existing work on Petersen matching, Morse and cut complexes treats different simplicial objects.

## Limitations
The theorem is restricted to characteristic two and to this specific graphic matroid. It proves a modular orbit basis, not a basis over the integers; a pair of orbit bases modulo two need not be integrally unimodular. Computational exhaustiveness depends on the fully specified 15-edge labeling and 2,000-facet ordering, both reconstructed in the checker. Earlier rational character computations and general matroid representation theorems remain relevant context; equivalent modular statements could exist in unindexed literature. Independent scientific validation is not claimed.

## References
1. E. Swartz, *Topological representations of matroids*, arXiv:math/0208157, originally posted 22 August 2002, sections 2–3. https://arxiv.org/abs/math/0208157
2. L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760, originally posted 11 January 2020, Theorem 19 and sections 6–7. https://arxiv.org/abs/2001.03760
3. A. E. Brouwer, *Petersen graph*, graph structure and symmetry. https://aeb.win.tue.nl/drg/graphs/Petersen.html
