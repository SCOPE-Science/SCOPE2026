# Integral equivariant homology and symmetric-coinvariant torsion of clique-tree two-cut complexes

## Finding
Let \(T\) be **any finite tree** on \(t\ge2\) vertices and let \(m\ge2\). Put \(G=K_m\square T\), \(N=mt\), and let \(\Delta=\Delta_2^t(G)\) be the total two-cut complex. Give it the natural action of \(\Gamma=S_m\times\operatorname{Aut}(T)\) by permuting the \(m\) row colors and the vertices of \(T\). There is a **natural isomorphism of integral \(\Gamma\)-lattices**
\[
\widetilde H_{N-4}(\Delta;\mathbb Z)
\cong (B_m\otimes_{\mathbb Z} E_T)\otimes
(\operatorname{sgn}_m^{\,t}\boxtimes\operatorname{sgn}_T^{\,m}),
\qquad B_m=\mathbb Z^m/\mathbb Z(1,\ldots,1),
\]
where \(E_T\) is the oriented-edge lattice of \(T\), with an automorphism acting by signed permutation of oriented edges, and \(\operatorname{sgn}_T\) is the sign of the permutation of the vertices of \(T\). All other reduced integral homology groups vanish. In particular, the displayed lattice has rank \((m-1)(t-1)\).

The rational character of this action is explicit. For \(\pi\in S_m\) and \(\tau\in\operatorname{Aut}(T)\), let \(f(\pi)\) be the number of fixed row colors. Let \(u_+(\tau)\) count edges fixed with both endpoints individually fixed, and \(u_-(\tau)\) count edges whose two endpoints are interchanged by \(\tau\). Then
\[
\operatorname{tr}((\pi,\tau)_*\mid\widetilde H_{N-4}(\Delta;\mathbb Q))
=\operatorname{sgn}(\pi)^t\operatorname{sgn}_T(\tau)^m
\bigl(f(\pi)-1\bigr)\bigl(u_+(\tau)-u_-(\tau)\bigr).
\]
The **integral row-permutation coinvariants** (not the homology of a topological quotient) are
\[
\bigl(\widetilde H_{N-4}(\Delta;\mathbb Z)\bigr)_{S_m}
\cong
\begin{cases}
(\mathbb Z/m\mathbb Z)^{t-1},&t\text{ even};\\
\mathbb Z^{t-1},&t\text{ odd and }m=2;\\
(\mathbb Z/2\mathbb Z)^{t-1},&t\text{ odd and }m\ge4\text{ even};\\
0,&t\text{ odd and }m\ge3\text{ odd}.
\end{cases}
\]
Here the exponents on abelian groups indicate direct sums. In particular, torsion in the coinvariants is compatible with torsion-free homology of the complex itself.

## Assumptions and scope
The Cartesian product graph has vertex set \(\{1,\ldots,m\}\times V(T)\); two distinct vertices are adjacent when they have the same tree coordinate and distinct colors, or have equal colors and adjacent tree coordinates. The total two-cut complex is the down-closed family of subsets \(F\) for which \(V(G)\setminus F\) contains two **nonadjacent** vertices. Its maximal faces have \(N-2\) vertices. A clique complex \(\operatorname{Cl}(G)\) contains all vertex subsets spanning complete subgraphs, including the empty face. The combinatorial Alexander dual \(K^\vee\) consists of sets whose complementary sets are not faces of \(K\). These definitions make \(\Delta=\operatorname{Cl}(G)^\vee\).

The lattice \(E_T\) is the free abelian group on unoriented edges after choosing an orientation of each, subject to \([v,u]=-[u,v]\). An automorphism acts by transporting oriented edges; its signed trace is \(u_+-u_-\). All tensor products are over \(\mathbb Z\). The case \(m=t=2\) is included and uses reduced degree-zero homology. No claim about a new integral homotopy type, nor about quotient-space homology, is made.

