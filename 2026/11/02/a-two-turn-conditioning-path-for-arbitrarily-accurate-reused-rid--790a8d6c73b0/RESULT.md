# A two-turn conditioning path for arbitrarily accurate reused ridge sketches

## Finding

The spectral condition number of a partly exact, Cholesky-preconditioned ridge least-squares system need not be monotone or even unimodal as the regularization parameter varies, **even for an arbitrarily accurate subspace embedding**. The following explicit two-column example has exactly one strict interior local minimum followed by one strict interior local maximum, for every positive sketch-perturbation strength.

Let
\[
G=\begin{pmatrix}4&0\\0&1\end{pmatrix},\qquad
D=\begin{pmatrix}5&1/4\\1/4&2\end{pmatrix},\qquad H_t=G+tD\quad(t>0).
\]
Take a full-column-rank real matrix \(A\) with \(A^{\mathsf T}A=G\), a sketch \(X\) satisfying \((XA)^{\mathsf T}(XA)=H_t\), and, for each \(\lambda\geq0\), the augmented matrix \(B_\lambda=[A;\sqrt\lambda I_2]\) and an upper triangular Cholesky factor \(R_\lambda\) satisfying
\[
R_\lambda^{\mathsf T}R_\lambda=H_t+\lambda I_2.
\]
Writing \(K_t(\lambda)=\kappa_2(B_\lambda R_\lambda^{-1})\), define
\[
U(\lambda)=(\lambda+4)(\lambda+1),\qquad
P(\lambda)=37\lambda^2-67\lambda+40,\qquad
W_t(\lambda)=2U(\lambda)+t(7\lambda+13).
\]
Then, for all \(t>0\) and \(\lambda\ge0\),
\[
\boxed{K_t(\lambda)^2=
\frac{W_t(\lambda)+(t/2)\sqrt{P(\lambda)}}
{W_t(\lambda)-(t/2)\sqrt{P(\lambda)}}.}
\]
Both numerator and denominator are positive. The derivative of \(K_t\) has sign opposite to the cubic
\[
\boxed{F_t(\lambda)=148\lambda^3-402\lambda^2-(942+1431t)\lambda+(1336+1431t).}
\]
It has precisely two positive simple roots, \(\lambda_-(t)\in(1,2)\) and \(\lambda_+(t)>2\), with \(\lambda_-<\lambda_+\). Therefore \(K_t\) decreases strictly until \(\lambda_-\), increases strictly until \(\lambda_+\), then decreases strictly to \(1\) at infinity. The first critical point is a strict local minimum and the second a strict local maximum. Neither a monotonicity nor a unimodality assertion for this ridge-path condition number follows solely from small embedding distortion.

The example persists under arbitrarily accurate sketching: for every \(\delta>0\), choose \(t>0\) sufficiently small that
\[
\left\|G^{-1/2}(H_t-G)G^{-1/2}\right\|_2<\delta.
\]
For a fixed matrix \(A\) as above, an iid Gaussian sketch \(X\) with two rows produces a condition-number path with at least the same two strict turning-point types and embedding error below \(\delta\) with strictly positive probability. This is an existence-and-support statement, not a high-probability failure claim.

## Assumptions and scope

The statement concerns exact real arithmetic, an overdetermined two-column ridge problem, the *partly exact* Cholesky preconditioner obtained from one fixed sketch reused across all values of \(\lambda\), and the spectral (two-norm) condition number of the augmented right-preconditioned matrix. A fully explicit realization takes \(m=6\) and
\[
A=\begin{pmatrix}2&0\\0&1\\0&0\\0&0\\0&0\\0&0\end{pmatrix}\in\mathbb R^{6\times2},
\]
so \(A^{\mathsf T}A=G\). Put \(L_t=\operatorname{chol}(H_t)\) in lower-triangular convention and take \(X\in\mathbb R^{2\times6}\) with its leading \(2\times2\) block \(L_t^{\mathsf T}\operatorname{diag}(1/2,1)\) and its other entries zero. Then \(XA=L_t^{\mathsf T}\) and \((XA)^{\mathsf T}(XA)=H_t\). The resulting sketch size is \(s=2<m=6\). Positive definiteness is immediate because \(G\) is positive definite and \(D\) has positive leading principal minors (\(5\) and \(159/16\)).

