# Aggregate controlled positivity does not provide pointwise coefficient square roots

## Finding
The coefficient-space construction in Proposition 3.3 and Theorem 3.4 of Ghosh--Samanta, *Continuous controlled generalized fusion frames in Hilbert spaces*, is not well-defined under the stated hypotheses.

The source forms, for almost every parameter \(x\),
\[
M_x=T^*P_{F(x)}\Lambda_x^*\Lambda_xP_{F(x)}U
\]
and then uses \(M_x^{1/2}\) as a positive square root. A controlled-frame inequality constrains only the integrated quadratic form
\[
\int_Xv(x)^2\langle M_xf,f\rangle\,d\mu(x).
\]
It does not force every \(M_x\) to be positive.

An exact two-atom example shows the gap. Let
\[
H=\mathbb R^2,\qquad X=\{1,2\}
\]
with counting measure, \(F(1)=F(2)=H\), and unit weights. Choose
\[
T=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
\qquad
U=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}.
\]
Let
\[
A_1=\frac1{10}
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
A_2=
\begin{pmatrix}
2/5&-1/10\\
-1/10&9/10
\end{pmatrix},
\]
and define
\[
\Lambda_i=A_i^{1/2}.
\]
Then
\[
A_1+A_2=
T^{-1}
=
\begin{pmatrix}
1/2&0\\
0&1
\end{pmatrix}.
\]
Consequently the total controlled energy is
\[
\sum_{i=1}^2
\langle\Lambda_iUf,\Lambda_iTf\rangle
=
\langle Uf,f\rangle,
\]
so this is a genuine continuous \((T,U)\)-controlled \(g\)-fusion frame.

Nevertheless,
\[
T A_1U
=
\begin{pmatrix}
3/5&2/5\\
3/10&1/5
\end{pmatrix}
\]
is not self-adjoint and is not positive. At
\[
f=(-3,5)^{\mathsf T}
\]
its quadratic form equals
\[
-\frac1{10}.
\]
Thus the positive square root used to define the source's coefficient field does not exist at the first atom.

