# Arithmetic splitting of the Burgers pre-Lie Nijenhuis locus

## Finding

Let \(K\) be a field with \(\operatorname{char}K\ne2\). On \(K^2\) with the standard symmetric bilinear form and \(a=e_1\), the Burgers pre-Lie product
\[
x\cdot_a y=\langle x,y\rangle a+\langle x,a\rangle y
\]
has table
\[
e_1\cdot e_1=2e_1,\qquad e_1\cdot e_2=e_2,\qquad e_2\cdot e_1=0,\qquad e_2\cdot e_2=e_1.
\]

For
\[
N=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\]
the complete Nijenhuis condition is
\[
\boxed{C(B+C)=0,\qquad C(A-D)=0,\qquad (A-D)^2+B(B+C)=0.}
\]

Hence the reduced solution set is
\[
\boxed{\operatorname{Nij}(A_K)_{\mathrm{red}}=\mathcal R\cup\mathcal Q,}
\]
with
\[
\mathcal R=\left\{\begin{pmatrix}u&-v\\v&u\end{pmatrix}:u,v\in K\right\}
\]
and
\[
\mathcal Q=\left\{\begin{pmatrix}A&B\\0&D\end{pmatrix}:(A-D)^2+B^2=0\right\}.
\]

If \(-1\) is a square, choose \(\iota^2=-1\). Then
\[
\mathcal Q=\{C=0,\ A-D=\iota B\}\cup\{C=0,\ A-D=-\iota B\},
\]
so the reduced locus is three affine \(2\)-planes meeting along the scalar line.

If \(-1\) is nonsquare, the only \(K\)-rational points of \(\mathcal Q\) satisfy \(A=D\) and \(B=0\). Thus
\[
\boxed{\operatorname{Nij}(A_K)(K)=\mathcal R(K),}
\]
even though \(\mathcal Q\) is a two-dimensional quadratic surface that splits over \(K(\sqrt{-1})\).

For an odd finite field \(\mathbf F_q\), if \(-1\) is a square then
\[
\boxed{|\operatorname{Nij}(A_{\mathbf F_q})|=3q^2-2q},
\qquad
\boxed{\operatorname{rank\ profile}=\left(1,6(q-1),(q-1)(3q-5)\right)}.
\]
If \(-1\) is nonsquare then
\[
\boxed{|\operatorname{Nij}(A_{\mathbf F_q})|=q^2},
\qquad
\boxed{\operatorname{rank\ profile}=(1,0,q^2-1)}.
\]

The full pre-Lie automorphism group is
\[
\boxed{\operatorname{Aut}(A_K)=\{I,\operatorname{diag}(1,-1)\}.}
\]
Over \(\mathbf F_q\), the conjugacy-class counts are
\[
\boxed{\frac{q(3q-1)}2}
\]
in the split case and
\[
\boxed{\frac{q(q+1)}2}
\]
in the nonsplit case.

The reduced Hasse--Weil zeta function is
\[
\boxed{Z(T)=\frac{(1-qT)^2}{(1-q^2T)^3}}
\]
when \(-1\) is a square in \(\mathbf F_q\).

When \(-1\) is nonsquare, it becomes square exactly over even-degree extensions, so
\[
|\operatorname{Nij}(A)(\mathbf F_{q^m})|=
\begin{cases}
q^{2m},&m\text{ odd},\\
3q^{2m}-2q^m,&m\text{ even}.
\end{cases}
\]
Therefore
\[
\boxed{Z(T)=\frac{1-q^2T^2}{(1-q^2T)(1-q^4T^2)}}.
\]

## Assumptions and scope

Wang, Bai, Liu, and Sheng introduce Nijenhuis operators on pre-Lie algebras and single out the Burgers family
\[
x\cdot_a y=\langle x,y\rangle a+\langle x,a\rangle y.
\]
Their preprint first appeared on 9 October 2017 and lists \(17B60\) first among its Mathematics Subject Classification codes.

Proposition 8.4 gives a Burgers criterion under the extra hypothesis that \(N\) is skew-adjoint. In this two-dimensional specialization that gives the skew line, while their polynomial-closure theorem also yields its scalar translates, the plane \(\mathcal R\).