The standard algorithm is defined for positive ridge parameters; the value at \(\lambda=0\) is included only as a continuous, nonsingular endpoint in this example. Gaussian sketches may have any nondegenerate independent entry distribution, including the conventional scaled normal distribution; only full support is used for the final probability statement.

## Proof

**1. Reduce the preconditioned condition number to a two-by-two positive-definite pencil.** The nonzero squared singular values of \(B_\lambda R_\lambda^{-1}\) are the eigenvalues of
\[
R_\lambda^{-\mathsf T}(G+\lambda I_2)R_\lambda^{-1}.
\]
Their reciprocals are the eigenvalues of
\[
C_\lambda=(G+\lambda I_2)^{-1/2}(H_t+\lambda I_2)(G+\lambda I_2)^{-1/2}=I_2+tJ_\lambda,
\]
where
\[
J_\lambda=\begin{pmatrix}
5/(\lambda+4)&1/[4\sqrt{U(\lambda)}]\\
1/[4\sqrt{U(\lambda)}]&2/(\lambda+1)
\end{pmatrix}.
\]
The squared condition number is therefore exactly the ratio of the larger and smaller eigenvalues of \(C_\lambda\). This conclusion is independent of the chosen Cholesky basis.

**2. Compute the two eigenvalues.** Directly,
\[
\operatorname{tr}J_\lambda=\frac{7\lambda+13}{U(\lambda)},\qquad
(\operatorname{tr}J_\lambda)^2-4\det J_\lambda=\frac{P(\lambda)}{4U(\lambda)^2}.
\]
The discriminant of \(P\) is \(-1431\) and its leading coefficient is positive, so \(P\) is strictly positive on the real line. The eigenvalues of \(C_\lambda\) are
\[
1+\frac{t(7\lambda+13)}{2U(\lambda)}\ \pm\ \frac{t\sqrt{P(\lambda)}}{4U(\lambda)}.
\]
Both are positive because \(J_\lambda\) is congruent to the positive-definite \(D\). Their ratio yields the displayed exact formula and shows \(K_t(\lambda)>1\) at every finite nonnegative \(\lambda\).

**3. Differentiate and count every stationary point.** For fixed \(t>0\), the ratio in the finding is strictly increasing as a function of the positive scalar \(\sqrt{P(\lambda)}/W_t(\lambda)\); the condition \(W_t>(t/2)\sqrt P\) follows from positive definiteness. Its derivative has the sign of
\[
P'(\lambda)W_t(\lambda)-2P(\lambda)W_t'(\lambda)=-F_t(\lambda).
\]
The cubic obeys
\[
F_t(0)=1336+1431t>0,\quad F_t(1)=140>0,\quad F_t(2)=-972-1431t<0,
\]
and has positive leading coefficient. Hence it has a root in \((1,2)\) and another in \((2,\infty)\). Its coefficient sign pattern is \((+,-,-,+)\), with exactly two sign changes. By Descartes' rule of signs, it has at most two positive roots counted with multiplicity. The two already located are therefore all the positive roots, both simple. The sign pattern of the cubic, and hence the opposite sign of \(K_t'\), is \((+,-,+)\) across its two roots. This proves strict decrease, increase, decrease, and the two strict turns. Since \(J_\lambda\to0\) as \(\lambda\to\infty\), we have \(K_t(\lambda)\to1\).

