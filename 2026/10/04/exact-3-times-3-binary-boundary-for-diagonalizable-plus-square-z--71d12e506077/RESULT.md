# Exact \(3\times 3\) binary boundary for diagonalizable-plus-square-zero decomposition
## Finding
For \(A\in M_3(\mathbb F_2)\), there are matrices \(D,N\in M_3(\mathbb F_2)\) with \(D\) diagonalizable over \(\mathbb F_2\), \(N^2=0\), and \(A=D+N\) if and only if \(A\) is not similar to one of
\[
J_3(0),\qquad I_3+J_3(0),\qquad C(x^3+x+1),\qquad C(x^3+x^2+1).
\]
Consequently exactly 380 of the 512 binary \(3\times3\) matrices admit the decomposition and 132 do not. The four exceptional similarity classes have sizes 42, 42, 24, and 24, respectively.

## Assumptions and scope
All matrices and similarity transformations are over \(\mathbb F_2\). Here \(C(f)\) denotes a companion matrix of the monic polynomial \(f\). Over \(\mathbb F_2\), a matrix is diagonalizable over the ground field exactly when its minimal polynomial divides \(x(x+1)\), equivalently when it is idempotent. Thus the problem is exactly to decide which \(A\) can be written as an idempotent plus a square-zero matrix.

## Proof
Let \(A=D+N\), where \(D^2=D\) and \(N^2=0\). Since \(N^2=0\) on a three-dimensional space, \(\operatorname{rank}N\le 1\). If \(N\ne0\), write \(N=uv^{\mathsf T}\) with \(v^{\mathsf T}u=0\). Up to similarity, \(D=\operatorname{diag}(I_r,0)\), with \(0\le r\le3\).

For \(r=0\), one has \(A=N\) and hence \(A^2=0\); therefore \(J_3(0)\) cannot occur. For \(r=3\), one has \((A+I_3)^2=N^2=0\); therefore \(I_3+J_3(0)\) cannot occur.

For \(r=1\), put \(\alpha=v^{\mathsf T}Du\in\mathbb F_2\). The matrix determinant lemma, together with \(v^{\mathsf T}u=0\), gives
\[
\chi_A(t)=t^2(t+1)+\alpha t.
\]
Thus \(\chi_A(t)\) is either \(t^2(t+1)\) or \(t(t^2+t+1)\). For \(r=2\), the same calculation gives
\[
\chi_A(t)=t(t+1)^2+\alpha(t+1),
\]
so \(\chi_A(t)\) is either \(t(t+1)^2\) or \((t+1)(t^2+t+1)\). Hence neither irreducible cubic \(x^3+x+1\) nor \(x^3+x^2+1\) can be the characteristic polynomial of a decomposable matrix. Together with the cases \(r=0,3\), this proves that all four displayed classes are impossible.

Conversely, the rational canonical classification in dimension three over \(\mathbb F_2\) has fourteen similarity types. Besides the four exceptional types, the remaining ten types have direct witnesses. Semisimple \(0/1\)-types are already idempotent; \(J_2(0)\oplus[0]\) is already square-zero; \(J_2(1)\oplus[1]=I_3+E_{12}\); the mixed Jordan types are obtained by adding \(E_{12}\) to the evident rank-one or rank-two idempotent. Finally, for
\[
Q=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
Z=\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix},
\]
one has \(Z^2=0\) and, for \(\varepsilon\in\{0,1\}\),
\[
Q\oplus[\varepsilon]
=\operatorname{diag}(1,0,\varepsilon)+Z.
\]
This covers the two types containing the irreducible quadratic \(x^2+x+1\), and therefore all ten nonexceptional similarity types are decomposable.

For the counts, \(|GL_3(\mathbb F_2)|=168\). The invertible centralizer of \(J_3(0)\) has order 4, so each of the two size-three Jordan classes has size \(168/4=42\). The centralizer of a companion matrix for an irreducible cubic is \(\mathbb F_8^\times\), of order 7, so each irreducible-cubic class has size \(168/7=24\). Hence the exceptional set has size \(42+42+24+24=132\), leaving \(512-132=380\) decomposable matrices.

## Verification
The accompanying exact verifier independently enumerates all 512 binary \(3\times3\) matrices. It finds 58 idempotents and 22 square-zero matrices, forms all sums, and obtains exactly 380 distinct decomposable matrices. Independently, it enumerates all 168 invertible binary \(3\times3\) matrices, constructs the four exceptional conjugacy classes, obtains sizes 42, 42, 24, 24, and verifies that their union is exactly the 132-element complement. It also checks explicit witnesses for the ten nonexceptional rational-canonical types.

## Relationship to prior work
Danchev, García, and Gómez Lozano prove in their 2026 characteristic-two work that the diagonalizable-plus-square-zero decomposition holds over finite fields of characteristic two with more than three elements. For \(\mathbb F_2\), they instead prove a weaker universal potent-plus-square-zero statement, with potency index at most four. Their earlier general theorem covers all \(2\times2\) matrices over arbitrary fields and, for dimension at least three, finite fields with at least \(n+1\) elements. The odd-characteristic companion paper identifies degree-three irreducible obstructions over \(\mathbb F_3\), but it does not settle the binary \(3\times3\) case. The classification here gives the exact first binary dimension beyond the universal \(2\times2\) theorem and shows that two Jordan classes join the two irreducible-cubic classes as the complete obstruction set.

## Limitations
The claim is only for \(3\times3\) matrices over \(\mathbb F_2\). It neither classifies larger binary matrices nor asserts that the four obstruction mechanisms remain complete in higher dimensions. The literature comparison is based on the inspected recent preprints and the published theorem scope; an older unindexed small-case computation could in principle overlap the finite classification.

## References
1. P. Danchev, E. García, and M. Gómez Lozano, *Matrices over Finite Fields of Characteristic 2 as Sums of Diagonalizable and Square-Zero Matrices*, arXiv:2604.15286v1, 2026.
2. P. Danchev, E. García, and M. Gómez Lozano, *Matrices over finite fields of odd characteristic as sums of diagonalizable and square-zero matrices*, arXiv:2507.05762v1; Linear Algebra and its Applications 730 (2026), 35–50.
3. P. Danchev, E. García, and M. Gómez Lozano, *Decompositions of matrices into diagonalizable and square-zero matrices*, Linear and Multilinear Algebra 70 (2022), 4056–4070, DOI 10.1080/03081087.2020.1862742.
