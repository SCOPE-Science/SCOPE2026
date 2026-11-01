# Integral automorphism modules of complete-bipartite higher-independence complexes

## Finding
Let \(A\) and \(B\) be disjoint labeled sets of sizes \(a,b\ge2\), put \(V=A\sqcup B\), and let \(X_r=\operatorname{Ind}_r(K_{a,b})\). For any nonempty finite set \(S\), put \(U_S=\ker(\varepsilon:\mathbb Z^S\to\mathbb Z)\), where each standard basis vector maps to \(1\). For every integer \(1\le r<a+b\), the only nonzero reduced integral homology module is
\[
\widetilde H_{r-1}(X_r;\mathbb Z)\cong
\frac{\bigwedge^r U_V}{\bigwedge^r U_A+\bigwedge^r U_B}.
\]
This is a **canonical integral \(S_a\times S_b\)-module isomorphism**, natural under relabeling. The two denominator terms are embedded by the inclusions of the two parts; they form a direct sum of primitive sublattices, so the quotient is free abelian of rank
\[
\binom{a+b-1}{r}-\binom{a-1}{r}-\binom{b-1}{r}.
\]
If \(a=b\), the same description is equivariant for the entire wreath-product automorphism group \((S_a\times S_a)\rtimes C_2\), with the nontrivial outer element exchanging the two part sublattices. For \(r\ge a+b\), \(X_r\) is contractible.

For a part-preserving permutation \(g=(\sigma,\tau)\), let \(P_\sigma(t)=\prod_{\ell\in\operatorname{cyc}(\sigma)}(1-(-t)^\ell)\), where the product runs over cycle lengths. The rational character of the displayed homology is
\[
\chi_r(\sigma,\tau)=[t^r]\frac{P_\sigma(t)P_\tau(t)-P_\sigma(t)-P_\tau(t)}{1+t}.
\]
In the balanced case, for an element exchanging the parts whose internal permutation product is \(\sigma\tau\), the character is
\[
\chi_r(g)=[t^r]\frac{\prod_{\ell\in\operatorname{cyc}(\sigma\tau)}(1-t^{2\ell})}{1+t}.
\]
At the first genuinely higher threshold \(r=2\), there is an additional integral consequence. Let \(G=S_a\times S_b\). Then
\[
\bigl(H_1(X_2;\mathbb Z)\bigr)_G\cong
(\mathbb Z/2\mathbb Z)^{\mathbf1_{a=2}+\mathbf1_{b=2}}.
\]
If \(a=b=m\), coinvariants under the full wreath product are \(\mathbb Z/2\mathbb Z\) when \(m=2\), and zero when \(m\ge3\). The torsion concerns **coinvariants of torsion-free homology**, not torsion in the homology of the complex.

## Assumptions and scope
A face \(F\subseteq V\) lies in \(X_r\) when every connected component of the induced graph \(K_{a,b}[F]\) has at most \(r\) vertices. Thus a mixed face meets both parts and must have \(|F|\le r\); faces contained entirely in one part have unrestricted size. All module isomorphisms are over \(\mathbb Z\); character calculations use their extension to \(\mathbb Q\). The convention is \(\binom{n}{k}=0\) if \(k<0\) or \(k>n\). The group action is induced by permutation of graph vertices, with the usual signed action on oriented simplices. No claim is made about Borel homology or equivariant homotopy splittings.

## Proof
**1. Simplicial decomposition.** Set \(T=\operatorname{Skel}_{r-1}\Delta_V\). The face criterion gives
\[
X_r=T\cup\Delta_A\cup\Delta_B,
\]
with intersections \(T\cap\Delta_S=\operatorname{Skel}_{r-1}\Delta_S\) for \(S=A,B\). After identifying integral oriented simplicial chains with exterior powers of \(\mathbb Z^V\), the reduced simplicial boundary is contraction by the augmentation \(\varepsilon\). Since \(\mathbb Z^V=U_V\oplus\mathbb Z e_v\) for any \(v\in V\), the cycle lattice of the \((r-1)\)-skeleton is naturally \(\bigwedge^r U_V\), and it has no other nonzero reduced homology (for \(1\le r<|V|\)). The corresponding assertion for each part gives \(\widetilde H_{r-1}(\operatorname{Skel}_{r-1}\Delta_S;\mathbb Z)=\bigwedge^r U_S\), also when that exterior power vanishes.

**2. Integral exact sequence.** Excision for the pair \((X_r,T)\) splits its relative chains into those of \((\Delta_A,T\cap\Delta_A)\) and \((\Delta_B,T\cap\Delta_B)\). The relative long exact sequence is concentrated in the displayed degrees and yields
\[
0\to\widetilde H_r(X_r)\to
\bigwedge^r U_A\oplus\bigwedge^r U_B
\xrightarrow{\ i\ }
\bigwedge^r U_V\to
\widetilde H_{r-1}(X_r)\to0.
\]
Here \(i\) is the sum of natural inclusions. The two images lie in disjoint exterior subspaces of \(\mathbb Z^V\), hence \(i\) is injective. The remaining reduced homology degrees vanish by the same pair sequence. This works in degree zero using reduced chains.