## Proof
**1. Equivariant Alexander duality with the orientation twist.** Order the \(N\) vertices. The augmented simplicial chain groups of the full simplex modulo those of \(K^\vee\) have a complementary-face basis paired with the simplicial cochains of \(K\). The map takes a face and its complement with the sign of the shuffle that moves its ordered vertices followed by its ordered complement into the ambient order. On boundaries this gives the standard Alexander-dual chain identification, with one degree shift; on a vertex permutation the shuffle signs introduce exactly the determinant \(\det(\mathbb Z^{V(G)})\). Passing from relative simplex homology to reduced homology (since the full simplex is contractible) yields naturally
\[
\widetilde H_{N-4}(\operatorname{Cl}(G)^\vee;\mathbb Z)
\cong \widetilde H^1(\operatorname{Cl}(G);\mathbb Z)
\otimes \det(\mathbb Z^{V(G)}).
\]
More generally, degree \(j\) on the left corresponds to cohomology in degree \(N-j-3\); we will show that reduced cohomology of the clique complex is concentrated in degree one. Under \((\pi,\tau)\in\Gamma\), the determinant is \(\operatorname{sgn}(\pi)^t\operatorname{sgn}_T(\tau)^m\), since the row permutation is repeated once at each of the \(t\) tree vertices and the tree permutation once at each of the \(m\) colors.

**2. The clique complex is a graph of contractible fibers.** As \(T\) has no triangles, every clique in \(K_m\square T\) of size at least three lies within a single \(K_m\)-fiber over some \(v\in V(T)\). All other edges are the \(m\) color-preserving edges above each edge of \(T\). Each fiber simplex is contractible; collapsing these disjoint simplices to points is an equivariant map and a nonequivariant homotopy equivalence. The quotient is the connected multigraph \(Q\) having one vertex per vertex of \(T\) and exactly \(m\) separately labeled, parallel oriented edges above each tree edge. Thus the integral cohomology of \(\operatorname{Cl}(G)\) vanishes outside degrees zero and one and is torsion-free in degree one.

**3. Integral identification, not just a rational character.** Orient the edges of \(T\) arbitrarily. Write \(C_1(Q)=\mathbb Z^m\otimes E_T\) and \(C_0(Q)=\mathbb Z^{V(T)}\). The incidence boundary factors as the color-sum map \(\varepsilon:\mathbb Z^m\to\mathbb Z\), tensored with the tree incidence map \(\partial_T:E_T\to\mathbb Z^{V(T)}\). Since \(T\) is a tree, \(\partial_T\) is injective; hence
\[
H_1(Q;\mathbb Z)=\ker\varepsilon\otimes E_T.
\]
Both maps and the resulting identification are equivariant: the color permutation acts on the first factor, and a tree automorphism acts on the second factor with the required orientation signs. Because this first homology is free, the universal coefficient theorem gives
\[
H^1(Q;\mathbb Z)=\operatorname{Hom}_{\mathbb Z}(\ker\varepsilon,\mathbb Z)\otimes E_T^*.
\]
The standard dot product induces an equivariant perfect duality \(\operatorname{Hom}(\ker\varepsilon,\mathbb Z)\cong\mathbb Z^m/\mathbb Z(1,\ldots,1)=B_m\). The chosen orthonormal oriented-edge basis gives an equivariant isomorphism \(E_T^*\cong E_T\). Combining this with Step 1 proves the claimed integral group representation and the concentration of homology in degree \(N-4\).

**4. Character formula.** The trace of \(\pi\) on \(B_m\otimes\mathbb Q\) equals \(f(\pi)-1\), subtracting the invariant all-ones line from the color permutation module. The signed trace on \(E_T\) equals \(u_+-u_-\). Multiply these traces and the ambient determinant character from Step 1 to obtain the formula, for every \(\pi\) and every tree automorphism \(\tau\).

