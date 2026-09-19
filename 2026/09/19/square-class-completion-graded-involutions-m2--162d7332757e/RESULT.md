# Square classes complete the order-two elementary involutions on \(M_2(F)\)

## Statement

Let \(F\) be a field of characteristic different from \(2\), let \(G\) be an abelian group, and equip
\[
A=M_2(F)
\]
with a nontrivial elementary \(G\)-grading induced by \((g_1,g_2)\) such that \(g_1^2=g_2^2\). Writing \(h=g_1^{-1}g_2\), we have \(h^2=1\), \(h\ne 1\), and
\[
A_1=F e_{11}\oplus F e_{22},\qquad A_h=F e_{12}\oplus F e_{21}.
\]

For each \(a\in F^\times\), define
\[
\sigma_a\!\begin{pmatrix}x&y\\ z&w\end{pmatrix}
=
\begin{pmatrix}x&a^{-1}z\\ ay&w\end{pmatrix}.
\]
Also set
\[
\rho_+\!\begin{pmatrix}x&y\\ z&w\end{pmatrix}
=
\begin{pmatrix}w&y\\ z&x\end{pmatrix},\qquad
\rho_-\!\begin{pmatrix}x&y\\ z&w\end{pmatrix}
=
\begin{pmatrix}w&-y\\ -z&x\end{pmatrix}.
\]
Then every graded \(F\)-linear involution on \(A\) is exactly one of the maps \(\sigma_a\), \(\rho_+\), or \(\rho_-\). Up to graded \(F\)-algebra isomorphism,
\[
\boxed{\sigma_a\cong\sigma_b\iff a/b\in(F^\times)^2,}
\]
and neither \(\rho_+\) nor \(\rho_-\) is graded-isomorphic to any \(\sigma_a\). The two maps \(\rho_+\) and \(\rho_-\) are also inequivalent. Consequently the isomorphism classes in this branch are naturally indexed by
\[
\boxed{F^\times/(F^\times)^2\ \sqcup\ \{\rho_+,\rho_-\}.}
\]

The usual transpose involution is \(\sigma_1\), while
\[
\sigma_{-1}\!\begin{pmatrix}x&y\\z&w\end{pmatrix}
=
\begin{pmatrix}x&-z\\-y&w\end{pmatrix}
\]
is the involution often denoted \(\gamma_4\). Thus the square-class family collapses to the transpose class over an algebraically closed field, but not over a general characteristic-zero field.

There is a second conclusion. If \(F\) has characteristic zero, then all of the square-class forms \((A,\sigma_a)\) have exactly the same \(G\)-graded \(*\)-polynomial identities and the same \(G\)-graded \(*\)-central polynomials:
\[
\boxed{
Id_F^{(G,*)}(A,\sigma_a)=Id_F^{(G,*)}(A,\sigma_b),\qquad
C_F^{(G,*)}(A,\sigma_a)=C_F^{(G,*)}(A,\sigma_b)
}
\]
for all \(a,b\in F^\times\). Hence their graded \(*\)-cocharacters, graded \(*\)-codimensions, central codimensions, and every invariant determined by these spaces agree. In particular, formulas proved for the transpose representative extend unchanged to all omitted square-class forms.

## Proof of the classification

The restriction of a graded involution \(*\) to
\(A_1=F e_{11}\oplus F e_{22}\cong F\times F\) permutes the two primitive idempotents. There are two cases.

### Case 1: the diagonal idempotents are fixed

Assume \(e_{11}^*=e_{11}\) and \(e_{22}^*=e_{22}\). Since
\(e_{12}=e_{11}e_{12}e_{22}\), anti-multiplicativity gives
\[
e_{12}^*\in e_{22}Ae_{11}=F e_{21}.
\]
Thus \(e_{12}^*=a e_{21}\) for a unique \(a\in F^\times\). Similarly
\(e_{21}^*=b e_{12}\). Applying \(*\) twice, or applying \(*\) to
\(e_{12}e_{21}=e_{11}\), gives \(ab=1\). Hence \(*=\sigma_a\).

### Case 2: the diagonal idempotents are swapped

Assume \(e_{11}^*=e_{22}\) and \(e_{22}^*=e_{11}\). Then
\[
e_{12}^*\in e_{11}Ae_{22}=F e_{12},
\]
so \(e_{12}^*=c e_{12}\); similarly \(e_{21}^*=d e_{21}\). The relations \((* )^2=1\) and
\((e_{12}e_{21})^*=e_{22}\) force \(c=d\) and \(c^2=1\). Since
\(\operatorname{char}F\ne2\), \(c=\pm1\), yielding \(\rho_+\) and \(\rho_-\).

### Isomorphism classes

Every \(F\)-algebra automorphism of \(M_2(F)\) is inner. A graded automorphism must normalize the diagonal algebra \(A_1\), hence is induced by a monomial matrix. Conjugation by a diagonal matrix \(\operatorname{diag}(r,s)\) sends the parameter \(a\) to
\[
a(s/r)^2.
\]
Conjugation by the permutation matrix interchanging the two coordinate lines sends \(a\) to \(a^{-1}\). Therefore the square class of \(a\) is invariant, and any two parameters in the same square class are conjugate. Since \(a/a^{-1}=a^2\), inversion does not change the square class. This proves
\(\sigma_a\cong\sigma_b\) exactly when \(a/b\) is a square.

