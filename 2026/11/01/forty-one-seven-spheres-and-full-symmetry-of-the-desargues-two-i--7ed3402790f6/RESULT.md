# Forty-one seven-spheres and full symmetry of the Desargues two-independence complex

## Finding
Let \(D\) be the bipartite Desargues graph with vertex set
\[V(D)=\binom{[5]}2\sqcup\binom{[5]}3,\]
with an edge between \(A\in\binom{[5]}2\) and \(B\in\binom{[5]}3\) precisely when \(A\subset B\). Let \(X=\operatorname{Ind}_2(D)\) consist of vertex subsets inducing a graph whose connected components each have at most two vertices. Then
\[\boxed{X\simeq \bigvee^{41}S^7.}\]
In particular, \(\widetilde H_7(X;\mathbb Z)\cong\mathbb Z^{41}\) and all other reduced integral homology groups vanish.

The full automorphism group is \(S_5\times C_2\), where \(S_5\) acts on the labels and the central involution complements subsets in \([5]\), exchanging the two bipartition layers. For each partition \(\lambda\vdash5\), let \(V_\lambda=S^\lambda\) be the corresponding rational Specht representation of \(S_5\), and denote its extension with layer-complement eigenvalue \(\pm1\) by \(V_\lambda^\pm\). Then
\[
\begin{aligned}
\widetilde H_7(X;\mathbb Q)\cong{}&
V_{(5)}^+\oplus V_{(4,1)}^+\oplus V_{(3,2)}^+
\oplus V_{(3,1,1)}^+\oplus V_{(2,2,1)}^+\\
&\oplus V_{(3,2)}^-\oplus V_{(3,1,1)}^-
\oplus V_{(2,2,1)}^-\oplus V_{(2,1,1,1)}^-.
\end{aligned}
\]
Every displayed irreducible occurs once. Consequently the central involution has eigenspace dimensions \(21\) and \(20\), and the only full-group invariant reduced rational homology is one line in degree seven. In particular the full-symmetry quotient has
\[\widetilde H_i(X/(S_5\times C_2);\mathbb Q)\cong\begin{cases}\mathbb Q,&i=7,\\0,&i\ne7.\end{cases}\]
This quotient statement does not determine its homotopy type or integral homology.

## Assumptions and scope
The graph is the unweighted, undirected, simple twenty-vertex Desargues graph with thirty edges; no geometric realization or edge subdivision is involved in its definition. A face of \(X\) is a subset whose induced subgraph has **maximum degree at most one**, equivalent here to the component-size-at-most-two condition. This is not the ordinary independence complex \(\operatorname{Ind}_1(D)\), and not the distance-two independence complex. Homology has constant integral or rational coefficients as explicitly indicated, and \(\widetilde H\) denotes reduced homology. The result is for exactly \(r=2\), with no assertion about other parameters or other graphs.

## Proof
**Graph symmetry.** The layer-preserving automorphism group induces the automorphism group of the triangular graph on the ten two-subsets: two two-subsets have a common three-subset neighbor if and only if they intersect in one element. Its five size-four star cliques recover the underlying five labels; hence every layer-preserving automorphism comes from \(S_5\). Complementation interchanges the two layers and commutes with label permutations. Since the connected bipartite graph has a unique bipartition up to exchange, \(\operatorname{Aut}(D)\cong S_5\times C_2\).

**Integral homotopy.** Enumerate the twenty vertices in lexicographic order, listing the two-subsets first, then the three-subsets. An exact exhaustive enumeration of all subsets whose induced degrees are at most one gives \(62{,}048\) nonempty faces. Their numbers by dimensions zero through eleven are
\[(20,190,1080,3985,9784,15910,16600,10390,3460,564,60,5).\]
On the augmented face poset, including the empty face, successively process each vertex \(v\): match each currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both faces remain. This produces exactly \(31{,}004\) pairs, leaving exactly forty-one unpaired faces, all of cardinality eight. An exhaustive topological sort of the full oriented Hasse diagram (reversing the matched edges) visits all \(62{,}049\) vertices, hence proves the matching is acyclic. Unmatching the unique pair containing the empty face yields an ordinary acyclic matching on nonempty faces with exactly one critical vertex and forty-one critical seven-faces. Forman's discrete Morse theorem supplies a CW model with a single zero-cell and forty-one seven-cells, and no cells in intermediate dimensions. All attachments of seven-cells to a point are nullhomotopic, so the complex is a wedge of forty-one seven-spheres. This is an **integral homotopy equivalence**, not an inference from field-valued Betti numbers.