**5. Integral coinvariants.** The group \(S_m\) acts trivially on the tree edge factor. If \(t\) is even, the row action on \(B_m\) is untwisted. In the quotient by relations \(b-\pi b\), all color generators become one class \(z\), while the diagonal relation becomes \(mz=0\), so the coinvariant group is \(\mathbb Z/m\mathbb Z\). If \(t\) is odd, row permutations act on \(B_m\) with their sign. At \(m=2\), the transposition acts by \(-1\) on \(B_2\cong\mathbb Z\), so the additional sign twist makes this rank-one lattice trivial and its coinvariants are \(\mathbb Z\). For \(m\ge3\), a transposition fixing any given color forces twice its coinvariant class to vanish. The signed transpositions relate all colors up to sign, and, because their classes are now two-torsion, they become a common class \(z\). The diagonal relation becomes \(mz=0\). Thus the coinvariants are \(\mathbb Z/\gcd(m,2)\mathbb Z\), interpreted as zero when the gcd is one. Finally tensor with the free rank \(t-1\) edge group. This yields all four cases without invoking semisimplicity or incorrectly replacing the integral quotient lattice by a root lattice.

## Verification
Two standalone scripts accompany this result. Run `python check_km_tree_equiv.py` to enumerate every simplex of the total two-cut complexes of ten small clique-tree products and, for every natural graph symmetry in the enumerated groups, compare its complete oriented fixed-simplex Lefschetz trace against the theorem. The run passed **148 complete character instances**, including branching stars and a five-vertex non-path tree. Run `python check_clique_tree_coinvariants.py` (requires `sympy`) to form the full integer relation matrices for \(S_m\)-coinvariants and compute Smith normal forms for \(2\le m\le8\), in both untwisted and sign-twisted cases; **14 presentations** matched the derived groups. These are finite checks. The all-tree result follows from the chain-level argument and the injectivity of the tree incidence map, not from extrapolation.

## Relationship to prior work
Chauhan–Shukla–Vinayak (first posted 2025-12-04, arXiv:2512.04486v1, Theorem 3.12) establish the **ordinary homotopy type** of the path subfamily \(\Delta_2^t(K_m\square P_n)\), with \((m-1)(n-1)\) spheres of dimension \(mn-4\). That result neither determines an integral \(S_m\times\operatorname{Aut}(T)\)-action nor treats branching trees. Carnero Bravo (arXiv:2602.21427, Section 5.4) studies other Cartesian graph products and ordinary homotopy calculations, without the present tree-equivariant lattice or coinvariants. Bayer–Denker–Jelić Milutinović–Sundaram–Xue (arXiv:2407.08158, Section 6) study representations for different cut-complex graph families (notably disjoint unions of complete graphs and paths/cycles). The general Alexander-dual construction and graph cycle-space argument are standard tools; the contribution here is their exact integral, natural, all-tree equivariant combination and its coinvariant torsion classification.

## Limitations
The topological conclusion is a concentration and classification of **integral homology**, not an equivariant homotopy equivalence to a representation sphere or bouquet. All groups stated are natural action modules for the subgroup \(S_m\times\operatorname{Aut}(T)\); this result does not assert it is the entire graph automorphism group in degenerate cases. The reported torsion belongs to **algebraic coinvariants**, not to the homology of \(|\Delta|/S_m\) or to the integral homology of \(\Delta\). A natural integral coefficient normalization is essential: replacing \(B_m\) with the augmentation-kernel lattice preserves its rational character but can change integral coinvariants. Existing proofs or implicit corollaries not found by the reported literature comparisons remain possible, and an independent mathematical audit has not been performed.

## References
1. Pratiksha Chauhan, Samir Shukla, Kumar Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, first posted 2025-12-04, arXiv:2512.04486v1, especially Theorem 3.12 and Section 3.2. https://arxiv.org/html/2512.04486v1
2. Andrés Carnero Bravo, *Total cut complexes and their duals*, first posted 2026-02-24, arXiv:2602.21427, especially Section 5.4. https://arxiv.org/html/2602.21427v3
3. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Sheila Sundaram, Lei Xue, *Topology of Cut Complexes II*, first posted 2024-07-11, arXiv:2407.08158, especially Section 6. https://arxiv.org/html/2407.08158v1
