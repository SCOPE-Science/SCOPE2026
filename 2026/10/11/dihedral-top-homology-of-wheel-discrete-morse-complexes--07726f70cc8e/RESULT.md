# Dihedral top homology of wheel discrete-Morse complexes

## Finding
For every integer \(k\ge5\), let \(W_{k+1}=C_k*K_1\) be the wheel with a rim of \(k\) vertices and one universal hub. The natural dihedral group \(D_k\) acts on the ordinary discrete-Morse complex \(\mathcal M(W_{k+1})\). Its reduced rational homology is concentrated in degree \(k-1\), and its degree-\(k-1\) character satisfies
\[
\chi_k(g)=\begin{cases}
k^3,&g=1,\\
0,&g\text{ is a nonidentity rotation},\\
0,&g\text{ is a reflection and }k\text{ is even},\\
(-1)^{(k-1)/2},&g\text{ is a reflection and }k\text{ is odd}.
\end{cases}
\]
In particular \(\mathcal M(W_{k+1})\simeq\bigvee^{k^3}S^{k-1}\). More precisely, as rational \(D_k\)-representations,
\[
\widetilde H_{k-1}(\mathcal M(W_{k+1});\mathbb Q)\cong
\begin{cases}
\mathbb Q[D_k]^{\oplus k^2/2},&k\text{ even},\\
\mathbb Q[D_k]^{\oplus (k^2-1)/2}\oplus
 (\mathbb Q^{\{0,\ldots,k-1\}}\otimes\varepsilon^{(k-1)/2}),&k\text{ odd}.
\end{cases}
\]
Here \(\varepsilon\) is the one-dimensional character that is \(+1\) on rotations and \(-1\) on reflections; the \(k\)-dimensional factor is the permutation module on rim vertices. The **new classification is the symmetry character and the resulting representation decompositions**, not the general complete-source shellability principle.

## Assumptions and scope
The graph is finite, simple, undirected, with edges of unit combinatorial length, but the metric plays no role. A vertex of the Morse complex is an incidence \((v,e)\) with \(v\in e\). Its simplices are discrete acyclic matchings of vertices to incident edges. Equivalently, replace \((v,\{v,w\})\) by the arrow \(v\to w\); then a simplex is a directed forest with each vertex having at most one outgoing arrow. Dihedral automorphisms act by permuting the rim and fixing the hub. All homology in this statement is reduced, with rational coefficients for the representation calculation. The homotopy type is integral and does not imply a claim about an integral group-module splitting. The group is of order \(2k\), including both sorts of reflections when \(k\) is even.

## Proof
**Homological concentration.** Reverse every arrow in the incidence model. This is an equivariant identification with the complex of directed forests used in the complete-source shellability theorem. Because the hub is adjacent to every rim vertex in both orientations, it is a complete source. The theorem of Kozlov, stated and proved in the version of Jojić [1], makes the complex pure shellable. A facet is a directed spanning tree on \(k+1\) vertices, hence has \(k\) arrows and dimension \(k-1\). Therefore the only possible reduced homology degree is \(k-1\), in which homology is free abelian, and the space is a wedge of \((k-1)\)-spheres. We calculate its rank together with every character value below.

**Equivariant forest determinant.** Fix \(g\in D_k\). Make a directed multigraph \(Q_g\) whose vertices are the \(g\)-orbits of graph vertices. For each orbit \(O\), choose a representative \(v\) of length \(\ell\). An edge \(v\to w\) supplies one directed edge in \(Q_g\) from \(O\) to the orbit of \(w\) exactly when \(g^\ell w=w\) and the two orbits differ. Distinct choices are retained as parallel edges. An equivariant directed forest in the wheel is exactly a rooted directed forest in \(Q_g\): equivariance enforces orbitwise choices; same-orbit arrows force directed cycles; a quotient directed cycle lifts to a directed cycle after finitely many traversals, because orbit lengths cannot increase along allowed edges and are equal around a cycle. Conversely, a quotient forest lifts without directed cycles.

Let \(L_g\) denote the outdegree Laplacian of \(Q_g\) (diagonal = number of outgoing arrows, off-diagonal = negative number of directed arrows). The directed matrix-forest identity gives
\[
\det(I+tL_g)=\sum_{F\text{ rooted forests of }Q_g}t^{|F|}.
\]
If a \(g\)-fixed simplex has \(a\) arrows grouped into \(c\) orbits, \(g\) acts on its orientation with sign \((-1)^{a-c}\). Its contribution to the reduced alternating simplicial trace is \((-1)^{a-1}(-1)^{a-c}=(-1)^{c-1}\); the empty face has reduced alternating contribution \(-1\). Thus the reduced Lefschetz number equals \(-\det(I-L_g)\). Since all reduced homology is in degree \(k-1\),
\[
\boxed{\chi_k(g)=(-1)^k\det(I-L_g).}
\]
The determinant identity can also be established by the all-minors directed matrix-tree theorem; the general graph-gradient determinant enumeration is discussed in [2].

