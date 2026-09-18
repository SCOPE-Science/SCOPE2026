# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The central identity follows entrywise from the tridiagonal inverse covariance:
\[
T_N(\rho)=\rho T_N(1)+(1-\rho)^2I+\rho(1-\rho)(e_0e_0^T+e_{N-1}e_{N-1}^T).
\]
The orthonormal DCT-II diagonalizes \(T_N(1)\). Its two boundary columns differ rowwise by the sign \((-1)^n\), so the two boundary rank-one terms cancel exactly between opposite-parity DCT indices and double on equal-parity indices. This proves the two diagonal-plus-rank-one correction blocks for every \(N\ge2\). Standard rank-one secular theory then gives the Cauchy eigenvector form and strict within-parity interlacing.

For odd \(N=2M+1\), direct substitution into the standard DCT-II parity split gives DCT-VI on the symmetric branch and DCT-VIII on the antisymmetric branch. Independent numerical checks over \(2\le N\le16\) and several interior correlations found only roundoff-scale residuals for the transformed identity, parity decoupling, orthogonality, and diagonalization; separate odd-size checks verify the DCT-VI/DCT-VIII split through \(N=17\).

Adversarial checks included the smallest odd case \(N=3\), correlations near both endpoints, row-ordering after correction, and the distinction between an exact algebraic factorization and tolerance-controlled accelerated application. No step of the proof relies on the numerical experiment.

## Originality

The closest source is arXiv:2609.20221. Its abstract, Lemma 4.1, and Theorem 4.2 restrict the fixed-core diagonal-plus-rank-one construction to even \(N\), using DCT-II and DCT-IV half-size cores. Searches for odd-order AR(1) KLT factorizations, DCT-VI/DCT-VIII corrections, parity-separated rank-one DCT corrections, and equivalent Kac–Murdock–Szegő formulations did not locate an earlier statement of the all-order identity above.

The most important overlapping source is arXiv:2608.06522. It already gives an exact all-order KLT algorithm and therefore dominates any claim of first fast exact treatment of odd sizes. Its odd-order theorem, however, uses a one-sided residual KLT recursively in both parity branches plus an arrowhead diagonalizer. Its \(\rho\to1\) limit recovers the DCT-VI/DST-VII split. The present contribution is narrower: the explicit nonrecursive fixed-DCT, rank-one correction representation for odd order and the unified all-order DCT-II conjugation identity.

A wording in arXiv:2608.06522 describes the companion conference work broadly as a fixed-DCT nonrecursive route. That creates a genuine simultaneous-work risk. The available companion paper arXiv:2609.20221 nevertheless states and proves its fixed-core construction only for even \(N\), and no odd-order formula was found there. Originality is therefore assessed as PASS only in the limited, to-the-best-of-our-knowledge sense above.

Reznik's 2013 ICASSP paper gives the fixed DCT-II/DCT-VI/DST-VII transform relationship; it does not supply the \(\rho\)-dependent AR(1) rank-one correction result. Torun–Akansu (2013) was inspected through its full text: it derives the explicit AR(1) KLT kernel from the classical eigenfrequency/root equations and contains no fixed-DCT factorization language matching the present result.

## Value

The result completes the recent even-order fixed-core theory at odd lengths without introducing a new recursive transform family. It replaces the published odd residual-KLT-plus-arrowhead representation by the same computational primitive used in the even case: fixed fast trigonometric cores plus diagonal-plus-rank-one secular corrections. This does not improve the known asymptotic complexity, but it materially simplifies the all-order structure and permits one uniform correction implementation across transform lengths.

## Limitations

The theorem treats \(0<\rho<1\), exact real arithmetic at the algebraic level, and stationary AR(1) covariances. The accelerated Cauchy-matrix application discussed in the source literature is approximate to prescribed numerical tolerance; no new stability theorem for FMM/HSS implementations is claimed. Negative correlations, nonstationary models, AR(p) with \(p>1\), and finite-precision backward error are outside scope.
