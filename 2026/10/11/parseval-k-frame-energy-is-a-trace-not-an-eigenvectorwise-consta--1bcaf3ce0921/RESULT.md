# Parseval \(K\)-frame energy is a trace, not an eigenvectorwise constant

## Finding
Sadri--Rahimlou Proposition 2.2 asserts that if \(F=\{f_j\}\) is a Parseval \(K\)-frame on an \(n\)-dimensional Hilbert space and \(S\) is its frame operator, then every eigenvalue of \(S\) is positive and, for an orthonormal eigenbasis \(\{e_k\}_{k=1}^n\),
\[
n\|K^*e_k\|^2=\sum_j\|f_j\|^2
\]
for every \(k\).

Both assertions fail for general \(K\)-frames.

Let
\[
H=\mathbb C^2,\qquad
K=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
F=\{e_1\}.
\]
For every
\[
x=(x_1,x_2),
\]
\[
\sum_{f\in F}|\langle x,f\rangle|^2
=
|x_1|^2
=
\|K^*x\|^2.
\]
Hence \(F\) is a Parseval \(K\)-frame.

Its frame operator is
\[
S=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
=
KK^*.
\]
Thus its eigenvalues are \(1\) and \(0\), contradicting the claimed strict positivity. Also,
\[
\sum_{f\in F}\|f\|^2=1,
\]
but
\[
2\|K^*e_1\|^2=2
\]
and
\[
2\|K^*e_2\|^2=0.
\]
Neither equals the total frame energy.

The correct invariant is the trace:
\[
\sum_j\|f_j\|^2
=
\operatorname{tr}(KK^*)
=
\sum_{k=1}^n\|K^*e_k\|^2.
\]
The source's eigenvectorwise equality holds for every \(k\) exactly when
\[
KK^*=cI.
\]

## Assumptions and scope
The result concerns finite-dimensional Parseval \(K\)-frames in the sense used by the source:
\[
\sum_j|\langle x,f_j\rangle|^2=\|K^*x\|^2
\]
for every \(x\).

The counterexample is two-dimensional and finite, so convergence, measurability, and closed-range issues do not arise.

The equality criterion
\[
KK^*=cI
\]
is stated for the simultaneous validity of the source's displayed identity for every member of an orthonormal eigenbasis. It does not claim that a single chosen eigenvector cannot accidentally have the mean eigenvalue.

## Proof
For a Parseval \(K\)-frame, the frame operator satisfies
\[
S=KK^*.
\]
Let
\[
Se_k=\lambda_ke_k
\]
for an orthonormal eigenbasis. Then
\[
\lambda_k
=
\langle Se_k,e_k\rangle
=
\langle KK^*e_k,e_k\rangle
=
\|K^*e_k\|^2.
\]
Therefore
\[
\lambda_k\ge0.
\]
It is strictly positive for every \(k\) exactly when
\[
\ker K^*=\{0\}.
\]
In finite dimension, this is equivalent to invertibility of \(K\).

The trace of the frame operator is
\[
\operatorname{tr}(S)
=
\sum_{k=1}^n\lambda_k.
\]
For a finite-dimensional Bessel family,
\[
\operatorname{tr}(S)
=
\sum_j\|f_j\|^2.
\]
Consequently,
\[
\sum_j\|f_j\|^2
=
\sum_{k=1}^n\lambda_k
=
\sum_{k=1}^n\|K^*e_k\|^2.
\]

Now suppose the source's stronger identity holds for every \(k\):
\[
n\|K^*e_k\|^2
=
\sum_j\|f_j\|^2.
\]
Since the right-hand side is independent of \(k\), every eigenvalue satisfies
\[
\lambda_k
=
\frac{\operatorname{tr}(KK^*)}{n}.
\]
Hence all eigenvalues of the self-adjoint operator \(KK^*\) are equal, so
\[
KK^*=cI,
\qquad
c=\frac{\|K\|_{\mathrm{HS}}^2}{n}.
\]
Conversely, if
\[
KK^*=cI,
\]
then every eigenvalue equals \(c\), the total energy is \(nc\), and the displayed identity holds for every \(k\).

## Verification
The first public preprint record was checked independently and is dated 23 April 2021. The later open-access journal full text was inspected at Definition 2.2, Remark 2.1, Proposition 2.2, its complete proof, and the immediate equal-norm consequence.

The source itself notes before Proposition 2.2 that a \(K\)-frame operator need not be invertible. Proposition 2.2 nevertheless infers strict positivity of all eigenvalues from
\[
\|K^*f\|^2=\lambda_k\|f\|^2,
\]
which does not exclude
\[
K^*f=0.
\]

The trace identity used by the source is valid. The error is replacing the sum of the eigenvalues by \(n\) times each individual eigenvalue without a hypothesis forcing a flat spectrum.

All computations in the counterexample and the equality classification are exact.

## Relationship to prior work
The paper's trace identity is the standard finite-dimensional frame-energy identity and remains valid for Parseval \(K\)-frames because their frame operator is \(KK^*\).

A related 2024 paper on continuous Parseval \(K\)-frames was checked as broader literature. Its displayed Proposition 2.2 concerns construction of a \(K\)-dual, not the eigenvaluewise identity corrected here.

The same 2022 source has another independently identified issue concerning its later subspace-correspondence theorem. That different result concerns dependence on a choice of unitary representation and does not imply the spectral failure in Proposition 2.2.

Targeted searches for the exact proposition, eigenvalue positivity, the trace/eigenvector formulation, and the scalar-\(KK^*\) equality condition did not locate an indexed correction of Proposition 2.2.

## Limitations
The result does not reassess the paper's other theorems. In particular, it does not infer failure of every downstream statement that cites Proposition 2.2; each such use would require its own hypotheses to be checked.

The criterion
\[
KK^*=cI
\]
characterizes the simultaneous eigenvectorwise identity. It is not asserted as a necessary condition for unrelated equal-norm \(K\)-frame constructions.

An unindexed correction or informal note may contain the same observation.

## References
1. V. Sadri and G. Rahimlou, *Equal-norm parseval \(K\)-frames in Hilbert Spaces*, arXiv:2104.11656v1, first public version 23 April 2021.
2. V. Sadri and G. Rahimlou, *Equal-norm Parseval \(K\)-frames in Hilbert spaces with a new inequality*, Journal of Inequalities and Applications 2022, 127, DOI 10.1186/s13660-022-02862-5.
3. H. Massit and M. Rossafi, *Equal-norm Parseval continuous \(K\)-frames in Hilbert spaces*, Annals of Mathematics and Computer Science 22 (2024), 45--53, DOI 10.56947/amcs.v22.281.