A sufficient repair is to require
\[
T^*P_{F(x)}\Lambda_x^*\Lambda_xP_{F(x)}U\ge0
\]
for almost every \(x\), together with the measurability of the resulting square-root field. This is precisely the type of pointwise positivity assumption inserted in the later discrete paper on \((C,C')\)-controlled \(g\)-fusion frames.

## Assumptions and scope
The example uses real Hilbert space, which is permitted by the source and is also used in one of its own examples. Both controls are positive and invertible:
\[
T>0,\qquad U>0.
\]
The eigenvalues of \(U\) are
\[
\frac{3-\sqrt5}{2},
\qquad
\frac{3+\sqrt5}{2}.
\]

Both analysis-energy operators are positive:
\[
A_1\ge0,
\qquad
A_2>0.
\]
For \(A_2\),
\[
\det A_2=\frac7{20}>0,
\qquad
\operatorname{tr}A_2=\frac{13}{10}>0.
\]
Thus the maps \(\Lambda_i=A_i^{1/2}\) are ordinary bounded positive operators.

The finding concerns the pointwise square-root analysis/synthesis construction. It does not claim that the integrated controlled frame operator fails to exist. In the example that integrated operator is the positive matrix \(U\).

## Proof
Let
\[
S=A_1+A_2=T^{-1}.
\]
For every \(f\in\mathbb R^2\),
\[
\begin{aligned}
\sum_{i=1}^2
\langle\Lambda_iUf,\Lambda_iTf\rangle
&=
\sum_{i=1}^2
\langle A_iUf,Tf\rangle\\
&=
\langle TSU f,f\rangle\\
&=
\langle Uf,f\rangle.
\end{aligned}
\]
Therefore
\[
\frac{3-\sqrt5}{2}\|f\|^2
\le
\sum_{i=1}^2
\langle\Lambda_iUf,\Lambda_iTf\rangle
\le
\frac{3+\sqrt5}{2}\|f\|^2.
\]
All controlled-frame hypotheses are satisfied.

For the first atom,
\[
M_1=T A_1U
=
\begin{pmatrix}
3/5&2/5\\
3/10&1/5
\end{pmatrix}.
\]
Its off-diagonal entries differ, so \(M_1\) is not self-adjoint. More strongly,
\[
M_1
\begin{pmatrix}
-3\\
5
\end{pmatrix}
=
\begin{pmatrix}
1/5\\
1/10
\end{pmatrix},
\]
and hence
\[
\left\langle
M_1
\begin{pmatrix}
-3\\
5
\end{pmatrix},
\begin{pmatrix}
-3\\
5
\end{pmatrix}
\right\rangle
=
-\frac1{10}.
\]
So \(M_1\not\ge0\).

The source's preliminary section defines \(R^{1/2}\) as the unique positive square root of a positive self-adjoint operator \(R\). Therefore \(M_1^{1/2}\) in the sense used by Proposition 3.3 and Theorem 3.4 does not exist.

For the repair, assume for almost every \(x\) that
\[
M_x=
T^*P_{F(x)}\Lambda_x^*\Lambda_xP_{F(x)}U
\ge0
\]
and that \(x\mapsto M_x^{1/2}f\) is measurable for every \(f\). Define
\[
(Jf)(x)=v(x)M_x^{1/2}f.
\]
Then the controlled Bessel inequality gives
\[
\|Jf\|_{L^2}^2
=
\int_Xv(x)^2\|M_x^{1/2}f\|^2\,d\mu(x)
=
\int_Xv(x)^2\langle M_xf,f\rangle\,d\mu(x)
\le B\|f\|^2.
\]
Thus \(J\) is bounded with
\[
\|J\|\le\sqrt B.
\]
Its Hilbert-space adjoint \(J^*\) is the synthesis operator, and
\[
J^*J
\]
is the positive controlled frame operator associated with the square-root coefficient representation.

## Verification
The open arXiv full text was inspected at the source's definition of positive square roots, Definition 3.1, Proposition 3.3, Theorem 3.4, and the complete proofs of Proposition 3.3 and Theorem 3.4. The two pages containing the pointwise square-root calculation and the theorem statement were also inspected visually.

The proof of Proposition 3.3 rewrites
\[
\langle M_xf,g\rangle
\]
through \(M_x^{1/2}\) and then applies Cauchy--Schwarz. The proof of Theorem 3.4 again defines its coefficient field by \(M_x^{1/2}\). No hypothesis in those statements ensures \(M_x\ge0\) pointwise.

The later discrete paper *\((C,C')\)-Controlled \(g\)-Fusion Frames in Hilbert Spaces* explicitly says, before defining its controlled analysis operator, that
\[
C^*P_{W_i}\Lambda_i^*\Lambda_iP_{W_i}C'
\]
is assumed positive for every index \(i\). This is exactly the missing structural condition in the continuous square-root construction.

All matrix computations in the counterexample are exact.

## Relationship to prior work
The 2021 continuous paper extends the controlled \(g\)-fusion framework to a measure-space setting and introduces coefficient-space analysis and synthesis operators based on pointwise square roots.

The 2023 discrete paper by Shakoory--Ahmadi--Rahimlou--Sadri uses the same type of square-root coefficient representation but explicitly places a per-index positivity assumption before doing so. Its formulation therefore supplies a natural repair mechanism for the continuous theorem, but it does not state the two-atom counterexample or identify Theorem 3.4 of the continuous paper as invalid.

A 2024 continuous controlled \(K\)-\(g\)-fusion paper by Ghosh--Samanta reproduces the older discrete square-root definition in its preliminaries. This shows that distinguishing integrated positivity from pointwise positivity remains relevant in subsequent formulations.

The closest operator-theoretic issue in controlled-frame theory is positivity of the aggregate mixed frame operator. Aggregate positivity is strictly weaker than the pointwise condition here: the example has
\[
\sum_iM_i=U>0
\]
while \(M_1\not\ge0\).

## Limitations
The finding does not say that a nonpositive bounded operator has no algebraic square root of any kind. It says that the positive square root used by the source's notation and norm identities is unavailable.

The sufficient repair includes an explicit measurability condition on the square-root field. No weakest measurable-field hypothesis is claimed.

The integrated controlled frame operator can remain perfectly well-defined and positive even when the source's pointwise coefficient factorization fails, as the example demonstrates.

## References
1. P. Ghosh and T. K. Samanta, *Continuous controlled generalized fusion frames in Hilbert spaces*, arXiv:2110.11234v1, 4 October 2021.
2. H. Shakoory, R. Ahmadi, G. Rahimlou and V. Sadri, *\((C,C')\)-Controlled \(g\)-Fusion Frames in Hilbert Spaces*, Iranian Journal of Mathematical Sciences and Informatics 18(1) (2023), 179--191, DOI 10.52547/ijmsi.18.1.179.
3. P. Ghosh and T. K. Samanta, *Construction of continuous controlled \(K\)-\(g\)-fusion frames in Hilbert spaces*, Acta et Commentationes Universitatis Tartuensis de Mathematica 28(1) (2024), DOI 10.12697/ACUTM.2024.28.04.