A 2026 paper classifies all Nijenhuis operators on two-dimensional complex pre-Lie algebras. Accordingly, the algebraically closed split case is prior coverage in substance. The result here concerns arbitrary-field descent, nonsplit rational points, finite-field ranks and conjugacy, and extension-field zeta behavior.

## Proof

The Nijenhuis identity is
\[
N(x)\cdot N(y)=N\!\left(N(x)\cdot y+x\cdot N(y)-N(x\cdot y)\right).
\]
Evaluating it on the four ordered basis pairs gives
\[
T_N(e_1,e_1)=C(B+C)e_1-C(A-D)e_2,
\]
\[
T_N(e_1,e_2)=T_N(e_2,e_1)=-C(A-D)e_1-C(B+C)e_2,
\]
and
\[
T_N(e_2,e_2)=\bigl((A-D)^2+B(B+C)\bigr)e_1+C(A-D)e_2.
\]
Thus the three displayed scalar equations are necessary and sufficient.

If \(C\ne0\), then \(B=-C\) and \(A=D\), giving \(\mathcal R\). If \(C=0\), the remaining equation is \((A-D)^2+B^2=0\), giving \(\mathcal Q\). The square-class descriptions follow immediately.

For automorphisms, write \(g=\begin{pmatrix}p&q\\r&s\end{pmatrix}\). Preservation of the four products forces
\[
r=0,\qquad p=1,\qquad q=0,\qquad s^2=1,
\]
hence \(s=\pm1\).

In the split finite-field case, the three planes have \(3q^2\) total points before subtracting the common scalar line twice, giving \(3q^2-2q\). Each plane contains \(2(q-1)\) nonzero rank-one matrices, with no rank-one overlap, yielding the stated profile.

In the nonsplit case, every nonzero matrix in \(\mathcal R\) has determinant \(u^2+v^2\ne0\), so the rank profile is \((1,0,q^2-1)\).

The nonidentity automorphism sends \((A,B,C,D)\) to \((A,-B,-C,D)\). Its fixed Nijenhuis operators are exactly the \(q\) scalar matrices. Burnside's formula gives the class counts.

The two zeta formulas follow from the stated extension-field point counts.

## Verification

The included checker reconstructs the product and all Nijenhuis torsion coefficients symbolically. It verifies the exact structural equations and independently reconstructs the automorphism group.

It exhaustively tests every \(2\times2\) matrix over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11},\quad\mathbf F_{13}.
\]
The totals are
\[
9,\quad65,\quad49,\quad121,\quad481,
\]
the rank profiles are
\[
(1,0,8),\quad(1,24,40),\quad(1,0,48),\quad(1,0,120),\quad(1,72,408),
\]
and the automorphism-orbit counts are
\[
6,\quad35,\quad28,\quad66,\quad247.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field decomposition is proved directly above.

## Relationship to prior work

The 2017 source defines pre-Lie Nijenhuis operators and studies the Burgers family. Its Proposition 8.4 assumes skew-adjointness, while Theorem 4.11 proves polynomial closure. Those results account naturally for \(\mathcal R\), but do not state the arbitrary-field quadratic branch.

The 2026 complete two-dimensional complex classification covers the split algebraically closed specialization. No originality is claimed for that complex classification. The contribution here is the descent phenomenon: over fields where \(-1\) is nonsquare, the two extra geometric planes are conjugate over a quadratic extension and have no nonscalar rational points.

Targeted searches for Burgers Nijenhuis operators over finite fields, square-class dependence, the exact point formulas, and the nonsplit zeta function found no covering result.

## Limitations

Characteristic \(2\) is excluded.

Only the two-dimensional standard-form Burgers specialization is treated.

The complex split case is prior coverage; originality is the arbitrary-field arithmetic refinement.

Failed searches do not prove absolute novelty.

## References

1. Q. Wang, C. Bai, J. Liu, and Y. Sheng, “Nijenhuis operators on pre-Lie algebras,” arXiv:1710.03749v1, first public 9 October 2017; *Communications in Contemporary Mathematics* 21 (2019), 1850050, DOI `10.1142/S0219199718500505`.
2. X. Zou, X. Gao, C. Kang, and J. Lü, “Nijenhuis Operators on 2D Pre-Lie Algebras and 3D Associative Algebras,” *Axioms* 15 (2026), 80, DOI `10.3390/axioms15010080`.
