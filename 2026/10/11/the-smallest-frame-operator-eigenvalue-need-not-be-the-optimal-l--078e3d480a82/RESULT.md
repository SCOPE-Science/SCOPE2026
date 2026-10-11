# The smallest frame-operator eigenvalue need not be the optimal lower K-frame bound

## Finding
A finite-dimensional \(K\)-frame paper claims that if its positive frame operator \(S\) has eigenvalues
\[
\lambda_1\ge\cdots\ge\lambda_N>0,
\]
then
\[
\frac{\lambda_N}{\|K\|^2}
\]
is the optimal lower \(K\)-frame bound. The proof shows that this is a lower bound, but not that it is optimal.

Take
\[
H=\mathbb C^2,
\qquad
K=\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad
\Phi=\{2e_1,e_2\}.
\]
The frame operator is
\[
S=\begin{pmatrix}4&0\\0&1\end{pmatrix}=KK^*.
\]
Therefore, for every \(x=(x_1,x_2)\),
\[
\sum_{\phi\in\Phi}|\langle x,\phi\rangle|^2
=4|x_1|^2+|x_2|^2
=\|K^*x\|^2.
\]
Thus \(\Phi\) is a Parseval \(K\)-frame and its optimal lower \(K\)-frame bound is exactly \(1\). The published expression gives
\[
\frac{\lambda_{\min}(S)}{\|K\|^2}=\frac14.
\]

The exact finite-dimensional formula, whenever \(S\) is positive definite, is
\[
A_{\mathrm{opt}}=\frac{1}{\|S^{-1/2}K\|^2}.
\]
The source's value is optimal precisely when a vector simultaneously realizes the smallest eigenvalue of \(S\) and the largest eigenvalue of \(KK^*\).

## Assumptions and scope
Let \(H\) be finite dimensional, let \(K\ne0\), and let \(\Phi\) be a \(K\)-frame whose ordinary frame operator \(S\) is positive definite, as in the hypothesis of the disputed proposition.

The optimal lower \(K\)-frame bound means the largest \(A>0\) such that
\[
A\|K^*x\|^2\le\langle Sx,x\rangle
\]
for all \(x\in H\).

The finding does not dispute that \(\lambda_{\min}(S)/\|K\|^2\) is always a valid lower bound. It disputes only the assertion that this bound is always optimal.

## Proof
The lower \(K\)-frame inequality is equivalent to the operator inequality
\[
A K K^*\le S.
\]
Because \(S\) is positive definite, conjugating by \(S^{-1/2}\) gives
\[
A(S^{-1/2}K)(S^{-1/2}K)^*\le I.
\]
For a positive operator \(Q\), the largest \(A\) satisfying \(AQ\le I\) is \(1/\|Q\|\). Since
\[
\|(S^{-1/2}K)(S^{-1/2}K)^*\|=\|S^{-1/2}K\|^2,
\]
we obtain
\[
A_{\mathrm{opt}}=\frac{1}{\|S^{-1/2}K\|^2}.
\]
Equivalently,
\[
A_{\mathrm{opt}}
=\inf_{K^*x\ne0}
\frac{\langle Sx,x\rangle}{\|K^*x\|^2}.
\]

The published estimate follows from the two inequalities
\[
\langle Sx,x\rangle\ge\lambda_{\min}(S)\|x\|^2
\]
and
\[
\|K^*x\|^2\le\|K\|^2\|x\|^2.
\]
Thus
\[
A_{\mathrm{opt}}\ge\frac{\lambda_{\min}(S)}{\|K\|^2}.
\]

Because the problem is finite dimensional, equality in this estimate occurs exactly when some nonzero minimizer saturates both inequalities. This is equivalent to
\[
Sx=\lambda_{\min}(S)x
\]
and
\[
KK^*x=\|K\|^2x.
\]
Hence the published estimate is optimal exactly when
\[
E_{\lambda_{\min}(S)}(S)\cap E_{\|K\|^2}(KK^*)\ne\{0\}.
\]

For the displayed counterexample, \(S=KK^*\), so the frame identity itself gives \(A_{\mathrm{opt}}=1\). But the smallest eigenspace of \(S\) is \(\operatorname{span}\{e_2\}\), while the top eigenspace of \(KK^*\) is \(\operatorname{span}\{e_1\}\); their intersection is zero, and the published estimate is strictly smaller.

## Verification
The primary article was inspected at Proposition 2.3 and its complete proof. The proposition labels \(\lambda_N/\|K\|^2\) as the optimal lower bound. The proof derives only the inequality
\[
\frac{\lambda_N}{\|K\|^2}\|K^*x\|^2\le\langle Sx,x\rangle,
\]
with no argument that a vector attains equality.

The two-dimensional witness was checked symbolically. It uses a Parseval \(K\)-frame, so there is no numerical optimization or approximation: the exact optimal bound is forced to be \(1\).

A 2021 article on finite \(K\)-frames was also inspected and repeats the same statement as its Proposition 4.7.

## Relationship to prior work
General operator-factorization theory already shows that optimal \(K\)-frame constants are governed by an operator inequality rather than by unrelated spectral extrema. Later literature on canonical \(K\)-duals likewise treats optimal lower bounds through minimal operator norms.

A 2020 Chinese-language paper by Fu and Zhu is identified in later primary literature as obtaining optimal \(K\)-frame bounds and canonical \(K\)-duals. Its full theorem text was not available in the bounded source inspection, so no claim is made that the abstract formula above is new in isolation.

The new source-specific point established here is that Proposition 2.3(i)'s eigenvalue quotient is not generally optimal, together with the exact finite-dimensional equality criterion explaining when that quotient does become optimal. Indexed searches for the proposition, its formula, generalized-eigenvalue variants, and corrections did not locate a source stating this counterexample or equality criterion.

## Limitations
The exact formula \(A_{\mathrm{opt}}=1/\|S^{-1/2}K\|^2\) is stated only under the positive-definiteness hypothesis used by the source proposition. More general \(K\)-frames can have singular frame operators and require restriction or pseudoinverse formulations.

No claim is made that every later paper repeating or citing the proposition is incorrect beyond the specific repeated optimality statement inspected here.

An unindexed correction or inaccessible source may already contain the same counterexample or equality criterion.

## References
1. V. R. Morshedi, M. Janfada and R. Kamyabi Gol, *Frame for operators in finite dimensional hilbert space*, Tamkang Journal of Mathematics 49(1) (2018), 35--48, DOI 10.5556/j.tkjm.49.2018.2383.
2. G. Upenderreddy and N. Kiran Kumar, *Finite K-frames in Hilbert spaces*, Journal of Mathematical and Computational Science 11(5) (2021), 6468--6480, DOI 10.28919/jmcs/6386.
3. Y. K. Fu and Y. C. Zhu, *Canonical K-dual Bessel sequence of a K-frame*, Acta Mathematica Sinica, Chinese Series 50 (2020), 287--300.