**4. Arbitrarily accurate embeddings and Gaussian stability of the phenomenon.** Let \(U_A=A G^{-1/2}\) be a column-orthonormal basis for the range of \(A\). The subspace embedding Gram error is
\[
\|U_A^{\mathsf T}X^{\mathsf T}XU_A-I_2\|_2
=\|G^{-1/2}(H_t-G)G^{-1/2}\|_2
=t\|G^{-1/2}DG^{-1/2}\|_2.
\]
This can be made strictly smaller than any prescribed positive \(\delta\). At the realizing sketch, the derivative \(K_t'\) is strictly negative at \(\lambda=1\), strictly positive at \(\lambda=2\), and strictly negative at a sufficiently large finite point \(L>\lambda_+(t)\). Strict inequalities persist in an open neighborhood of the sketch because the Cholesky factors, distinct generalized eigenvalues, and their derivatives vary continuously with its entries. The derivative sign changes force an interior local minimum between \(1\) and \(2\) and an interior local maximum between \(2\) and \(L\); the signs can be chosen to retain strict, nondegenerate turning points by the implicit-function theorem at the two simple roots. The embedding error also stays below \(\delta\) in a sufficiently small neighborhood. An iid nondegenerate Gaussian matrix has a strictly positive density everywhere on this finite-dimensional matrix space. Hence that neighborhood has strictly positive probability.

## Verification

A standalone script, `verify.py`, checks the exact polynomial derivative identity using symbolic algebra; checks that \(D\) is positive definite; constructs a real sketch realizing \(H_t\); and compares the closed-form condition number with a direct singular-value computation for eight positive perturbation strengths and multiple ridge parameters. It also checks the two real positive stationary roots, local extremal behavior, and the exact scaling of the embedding distortion. All checks passed in the reported environment. The proof above, rather than finite numerical tests, establishes the claim for every \(t>0\) and \(\lambda\ge0\).

For illustration only, at \(t=1\) the two critical parameters are approximately \(1.0512734601\) and \(5.1309714084\). Corresponding condition numbers are approximately \(1.0401613075\) and \(1.0839800834\); the value at the left endpoint is approximately \(1.1638559619\). The phenomenon also persists as \(t\) tends to zero, although all condition numbers approach \(1\).

## Relationship to prior work

Meier and Nakatsukasa (arXiv:2203.07329v1, 2022) introduced the motivating partly exact, Cholesky-based sketch preconditioner for solving many ridge-regularized least-squares problems using one sketch. Their Algorithm 1 gives precisely the Gram factorization studied here. Their Lemma 2 bounds conditioning under a subspace embedding but does not characterize its dependence on the ridge parameter; the bound does not imply monotonicity. The novel assertion here is limited to the exact two-turn path and its persistence with arbitrarily small embedding distortion in a concrete two-column instance; the algorithm, the embedding guarantee, and general eigenvalue theory are not claimed as new.

Meier, Nakatsukasa, Townsend and Webb (arXiv:2302.07202, first posted 2023) study numerical stability and roundoff in sketch-and-precondition least squares rather than the exact-arithmetic ridge-path shape. The classical LSRN paper (arXiv:1109.5981) discusses least-squares preconditioning and a regularized formulation, but not this shifted-Gram cubic classification. Comparison with the general theory of shifted generalized eigenvalue pencils remains a possible priority risk; this report does not assert a comprehensive publication-priority certificate.

## Limitations

The result concerns a constructive two-column family and a fixed reused sketch in exact arithmetic. It does not say Gaussian sketches usually exhibit such turns, nor that the nonmonotone variation has a large amplitude or noticeably degrades iterative performance. For small \(t\), the observed effect necessarily has small amplitude. It also does not extend without further proof to a general number of columns, to finite-precision Cholesky, or to all sketch distributions. The positive-probability statement relies on an open-set/full-support argument, with no quantitative probability lower bound. No independent scientific audit has been performed.

## References

1. M. Meier and Y. Nakatsukasa, *Randomized algorithms for Tikhonov regularization in linear least squares*, arXiv:2203.07329v1, first posted 14 March 2022. https://arxiv.org/html/2203.07329v1 (Algorithm 1, Section 2.1 and Lemma 2).
2. M. Meier, Y. Nakatsukasa, A. Townsend and M. Webb, *Are sketch-and-precondition least squares solvers numerically stable?*, arXiv:2302.07202. https://arxiv.org/html/2302.07202v2 (Sections 1, 2, and 6).
3. X. Meng, M. Saunders and M. W. Mahoney, *LSRN: A Parallel Iterative Solver for Strongly Over- or Underdetermined Systems*, arXiv:1109.5981. https://arxiv.org/abs/1109.5981 (regularization discussion).
