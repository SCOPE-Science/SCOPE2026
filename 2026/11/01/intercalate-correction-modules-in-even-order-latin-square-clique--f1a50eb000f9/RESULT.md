# Intercalate correction modules in even-order Latin-square clique homology

## Finding

Let \(A\) be a finite abelian group of **even** order \(n\ge6\), let \(T=A\times A\), and let \(G_A\) have vertex set \(A\times A\), with two distinct vertices \((r,c)\) and \((r',c')\) adjacent exactly when \(r=r'\), \(c=c'\), or \(r+c=r'+c'\). Write \(X=\operatorname{Cl}(G_A)\). The group \(T\) acts on \(X\) by simultaneous translations. Let \(E=A[2]=\{h\in A:2h=0\}\), and for every nonzero \(h\in E\) put

\[
H_h=\{(0,0),(h,0),(0,h),(h,h)\}\le T.
\]

Let \(Z\subseteq X\) be the subcomplex obtained by deleting exactly the three-simplices corresponding to the \(2\)-by-\(2\) Latin intercalates, while retaining their proper faces and all other simplices. Then there is a natural short exact sequence of **integral** \(T\)-modules

\[
0\longrightarrow\bigoplus_{h\in E\setminus\{0\}}\mathbb Z[T/H_h]
\longrightarrow H_2(Z;\mathbb Z)
\longrightarrow H_2(X;\mathbb Z)\longrightarrow0.
\]

Let \(V=\ker(\mathbb Q[A]\xrightarrow{\mathrm{sum}}\mathbb Q)\), and let \(V_r,V_c,V_s\) be the representations of \(T\) obtained by pulling back \(V\) through \((u,v)\mapsto u\), \((u,v)\mapsto v\), and \((u,v)\mapsto u+v\). The rational homology is consequently the following noncanonical direct-summand complement:

\[
H_2(X;\mathbb Q)\oplus\bigoplus_{h\in E\setminus\{0\}}\mathbb Q[T/H_h]
\cong_{\mathbb Q[T]}V_r\otimes V_c\otimes V_s.
\]

In particular, writing \(\delta(a)=1\) when \(a=0\) and \(0\) otherwise, its complete translation character is

\[
\chi_X(u,v)=
(n\delta(u)-1)(n\delta(v)-1)(n\delta(u+v)-1)
-\frac{n^2}{4}\sum_{h\in E\setminus\{0\}}\mathbf1_{(u,v)\in H_h}.
\]

For complex one-dimensional characters \(\alpha,\beta\in\widehat A\), the multiplicity of \((u,v)\mapsto\alpha(u)\beta(v)\) in \(H_2(X;\mathbb C)\) equals

\[
m_{\alpha,\beta}
=n-|\{\mathbf1,\alpha,\beta\}|
-|\{h\in E\setminus\{0\}:\alpha(h)=\beta(h)=1\}|.
\]

The translation-invariant subspace has the particularly simple dimension

\[
\dim_{\mathbb Q}H_2(X;\mathbb Q)^T=n-|A[2]|.
\]

Thus for any elementary abelian \(2\)-group of order at least \(8\), the second homology is nonzero but contains **no** translation-invariant rational class.

## Assumptions and scope

The order \(n\) is even and at least \(6\). The clique complex includes all cliques, not just the triangle skeleton. The labels \(r,c\) are group elements and the third adjacency type is equality of sums. The notation \(\mathbb Z[T/H_h]\) denotes the integral permutation lattice on left cosets. The integral exact sequence is not claimed to split over \(\mathbb Z[T]\); the rational direct-sum decomposition is noncanonical. Nothing is asserted about the full automorphism group, equivariant homotopy types, or nonabelian Latin tables.

## Proof

**1. Simplices and intercalate orbits.** For \(n\ge5\), every clique with at least five vertices lies on one row, column, or sum line. Every four-vertex clique is either contained in such a line or is a \(2\)-by-\(2\) intercalate. A triangle is either contained in one line or is a rainbow triangle, with exactly one edge of each of the three adjacency types. The latter triangles are uniquely of the form

\[
\{(r,c),(r,c+h),(r+h,c)\},\quad (r,c)\in A^2,\quad h\in A\setminus\{0\}.
\]

These assertions follow by distinguishing which equality holds for each pair; the full classification of large cliques and disjointness of the intercalate-boundary triangles is also established in the primary source [1, Section 3.3]. In the group table, an intercalate is uniquely determined by its nonzero involution \(h\) and an unordered pair of rows \(\{r,r+h\}\) and columns \(\{c,c+h\}\). Hence exactly \(n^2/4\) intercalates occur for each \(h\in E\setminus\{0\}\). Translations act transitively on these \(n^2/4\) intercalates; the stabilizer is exactly \(H_h\). Each of its three nonidentity elements induces two disjoint swaps of the tetrahedron's four vertices, so preserves the simplex orientation. Therefore the relative integral third chain group is, as a \(T\)-module,

\[
C_3(X,Z;\mathbb Z)\cong\bigoplus_{h\in E\setminus\{0\}}\mathbb Z[T/H_h],
\]

and all other relative chain groups vanish.

**2. Integral exact sequence.** Theorem 3.12 of [1] proves that \(H_i(X;F)=0\) for every field \(F\) and every \(i\ge3\); it also computes \(\dim_F H_2(X;F)\) independently of the field. Finite generation and the universal coefficient theorem therefore give \(H_3(X;\mathbb Z)=0\) and torsion-free \(H_2(X;\mathbb Z)\). The relative long exact sequence for \((X,Z)\), with \(H_2(X,Z)=0\), now yields