**Identity.** The wheel Laplacian has eigenvalues \(0\), \(k+1\), and \(3-2\cos(2\pi j/k)\) for \(1\le j<k\). The classical cycle product \(\prod_{j=1}^{k-1}(2-2\cos(2\pi j/k))=k^2\) yields \(\det(I-L_1)=(-1)^k k^3\). Therefore \(\chi_k(1)=k^3\), proving the claimed rank and sphere multiplicity.

**Nonidentity rotations.** Write \(d=\gcd(k,r)\) for rotation by \(r\) rim positions. Its \(d\) rim orbits all have length \(k/d>1\), while the hub is fixed. The hub has no admissible outgoing orbit-arrow. For \(d=1\), the unique rim orbit has only the spoke-to-hub option and its diagonal in \(I-L_g\) vanishes. For \(d\ge2\), rim orbits form a cycle quotient, permitting an outgoing spoke and two neighbor arrows per orbit (the two neighbor arrows can be parallel when \(d=2\)). Eliminating the hub's unit row leaves the negative cycle Laplacian on rim orbits, which has a zero row sum. In both cases \(\det(I-L_g)=0\).

**Even rim, reflections.** The reflection through opposite rim vertices fixes those two rim vertices and the hub. Each of the two fixed rim vertices can choose only its spoke as an invariant outgoing arrow: its incident rim neighbors are swapped, so two rows of \(I-L_g\) are identical. The other reflection conjugacy class fixes the hub and no rim vertex; its rim orbits form a path with a spoke to the hub from each orbit. The rim block of \(I-L_g\) is minus the path Laplacian (a singleton path has zero Laplacian), and so is singular. Every even-rim reflection therefore has trace zero.

**Odd rim, reflections.** Put \(k=2q+1\). Every reflection fixes the hub and one rim vertex; the remaining \(q\) rim orbits occur as paired vertices in a path. Order the quotient orbits as hub, fixed rim vertex, then successive paired orbits. The first two rows of \(I-L_g\) give the upper-left block
\[\begin{pmatrix}0&1\\1&0\end{pmatrix}.\]
The lower-right \(q\)-by-\(q\) block is tridiagonal, with off-diagonal entries \(1\), diagonal \(-2\) except the last diagonal \(-1\). Its determinant is \((-1)^q\), by the terminal recurrence (or the determinant-one Dirichlet path Laplacian). Therefore \(\det(I-L_g)=(-1)^{q+1}\), and because \(k\) is odd, \(\chi_k(g)=(-1)^q\).

**Decomposition.** The regular character vanishes away from the identity and has value \(2k\) at identity. When \(k\) is odd, the rim permutation character has value \(k\) at identity, zero on nontrivial rotations and one on reflections; twisting by \(\varepsilon^q\) changes the reflection value to \((-1)^q\). The displayed modules therefore have exactly the computed character. Maschke semisimplicity and rational character injectivity prove the rational module isomorphisms.

## Verification
The standalone standard-library Python program `verify_wheel_character.py` constructs the wheel action and the admissible orbit digraph from definitions, computes all quotient determinants with exact integer arithmetic, and separately enumerates equivariant directed forests in the tractable cases. Across \(5\le k\le12\), it checks all \(136\) dihedral elements. For \(k=5,6,7\), it additionally enumerates every simplex (including the empty one) and computes each automorphism's signed augmented chain trace independently. Those complete face counts are respectively \(2527\), \(10800\), and \(45369\). Successful execution prints `VERIFY_OK`. Finite checks do not replace the general proof above.

## Relationship to prior work
The complete-source shellability theorem of Kozlov, as presented in [1], establishes concentrated homology for graph Morse complexes with a universal vertex but gives no dihedral representation formula. The Laplacian/forest-counting framework of [2] can determine ordinary ranks, not the nontrivial symmetry traces without orbit compatibility and oriented-sign analysis. The study [3] develops star-cluster reductions and homotopy types for particular graph Morse and matching complexes, not this wheel symmetry representation. A published exact calculation [4] covers only the five-vertex wheel (four rim vertices) at the level of homotopy type; the present theorem explicitly concerns \(k\ge5\) and determines characters, including the odd-rim nonzero reflection traces. No covering character formula was identified in the inspected works.

## Limitations
The representation splitting is asserted only over \(\mathbb Q\), not integrally. The homotopy assertion follows from a previously known shellability theorem; the dihedral character and decomposition are the claimed contribution. Searches and inspected primary texts cannot exclude every unindexed equivalent representation calculation; independent evaluation of novelty and proof remains appropriate. No extension to wheel graphs with a different rim or to non-dihedral actions is claimed.

## References
1. Duško Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475v2, 2012, §§1–2; recalls Kozlov's complete-source shellability theorem.
2. I. Contreras and A. R. Tawfeek, *On discrete gradient vector fields and Laplacians of simplicial complexes*, arXiv:2105.05388, §3, especially Theorem 3.5 and Figure 6.
3. Connor Donovan and Nicholas A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, first public 2022-07-27, primary MSC 57Q70.
4. *The five-vertex wheel Morse complex is a wedge of 64 three-spheres*, public mathematical record at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-five-vertex-wheel-morse-complex-is-a-wedge-of-64-three-spher--c2f501a8bea1.
