# A cyclic four-dimensional collapse and a nonzero cup product for fourth-power cycle neighborhood complexes

## Finding
For every integer \(n\ge17\), let \(G_n=C_n^4\) be the simple graph with vertex set \(\mathbb Z/n\mathbb Z\) and edges at cyclic distance \(1,2,3,4\). Let \(K_n=\mathcal N(G_n)\) be its ordinary *open* Lovász neighborhood complex: a nonempty vertex set is a face precisely when it has a common neighbor in \(G_n\). Define a subcomplex \(L_n\) by the \(8n\) distinct four-dimensional facets
\[
P_{i,\epsilon}=\{i,i+8,i+1+4\epsilon_1,i+2+4\epsilon_2,i+3+4\epsilon_3\},
\qquad i\in\mathbb Z/n\mathbb Z,\quad\epsilon\in\{0,1\}^3.
\]
All indices in this document are modulo \(n\), and every displayed set is an unordered simplex. Then \(K_n\) simplicially collapses to \(L_n\) in exactly \(58n\) explicit elementary collapse pairs, using the accompanying 58-orbit certificate. The nonempty face vectors are
\[
f(K_n)=n(1,8,27,49,49,27,8,1),\quad
f(L_n)=n(1,7,18,20,8).
\]
Moreover, the mod-two cup product
\[
H^1(K_n;\mathbb F_2)\otimes H^3(K_n;\mathbb F_2)
\longrightarrow H^4(K_n;\mathbb F_2)
\]
is **nonzero** for every \(n\ge17\). Hence none of these complexes is homotopy equivalent to a wedge of positive-dimensional spheres. No assertion of a complete homotopy classification is made.

## Assumptions and scope
The threshold is inclusive, and the complex uses common *open* graph neighborhoods, not closed neighborhoods or a Vietoris–Rips construction. For \(n\ge17\), the graph is 8-regular, and each maximal face of \(K_n\) is contained in one of the eight-element open neighborhoods. The cohomology coefficient field is \(\mathbb F_2\). An elementary collapse removes a free proper face together with its unique coface, both of which are simplices of the current complex.

## Proof
**1. Local finite model and uniform collapse.** Translate any nonempty simplex until its cyclic support begins at 0. Because it is contained in a cyclic interval of length eight and \(n\ge17\), its cyclic vertex-gap sequence has a unique gap strictly larger than eight. Thus its translate representative is uniquely a nonempty subset of \(B=\{0,1,2,3,5,6,7,8\}\), shifted so its minimum is zero. Enumerating subsets of \(B\) gives exactly 170 orbit types. The corresponding types belonging to the displayed facets of \(L_n\) number exactly 54.

For a type \(s\) containing zero, every witness center for a one-vertex coface has an integer representative \(c\in\{-4,-3,-2,-1,1,2,3,4\}\). Every admissible new vertex has an integer representative \(w\in[-8,8]\); these are distinct residues for \(n\ge17\). Since \(|w-c|\le12<n-4\), cyclic neighborhood incidence is equivalent to the integer test
\[
\exists c\in\{-4,-3,-2,-1,1,2,3,4\}\quad
1\le |v-c|\le4\quad\text{for every }v\in s\cup\{w\}.
\]
Consequently the complete one-vertex coface incidence *with multiplicity* is independent of \(n\). The accompanying `collapse_templates.json` has 58 ordered pairs of orbit types. The standalone verifier constructs all 170 types from \(B\), checks in the current orbit-poset at each step that the lower member has exactly one still-present coface, determines its required translation offset, and removes both types. Exactly the 54 types of \(L_n\) remain. Since every type has precisely \(n\) translates and the orbitwise unique-coface condition gives mutually disjoint free pairs, this is an actual sequence of \(58n\) elementary collapses for every \(n\ge17\), not a finite extrapolation.

**2. Four-cycle and explicit cap product.** Work over \(\mathbb F_2\). For each \(i\), let \(P_i\) be the mod-two sum of the eight facets \(P_{i,\epsilon}\), and let \(\Sigma_i\) be the sixteen-tetrahedron octahedral three-sphere with facets
\[
\{i+\epsilon_0 4,i+1+\epsilon_1 4,i+2+\epsilon_2 4,i+3+\epsilon_3 4\},
\quad(\epsilon_0,\epsilon_1,\epsilon_2,\epsilon_3)\in\{0,1\}^4.
\]
Each \(P_i\) is the join of an edge with the boundary of a 3-dimensional crosspolytope. Direct face cancellation gives \(\partial P_i=\Sigma_i+\Sigma_{i+1}\). Hence \(\Gamma=\sum_i P_i\) is a nonzero simplicial four-cycle with \(8n\) facets.

