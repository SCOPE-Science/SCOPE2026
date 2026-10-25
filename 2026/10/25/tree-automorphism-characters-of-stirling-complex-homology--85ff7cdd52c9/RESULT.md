# Tree-automorphism characters of Stirling-complex homology

## Finding
Let \(T\) be any finite tree with \(m\ge2\) vertices, let \(n\ge m\), let \(G\le\operatorname{Aut}(T)\) be any finite subgroup, and let \(X=\mathcal{S}tr(T,n)\) be its Stirling complex. The action of \(G\) is **diagonal on the occupied tree locations**, not a permutation of the \(n\) resource-coordinate labels. Set \(d=n-m\) and
\[
f(m,n)=\sum_{a=1}^{m-1}(-1)^{m+a+1}\binom{m}{a+1}a^n,
\qquad \varepsilon=(-1)^{d+1},\qquad
q=\frac{f(m,n)-\varepsilon}{|G|}.
\]
Then \(q\) is an integer, \(q\ge0\), and the only nonzero reduced rational homology representation is, in the rational representation ring,
\[
[\widetilde H_d(X;\mathbb Q)]
=q[\mathbb Q[G]]+\varepsilon[\mathbf1].
\]
Equivalently, the ordinary (not virtual) representation is
\[
\widetilde H_d(X;\mathbb Q)\cong
\begin{cases}
\mathbb Q[G]^{\oplus q}\oplus\mathbf1,&d\text{ odd},\\
\mathbb Q[G]^{\oplus(q-1)}\oplus\ker(\mathbb Q[G]\xrightarrow{\mathrm{augmentation}}\mathbb Q),&d\text{ even}.
\end{cases}
\]
The second line necessarily has \(q\ge1\). All other reduced rational homology vanishes. In particular, every nonidentity element of \(G\) has the **same trace** \(\varepsilon\) on the nonzero homology, while the identity has trace \(f(m,n)\).

For the star with \(r\ge2\) leaves, \(G=S_r\), and \(m=r+1\), this supplies the irreducible decomposition explicitly requested in Open Question 1 of Kozlov's *Stirling complexes*. For each partition \(\lambda\vdash r\), the multiplicity of the rational Specht module \(S^\lambda\) is
\[
\boxed{\frac{f(r+1,n)-(-1)^{n-r}}{r!}\dim S^\lambda
+(-1)^{n-r}\,\mathbf1_{\lambda=(r)}.}
\]
The formula applies to every \(n\ge r+1\), including the disconnected degree-zero endpoint \(n=r+1\).

The rational reduced homology of the unlabelled-location quotient vanishes outside degree \(d\), with
\[
\dim_{\mathbb Q}\widetilde H_d(X/G;\mathbb Q)=q+\varepsilon.
\]
For \(d\ge2\), the quotient has \(\pi_1(X/G)\cong G\). For \(d=1\), the quotient is a connected graph with free fundamental group of rank \(q+1\).

## Assumptions and scope
A product cubical cell of \(|T|^n\) is a tuple whose entries are vertices of \(T\) or open one-cells corresponding to its edges. Its *support* is the set of vertices occurring as vertex (zero-cell) entries. The Stirling complex is the union of precisely those product cubes whose support is **all** \(V(T)\). This is a genuine cubical subcomplex: passing to a face can only increase vertex support. Its geometric realization consists of tuples in which every vertex occurs as at least one exactly stationary coordinate. The action of \(g\in G\) applies \(g\) to each coordinate without reordering the coordinates.

The group \(G\) is a subgroup of actual graph automorphisms of \(T\), hence acts faithfully on the vertex set. The representation statements are over characteristic zero. The wedge-of-spheres theorem used as an input is the established theorem for all trees; no equivariant wedge decomposition or integral representation-lattice classification is asserted. A single vertex is excluded, and \(n<m\) would give the empty configuration space.

When \(d=0\), \(X\) is the discrete set of \(m!\) surjective bijections and its reduced degree-zero homology has rank \(m!-1\). The virtual representation identity and its nonvirtual decomposition both remain valid. The quotient has \(m!/|G|\) components, as the degree-zero formula predicts.