**Full rational character.** For any label permutation \(\pi\) and complement flag \(e\in\{0,1\}\), construct the induced permutation of the twenty vertices and calculate the signed trace of its action on each oriented simplicial chain group: a face contributes only when setwise fixed, with the sign of its induced vertex ordering. Subtract one for the reduced degree-minus-one chain. Thus the computed reduced Lefschetz number is
\[L(\pi,e)=-1+\sum_{\substack{\sigma\in X\\\sigma\ne\varnothing,\ (\pi,e)\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}((\pi,e)|_\sigma).\]
Since reduced homology is concentrated in degree seven, \(\operatorname{tr}((\pi,e)|\widetilde H_7)=-L(\pi,e)\). It suffices to calculate the fourteen conjugacy classes of \(S_5\times C_2\). In cycle-type order \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\), the traces with \(e=0\) are
\[(1,1,1,-1,1,1,41),\]
and with \(e=1\) are
\[(1,1,-1,1,1,5,1).\]
Taking exact character inner products against the seven rational irreducibles of \(S_5\) tensored with the two signs of \(C_2\) produces exactly the nine constituents displayed above. The calculation separately verifies orthogonality of the seven \(S_5\) character formulas, the dimension sum \(41\), and the two central eigenspace dimension sums \(21\) and \(20\). The trivial representation appears once. For a finite simplicial group action, rational homology of the quotient agrees with rational invariants (for example after equivariant barycentric subdivision and averaging); the quotient assertion follows.

## Verification
Run `python3 verify_desargues_higher.py` with Python's standard library. The self-contained program reconstructs the graph from subset inclusion, enumerates all allowed faces recursively and independently by exhaustive dynamic processing of all \(2^{20}\) vertex subsets, checks the full face vector, constructs every matching pair, and checks acyclicity by topological sorting of all augmented Hasse faces. It also explicitly checks that all \(240\) proposed automorphisms preserve adjacency, calculates reduced signed Lefschetz traces for representatives of all fourteen conjugacy classes, and checks exact irreducible character orthogonality, multiplicities, dimensions and invariant rank. The expected exact output is embedded as `verify_desargues_higher.out`. The program ends with `ALL_CHECKS_PASS` only after all assertions hold. It supplies the finite certificate for the global matching and group-character calculations; the mathematical implications are given in the proof above.

## Relationship to prior work
Salvetti introduced higher/d-independent graph complexes in connection with Artin groups; the earliest verified date-only public bibliographic record for the foundational chapter used here is January 25, 2016. Its publisher preview describes the general construction, not a Desargues-specific computation. Deshpande and Singh's full openly accessible 2020 preprint treats complete multipartite, fully whiskered, cycle, and perfect rooted-tree families. Its matching lemmas support the proof technique but its stated classifications do not include the cubic Desargues graph. Previously available ordinary independence-complex and matching-complex calculations for this graph concern **different** face conditions; their Betti numbers and symmetry actions do not imply this result. The new contribution is the exact two-independence integral homotopy type together with its full rational symmetry decomposition, not the general matching method, the graph description, or the ordinary independence homology.

## Limitations
This classification is limited to the Desargues graph at independence parameter two. It does not establish an integral representation-lattice splitting, an equivariant homotopy equivalence, torsion or homotopy invariants of the symmetry quotient, or uniform formulas for arbitrary generalized Petersen graphs. Publication-priority uncertainty persists for unindexed sources, and the Salvetti chapter was available in abstract/preview form rather than as accessible full text. The finite exact computation and its reproducibility artifacts are included and delimit the computational component of the proof.

## References
- M. Salvetti, *Some Combinatorial Constructions and Relations with Artin Groups*, in *Combinatorial Methods in Topology and Algebra*, Springer INdAM Series 12, 121–126, DOI: https://doi.org/10.1007/978-3-319-20155-9_22 . Bibliographic online availability record dated January 25, 2016: https://portal.mardi4nfdi.de/wiki/Some_combinatorial_constructions_and_relations_with_Artin_groups .
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (first posted January 15, 2020): https://arxiv.org/abs/2001.05448 .
- P. Deshpande, S. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775 (first posted January 19, 2020): https://arxiv.org/abs/2001.06775 .
- R. Forman, *A user's guide to discrete Morse theory*, Séminaire Lotharingien de Combinatoire 48 (2002), Article B48c.
