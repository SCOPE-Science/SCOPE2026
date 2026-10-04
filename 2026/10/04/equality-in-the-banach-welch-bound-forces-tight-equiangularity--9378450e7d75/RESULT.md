# Equality in the Banach Welch bound forces tight equiangularity
## Finding
Let \(X\) be a \(d\)-dimensional real or complex Banach space, let \(n\ge d\) with \(n\ge2\), and let
\[
(\{f_j\}_{j=1}^n,\{\tau_j\}_{j=1}^n)
\]
be an approximate Schauder frame with \(\|f_j\|=\|\tau_j\|=1\) and \(f_j(\tau_j)=1\) for every \(j\). Assume its frame operator
\[
Sx=\sum_{j=1}^n f_j(x)\tau_j
\]
is diagonalizable and all its eigenvalues are nonnegative. Define
\[
M=\max_{j\ne k}|f_j(\tau_k)|,
\qquad
\gamma=\sqrt{\frac{n-d}{d(n-1)}}.
\]
If \(M=\gamma\), then
\[
S=\frac nd I_X
\]
and
\[
|f_j(\tau_k)|=\gamma\qquad(j\ne k).
\]
Hence equality in the first-order Banach Welch bound forces both tightness and constant off-diagonal modulus. For \(n=d\), the statement becomes \(M=0\), \(S=I_X\), and all off-diagonal pairings vanish. In the squared-modulus convention appearing in Definition 3.9 of the motivating source, the corresponding equiangular parameter is \(\gamma^2=(n-d)/(d(n-1))\).

## Assumptions and scope
An approximate Schauder frame here means that \(S\) is invertible. Consequently \(n\ge d\). The statement uses exactly the normalization and spectral assumptions of the motivating first-order Banach Welch bound. The result concerns equality in the maximum-correlation inequality; it does not assert existence of equality cases for every \((d,n,X)\), nor does it classify all tight equiangular systems in a fixed Banach norm.

## Proof
Write
\[
a_{jk}=f_j(\tau_k).
\]
The trace of the frame operator is
\[
\operatorname{tr}S=\sum_{j=1}^n f_j(\tau_j)=n.
\]
If \(\lambda_1,\ldots,\lambda_d\ge0\) are the eigenvalues of \(S\), then
\[
\operatorname{tr}(S^2)=\sum_{r=1}^d\lambda_r^2
=\sum_{j,k=1}^n a_{jk}a_{kj}
=n+\sum_{j\ne k}a_{jk}a_{kj}.
\]
Cauchy--Schwarz gives
\[
\frac{n^2}d\le \operatorname{tr}(S^2).
\]
Since \(\operatorname{tr}(S^2)-n\) is real and nonnegative,
\[
\frac{n^2}d-n
\le
\operatorname{tr}(S^2)-n
=
\left|\sum_{j\ne k}a_{jk}a_{kj}\right|
\le
\sum_{j\ne k}|a_{jk}a_{kj}|
\le
n(n-1)M^2.
\]
When \(M=\gamma\), the first and last expressions are equal because
\[
n(n-1)\gamma^2=\frac{n^2}d-n.
\]
Therefore every inequality in the chain is an equality. Equality in Cauchy--Schwarz yields
\[
\lambda_1=\cdots=\lambda_d=\frac nd.
\]
Because \(S\) is diagonalizable, this forces \(S=(n/d)I_X\).

Also,
\[
\sum_{j\ne k}|a_{jk}a_{kj}|=n(n-1)M^2.
\]
There are exactly \(n(n-1)\) ordered pairs \((j,k)\) with \(j\ne k\), and every term satisfies \(|a_{jk}a_{kj}|\le M^2\). Hence every term equals \(M^2\). If \(M>0\), then \(|a_{jk}|\le M\), \(|a_{kj}|\le M\), and \(|a_{jk}a_{kj}|=M^2\) force
\[
|a_{jk}|=|a_{kj}|=M.
\]
If \(M=0\), the same conclusion is immediate. Thus \(|f_j(\tau_k)|=\gamma\) for all \(j\ne k\).

## Verification
The proof is symbolic and finite-dimensional; no numerical experiment or finite search is used to establish the theorem. The critical identities were independently recomputed from the rank-one expansion \(S=\sum_j \tau_j\otimes f_j\): \(\operatorname{tr}S=n\) and \(\operatorname{tr}(S^2)=\sum_{j,k}f_j(\tau_k)f_k(\tau_j)\). The equality case was checked at both boundaries: \(n>d\), where \(\gamma>0\), and \(n=d\), where \(\gamma=0\).

## Relationship to prior work
Krishna's paper proves the Banach-space Welch inequality and states Question 3.12(i), asking whether equality in its first-order maximum-correlation bound forces equiangularity. The argument above supplies that missing implication and, in fact, also forces the frame operator to be tight. The classical Hilbert-space result of Waldron identifies Welch-bound-equality vector sequences with tight frames, but it does not treat the Banach dual-pair setting where \(f_j\) and \(\tau_j\) are independent objects. A 2026 preprint by Zeraoulia and Menasri classifies normalized equiangular tight systems only in complex \(\ell_\infty^2\) and \(\ell_1^2\); it assumes tight equiangularity and therefore does not imply the general equality-case theorem here.

## Limitations
The theorem retains the motivating source's hypothesis that \(S\) is diagonalizable with nonnegative eigenvalues. It does not address the continuous analogue, higher-order symmetric-tensor Welch bounds, or the existence problem for equality cases. The source uses two nearby conventions for the equiangular parameter; to avoid ambiguity, the claim is stated directly in terms of the off-diagonal modulus \(M\), with the squared-modulus translation recorded explicitly.

## References
1. K. Mahesh Krishna, *Discrete and Continuous Welch Bounds for Banach Spaces with Applications*, arXiv:2201.00980, first submitted 2022-01-04; Journal of Classical Analysis 22 (2023), 81--111, doi:10.7153/jca-2023-22-07.
2. S. Waldron, *Generalized Welch Bound Equality Sequences Are Tight Frames*, IEEE Transactions on Information Theory 49 (2003), 2307--2309, doi:10.1109/TIT.2003.815788.
3. R. Zeraoulia and M. Abdellah, *Equiangular Finite Unit-Norm Tight Systems in Complex \(\ell_\infty^2\) and \(\ell_1^2\)*, Preprints.org 202608.1175, posted 2026-08-18.