## Proof
**1. Cellular freeness.** Every product cube \(c\subseteq X\) has, for each tree vertex \(v\), at least one coordinate that is exactly the vertex-cell \(\{v\}\). If \(g\) stabilizes \(c\) as a product cell, its action must carry this coordinate-cell to itself, forcing \(g(v)=v\). This applies to every vertex, and a graph automorphism fixing all vertices is the identity. Thus **every cell stabilizer is trivial**. Similarly, if \(g\) fixes a point of \(X\), it fixes each vertex that appears as one of its coordinates, hence every vertex; the action is free on points as well.

Choose an oriented representative in each cell orbit and propagate its orientation using \(G\). Cellular \(k\)-chains therefore form a free rational group-algebra module:
\[
C_k(X;\mathbb Q)\cong\mathbb Q[G]^{\oplus c_k/|G|},
\]
where \(c_k\) denotes the number of \(k\)-dimensional product cubes. In particular, every \(c_k\) is divisible by \(|G|\). The cell dimension is at most \(d=n-m\), since at least \(m\) coordinates must be vertex-cells to cover the \(m\) vertices.

**2. Homology input and Euler characteristic.** Kozlov's Theorem 2.1 (*Stirling complexes*, 2022) gives
\[
X\simeq\bigvee^{f(m,n)} S^d.
\]
For \(d=0\), this is interpreted as \(f(m,m)+1=m!\) isolated points. Consequently the sole reduced homology is \(\widetilde H_d(X;\mathbb Q)\cong\mathbb Q^{f(m,n)}\), and the Euler characteristic is
\[
\chi(X)=1+(-1)^d f(m,n).
\]
For a direct finite description of the chain ranks, a \(k\)-cell has \(k\) designated moving coordinates, each one of the \(m-1\) tree edges, while its other \(n-k\) coordinates surject onto all \(m\) vertices. Thus
\[
c_k=\binom nk(m-1)^k\,m!\left\{\!\begin{matrix}n-k\\m\end{matrix}\!\right\}
\qquad (0\le k\le d),
\]
with braces denoting a Stirling number of the second kind. This also exhibits the finite cubical chain complex used in verification.

**3. Exact equivariant Euler identity.** In the rational representation ring \(R_{\mathbb Q}(G)\), Euler–Poincaré for the finite cellular chain complex, with the augmentation to the trivial module, yields
\[
\sum_{k=0}^d(-1)^k[C_k(X;\mathbb Q)]-[\mathbf1]
=(-1)^d[\widetilde H_d(X;\mathbb Q)].
\]
Substituting the free chain-module decomposition and the Euler characteristic gives
\[
[\widetilde H_d(X;\mathbb Q)]
=(-1)^d\left(\frac{\chi(X)}{|G|}[\mathbb Q[G]]-[\mathbf1]\right)
=q[\mathbb Q[G]]+(-1)^{d+1}[\mathbf1].
\]
The freeness makes \(\chi(X)/|G|\) integral, so \(q=(-1)^d\chi(X)/|G|\) is integral. Its nonnegativity follows from the displayed actual character in degree \(d\): for each rational irreducible \(\rho\), let \(a_\rho>0\) denote its multiplicity in the regular rational representation. In odd degree the trivial multiplicity is \(q+1\), and each nontrivial irreducible has multiplicity \(q a_\rho\); in even degree the trivial multiplicity is \(q-1\), and each nontrivial irreducible has multiplicity \(q a_\rho\). As \(G\) is finite and rational representations are semisimple, all multiplicities are nonnegative. For trivial \(G\) the same bound follows from \(f(m,n)\ge0\); in the even case \(q=f+1\ge1\). For nontrivial \(G\), at least one nontrivial rational irreducible occurs in the regular representation; its multiplicity is \(q a_\rho\), which forces \(q\ge0\). In even degree the trivial multiplicity then forces \(q\ge1\). Maschke's theorem then converts the representation-ring identity into the asserted direct-sum decompositions.

The regular representation has trace zero at every nonidentity group element, so the nonidentity trace is \(\varepsilon=(-1)^{d+1}\). At the identity the trace is \(q|G|+\varepsilon=f(m,n)\). For \(G=S_r\), the regular character contains \(\dim S^\lambda\) copies of each Specht module, producing the stated multiplicity formula for all partitions.