**3. Primitivity.** Choose \(a_0\in A\) and \(b_0\in B\). The union of the standard difference bases of \(U_A\) and \(U_B\), together with \(e_{a_0}-e_{b_0}\), forms an integral basis of \(U_V\). Thus, as lattices (not necessarily equivariantly), \(U_V=U_A\oplus U_B\oplus\mathbb Z(e_{a_0}-e_{b_0})\). In its exterior-power basis, \(\bigwedge^rU_A\) and \(\bigwedge^rU_B\) occupy disjoint subsets of basis vectors. Their direct sum is therefore primitive. Taking ranks proves the displayed Betti formula and torsion-freeness.

**4. Entire automorphism group and characters.** Every part-preserving permutation preserves the exact sequence, and when the two parts have equal size, their exchange interchanges its two source summands. Thus the quotient is equivariant under the full graph-automorphism group. For a permutation \(h\) of a finite set \(S\), the determinant identity
\[
\sum_{j\ge0}\operatorname{tr}\bigl(h\mid\bigwedge^jU_S\otimes\mathbb Q\bigr)t^j
=\frac{\prod_{\ell\in\operatorname{cyc}(h)}(1-(-t)^\ell)}{1+t}
\]
follows by removing the invariant augmentation line from its permutation representation. Subtracting the two part-summand characters gives the first formula. For an exchange element, both denominator summands are permuted into each other and their sum has trace zero. Each full-vertex cycle has even length \(2\ell\), with \(\ell\) a cycle length of the internal product, proving the second formula.

**5. The sharp integral coinvariant threshold.** For \(r=2\), relative chains for the pair \((X_2,\Delta_A\sqcup\Delta_B)\) have one generator for each cross edge, oriented from \(A\) to \(B\), and no higher generators. The long exact sequence identifies
\[
H_1(X_2;\mathbb Z)\cong\ker\bigl(\mathbb Z^{A\times B}\xrightarrow{\varepsilon}\mathbb Z\bigr).
\]
Under \(G=S_a\times S_b\), the cross-edge set \(A\times B\) is transitive with point stabilizer \(S_{a-1}\times S_{b-1}\). Applying group coinvariants to \(0\to\ker\varepsilon\to\mathbb Z[A\times B]\to\mathbb Z\to0\), and applying Shapiro's lemma to the permutation module, identifies the coinvariants of the kernel with the cokernel of
\[
(S_{a-1}\times S_{b-1})_{\mathrm{ab}}
\longrightarrow (S_a\times S_b)_{\mathrm{ab}}.
\]
For \(n\ge2\), \((S_n)_{\mathrm{ab}}=\mathbb Z/2\mathbb Z\), whereas \((S_1)_{\mathrm{ab}}=0\); inclusion \(S_{n-1}\hookrightarrow S_n\) surjects on abelianizations precisely when \(n\ge3\). This proves the integral threshold. For \(a=b=m\), the part-swap sends the cross-edge basis vector indexed \((i,j)\) to the **negative** of that indexed \((j,i)\), so it exchanges the two \(\mathbb Z/2\mathbb Z\) classes when \(m=2\). Taking the remaining swap coinvariants gives one \(\mathbb Z/2\mathbb Z\); for \(m\ge3\) the first-stage coinvariants are already zero.

## Verification
The accompanying standalone \(check.py\) enumerates the full face complexes and computes signed reduced Lefschetz traces directly from face permutations, independently of the exterior-power formula. Its recorded run passed 96 parameter/rank cases, 1,512 signed character comparisons (including part exchanges), and 30 independent integral Smith-normal-form tests of the claimed coinvariants. It covers \(2\le a,b\le5\) for characters and \(2\le a,b\le6\) for Smith forms. These finite computations do **not** replace the preceding all-parameter proof. Run with Python 3 and SymPy installed: `python check.py`.

## Relationship to prior work
Deshpande and Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types* (arXiv:2001.05448, first public 2020-01-15), Theorem 3.5, already prove the ordinary wedge-of-spheres homotopy classification for all complete multipartite graphs, including the displayed Betti ranks. The homotopy type and ranks **are not claimed as new**. Ghosh and Selvaraja, *Shellability of Higher Independence Complexes of Graphs* (arXiv:2505.06614, first public 2025-05-10), investigate the structural topology and shellability of higher-independence complexes, motivating finer invariants beyond their ordinary homotopy types. The new assertion here is the integral automorphism module, its full character including part exchanges, and the sharp integral coinvariant calculation. A general exterior-power representation of simplex-skeleton homology is standard background, but the natural quotient module and its coinvariant torsion are not supplied by the cited ordinary homotopy classification.

## Limitations
The theorem concerns complete bipartite graphs, their specific automorphism groups, and ordinary reduced integral homology with a group action, not a complete equivariant homotopy type. The coinvariant formula is stated only at threshold \(r=2\); no claim of a classification of integral coinvariants at every threshold is made. The ordinary sphere-wedge count was previously known. Equivalent unindexed derivations may exist; an independent mathematical audit has not been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, Theorem 3.5, https://arxiv.org/abs/2001.05448 (first public 2020-01-15).
2. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, https://arxiv.org/abs/2505.06614 (first public 2025-05-10).
3. Standard integral simplicial-chain description of simplex skeleta and the degree-one Shapiro lemma for transitive permutation modules; proofs of the required instances are included above.