On an ordered edge \(0\le a<b<n\), define \(\alpha([a,b])=1\) if \(b-a>8\), and 0 otherwise. Every simplex has a unique cyclic short-arc chart, so every triangle crosses the cut an even number of times; equivalently a direct three-edge check gives \(\delta\alpha=0\). The \(n\)-edge cycle \((0,1,\ldots,n-1,0)\), contained in the one-skeleton of \(L_n\), evaluates to 1 on \(\alpha\). Thus \([\alpha]\ne0\). The Alexander–Whitney cap computation on the sorted simplices gives the exact identity
\[
\alpha\frown\Gamma=\Sigma_{n-8}.
\]
This is a bounded local-index calculation: the contributing prisms are precisely those crossing the cut with one vertex on its lower side; their sixteen remaining tetrahedra are the stated crosspolytope-sphere facets. The verifier independently reconstructs this cancellation at several separated orders. Translation symmetry makes the homology classes of all \(\Sigma_i\) equal, because \(\partial P_i=\Sigma_i+\Sigma_{i+1}\).

**3. Nonbounding sphere by a dual cocycle.** Put \(A_i=\{i,i+1,i+2,i+3,i+8\}\), \(B_i=\{i,i+1,i+2,i+7,i+8\}\), and let \(B_{i+1}=\{i+1,i+2,i+3,i+8,i+9\}\). All are facets of \(L_n\). For each \(i\), the pair \((B_i,A_i)\) and the pair \((A_i,B_{i+1})\) share exactly one tetrahedron. The \(2n\) shared tetrahedra form a closed loop in the adjacency graph of four-simplices. Define the mod-two three-cochain \(\lambda\) to be its characteristic function, canceling repeated tetrahedra mod two. Its coboundary vanishes: every four-simplex is incident to an even number of edges of the dual loop (and all other four-simplices to zero). Moreover, a direct offset comparison gives \(\langle\lambda,\Sigma_0\rangle=1\): no internal intersection meets \(\Sigma_0\), and among the inter-block intersections only that for \(i=n-1\) is a facet of \(\Sigma_0\). Hence \([\Sigma_0]\ne0\) in \(H_3(L_n;\mathbb F_2)\). This conclusion transfers to \(K_n\) by the collapse.

Since the mod-two homology–cohomology pairing is perfect, choose \(\beta\in H^3(K_n;\mathbb F_2)\) evaluating to 1 on \([\Sigma_{n-8}]\). By the Alexander–Whitney cap/cup identity,
\[
\langle[\alpha]\smile\beta,[\Gamma]\rangle
=\langle\beta,[\alpha]\frown[\Gamma]\rangle=1.
\]
Thus the cup product is nonzero. A wedge of positive-dimensional spheres has trivial cup products in positive degrees, giving the final obstruction.

## Verification
Run `python3 verify.py collapse_templates.json` from the directory holding these two files. The program uses only the Python standard library. It checks all 58 orbit pairs against complete *integer* local coface enumerations and replays the full collapse on \(n=17,18,19,23,32\). It independently enumerates all original and residual faces, verifies all codimension-one incidence counts, and recomputes \(\Gamma\), the cocycle \(\alpha\), its cap-chain identity, the dual-loop cocycle and its odd evaluation. The retained output is `verification_output.txt`, ending in `VERIFY_OK`. The proof of the **uniform** assertion is the local-incidence reduction above; the sampled values alone are not used as an infinite proof.

## Relationship to prior work
The ordinary neighborhood complex and its relationship to graph Hom complexes are classical; Kozlov (2005) provides simple-homotopy equivalences for arbitrary graphs. Bagchi–Datta (2006) studies triangulations of sphere bundles over a circle, a relevant geometric context but not a calculation of these fourth-power cycle neighborhood complexes. An accessible earlier result on *third* powers identifies an \(S^2\)-bundle core for \(C_n^3\); it neither includes the fourth-power graph nor the explicit 58-orbit collapse. The present claim is limited to its new uniform four-dimensional collapse and nonzero cup-product obstruction, not to a previously known homology rank or to an identification of the core as a specific manifold.

## Limitations
No integral cohomology ring, full homotopy type, manifold classification, or assertion for \(n<17\) is established. The source comparison has residual publication-priority uncertainty for unindexed or inaccessible equivalent results. All verification is non-independent; human mathematical evaluation remains necessary.

## References
1. Dmitry N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, initial public version 2005-03-28, https://arxiv.org/abs/math/0503613.
2. Bhaskar Bagchi and Basudeb Datta, *Minimal triangulations of sphere bundles over the circle*, arXiv:math/0610829, initial public version 2006-10-27, https://arxiv.org/abs/math/0610829.
3. *Third-power cycle neighborhood complexes collapse to parity-twisted sphere bundles*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-third-power-cycle-neighborhood-complexes-collapse-to-parity-twis--5e7bfbfa5a7e (indexed summary checked; full file unavailable during this comparison).
