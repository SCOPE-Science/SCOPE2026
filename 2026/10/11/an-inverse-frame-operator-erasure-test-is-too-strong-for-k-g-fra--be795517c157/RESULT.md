# An inverse-frame-operator erasure test is too strong for \(K\)-\(g\)-frames

## Finding
A redundancy theorem of Cheshmavar--Rezaei Sarkhaei gives an incorrect invertibility criterion for deleting coefficients from a \(K\)-\(g\)-frame.

In the first public version, Theorem 4.2 states that if a \(K\)-\(g\)-frame has frame operator \(S_J\), then the family remaining after deleting the indices in \(I\) is a \(K\)-\(g\)-frame if and only if
\[
I-S_J^{-1}S_I
\]
is boundedly invertible. Since
\[
S_{J\setminus I}
=
S_J-S_I
=
S_J\left(I-S_J^{-1}S_I\right),
\]
this condition is equivalent, whenever \(S_J\) is invertible, to invertibility of \(S_{J\setminus I}\). That is the ordinary \(g\)-frame condition, not the \(K\)-\(g\)-frame condition.

A two-dimensional example separates the two notions exactly. Let
\[
H=\mathbb C^2,
\qquad
K=P_{\operatorname{span}\{e_1\}},
\]
and use scalar coefficient operators induced by
\[
f_1=(1,1),
\qquad
f_2=e_1.
\]
The full family is an ordinary frame. Its frame operator and the contribution of the first vector are
\[
S_J=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix},
\qquad
S_{\{1\}}=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
\]
Delete \(f_1\). The remaining singleton is
\[
\{e_1\},
\]
and for every \(x=(x_1,x_2)\),
\[
|\langle x,e_1\rangle|^2
=
|x_1|^2
=
\|K^*x\|^2.
\]
Hence the erased family is a Parseval \(K\)-frame.

However,
\[
S_J^{-1}
=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix},
\]
so
\[
I-S_J^{-1}S_{\{1\}}
=
\begin{pmatrix}
1&0\\
-1&0
\end{pmatrix},
\]
which is singular. Therefore the claimed necessity is false.

The 2021 published version changes the criterion to an inverse on \(R(K)\). The same example shows a second obstruction:
\[
R(K)=\operatorname{span}\{e_1\},
\]
but
\[
\left(I-S_J^{-1}S_{\{1\}}\right)e_1
=
(1,-1)
\notin R(K).
\]
Thus the displayed expression is not an operator from \(R(K)\) to itself.

The exact erasure criterion is instead the defining positive-operator domination:
\[
S_{J\setminus I}\ge a\,KK^*
\]
for some \(a>0\), equivalently
\[
R(K)\subseteq R\!\left(S_{J\setminus I}^{1/2}\right).
\]

## Assumptions and scope
The counterexample uses the scalar specialization of a \(g\)-frame:
\[
H_j=\mathbb C,
\qquad
\Lambda_jx=\langle x,f_j\rangle.
\]
Thus it lies inside the stated \(K\)-\(g\)-frame setting.

The full family is deliberately an ordinary frame, so its frame operator \(S_J\) is genuinely invertible. The failure of the first-public theorem therefore cannot be attributed merely to writing \(S_J^{-1}\) for a singular operator.

The correction is an exact characterization for arbitrary \(K\)-\(g\)-Bessel families. It does not require \(K\) to have closed range. The range-inclusion formulation is understood through Douglas' factorization theorem.

## Proof
For the full two-vector family,
\[
S_J
=
f_1f_1^*+f_2f_2^*
=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
+
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}.
\]
Its determinant is \(1\), so it is invertible.

Take
\[
I=\{1\}.
\]
The remaining frame operator is
\[
S_{J\setminus I}
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
=
KK^*.
\]
Therefore
\[
\langle S_{J\setminus I}x,x\rangle
=
\|K^*x\|^2
\]
for every \(x\), and the remaining singleton is a Parseval \(K\)-frame.