\[
0\longrightarrow H_3(X,Z;\mathbb Z)
\xrightarrow{\partial}H_2(Z;\mathbb Z)
\longrightarrow H_2(X;\mathbb Z)\longrightarrow0.
\]

This is \(T\)-equivariant and proves the integral assertion.

**3. Character before attaching the intercalate tetrahedra.** Let \(Y\subset Z\) be the union of the \(3n\) row, column, and sum simplices. For a nonzero translation \((u,v)\), the Lefschetz number of a row family is \(n\delta(u)\), and similarly it is \(n\delta(v)\) or \(n\delta(u+v)\) for the other two families: each preserved simplex has Lefschetz number one, even if its vertices are permuted. All pairwise and triple intersections between these three families are discrete vertex sets, on which a nonzero translation has no fixed vertex. At the identity, inclusion-exclusion gives \(\chi(Y)=3n-2n^2\).

The remaining \(n^2(n-1)\) triangles of \(Z\) are the rainbow triangles described in Step 1. A nonzero translation cannot preserve one setwise: it preserves edge types, whereas a rainbow triangle has exactly one edge of each type, so a color-preserving permutation of the triangle must fix all vertices. Thus the additional relative degree-two chain character is \(n^2(n-1)\) at the identity and zero elsewhere. Consequently the equivariant Euler characteristic of \(Z\) minus the trivial degree-zero character is

\[
(u,v)\longmapsto(n\delta(u)-1)(n\delta(v)-1)(n\delta(u+v)-1).
\]

Indeed at the identity it equals \((n-1)^3\); for a nonidentity translation, at most one of \(u=0\), \(v=0\), \(u+v=0\) can occur, and the two expressions agree by direct multiplication. By [1, Theorem 3.12] and the relative homology sequence, \(Z\) has only degree-zero and degree-two rational homology. Thus this virtual character is the actual character on \(H_2(Z;\mathbb Q)\).

The rational augmentation representation \(V\) has character \(a\mapsto n\delta(a)-1\). Therefore \(H_2(Z;\mathbb Q)\cong V_r\otimes V_c\otimes V_s\) as rational \(T\)-modules, by character equality and semisimplicity. The rationalization of the exact sequence in Step 2 splits by Maschke's theorem and yields the asserted direct-summand decomposition. Each coset module \(\mathbb Q[T/H_h]\) has character \(n^2/4\) on \(H_h\) and zero elsewhere, proving the displayed correction formula.

**4. Fourier multiplicities.** After complexification, the tensor product \(V_r\otimes V_c\otimes V_s\) contains the irreducible \((\alpha,\beta)\) once for each \(\gamma\in\widehat A\setminus\{\mathbf1,\alpha,\beta\}\). Its multiplicity is therefore \(n-|\{\mathbf1,\alpha,\beta\}|\). A coset representation \(\mathbb C[T/H_h]\) contains \((\alpha,\beta)\) precisely when \(\alpha(h)=\beta(h)=1\), with multiplicity one. Subtraction proves the exact multiplicity formula. Setting \(\alpha=\beta=\mathbf1\) gives \(n-1-(|E|-1)=n-|E|\). When \(A\cong(C_2)^r\), this vanishes, whereas the dimension of \(H_2(X;\mathbb Q)\), computed in [1], is \((n-1)^3-(n^2/4)(n-1)>0\) for \(n=2^r\ge8\). This completes the proof.

## Verification

Run `python3 verify.py` with standard Python 3.10 or later; no third-party package is needed. The checker independently constructs the adjacency graphs for \(A=C_6\), \(C_8\), \(C_4\times C_2\), and \((C_2)^3\), enumerates all graph triangles and tetrahedra, checks the face model, calculates signed simplicial Lefschetz traces for every translation, checks every Fourier multiplicity, and computes mod-two boundary ranks in degrees two and three. It verifies \(H_2\) ranks \(116,327,295,231\) and invariant dimensions \(4,6,4,0\), respectively. These finite tests are supplementary: the proof covers all finite abelian even-order groups of order at least six.

## Relationship to prior work

Cioabă and Mim [1, Theorems 3.6, 3.8, 3.12; Proposition 3.7] proved the field-independent, nonequivariant Betti number \((n-1)^3-I(M)\), higher-homology vanishing, and the decomposition of the intercalate boundaries. Their work supplies the exact homological input used above, but not the action of the translation group, the integral coset-module sequence, the Fourier multiplicities, or the disappearance of invariant classes for elementary abelian \(2\)-groups. Their earlier collaboration [2] investigates Laplacian spectra and the first cohomology of strongly regular graphs, not these translation representations. The odd-order case has no intercalates and yields the augmentation tensor character without a correction; the even-order formula here exhibits and classifies the new order-two correction.

## Limitations

The complete rational translation representation and integral relative exact sequence are established, but an explicit integral identification of \(H_2(Z;\mathbb Z)\) with an augmentation tensor lattice and an integral splitting criterion are not claimed. The result does not determine the full automorphism-group representation or the equivariant homotopy type. Prior-work comparisons cannot exclude an implicit equivalent in unindexed literature. The proof uses [1] for field-independent homology vanishing; the standalone finite checker does not prove this input in arbitrary size.

## References

[1] S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328v1, first public version June 25, 2026. Sections 3.2–3.5. https://arxiv.org/abs/2606.27328 ; accessible full PDF: https://pdfs.assets.alphaxiv.org/2606.27328v1.pdf

[2] S. M. Cioabă, K. Guo, C. Ji, M. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, arXiv:2508.05871, first public version August 7, 2025; published in *Linear Algebra and its Applications* 730 (2026), 152–197. https://arxiv.org/abs/2508.05871
