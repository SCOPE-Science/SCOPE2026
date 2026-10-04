# The numerical Euler lattice of a surface has the Néron–Severi discriminant group
## Finding
Let \(X\) be a smooth projective surface over an algebraically closed field and put
\[
N^1(X)=\operatorname{Pic}(X)/\equiv_{\mathrm{num}}.
\]
Choose an integral basis \(D_1,\ldots,D_\rho\) of \(N^1(X)\), and let
\[
Q=(D_i\cdot D_j)_{i,j}
\]
be its intersection matrix. Then the homomorphism
\[
K_{\mathrm{num}}(X)\longrightarrow \mathbf Z\oplus N^1(X)\oplus\mathbf Z,
\qquad
[E]\longmapsto\bigl(\operatorname{rk}E,c_1(E),\chi(E)\bigr)
\]
is an isomorphism of abelian groups.

With respect to an explicit integral basis induced by this isomorphism, the Euler-pairing matrix is Smith-equivalent over \(\mathbf Z\) to
\[
H\oplus(-Q),
\qquad
H=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Therefore
\[
\operatorname{coker}\bigl(K_{\mathrm{num}}(X)\xrightarrow{\;\chi\;}K_{\mathrm{num}}(X)^\vee\bigr)
\cong
N^1(X)^\vee/N^1(X).
\]
Equivalently, the Smith normal form of the numerical Euler matrix consists of two unit factors together with the invariant factors of the Néron–Severi intersection matrix.

In particular,
\[
\det M_\chi(X)=\left|\operatorname{disc}N^1(X)\right|>0,
\]
and the numerical Euler lattice is unimodular if and only if the numerical Néron–Severi lattice is unimodular.

## Assumptions and scope
Here \(K_{\mathrm{num}}(X)\) is the Grothendieck group modulo the radical of the Euler pairing. The lattice \(N^1(X)\) is the free group of divisor classes modulo numerical equivalence, equipped with the nondegenerate intersection pairing. Its dual is taken with respect to that pairing.

The statement is integral: it determines all elementary divisors of the Euler pairing, not only its determinant over \(\mathbf Q\).

The initiating paper of Liu, Shen, and Zhang defines the numerical Cartan determinant and asks which geometric properties force it to be \(1\). It proves positivity in broad classes and notes special surface examples, but does not give the integral surface formula above.

## Proof
Write a class in the target group as
\[
(r,D,u)\in\mathbf Z\oplus N^1(X)\oplus\mathbf Z.
\]
For classes \(E,F\) with invariants
\[
(r,D,u)=\bigl(\operatorname{rk}E,c_1(E),\chi(E)\bigr),
\qquad
(s,E',v)=\bigl(\operatorname{rk}F,c_1(F),\chi(F)\bigr),
\]
Riemann–Roch gives
\[
\chi(E,F)=rv+su-rs\chi(\mathcal O_X)+s(D\cdot K_X)-D\cdot E'.
\]
Thus the Euler pairing depends only on \((r,D,u)\).

The invariant map is surjective integrally. A closed point \(p\in X\) gives
\[
[\mathcal O_p]\longmapsto(0,0,1).
\]
Hence
\[
[\mathcal O_X]-\chi(\mathcal O_X)[\mathcal O_p]
\]
maps to \((1,0,0)\). For each basis divisor \(D_i\), the class
\[
[\mathcal O_X(D_i)]-[\mathcal O_X]-
\bigl(\chi(\mathcal O_X(D_i))-\chi(\mathcal O_X)\bigr)[\mathcal O_p]
\]
maps to \((0,D_i,0)\). These classes generate the target.

The displayed Riemann–Roch form on the target is nondegenerate because the intersection form on \(N^1(X)\) is nondegenerate. Consequently the kernel of the invariant map is exactly the numerical radical of \(K_0(X)\), so it induces the asserted integral isomorphism on \(K_{\mathrm{num}}(X)\).

Let
\[
e=(1,0,0),\qquad f_i=(0,D_i,0),\qquad p=(0,0,1),
\]
and set
\[
k_i=D_i\cdot K_X,
\qquad
c=\chi(\mathcal O_X).
\]
In the ordered basis \((e,f_1,\ldots,f_\rho,p)\), the Euler matrix is
\[
M=
\begin{pmatrix}
-c&0&1\\
k&-Q&0\\
1&0&0
\end{pmatrix}.
\]
Reorder rows and columns to \((e,p,f_1,\ldots,f_\rho)\). The matrix becomes
\[
\begin{pmatrix}
-c&1&0\\
1&0&0\\
k&0&-Q
\end{pmatrix}.
\]
For each \(i\), subtract \(k_i\) times the \(p\)-row from the \(f_i\)-row. Then add \(c\) times the \(p\)-column to the \(e\)-column. These are unimodular integral row and column operations, and they transform the matrix into
\[
H\oplus(-Q).
\]
This proves the Smith-equivalence statement and the cokernel identification.

Taking determinants gives
\[
\det M=(-1)^{\rho+1}\det Q.
\]
By the Hodge index theorem the intersection form on \(N^1(X)\) has signature \((1,\rho-1)\), so
\[
\operatorname{sgn}(\det Q)=(-1)^{\rho-1}.
\]
Hence
\[
\det M=|\det Q|=\left|\operatorname{disc}N^1(X)\right|>0.
\]
The unimodularity criterion follows immediately.

## Verification
The accompanying `verify.py` reconstructs the Euler matrix from \(Q\), the canonical intersection vector, and \(\chi(\mathcal O_X)\) for several nonsingular integral test lattices. It executes exactly the row and column operations used in the proof and checks that the result is \(H\oplus(-Q)\). It also checks the determinant identity and compares Smith invariant factors using exact integer arithmetic.

These finite checks are consistency tests only. The theorem for arbitrary Picard rank is proved by the uniform symbolic row and column operations above, together with Riemann–Roch and the Hodge index theorem.

The stored replay output ends in `VERIFY_OK`.

## Relationship to prior work
Liu, Shen, and Zhang introduce the numerical Cartan determinant for smooth proper dg categories and ask which geometric properties imply determinant \(1\). They prove positivity for odd-dimensional smooth projective varieties and for even-dimensional varieties satisfying the numerical Hodge standard conjecture. Their discussion includes the rank-one K3 value and notes that surfaces satisfy the relevant positivity input, but it does not state the exact determinant or the Smith normal form for arbitrary surfaces.

Krah writes the surface Riemann–Roch Euler form explicitly and develops the associated surface-like pseudolattice and its Néron–Severi lattice. Vial relates maximal numerical exceptional collections on surfaces to unimodularity properties of the Néron–Severi lattice in the setting \(\chi(\mathcal O_X)=1\). Special integral decompositions are also standard for classes such as K3 and bielliptic surfaces. These results are compatible with the theorem above, but the checked sources do not state the all-surfaces Smith-equivalence or the resulting discriminant-group identification.

The new statement resolves the determinant-one question completely in dimension two and strengthens it from one integer to the full finite cokernel of the Euler homomorphism.

## Limitations
The theorem is specific to smooth projective surfaces. It does not determine numerical Cartan determinants in dimension at least three, where higher-codimension numerical cycle lattices enter and an analogous two-step integral reduction need not exist.

The originality comparison found closely related surface-pseudolattice and exceptional-collection literature, so an unindexed source could conceivably contain the same elementary lattice reduction. No checked source states the general Smith-normal-form conclusion.

## References
1. Y. Liu, Y. Shen, Z. Zhang, *Cartan Determinants in algebraic geometry*, arXiv:2609.29598v1, 2026.
2. J. Krah, *Mutations of numerically exceptional collections on surfaces*, Mathematische Zeitschrift 307 (2024), article 78.
3. C. Vial, *Exceptional collections, and the Néron–Severi lattice for surfaces*, Advances in Mathematics 305 (2017), 895–934; arXiv:1504.01776.
