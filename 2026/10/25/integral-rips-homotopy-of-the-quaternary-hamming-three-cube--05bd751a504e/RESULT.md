# Integral Rips homotopy of the quaternary Hamming three-cube

## Finding

Give \(X=\{0,1,2,3\}^{3}\) the Hamming distance \(d_H(x,y)=|\{i:x_i\ne y_i\}|\). For each real \(r\ge0\), let \(R_r=\operatorname{VR}_{\le r}(X)\) be the flag complex on those edges whose Hamming distance is at most \(r\). Then the **integral homotopy types at all filtration scales** are

\[
|R_r|\simeq
\begin{cases}
\bigsqcup^{64}\{*\},&0\le r<1,\\
\bigvee^{81}S^1,&1\le r<2,\\
\bigvee^{405}S^3,&2\le r<3,\\
\{*\},&r\ge3.
\end{cases}
\]

At the difficult intermediate scale there is an equality of abstract simplicial complexes,
\[
R_2=\operatorname{Ind}(K_4\times K_4\times K_4),
\]
where the product is categorical (tensor): a pair is joined in the product precisely when its three coordinates all differ. Thus this calculation proves the \((4,4,4)\) case of the *previously formulated* three-factor independence-complex homotopy conjecture; the predicted number of \(405\) spheres is not claimed as a new conjectural formula.

For any field, the nontrivial persistent-homology bars are \(63\) reduced degree-zero bars \([0,1)\), \(81\) degree-one bars \([1,2)\), and \(405\) degree-three bars \([2,3)\). The unreduced degree-zero persistence also has one infinite bar. The corresponding groups are free over \(\mathbb Z\).

## Assumptions and scope

The sixty-four points are all length-three words on the four-symbol alphabet, not points of a continuous cube. Only the discrete Hamming metric is used. Distance thresholds are **inclusive**, and all homotopy types refer to geometric realizations of finite abstract simplicial complexes. For the finite certificate, index words lexicographically by \((a,b,c)\mapsto16a+4b+c\). The single claim concerns this fixed three-coordinate, four-symbol space, at every real \(r\ge0\); no arbitrary-alphabet conclusion is asserted.

## Proof

**Thresholds zero, one and three.** Distinct points have integer Hamming distance \(1\), \(2\), or \(3\). Below scale one there are only sixty-four isolated vertices, and at scale three all pairs are edges, giving the full simplex. At scale one, a clique of at least two vertices varies in only one coordinate: if neighbors of a point vary in different coordinates, those two neighbors have distance two and cannot be a scale-one edge. Consequently every nonsingleton face lies in a unique coordinate line, a full three-simplex on four points. There are \(3\cdot 4^2=48\) coordinate lines, with pairwise intersections at most single vertices, and every line-simplex collapses onto any spanning tree on its four vertices. These local collapses leave a connected graph with \(64\) vertices and \(48\cdot3=144\) edges. Its cycle rank is \(144-64+1=81\), so the scale-one complex is a wedge of \(81\) circles.

**Scale-two graph duality.** Two distinct words have distance at most two exactly when they agree in at least one coordinate. Their pair is an edge of the categorical product \(K_4\times K_4\times K_4\) precisely when they differ in all three coordinates. Hence the scale-two flag complex is exactly the independence complex of that product.

**Exhaustive maximal-simplex characterization.** The scale-two complex has exactly \(508\) maximal simplices: \(12\) coordinate planes of \(16\) vertices (one coordinate fixed), \(64\) Hamming balls of radius one of \(10\) vertices, and \(432\) four-vertex parity tetrahedra. To specify the latter, choose a two-element subset in each coordinate (\(\binom42^3=216\) choices), identify the eight resulting words with \(\{0,1\}^3\), and select either the four even-parity or four odd-parity words. This explicitly produces \(216\cdot2=432\) tetrahedra. The checker independently enumerates maximal cliques of the scale-two graph by a pivoted Bron--Kerbosch algorithm and verifies **equality of the complete sets** with these three constructed families. This finite exhaustive equality, not a guessed facet list, proves the characterization for the specified space.

**All faces and the discrete-Morse certificate.** Generate every subset of every maximal simplex and merge duplicates. The checker obtains exactly \(830{,}101\) faces including the empty face, with nonempty face numbers in dimensions zero through fifteen:
\[
(64,1152,8256,29136,64512,108192,144768,157320,137920,96160,52416,21840,6720,1440,192,12).
\]