Direct inversion gives
\[
S_J^{-1}
=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix}.
\]
Multiplication gives
\[
S_J^{-1}S_I
=
\begin{pmatrix}
0&0\\
1&1
\end{pmatrix},
\]
hence
\[
Q
=
I-S_J^{-1}S_I
=
\begin{pmatrix}
1&0\\
-1&0
\end{pmatrix}.
\]
The determinant of \(Q\) is \(0\), so the preprint criterion fails.

For the published restriction, \(R(K)=\operatorname{span}\{e_1\}\), but
\[
Qe_1=e_1-e_2.
\]
Thus \(Q\) does not preserve \(R(K)\), so it cannot be boundedly invertible as an operator on that subspace.

For the exact replacement, let
\[
S_{J\setminus I}
=
\sum_{j\in J\setminus I}\Lambda_j^*\Lambda_j.
\]
The remaining family is a \(K\)-\(g\)-frame exactly when there is \(a>0\) such that
\[
a\|K^*x\|^2
\le
\sum_{j\in J\setminus I}\|\Lambda_jx\|^2
\]
for all \(x\). This is exactly
\[
a\,KK^*\le S_{J\setminus I}.
\]
Douglas' factorization theorem says that this positive-operator inequality is equivalent to
\[
R(K)\subseteq R\!\left(S_{J\setminus I}^{1/2}\right).
\]

## Verification
The complete first-public Theorem 4.2 and its proof were inspected. The proof explicitly factors
\[
S_{J\setminus I}
=
S_J\left(I-S_J^{-1}S_I\right)
\]
and then states that the erased family is a \(K\)-\(g\)-frame exactly when \(S_{J\setminus I}\) is boundedly invertible. That implication confuses the \(K\)-\(g\)-frame lower inequality with the ordinary \(g\)-frame lower inequality.

The published full text was also inspected at its revised Theorem 2.1. It notes immediately beforehand that a \(K\)-\(g\)-frame operator need not be invertible on the whole space, then replaces the identity by \(I_{R(K)}\). The proof still uses the inverse frame operator and does not establish that the displayed map preserves \(R(K)\).

The matrix calculations above are exact. No numerical approximation, finite enumeration, or computational inference is used.

## Relationship to prior work
Douglas' range-inclusion theorem gives the standard operator characterization underlying the corrected criterion:
\[
a\,KK^*\le S
\]
for some \(a>0\) if and only if \(R(K)\subseteq R(S^{1/2})\).

A close published result on closed-range \(K\)-frame reconstruction observes that a \(K\)-frame operator need not preserve \(R(K)\), so inverse-on-\(R(K)\) formulas can be ill-typed. That structural issue is relevant to the published revision here, but it does not by itself supply the two-vector erasure counterexample: in the present example the full frame operator is invertible on all of \(H\), yet the preprint's full-space criterion is still false because the erased family is a \(K\)-frame without being an ordinary frame.

Later papers on redundancy of \(K\)-\(g\)-frames study other sufficient or exactness conditions. No inspected indexed source was found that states this source-specific two-vector counterexample or the comparison between the preprint and published versions.

## Limitations
The finding concerns the redundancy equivalence theorem only. It does not assess the paper's approximate-dual results.

The range-inclusion criterion is an exact mathematical replacement for the erased-family question, but it is not presented as a new version of every quantitative lower-bound formula in the source.

A nonindexed erratum, thesis remark, or informal correction may contain the same counterexample.

## References
1. J. Cheshmavar and M. Rezaei Sarkhaei, *K-g-frames and approximate K-g-duals in Hilbert spaces*, arXiv:1810.03137v1, first public version 7 October 2018.
2. J. Cheshmavar and M. Rezaei Sarkhaei, *Approximate K-G-duals in Hilbert spaces*, U.P.B. Scientific Bulletin, Series A 83(2) (2021), 111--120.
3. R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proceedings of the American Mathematical Society 17 (1966), 413--415, DOI 10.1090/S0002-9939-1966-0203464-1.
