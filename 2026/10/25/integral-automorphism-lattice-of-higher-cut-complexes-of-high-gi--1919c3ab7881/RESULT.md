# Integral automorphism lattice of higher cut complexes of high-girth graphs

## Finding

Let \(k\geq4\), and let \(G=(V,E)\) be any finite simple graph with \(N=|V|\geq k+4\) and girth at least \(k+2\), allowing forests to have infinite girth. Put \(\Gamma=\operatorname{Aut}(G)\). Let \(\mathcal C_k(G)\) be the collection of connected induced vertex sets of cardinality \(k\). The group \(\Gamma\) acts naturally on all of these objects.

Write \(P=\mathbb Z^V\) for the vertex-permutation lattice, \(U=\ker(\epsilon:P\longrightarrow\mathbb Z)\) for its augmentation lattice, and
\[
 W_k(G)=\bigoplus_{T\in\mathcal C_k(G)}\bigwedge^k\mathbb Z^T.
\]
Each summand is an orientation line; automorphisms may permute lines and reverse their signs. Contraction by \(\epsilon\) defines an integral \(\Gamma\)-equivariant map
\[
 \Phi:W_k(G)\longrightarrow\bigwedge^{k-1}U,
 \qquad e_{t_1}\wedge\cdots\wedge e_{t_k}\longmapsto
 \sum_{j=1}^{k}(-1)^{j-1}e_{t_1}\wedge\cdots\wedge\widehat{e_{t_j}}\wedge\cdots\wedge e_{t_k}.
\]
This lands in \(\bigwedge^{k-1}U\subseteq\bigwedge^{k-1}P\) canonically; the expression does not depend on the chosen ordering of an oriented generator.

**Integral automorphism-lattice theorem.** The map \(\Phi\) is injective with **torsion-free cokernel** \(Q_k(G)\), and the ordinary cut complex \(\Delta_k(G)\) has exactly one potentially nonzero reduced integral homology group, given as a \(\mathbb Z\Gamma\)-lattice by
\[
 \boxed{\quad
 \widetilde H_{N-k-1}(\Delta_k(G);\mathbb Z)
 \cong \operatorname{sgn}_V\otimes_{\mathbb Z} Q_k(G)^\vee,
 \quad Q_k(G)=\operatorname{coker}(\Phi).\quad}
\]
Here \(\operatorname{sgn}_V(g)\) is the sign of \(g\) on the vertex set, and \(Q^\vee=\operatorname{Hom}_{\mathbb Z}(Q,\mathbb Z)\). All other reduced integral homology groups vanish. Its rank is \(\binom{N-1}{k-1}-|\mathcal C_k(G)|\). If that rank is zero, the displayed group is zero.

The presentation is valid integrally and hence retains the action after reduction modulo **every** characteristic, including primes dividing \(|\Gamma|\). It does not merely determine the rational character, and it does not assert an equivariant splitting of the short exact sequence defining \(Q_k(G)\).

For completeness, if \(g\in\Gamma\) has vertex-permutation cycle lengths \(\ell_1,\ldots,\ell_s\), its rational character is
\[
 \chi(g)=\operatorname{sgn}_V(g)\left(
 [t^{k-1}]\frac{\prod_{i=1}^s(1-(-t)^{\ell_i})}{1+t}
 -\sum_{\substack{T\in\mathcal C_k(G)\\gT=T}}\operatorname{sgn}(g|_T)
 \right).
\]
This rational trace is included as a check, **not** claimed as a separate novel result: an existing general virtual-character formula already implies it.

## Assumptions and scope

A \(k\)-set of vertices is called connected when its induced graph is connected. The ordinary \(k\)-cut complex \(\Delta_k(G)\) has facets \(V\setminus S\) for all disconnected induced \(k\)-sets \(S\). The girth of a forest is infinite by convention. There is no connectedness or regularity assumption on \(G\). The stated range is \(k\ge4\), \(N\ge k+4\) and girth \(\ge k+2\). Degrees, duals and signs refer to honest integral modules; no rational semisimplicity is used for the classification.

## Proof

**1. Exact Alexander dual.** Denote the simplicial Alexander dual of \(\Delta_k(G)\) on \(V\) by \(Y\). A set \(A\subseteq V\) lies in \(Y\) precisely when every \(k\)-subset of \(A\) induces a connected graph. Hence every set of size at most \(k-1\) lies in \(Y\), and its \(k\)-faces are exactly \(\mathcal C_k(G)\). There are no \((k+1)\)-faces: such a vertex set would remain connected after deletion of every vertex, forcing an induced connected graph with no cut vertex, therefore containing a cycle of length at most \(k+1\). This contradicts the girth hypothesis. Since \(Y\) is simplicial, no larger faces exist either. Thus \(Y\) is the complete \((k-2)\)-skeleton of a simplex together with the \((k-1)\)-simplices indexed by \(\mathcal C_k(G)\).

**2. The skeleton lattice.** Under oriented simplicial boundary, the top reduced integral homology of the complete \((k-2)\)-skeleton is canonically the image of the contraction \(\iota_\epsilon:\bigwedge^{k}P\to\bigwedge^{k-1}P\). Splitting \(P=U\oplus\mathbb Ze_v\) as abelian groups (for any chosen vertex \(v\)) identifies this image with \(\bigwedge^{k-1}U\); the image is canonical and \(\Gamma\)-invariant regardless of the splitting. Attaching the connected \(k\)-simplices gives the cellular boundary map \(\Phi\) above. Consequently \(\widetilde H_{k-2}(Y;\mathbb Z)=\operatorname{coker}\Phi\), while \(\widetilde H_{k-1}(Y;\mathbb Z)=\ker\Phi\).