The induced permutation of the two primitive idempotents of \(A_1\) is invariant under graded conjugacy, so the diagonal-fixing family cannot be isomorphic to either diagonal-swapping involution. Finally, diagonal and antidiagonal graded conjugations preserve the sign distinguishing \(\rho_+\) and \(\rho_-\), so those two classes are distinct.

## Scalar-extension collapse of the PI theory

Fix \(a,b\in F^\times\) and let
\[
K=F\bigl(\sqrt{a/b}\bigr).
\]
Over \(K\), a diagonal conjugation makes \(\sigma_a\) and \(\sigma_b\) graded-isomorphic. Thus
\[
(A,\sigma_a)\otimes_F K\cong (A,\sigma_b)\otimes_F K
\]
as graded algebras with involution.

For an infinite base field, graded \(*\)-identities are unchanged by scalar extension. Indeed, after multihomogenization and complete linearization, evaluation of a multilinear graded \(*\)-polynomial on \(A\otimes_FK\) expands as a \(K\)-linear combination of evaluations on \(A\). The converse follows by restriction. The same argument applies to central polynomials because
\[
Z(M_2(F))\otimes_FK=Z(M_2(K))=K I_2.
\]
Characteristic zero supplies the required multilinearization. Therefore the identity ideals and central-polynomial spaces over \(F\) coincide for every \(\sigma_a\), proving the second assertion.

## Concrete counterexample to an arbitrary-field classification

Take \(F=\mathbb Q\) and \(a=2\). Then
\[
\sigma_2\!\begin{pmatrix}x&y\\z&w\end{pmatrix}
=
\begin{pmatrix}x&z/2\\2y&w\end{pmatrix}
\]
is a graded involution for the nontrivial \(C_2\)-grading. Its square class is neither that of \(1\) nor that of \(-1\), so it is graded-isomorphic to neither the transpose involution \(\gamma_1=\sigma_1\) nor \(\gamma_4=\sigma_{-1}\). It fixes the two diagonal primitive idempotents, so it is not isomorphic to the two swapping involutions \(\gamma_2,\gamma_3\). Thus it is absent from any list containing only \(\gamma_1,\gamma_2,\gamma_3\) (or even only the four displayed \(\gamma_i\)). Over \(\mathbb Q\) there are infinitely many such square classes.

## Relation to recent literature

Bezerra dos Santos and Reis, arXiv:2609.20488v1 (submitted 17 September 2026), state their base field assumption as characteristic zero and say that they consider all \(G\)-graded involutions on \(M_2(F)\). Their Theorem 2.1, in the branch \(g_1^2=g_2^2\), lists only \(\gamma_1,\gamma_2,\gamma_3\). Immediately before that theorem they cite the classification of Bahturin and Zaicev. The cited Bahturin--Zaicev work explicitly assumes an algebraically closed base field of characteristic different from \(2\). Under that hypothesis the square-class group is trivial, so the diagonal-fixing family above does collapse to \(\gamma_1\); over the stated arbitrary characteristic-zero field it need not.

This identifies a missing hypothesis or, equivalently, a missing square-class family in the arbitrary-field formulation. Importantly, the defect is structural rather than a defect in the transpose-class PI formulas: the scalar-extension argument above shows that every omitted \(\sigma_a\) has the same graded \(*\)-identities and central polynomials as \(\gamma_1\). Thus the existing transpose formulas can be reused for the whole square-class family after the classification statement is corrected.

## Limitations

This result addresses only the nontrivial elementary grading with \(g_1^2=g_2^2\). It does not classify all group gradings on split \(M_2(F)\) over arbitrary non-algebraically-closed fields, and it does not analyze whether the paper's Klein-group \((-1)\)-grading classification also requires extra forms. The square-class classification itself is consistent with standard discriminant theory for orthogonal involutions on split quaternion algebras; novelty is claimed only for the explicit completion/correction of the stated arbitrary-field theorem and the observation that all missing square-class forms are nevertheless graded-\(*\)-PI and central-PI equivalent to the transpose representative. Originality is therefore only to the best of our knowledge.

## References

1. R. Bezerra dos Santos and L. Reis, *Polynomial identities, central polynomials and cocharacters of \(M_2(F)\) with \(G\)-graded involution*, arXiv:2609.20488v1 (2026).
2. Y. Bahturin and M. Zaicev, *Involutions on graded matrix algebras*, Journal of Algebra 315 (2007), 527--540; arXiv:math/0609417. The paper works over an algebraically closed field of characteristic different from \(2\).
3. J. P. Cruz and A. C. Vieira, *Central polynomials of the second-order matrix algebra with graded involution*, Journal of Algebra 639 (2024), 574--595, DOI: 10.1016/j.jalgebra.2023.11.002.