Starting with all faces unused (including the empty face), scan vertex indices \(v=0,1,\ldots,63\). For each \(v\), pair every still-unused face \(F\) not containing \(v\) with \(F\cup\{v\}\) when both remain unused; delete both from the unused set before the next index. Each stage is a valid collection of disjoint Hasse cover pairs: lower faces omit \(v\), upper faces contain it. The result is \(414{,}848\) matched pairs, including the empty-to-first-vertex pair, and **exactly \(405\) unmatched tetrahedra** (three-dimensional faces). Removing the empty face and its paired incidence yields an ordinary matching on the nonempty face poset with one unmatched zero-dimensional vertex and \(405\) unmatched three-dimensional cells.

**Complete acyclicity.** Orient every codimension-one face-poset relation from upper face to lower, reversing precisely the matched relations. The checker builds these directions explicitly for all \(830{,}101\) augmented faces and all \(6{,}539{,}456\) cover relations, computes every directed indegree, and performs a complete Kahn topological sort. It visits all \(830{,}101\) face nodes and reduces all indegrees to zero. Consequently the augmented matching is acyclic. The ordinary nonempty matching is a restriction of this acyclic directed graph, hence also acyclic. Forman's discrete-Morse theorem supplies a CW complex with one zero-cell and \(405\) three-cells and **no other cells**. Each three-cell therefore attaches to the unique point, yielding the integral homotopy equivalence \(R_2\simeq\bigvee^{405}S^3\); neither a rank calculation nor a field-specific argument is needed.

**Persistence.** The Rips complex changes only at distances one, two and three. Reduced homology is nonzero in degrees zero, one, and three, respectively, in distinct consecutive scale intervals; its maps to the next scale necessarily vanish since the corresponding target group is zero. The groups are free, so the interval description follows over fields, with the stated integral ranks, and there is one permanent unreduced degree-zero class.

## Verification

Run `python3 verify.py` with ordinary Python 3 and the standard library only. The program reconstructs all edges from Hamming distances; independently verifies the complete \(508\)-facet taxonomy; enumerates all face subsets; recomputes the staged matching; and tests every directed face-poset cover via a complete topological sort. A successful run emits the lines `FACETS_OK`, `FACES_OK`, `MATCHING_OK`, `ACYCLIC_OK`, and `VERIFY_OK`. It verifies the full face vector, \(414{,}848\) augmented pairs, \(405\) critical tetrahedra, and \(6{,}539{,}456\) directed incidences. The elementary scale-one and scale-three calculations are proved above without relying on the executable. The exhaustive computation proves the finite scale-two assertion because it checks **every** face and matching incidence of this finite complex, not because sampling suggests the result.

## Relationship to prior work

Antolín Camarena and Carnero Bravo formulated the general three-complete-graph product homotopy formula as Conjecture 26 in 2023, and proved its case with one factor \(K_2\) (Proposition 25). Their formula predicts \(405\) three-spheres for three factors \(K_4\), but their proved case does **not** cover this case. Carnero Bravo's 2026 generalized-Mycielskian work treats Kronecker covers and applications to products of **two** complete graphs, not the three \(K_4\) product itself. Earlier work of Goyal, Shukla, and Singh addresses two-factor complete-graph products.

Two published exact ternary Rips calculations separately establish the scale-two homotopy type for \(\{0,1,2\}^3\), namely \(\bigvee^{46}S^3\). They give neither a uniform alphabet-size theorem nor the present sixty-four-vertex quaternary certificate. Here the extra facets of parity-tetrahedron type and all \(830{,}101\) faces are resolved explicitly. The work is a single natural finite case of the published conjecture and a complete metric filtration, not a proof of the conjecture for every alphabet size.

## Limitations

The theorem is specific to the \(64\)-point quaternary three-cube; it does not prove the full three-factor conjecture or an arbitrary-parameter recurrence. Its main finite proof relies on reproducible exhaustive integer and bitset computation and ordinary trust in a Python interpreter and mathematical implementation of the graph. The verifier itself is supplied; there is no external formal proof assistant or independent validation. Bibliographic priority remains conditional on discoverable sources: an unindexed equivalent result might exist. The formula for the sphere count was already conjectured and is not presented as numerically unforeseen.

## References

1. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432 (first public 2026-01-19), https://arxiv.org/abs/2601.13432; Section 3 applications to products of two complete graphs.
2. Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public 2023-07-23), https://arxiv.org/abs/2307.12401; Proposition 25 and Conjecture 26.
3. Shuchita Goyal, Shamik Shukla, and Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019), https://arxiv.org/abs/1905.06926.
4. *Complete Vietoris--Rips persistence of the ternary three-cube*, published-finding corpus mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-vietoris-rips-persistence-of-the-ternary-three-cube--62d7487289d8.
5. *The ternary Hamming Rips filtration and the \(K_3\times K_3\times K_3\) case*, published-finding corpus mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-ternary-hamming-rips-filtration-and-the-k-3-times-k-3-times--964b171a73c5.
6. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90--145.
