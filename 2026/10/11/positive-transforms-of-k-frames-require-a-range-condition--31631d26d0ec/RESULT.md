# Positive transforms of \(K\)-frames require a range condition

## Finding
Theorem 3.8 of Ghosh--Samanta states that if \((f_i)_{i\ge1}\) is a \(K\)-frame associated to fixed anchors in an \(n\)-Hilbert space and \(U:X_F\to X_F\) is positive, then \((f_i+Uf_i)_{i\ge1}\) is again a \(K\)-frame. This is false.

Let \(S=I+U\). The exact universal preservation condition on the Hilbert-space reduction \(X_F\) is
\[
R(K)\subseteq S R(K).
\]
More quantitatively, put
\[
\eta(S,K)=\sup\{\eta\ge0: \eta KK^*\le SKK^*S^*\}.
\]
Then \(\eta(S,K)>0\) if and only if \(R(K)\subseteq R(SK)=S R(K)\). If a \(K\)-frame has bounds \(A,B\), its image under \(S\) has valid bounds
\[
A\eta(S,K)\quad\text{{and}}\quad B\|S\|^2.
\]
The factor \(\eta(S,K)\) is the largest lower-bound multiplier that can be guaranteed uniformly over all \(K\)-frames with a given lower bound.

## Assumptions and scope
The claim is about the Hilbert space \(X_F\) used by the source to encode frames associated to fixed anchors. No closed-range assumption on \(K\) is required for the range criterion. For the explicit source-level counterexample, take the standard real 2-inner-product space \(X=\mathbb R^3\),
\[
\langle x,y\mid z\rangle=\langle x,y\rangle\langle z,z\rangle-\langle x,z\rangle\langle z,y\rangle,
\]
with anchor \(a_2=e_3\). Then \(X_F\) identifies with \(\operatorname{{span}}\{{e_1,e_2\}}\cong\mathbb R^2\) with its ordinary inner product.

Set
\[
K=P_{e_1},\qquad f_i=\frac{{\sqrt3}}{{2^i}}e_1\quad(i\ge1),
\]
and
\[
U=\begin{{pmatrix}}1&1\\1&1\end{{pmatrix}},\qquad S=I+U=\begin{{pmatrix}}2&1\\1&2\end{{pmatrix}}.
\]
The matrix \(U\) is positive semidefinite.

## Proof
For \(x=(x_1,x_2)\in X_F\),
\[
\sum_{{i=1}}^\infty |\langle x,f_i\rangle|^2
=3\sum_{{i=1}}^\infty4^{{-i}}|x_1|^2
=|x_1|^2
=\|K^*x\|^2.
\]
Hence \((f_i)\) is a Parseval \(K\)-frame.

All transformed vectors are scalar multiples of
\[
S e_1=(2,1).
\]
For \(x=(1,-2)\),
\[
\langle x,S e_1\rangle=0
\quad\text{{but}}\quad
K^*x=e_1\ne0.
\]
Thus
\[
\sum_{{i=1}}^\infty|\langle x,Sf_i\rangle|^2=0
\]
while \(\|K^*x\|^2=1\), so the transformed family has no positive lower \(K\)-frame bound.

The source proof uses the implication
\[
S_F\ge A K K^*,\quad U\ge0
\quad\Longrightarrow\quad
(I+U)S_F(I+U)^*\ge S_F.
\]
This operator inequality is false without additional compatibility. In the counterexample \(S_F=P_{e_1}\), and
\[
S S_F S-S_F
=\begin{{pmatrix}}3&2\\2&1\end{{pmatrix}},
\]
whose determinant is \(-1\), so it is not positive.

For the exact repair, let \(V:\ell^2\to X_F\) be the synthesis operator of an arbitrary \(K\)-frame. The standard range characterization gives
\[
R(K)\subseteq R(V).
\]
The transformed family has synthesis operator \(SV\), so it is a \(K\)-frame exactly when
\[
R(K)\subseteq R(SV)=S R(V).
\]
Therefore \(R(K)\subseteq S R(K)\) is sufficient for every \(K\)-frame.

It is also necessary for universal preservation. If \((e_i)\) is an orthonormal basis, then \((Ke_i)\) is a Parseval \(K\)-frame because
\[
\sum_i|\langle x,Ke_i\rangle|^2=\|K^*x\|^2.
\]
Its transformed synthesis operator is \(SK\). If every \(K\)-frame is preserved, then this particular transformed family is a \(K\)-frame, and the range characterization forces
\[
R(K)\subseteq R(SK)=S R(K).
\]

Finally, Douglas factorization gives
\[
\eta(S,K)>0\iff R(K)\subseteq R(SK).
\]
For any source \(K\)-frame with lower bound \(A\),
\[
\sum_i|\langle x,Sf_i\rangle|^2
=\sum_i|\langle S^*x,f_i\rangle|^2
\ge A\|K^*S^*x\|^2
\ge A\eta(S,K)\|K^*x\|^2.
\]
The upper bound is at most \(B\|S\|^2\|x\|^2\). Sharpness of the universal lower multiplier follows by testing the Parseval \(K\)-frame \((Ke_i)\), whose transformed frame operator is exactly \(SKK^*S^*\).

## Verification
The target preprint was inspected in full at arXiv:2102.05255v1. Its Theorem 3.8 states the positive-operator preservation claim, and the proof explicitly asserts \((I+U)S_F(I+U)^*\ge S_F\) from positivity of \(S_F\) and \(U\). The same paper records the synthesis-range characterization used in the repair. The counterexample is symbolic and finite-dimensional; the matrix witnessing failure has determinant \(-1\).

## Relationship to prior work
The range characterization of \(K\)-frames is classical and is already quoted by the target paper. The contribution here is not that characterization itself, but its use to identify the exact universal condition for the positive atomwise transform in Theorem 3.8, together with the explicit failure of the printed theorem and the sharp universal lower multiplier \(\eta(S,K)\).

A 2024 paper on weaving \(K\)-frames in \(n\)-Hilbert spaces uses the same general \(K\)-frame framework and cites the 2021 source, but its inspected definitions and stability section do not state this positive-transform correction. Search results for later construction papers were also compared at the implication level; no checked source supplied the source-specific counterexample or the universal criterion above.

## Limitations
The result does not claim that \(R(K)\subseteq S R(K)\) is necessary for one particular \(K\)-frame; for a fixed synthesis operator \(V\), the exact condition is the weaker statement \(R(K)\subseteq S R(V)\). The universal criterion concerns preservation of every \(K\)-frame for the same \(K\). An unindexed erratum or thesis note could contain the same correction.

## References
1. P. Ghosh and T. K. Samanta, *Some properties of K-frame in n-Hilbert space*, arXiv:2102.05255v1, 10 February 2021.
2. G. Wang, *Some properties of weaving K-frames in n-Hilbert space*, AIMS Mathematics 9 (2024), 25438--25456, doi:10.3934/math.20241242.
3. L. Găvruţa, *Frames for operators*, Applied and Computational Harmonic Analysis 32 (2012), 139--144, doi:10.1016/j.acha.2011.07.006.