**3. Private faces imply integral saturation.** Fix \(T\in\mathcal C_k(G)\). Since the induced graph on \(T\) is a tree with \(k\ge4\), choose a nonleaf vertex \(v\in T\) and set \(A=T\setminus\{v\}\). The induced graph on \(A\) has at least two components. Suppose a different vertex \(w\notin T\) made \(A\cup\{w\}\) connected. Both \(v\) and \(w\) would have neighbors in each component of \(G[A]\). Taking two components and their connecting paths inside those components produces a cycle through \(v,w\) of length at most \(|A|+2=k+1\). This is impossible. Therefore the \((k-2)\)-face \(A\) belongs to exactly one attached \((k-1)\)-simplex, namely \(T\).

Choosing one such **private face** for each \(T\), the matrix of \(\Phi\), viewed in the ambient integral \((k-2)\)-chain group, has an identity submatrix up to independent signs. Hence \(\Phi\) is injective, and its image is primitive in that ambient chain group. The skeleton top-cycle lattice \(\bigwedge^{k-1}U\) is itself a primitive sublattice of the chain group; therefore the quotient \(Q_k(G)\) embeds in a free abelian quotient of the ambient chains and is torsion-free. Its rank is the difference of the ranks of \(\bigwedge^{k-1}U\) and \(W_k(G)\). The complete skeleton has no other reduced homology below degree \(k-2\), so \(Y\) has reduced homology only in degree \(k-2\).

**4. Integral equivariant Alexander duality.** For a simplicial complex on \(N\) labeled vertices, combinatorial Alexander duality identifies \(\widetilde H_j(\Delta;\mathbb Z)\) with \(\operatorname{sgn}_V\otimes\widetilde H^{N-j-3}(\Delta^*;\mathbb Z)\), equivariantly under vertex permutations. Since \(Y\) has a single free reduced homology group \(Q_k(G)\), the integral universal-coefficient theorem identifies its only nonzero reduced cohomology with \(Q_k(G)^\vee\). Substituting \(j=N-k-1\) yields the asserted canonical integral representation, its sole nonzero degree and the vanishing of torsion. The integral result also gives the same module presentation in any field by tensoring and universal coefficients.

**5. Character identity.** Over \(\mathbb Q\), taking characters of the defining short exact sequence gives \(\chi_Q(g)=\operatorname{tr}(g|\bigwedge^{k-1}U)-\operatorname{tr}(g|W_k)\). The former trace is the indicated coefficient of \(\det(1+t g|U)\). The latter is the signed sum over setwise-fixed connected \(k\)-subsets. Dualization preserves traces for finite-order rational matrices, and Alexander duality gives the vertex sign. This proves the displayed character formula without using a nonintegral splitting to prove the integral module statement.

## Verification

The accompanying `verify_cut.py` tests the graph definitions directly. It compares direct signed simplicial Lefschetz traces against the displayed character for 81 automorphism/parameter tests, computes independent mod-two Betti vectors for seven cut complexes, and checks 446 connected \(k\)-faces in 15 parameter families have private codimension-one faces. These are finite tests of orientations, boundary dimensions and primitivity; the universal conclusion is established by the proof above, not by finite enumeration. Execute `python verify_cut.py` using Python 3; no third-party packages are needed.

## Relationship to prior work

Bayer et al. (2023), *Topology of Cut Complexes of Graphs*, introduced these ordinary cut complexes, their face-lattice skeleton condition and related homology results for forests, cycles, and other graphs. Bayer et al. (2024), *Topology of Cut Complexes II*, Section 6.2, equation (15), give a general **virtual rational homology-module** formula under the skeleton condition; this covers the rational character consequence here. A separate published high-girth result proves the nonequivariant wedge-of-spheres homotopy type and private-face mechanism under essentially the same girth bound. Those results are prior work, **not claimed here as discoveries**. The distinct result here is the complete, functorial **integral automorphism lattice** as an explicit quotient of the augmentation exterior power by signed connected-set boundaries, including saturation and all-characteristic action. Unlike rational virtual characters or the abstract homotopy type, this describes the lattice and its modular reductions. A differently formulated integral-equivariant antecedent could exist; see the separate review.

## Limitations

The theorem requires the stated girth and parameter bounds. It provides a presentation of the integral module, not an irreducible integral direct-sum decomposition or an equivariant splitting. It does not extend by assertion to arbitrary lower-girth graphs. In positive characteristic the representation may fail to be semisimple; the integral presentation remains valid without such a claim. The literature comparison does not prove priority over every unpublished or unindexed treatment.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first submitted April 26, 2023; Sections 6–7. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first submitted July 11, 2024; Section 6.2, especially equation (15). https://arxiv.org/abs/2407.08158
3. *High-girth cut complexes are wedges of top-dimensional spheres*, published mathematical-result record `ec8bbe3d352b` (2026). Cited for the nonequivariant high-girth classification and private-face antecedent, not for the integral automorphism presentation.
