# Integral induced-forest topology and signed permutation symmetry of the folded five-cube

## Finding

Let \(C\) be the five-regular, sixteen-vertex Clebsch graph (the folded five-cube), with vertices \(\{0,\ldots,15\}\) and edges \(uv\) whenever the bitwise XOR \(u\mathbin{\mathrm{xor}}v\) is one of \(1,2,4,8,15\). Define its **induced-forest complex**
\[
\mathcal F(C)=\{A\subseteq V(C):C[A]\text{ is a forest}\}.
\]
Then the integral homotopy type is
\[
\boxed{\mathcal F(C)\simeq\bigvee^{15}S^5.}
\]
For its complete automorphism group \(G\cong(\mathbb Z/2)^4\rtimes\mathfrak S_5\), the rational fifth homology is the sign-twisted augmentation representation of the sixteen-vertex permutation action:
\[
\boxed{\widetilde H_5(\mathcal F(C);\mathbb Q)\cong_{\mathbb QG}
\bigl(\operatorname{sgn}\circ\pi\bigr)\otimes
\ker\bigl(\mathbb Q[V(C)]\xrightarrow{\sum}\mathbb Q\bigr),}
\]
where \(\pi:G\to\mathfrak S_5\) is the permutation of the five neighbors of zero after translation to zero. This fifteen-dimensional rational representation splits into nonisomorphic irreducible summands of dimensions five and ten, and has no nonzero \(G\)-fixed vector.

## Assumptions and scope

The graph is specifically the **five-regular** Clebsch graph, not its ten-regular complement. All graphs are simple and undirected; all complexes are abstract simplicial complexes of **vertex** subsets, not graphic-matroid complexes of edge subsets. A subset is a face exactly when the induced graph is acyclic. Homotopy equivalences concern ordinary geometric realizations. Integral claims use \(\mathbb Z\) coefficients; representation claims are only over \(\mathbb Q\).

The graph's forty edges are precisely the pairs whose four-bit XOR is one of \(1,2,4,8,15\). It has parameters \((16,5,0,2)\). The complex has 13,839 faces including the empty face, and nonempty face numbers in dimensions zero through eight are
\[
(16,120,560,1780,3696,4376,2560,650,80).
\]
Thus it is nonpure and contains eighty eight-simplices, although its homotopy is concentrated in dimension five.

## Proof

**Graph model and symmetry.** Regard the four-bit vertex set as the additive group \(V=(\mathbb Z/2)^4\). Its five connection vectors are \(e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\); their only nontrivial linear relation is their sum. Every permutation of these five vectors extends uniquely to a linear automorphism of \(V\), and translations preserve adjacency. Any automorphism fixing zero acts faithfully on the five neighbors: the remaining ten vertices are in bijection with the ten distinct pairwise sums of neighbors, and each is determined by its two common neighbors with zero. Hence the full automorphism group has order \(16\cdot120=1920\), and equals \(V\rtimes\mathfrak S_5\). Identifying vertices with even-parity five-bit vectors sends the five connection vectors to the five vectors of Hamming weight four, making explicit the folded-five-cube description.