**4. Quotients.** Since the cellular action is free, the quotient is a finite CW complex and \(C_*(X/G;\mathbb Q)\) is obtained as group coinvariants of \(C_*(X;\mathbb Q)\). Exactness of the coinvariants functor over \(\mathbb Q\) identifies \(H_*(X/G;\mathbb Q)\) with \(G\)-invariant homology. The invariant multiplicity in the sole reduced degree is \(q+\varepsilon\), and it is zero in all other reduced degrees. For \(d\ge2\), the sphere-wedge theorem makes \(X\) connected and simply connected. The free action gives a connected regular covering \(X\to X/G\) with deck group \(G\); hence \(\pi_1(X/G)\cong G\). For \(d=1\), \(X\) and its quotient are connected graphs, whose fundamental groups are free with ranks equal to their first Betti numbers. This proves all assertions. \(\square\)

## Verification
The standalone standard-library script `verify_stirling_leaf_action.py` reconstructs product cells for six path/star instances, checks their graph-automorphism fixed-cell traces for every small symmetry tested, constructs exact mod-two boundary matrices, and verifies that their complete Betti vectors agree with the wedge theorem and that their Euler characteristics agree with the character formula. In the star cases every element of \(S_3\) is checked. It also verifies integrality of the proposed regular-character multiplicity for stars with \(2\le r\le6\) and the first six values \(n\ge r+1\).

A successful run prints `STIRLING_TREE_AUTOMORPHISM_CERTIFICATE_OK`. These finite calculations do **not** establish the all-trees theorem; the mathematical proof is the cellular freeness, equivariant Euler identity, and published nonequivariant homotopy theorem above. The script uses only the Python standard library and contains no external data dependencies.

## Relationship to prior work
Kozlov's *Stirling complexes* (first public 2022-09-24, Theorem 2.1 and Open Question 1) establishes the sphere-wedge homotopy type and explicitly asks for the irreducible \(S_r\)-representation arising from permutations of the leaves of a star. Its Betti numbers do not imply this representation: many inequivalent \(S_r\)-modules share the same dimension. The new calculation determines those multiplicities, for all parameters in the question and for all tree automorphism subgroups, by making essential use of cellular freeness and equivariant Euler–Poincaré. The non-equivariant theorem itself is not claimed as new.

Kozlov's later *Homology and Euler characteristic of generalized anchored configuration spaces of graphs* extends the anchored-space study to other graphs, but the inspected results concern Euler characteristics and homology groups, not the action on homology induced by automorphisms of the occupied tree vertices. The published *Integral homology of anchored configurations on every connected graph* similarly provides integral Betti ranks for a broader graph domain, but explicitly does not compute equivariant homology representations. The published *Integral branch-permutation homology of extended-star Morse complexes* concerns a different object (acyclic discrete matchings of a tree), so its branch-permutation character does not cover Stirling complexes.

A separate classification of resource-coordinate permutations of Stirling complexes also concerns a different action: coordinate relabelings exchange resources, whereas the present theorem permutes the tree's occupied vertices without changing the ordering of coordinates. These two representations should not be identified.

## Limitations
The formula is for **rational** representations of finite subgroups of tree automorphisms, not a classification of integral \(\mathbb Z[G]\)-lattices, equivariant homotopy types, or nonlinear group actions. No finite computations are used as a substitute for the all-parameter proof. The independent external audit of this mathematical claim has not been performed. The literature comparisons include the original open question, subsequent related literature and published mathematical records; they cannot exclude every unindexed equivalent result. Quotient rational homology does not determine quotient integral torsion.

## References
1. D. N. Kozlov, *Stirling complexes*, *Journal of Applied and Computational Topology* **7** (2023), 57–74; first online publication 2022-09-24, Theorem 2.1, Definition 2.4, Proposition 4.3, and Open Question 1. https://doi.org/10.1007/s41468-022-00096-4 . Preprint: https://arxiv.org/abs/2309.17142 .
2. D. N. Kozlov, *Homology and Euler characteristic of generalized anchored configuration spaces of graphs*, *Journal of Applied and Computational Topology* **8** (2024), 1053–1067. https://doi.org/10.1007/s41468-024-00167-8 .
3. *Integral homology of anchored configurations on every connected graph*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homology-of-anchored-configurations-on-every-connected--58ff949a206c .
4. *Integral branch-permutation homology of extended-star Morse complexes*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-branch-permutation-homology-of-extended-star-morse-comp--348812728b63 .
