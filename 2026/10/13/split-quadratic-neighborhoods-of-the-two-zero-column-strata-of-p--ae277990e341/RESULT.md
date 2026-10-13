# Split quadratic neighborhoods of the two-zero-column strata of permanent hypersurfaces

## Finding
For every integer \(n\geq3\), let \(X_n\subset\mathbb P^{n^2-1}_{\mathbb C}\) be the hypersurface defined by the permanent of a generic \(n\times n\) matrix. For any two distinct columns, let \(L\cong\mathbb P^{n(n-2)-1}\) be the linear space where both columns vanish. There is an explicit nonempty Zariski-open subset \(L^\circ\subset L\) on which the surrounding hypersurface is **Zariski-locally a product of a smooth base with a split ordinary quadratic cone of transverse dimension \(2n-1\)**. The complete Jacobian singular scheme on this neighborhood is exactly \(L^\circ\), reduced. Consequently each of the \(2\binom n2=n(n-1)\) row/column two-zero spaces is a distinct irreducible component of the projective singular locus of codimension \(2n\) in the ambient projective matrix space, and its generic multiplicity in \(X_n\) is two. The complementary-permanent matrix defines an effective divisor of degree \(n(n-2)\) on each \(L\); its support is exactly where the transverse Hessian rank drops.

## Assumptions and scope
Work over \(\mathbb C\), and fix \(n\ge3\). By permuting columns, write an affine matrix as \(M=[u\mid v\mid B]\), with column vectors \(u,v\in\mathbb A^n\) and \(B\in\operatorname{Mat}_{n,n-2}\). For \(i\ne j\), write \(B_{\widehat i\widehat j}\) for the square matrix obtained by deleting rows \(i,j\) from \(B\). Set \(A(B)_{ii}=0\) and \(A(B)_{ij}=\operatorname{per}(B_{\widehat i\widehat j})\) for \(i\ne j\). Let \(U=\{B:\det A(B)\ne0\}\) in affine \(B\)-space. The corresponding projective open subset of \(L\) is the complement of the homogeneous zero locus of \(\det A(B)\). This theorem asserts no classification of singular components other than the explicitly specified two-zero-column/row components, nor of singularities where \(\det A(B)=0\).

## Proof
Expansion of the permanent along its first two columns chooses two **ordered distinct** rows. Consequently the following is an exact polynomial identity, with no factorial or scalar missing:
\[
\operatorname{per}([u\mid v\mid B])=\sum_{i\ne j}u_iv_j\operatorname{per}(B_{\widehat i\widehat j})=u^{\mathsf T}A(B)v.
\]
Each entry of \(A(B)\) is homogeneous of degree \(n-2\), and \(A(B)\) is symmetric. If all entries of \(B\) equal one, then every complementary permanent is \((n-2)!\); thus \(A(B)=(n-2)!(J_n-I_n)\) and
\[
\det A(B)=(-1)^{n-1}(n-1)((n-2)!)^n\ne0.
\]
In particular \(U\) is a nonempty dense principal open subset and \(\det A(B)\) is a nonzero homogeneous polynomial of degree \(n(n-2)\).

Over \(U\), substitute \(w=A(B)v\). Its inverse is \(v=A(B)^{-1}w\), whose entries are regular functions on \(U\). Therefore this is a polynomial-coordinate isomorphism over \(U\), taking the affine permanent hypersurface **scheme-theoretically** to
\[
U\times Q_n,\qquad Q_n=\{(u,w)\in\mathbb A^{2n}:\sum_{i=1}^nu_iw_i=0\}.
\]
The Jacobian ideal of the displayed equation for \(Q_n\) is exactly \((u_1,\ldots,u_n,w_1,\ldots,w_n)\). Its singular scheme is the reduced origin and the quadratic form has Hessian of rank \(2n\). It follows that the singular scheme of the permanent hypersurface over \(U\) is exactly \(U\times\{0\}\), corresponding to \(u=v=0\). In particular the closed irreducible linear space \(L\) contains a nonempty open subset on which it is the *entire* singular locus, so it is an irreducible component globally. On any standard projective chart where a coordinate of \(B\) is one, the same construction gives a product of an open subset of \(\mathbb A^{n(n-2)-1}\) and \(Q_n\). The latter has dimension \(2n-1\), an isolated ordinary quadratic vertex, and Hilbert--Samuel multiplicity two. Repeating with any unordered pair of columns and any unordered pair of rows yields \(2\binom n2\) distinct projective linear components. Distinctness follows because these linear spaces impose distinct pairs of rows or columns to vanish, and no two of these constraints define the same linear subspace.