**Exact finite Morse model.** Enumerate all \(2^{16}=65,536\) vertex subsets. For each subset independently test acyclicity by union-find and by the identity \(|E(C[A])|=|A|-\#\operatorname{components}(C[A])\); the two predicates agree on every subset. Sort the valid masks and process pivot vertices \(v=0,1,\ldots,15\). At pivot \(v\), pair every currently unmatched face \(A\not\ni v\) with \(A\cup\{v\}\) whenever both are present. This constructs 6,908 disjoint incident pairs and leaves nineteen unmatched five-faces and four unmatched six-faces; the empty face is paired. Orient the full Hasse diagram downward except for the paired incidences, which point upward. Complete topological sorting of all 13,839 faces and all 77,632 incidences finds no directed cycle. This is therefore an acyclic algebraic/discrete-Morse matching.

Orient each simplex by its ascending vertex list. For a matched lower face \(L\subset U\) of incidence sign \(\epsilon\), eliminate \(L\) using the relation
\[
[L]\longmapsto-\epsilon\sum_{J\subset U,\,|J|=|L|,\,J\ne L}[U:J]\,[J],
\]
recursively substituting matched lower faces and sending matched upper faces to zero. Here \([U:J]=\pm1\) is the standard oriented incidence coefficient. Acyclicity makes the gradient recursion finite. Applied to the four critical six-cells, this yields an explicit \(19\times4\) integral Morse differential. Its rows with zero-based indices \(0,1,3,4\) and all four columns give
\[
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
-1&0&0&0\\
0&-1&0&0
\end{pmatrix},
\]
with determinant \(1\). Thus the differential is a primitive rank-four embedding of free abelian groups. After removing the augmented empty-face pair, the ordinary Morse CW complex has one zero-cell, nineteen five-cells and four six-cells, with no other positive-dimensional cells. The five-skeleton is a bouquet of nineteen five-spheres. Since \(\pi_5(\bigvee^{19}S^5)\cong\mathbb Z^{19}\), the four six-cell attaching maps are classified by their integral degree vectors. The primitive rank-four differential can be put into a four-by-four identity block by integer changes of basis, so four sphere/cell pairs cancel up to homotopy. The remaining fifteen five-spheres prove the displayed integral equivalence. In particular, no higher attaching-map ambiguity or integral torsion is being inferred merely from Betti numbers.

**Equivariant identification.** For each \(g=(t,\sigma)\in V\rtimes\mathfrak S_5\), a face fixed setwise by \(g\) is a union of vertex orbits. If it uses \(r\) orbits and contains \(m\) vertices, the induced permutation on that simplex has sign \((-1)^{m-r}\). The simplicial Lefschetz formula, including the reduced empty-face term and the fact that only fifth reduced homology survives, gives
\[
\operatorname{tr}\bigl(g\mid\widetilde H_5(\mathcal F(C);\mathbb Q)\bigr)
=\sum_{\substack{A\in\mathcal F(C)\\gA=A}}(-1)^{r_g(A)},
\]
where \(r_g(A)\) denotes the number of selected vertex orbits and the empty face contributes \(1\). Exhaustively evaluating this finite sum for all 1,920 graph automorphisms gives the exact identity
\[
\operatorname{tr}\bigl(g\mid\widetilde H_5\bigr)
=\operatorname{sgn}(\sigma)\bigl(|\operatorname{Fix}_{V(C)}(g)|-1\bigr).
\]
The right side is precisely the character of the claimed sign-twisted augmentation representation; equality of rational characters of finite groups establishes the rational-module isomorphism.

To see the two irreducible rational summands, diagonalize the translation subgroup \(V\) by its rational Walsh characters (taking only values \(\pm1\)). The augmentation module contains each nontrivial character once. Permuting the five connection-vector labels acts on the fifteen nontrivial dual characters with two orbits, of cardinalities five and ten (represented by singleton and two-element subsets of a five-element set, modulo complementation). Each orbit span is irreducible: a translation-invariant submodule splits into character lines, and \(\mathfrak S_5\) acts transitively on the lines of each orbit. Twisting by the sign character preserves irreducibility. The character sum over the entire group is zero, so the fixed subspace is zero.

## Verification

Run `python3 verify_clebsch.py` with Python 3.8 or newer. It uses only the standard library and terminates with `VERIFY_OK`. The complete deterministic output is included in `verification_output.txt`, including all critical-cell masks, the full signed Morse matrix, the unimodular minor, independent mod-two simplicial boundary ranks, and all character multiplicities. It independently enumerates and compares two predicates for all subsets, topologically sorts the directed Hasse graph, evaluates gradient-path boundaries over \(\mathbb Z\), computes every ordinary mod-two boundary rank, and checks all 1,920 automorphism characters. These are finite exhaustive certificates for this finite graph, not a claim about all folded cubes.

The resulting character-value distribution (value, number of group elements) is
\[
(-7,20),\ (-1,835),\ (0,384),\ (1,540),\ (3,140),\ (15,1).
\]
Its squared character norm is \(2\), consistent with the two inequivalent rational irreducible constituents. All ordinary reduced mod-two Betti numbers vanish except the fifth, which is \(15\).

## Relationship to prior work

Taylan (arXiv:1501.06754, first made public 2015-01-27) introduced a general vertex-set devoid-complex framework and methods based on matching trees. Its worked homotopy families concern path, cycle and forest hosts with specified forbidden small subgraphs, not this Clebsch induced-cycle avoidance construction. Carnero Bravo (arXiv:2307.13271, first made public 2023-07-25) explicitly studies the induced-forest endpoint of the forest filtration and establishes results for paths, cycles, cactus graphs, multipartite graphs and graph operations. Those published statements do not imply this case, since the Clebsch graph is a nonplanar, triangle-free strongly regular graph outside the listed families.

Published calculations of the ordinary Clebsch independence complex, neighborhood complex, and intrinsic Čech nerves concern different face conditions. In particular, the independence complex has only independent vertex subsets, whereas \(\mathcal F(C)\) allows every induced tree and disconnected forest. A general folded-cube neighborhood-complex theorem does not imply its induced-forest topology. Searches of equivalent terminology and indexed mathematical records did not identify a stronger result determining both the present integral homotopy type and equivariant fifth homology. This is a best-knowledge originality assessment, not a proof that no unpublished or unindexed equivalent exists.

## Limitations

The proof is an exact, finite, computer-checkable calculation for the specific five-regular Clebsch graph; no theorem is asserted for other folded hypercubes. The integral homotopy type is established, while the group action is classified only rationally (no integral lattice isomorphism is claimed). The Morse matching and group character evaluation require the accompanying executable finite verifier for full independent reproduction. No independent external mathematical audit has been performed. Relevant published-source comparisons include accessible full-text portions and index records; possible unindexed equivalent results remain an originality risk.

## References

1. Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1, 27 January 2015, https://arxiv.org/abs/1501.06754.
2. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271v1, 25 July 2023, https://arxiv.org/abs/2307.13271.
3. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
4. Published indexed results on the ordinary Clebsch independence complex and folded-cube neighborhood complexes, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-clebsch-independence-complex-is-a-wedge-of-nine-3-spheres--344f83b86fa0 and https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-neighborhood-complexes-of-odd-folded-hypercubes-are-wedges-o--438357602cff (indexed descriptions; complete repository documents were not accessible at review).
