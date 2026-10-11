# Approximate \(K\)-duality needs generalized-inverse-scaled error

## Finding
Sun--Li Lemma 19 asserts that an approximate \((K,K^*)\)-dual Bessel pair automatically makes
\[
K^\dagger T_FR_G
\]
invertible when \(K\) is injective, has a generalized inverse \(K^\dagger\), and satisfies \(\|K\|>1\). Proposition 20 then uses this invertibility to conclude that \(G\) is a \(K\)-frame.

Both conclusions fail under the printed hypotheses.

Take
\[
X=\mathbb R^2,\qquad X_d=\ell^2,
\]
with the Euclidean norm, and set
\[
K=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix},
\qquad
K^\dagger=K^{-1}=
\begin{pmatrix}
1/2&0\\
0&2
\end{pmatrix}.
\]
Thus \(K\) is injective and invertible, \(\|K\|=2>1\), and \(K^\dagger\) is its generalized inverse.

Let \(e_1,e_2\) be the standard basis and \(e_1^*,e_2^*\) the coordinate functionals. Define
\[
f_1=e_1,\qquad f_2=e_2,\qquad f_i=0\quad(i\ge3),
\]
and
\[
g_1=2e_1^*,\qquad g_i=0\quad(i\ge2).
\]
These are Bessel sequences in the source's Banach-frame sense. Their mixed reconstruction operators are
\[
T_FR_G=
\begin{pmatrix}
2&0\\
0&0
\end{pmatrix}
\]
on \(X\), and
\[
T_GR_F=
\begin{pmatrix}
2&0\\
0&0
\end{pmatrix}
\]
on \(X^*\). Since \(K^*=K\) under the standard Euclidean identification,
\[
\|K-T_FR_G\|
=
\|K^*-T_GR_F\|
=
\frac12<1.
\]
Therefore \((F,G)\) is an approximate \((K,K^*)\)-dual pair according to Definition 18.

However,
\[
K^\dagger T_FR_G
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\]
which is not invertible. This disproves Lemma 19.

The same example disproves Proposition 20. For \(x=e_2\),
\[
R_Ge_2=0,
\]
while
\[
\|Ke_2\|=\frac12.
\]
Hence no positive constant \(A\) can satisfy
\[
A\|Kx\|\le \|R_Gx\|
\]
for every \(x\), so \(G\) is not a \(K\)-frame.

The missing quantity is the norm of the generalized inverse. A valid sufficient repair is
\[
\boxed{
\|K^\dagger\|\,\|K-T_FR_G\|<1.
}
\]
In the displayed counterexample the product equals exactly \(1\), and singularity occurs.

## Assumptions and scope
The counterexample is finite-dimensional and uses \(X_d=\ell^2\), whose canonical basis has all of the sequence-space properties assumed in the source. No issue of convergence, weak topology, closed range, or existence of a generalized inverse is involved.

The second approximate-duality inequality on \(X^*\) is also satisfied exactly, so the failure does not arise from checking only one side of Definition 18.

The repaired condition is a universal sufficient condition for the Neumann-series argument. It is sharp in the sense that equality of the norm product can already produce a singular operator. It is not claimed to be a necessary condition for invertibility in every individual example.

## Proof
The sequence \(F\) is Bessel because, for \(x^*=(u,v)\in X^*\),
\[
\big\|(\langle f_i,x^*\rangle)_i\big\|_{\ell^2}
=
\sqrt{u^2+v^2}
=
\|x^*\|.
\]
The sequence \(G\) is Bessel because, for \(x=(x_1,x_2)\in X\),
\[
\big\|(g_i(x))_i\big\|_{\ell^2}
=
2|x_1|
\le
2\|x\|.
\]

The analysis map of \(G\) is
\[
R_G(x_1,x_2)=(2x_1,0,0,\ldots),
\]
and the synthesis map of \(F\) sends
\[
(c_i)_i
\longmapsto
c_1e_1+c_2e_2.
\]
Thus
\[
T_FR_G(x_1,x_2)=(2x_1,0).
\]
The dual mixed operator has the same diagonal matrix, because \(F\) is the standard coordinate pair and \(G\) has only the first coordinate functional:
\[
T_GR_F(u,v)=(2u,0).
\]
Consequently,
\[
K-T_FR_G
=
K^*-T_GR_F
=
\begin{pmatrix}
0&0\\
0&1/2
\end{pmatrix},
\]
whose norm is \(1/2\).