Finally, the normal-to-\(L\) Hessian at \((u,v)=(0,0)\) is
\[
H(B)=\begin{pmatrix}0&A(B)\\A(B)&0\end{pmatrix},\qquad \det H(B)=(-1)^n\det(A(B))^2.
\]
Thus the support of the rank-drop locus on \(L\) is precisely \(V(\det A(B))\). The natural effective divisor defined by the complementary matrix \(A(B)\) has homogeneous degree \(n(n-2)\); the rank-drop determinantal divisor of the **full Hessian** is instead its double, since its defining determinant is \(\det A(B)^2\) up to sign. We do not assert that \(\det A(B)\) is squarefree.

## Verification
The self-contained `checker.py` uses integer-exact dynamic programming to evaluate permanents and integer-exact Bareiss elimination for determinants. It checks the expansion identity on 42 explicit matrix samples in sizes \(3\le n\le8\), and the all-ones invertibility formula in all six sizes. Run `python3 checker.py`; the exact output is in `checker_output.txt`. These finite tests are independent checks of the implementation and **not** the proof for unbounded \(n\), which is the formal expansion, nonvanishing specialization, and invertible coordinate change above.

## Relationship to prior work
Alper--Bogart--Velasco (2015), Remark 1.5, explicitly notes that matrices with two zero columns are singular on the permanent hypersurface. Boralevi--Carlini--Michałek--Ventura (2024), particularly Section 4.5, studies the global codimension and irreducible-component bounds for the singular locus, including the upper bound \(2n\), but does not state the present full-rank complementary-permanent coordinate trivialization or its exact scheme-theoretic local normal form. Laubenbacher--Swanson (1998) analyzes ideals of \(2\times2\) permanents, which relate to the smallest instance, but does not establish this all-size normal form. The known singular containment and upper bound are **not** claimed to be new. The contribution is the uniform explicit open-neighborhood isomorphism, reduced local Jacobian scheme, and rank-drop divisor along every such linear stratum.

## Limitations
No assertion is made that these are all singular-locus components, that the transverse-rank-drop divisor is reduced or irreducible, or that any particular singularity occurs on the degeneracy divisor. Published equivalent specializations may exist beyond the inspected sources; no independent validation has been performed. The finite checker is not an exhaustive proof.

## References
1. J. Alper, T. Bogart, M. Velasco, *A lower bound for the determinantal complexity of a hypersurface*, arXiv:1505.02205v1 (first public 2015-05-08), Remark 1.5. https://arxiv.org/pdf/1505.02205
2. A. Boralevi, E. Carlini, M. Michałek, E. Ventura, *On the codimension of permanental varieties*, arXiv:2402.17839, Section 4.5, Theorem 4.23 and Conjecture 4.27. https://arxiv.org/pdf/2402.17839
3. R. Laubenbacher, I. Swanson, *Permanental ideals*, arXiv:math/9812112 (1998). https://arxiv.org/pdf/math/9812112
4. J. von zur Gathen, *Feasible arithmetic computations: Valiant's hypothesis*, Journal of Symbolic Computation 4 (1987), 137--172, DOI:10.1016/S0747-7171(87)80063-9 (older codimension bounds).