Multiplying by \(K^\dagger\) gives
\[
K^\dagger T_FR_G
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\]
so the claimed inverse does not exist.

For the repair, let \(K\) be injective and let \(K^\dagger\) be a generalized inverse. The generalized-inverse identity
\[
KK^\dagger K=K
\]
implies
\[
K(K^\dagger K-I)=0.
\]
Injectivity of \(K\) therefore yields
\[
K^\dagger K=I.
\]
Writing \(A=T_FR_G\),
\[
I-K^\dagger A
=
K^\dagger(K-A),
\]
so
\[
\|I-K^\dagger A\|
\le
\|K^\dagger\|\,\|K-A\|.
\]
If the right-hand side is strictly below \(1\), the Neumann lemma makes \(K^\dagger A\) invertible.

Put
\[
S=K^\dagger T_FR_G.
\]
Then
\[
x=S^{-1}K^\dagger T_FR_Gx.
\]
Hence
\[
\|Kx\|
\le
\|K\|\,\|S^{-1}K^\dagger T_F\|\,\|R_Gx\|.
\]
Since \(T_F\) is bounded, this supplies a positive lower \(K\)-frame bound for \(G\), while its Bessel property supplies the upper bound. Thus the repaired smallness condition also restores the intended Proposition 20 conclusion.

## Verification
The full publisher text was inspected at Definition 18, Lemma 19, Proposition 20, and the Neumann lemma cited by the proof. Definition 18 assumes only that the two reconstruction errors are less than \(1\). Lemma 19 then estimates the defect of \(K^\dagger T_FR_G\) by multiplying one of those errors by \(\|K^\dagger\|\), but no hypothesis bounds that product below \(1\).

The displayed matrices verify every premise directly. In particular,
\[
\|K^\dagger\|=2,
\qquad
\|K-T_FR_G\|=\frac12,
\]
so the proof's Neumann defect estimate reaches \(1\), and the resulting operator is indeed singular.

The argument is exact and symbolic. No numerical experiment or finite search is used as evidence for an infinite-dimensional conclusion.

## Relationship to prior work
Approximate dual frames were introduced in the Hilbert-space setting as a controlled near-reconstruction concept, where a reconstruction operator close enough to the identity is invertible by a Neumann-series argument. Sun--Li adapt this idea to reconstruction near a general operator \(K\).

The change from the identity to \(K\) introduces the conditioning factor \(K^\dagger\): closeness of \(T_FR_G\) to \(K\) by an absolute error below \(1\) does not imply that \(K^\dagger T_FR_G\) is close to the identity by less than \(1\). The correct dimensionless perturbation quantity is
\[
\|K^\dagger\|\,\|K-T_FR_G\|.
\]

Targeted searches for the exact source, Lemma 19, Proposition 20, generalized-inverse scaling, and approximate \((K,K^*)\)-duality did not locate an indexed correction or a source-specific counterexample. Related results on ordinary approximate dual frames use identity-centered reconstruction and therefore do not cover this generalized-inverse obstruction.

## Limitations
The repaired inequality is sufficient and sharp as a universal norm-product threshold, but it is not necessary for every invertible \(K^\dagger T_FR_G\).

The finding concerns Lemma 19 and Proposition 20. Later statements in the source that invoke the same inverse would need to be reconsidered under a corrected hypothesis, but no separate claim about them is made here.

An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. B. Sun and C. Li, *K-frames for Banach Spaces*, Journal of Function Spaces 2022, Article ID 6385365, DOI 10.1155/2022/6385365, first published 8 April 2022.
2. O. Christensen and R. S. Laugesen, *Approximately dual frame pairs in Hilbert spaces and applications to Gabor frames*, arXiv:0811.3588.
