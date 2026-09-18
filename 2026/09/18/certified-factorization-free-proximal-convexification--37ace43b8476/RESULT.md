# Certified sparse-matvec convexification for proximal nonconvex QP

## Result

Consider a real symmetric matrix \(Q\in\mathbb R^{n\times n}\), and suppose a proximal nonconvex-QP method needs a scalar shift \(s=\gamma^{-1}>0\) satisfying
\[
Q+sI\succ0.
\]
PDNQP (Chen--Lu, arXiv:2609.19557v1) states the practical rule
\[
s=-\widehat\lambda_Q+\eta,
\qquad
\eta=\delta_\gamma\max\{1,\|Q\|_\infty\},
\qquad \delta_\gamma=10^{-2},
\]
where \(\widehat\lambda_Q\) is described as an estimate of the smallest eigenvalue obtained by Lanczos iterations.

There are two conclusions.

1. **A finite-step minimum Ritz estimate plus a fixed margin is not a deterministic convexity certificate.** If \(\widehat\lambda_Q\) is the usual smallest Ritz value, then
   \[
   \lambda_{\min}(Q+sI)
   =
   \eta-\bigl(\widehat\lambda_Q-\lambda_{\min}(Q)\bigr).
   \]
   Hence the displayed rule is strongly convex exactly when
   \[
   \widehat\lambda_Q-\lambda_{\min}(Q)<\eta
   \]
   (together with \(s>0\)). For every fixed finite Lanczos depth \(m\), there are symmetric matrices and an open set of starting vectors for which this inequality fails.

2. **The convexification can instead be certified with only sparse matrix-vector products.** Define the signed comparison matrix
   \[
   C(Q)_{ii}=q_{ii},\qquad
   C(Q)_{ij}=-|q_{ij}|\quad(i\ne j).
   \]
   For any \(d>0\),
   \[
   L(d):=\min_i\left(q_{ii}-\sum_{j\ne i}|q_{ij}|\frac{d_j}{d_i}\right)
   \le \lambda_{\min}(Q).
   \]
   These certified lower bounds can be monotonically improved by a nonnegative power iteration and converge to the best possible positive-diagonal-scaling Gershgorin bound
   \[
   \sup_{d>0} L(d)=\lambda_{\min}(C(Q)).
   \]
   Therefore
   \[
   s_k=\eta+\max\{0,-L_k\}
   \]
   guarantees
   \[
   \lambda_{\min}(Q+s_k I)\ge \eta
   \]
   at every iteration. In the genuinely indefinite case \(L_k<0\), this is simply \(s_k=\eta-L_k\), i.e. the PDNQP formula with a certified lower bound in place of an uncertified estimate.

The refinement costs one sparse multiplication by the absolute-off-diagonal comparison operator per step, plus elementwise operations. It preserves the factorization-free sparse-matvec computational model.

## Why the fixed Lanczos margin is not a certificate

Let
\[
M=\max\{1,\|Q\|_\infty\},\qquad \eta=\delta M,
\]
and set
\[
s=-\widehat\lambda+\eta.
\]
Because a Ritz value is a Rayleigh quotient minimized only over a Krylov subspace,
\[
\widehat\lambda\ge \lambda_{\min}(Q).
\]
The post-shift minimum eigenvalue is exactly
\[
\lambda_{\min}(Q+sI)
=
\lambda_{\min}(Q)-\widehat\lambda+\eta
=
\eta-e,
\]
where
\[
e=\widehat\lambda-\lambda_{\min}(Q)\ge0.
\]
Thus the numerical margin \(\eta\) is precisely an admissible one-sided eigenvalue-estimation error budget; it is not by itself a proof that the budget was met.

### Failure at every fixed finite Lanczos depth

Fix \(m\ge1\) and \(0<\delta<1\). Let
\[
Q_m=\operatorname{diag}(-1,\beta_1,\ldots,\beta_m),
\qquad
0=\beta_1<\beta_2<\cdots<\beta_m\le\frac12.
\]
Then
\[
\lambda_{\min}(Q_m)=-1,\qquad
\max\{1,\|Q_m\|_\infty\}=1.
\]

Take a starting vector
\[
v_0=(0,w_1,\ldots,w_m)^T
\]
with every \(w_j\ne0\). Its \(m\)-dimensional Krylov space is exactly the benign invariant subspace spanned by the last \(m\) coordinate vectors: the corresponding Vandermonde matrix has full rank because the \(\beta_j\) are distinct. Therefore the smallest \(m\)-step Ritz value is exactly
\[
\widehat\lambda_m(v_0)=0.
\]

Now perturb the start to
\[
v_\varepsilon
=
\frac{(\varepsilon,w_1,\ldots,w_m)^T}
{\|(\varepsilon,w_1,\ldots,w_m)\|}.
\]
The matrix
\[
[v_\varepsilon,Q_mv_\varepsilon,\ldots,Q_m^{m-1}v_\varepsilon]
\]
has rank \(m\) at \(\varepsilon=0\), hence its column space, orthogonal projector, and the eigenvalues of the compressed matrix vary continuously for sufficiently small \(\varepsilon\). Consequently
\[
\widehat\lambda_m(v_\varepsilon)\to0
\quad(\varepsilon\to0).
\]
For all sufficiently small nonzero \(\varepsilon\),
\[
\widehat\lambda_m(v_\varepsilon)>\delta-1,
\]
so the proposed shift satisfies
\[
s_m=-\widehat\lambda_m+\delta<1
\]
and therefore
\[
\lambda_{\min}(Q_m+s_mI)=-1+s_m<0.
\]

The inequality is strict and persists on an open neighborhood of such starts. Hence any initialization distribution with positive density on that neighborhood has positive probability of producing an insufficient shift. This is an exact-arithmetic obstruction: no fixed finite number of ordinary single-start Lanczos/Ritz steps, followed only by a fixed additive margin, gives a deterministic guarantee for all symmetric matrices.

This statement is conditional on \(\widehat\lambda_Q\) being an ordinary Ritz estimate. If an implementation instead produces a rigorously certified lower bound, the obstruction does not apply.

## Certified comparison-matrix lower bounds

For \(x\in\mathbb R^n\), let \(y=|x|\) componentwise. Then
\[
\begin{aligned}
x^TQx
&=
\sum_i q_{ii}x_i^2
+
2\sum_{i<j}q_{ij}x_ix_j\\
&\ge
\sum_i q_{ii}y_i^2
-
2\sum_{i<j}|q_{ij}|y_iy_j\\
&=
y^TC(Q)y.
\end{aligned}
\]
Since \(\|y\|_2=\|x\|_2\),
\[
\boxed{\lambda_{\min}(Q)\ge\lambda_{\min}(C(Q)).}
\]

For any positive vector \(d\), applying Gershgorin after the diagonal similarity scaling \(D^{-1}C(Q)D\), \(D=\operatorname{diag}(d)\), gives
\[
\boxed{
L(d)=
\min_i \frac{(C(Q)d)_i}{d_i}
\le
\lambda_{\min}(C(Q))
\le
\lambda_{\min}(Q).
}
\]

## A monotone sparse-matvec refinement

Choose
\[
\mu>\max_i q_{ii},
\qquad
A=\mu I-C(Q).
\]
Then \(A\ge0\) entrywise and has strictly positive diagonal. Starting from any \(d_0>0\), iterate
\[
d_{k+1}=Ad_k.
\]
Define
\[
U_k=\max_i\frac{d_{k+1,i}}{d_{k,i}},
\qquad
L_k=\mu-U_k.
\]
Because
\[
C(Q)d_k=\mu d_k-Ad_k,
\]
we have exactly
\[
L_k=L(d_k),
\]
so every \(L_k\) is a certified lower bound for \(\lambda_{\min}(Q)\).

The sequence is monotone. From
\[
Ad_k\le U_kd_k
\]
componentwise, multiplication by the nonnegative matrix \(A\) gives
\[
A^2d_k\le U_kAd_k,
\]
hence
\[
U_{k+1}\le U_k,
\qquad
L_{k+1}\ge L_k.
\]

Because \(C(Q)\) is symmetric, \(A\) is symmetric and nonnegative. On each connected component of its support graph, the positive diagonal makes the corresponding irreducible block primitive. Perron--Frobenius therefore yields
\[
U_k\downarrow\rho(A).
\]
Since
\[
\rho(A)=\mu-\lambda_{\min}(C(Q)),
\]
it follows that
\[
\boxed{L_k\uparrow\lambda_{\min}(C(Q)).}
\]

The Collatz--Wielandt min-max formula also gives
\[
\boxed{
\sup_{d>0}L(d)
=
\lambda_{\min}(C(Q)).
}
\]
Thus the iteration converges to the best lower bound obtainable from positive diagonal similarity-scaled Gershgorin discs.

For \(d_0=\mathbf 1\),
\[
L_0=\min_i\left(q_{ii}-\sum_{j\ne i}|q_{ij}|\right)
\]
is the ordinary Gershgorin lower bound, so each subsequent step is a certified monotone improvement.

## Convexification certificate

Let \(\eta>0\) be the desired curvature margin, and use
\[
s_k=\eta+\max\{0,-L_k\}.
\]
If \(L_k\le0\), then
\[
\lambda_{\min}(Q+s_kI)
\ge L_k+\eta-L_k
=\eta.
\]
If \(L_k>0\), then
\[
\lambda_{\min}(Q+s_kI)
\ge L_k+\eta>\eta.
\]
Therefore
\[
\boxed{Q+s_kI\succeq \eta I}
\]
for every iterate \(k\).

For an indefinite \(Q\), necessarily \(L_k\le\lambda_{\min}(Q)<0\), so
\[
s_k=\eta-L_k.
\]
Because \(L_k\) increases monotonically, the certified shift decreases monotonically toward
\[
\eta-\lambda_{\min}(C(Q)).
\]

## Exactness for sign-switchable Z-matrices

Suppose there is a diagonal signature matrix
\[
S=\operatorname{diag}(\pm1)
\]
such that
\[
SQS=C(Q).
\]
Then \(Q\) and \(C(Q)\) are orthogonally similar, hence
\[
\lambda_{\min}(Q)=\lambda_{\min}(C(Q)).
\]
This includes symmetric Z-matrices themselves and matrices that become Z-matrices after sign switching.

For indefinite matrices in this class,
\[
L_k\uparrow\lambda_{\min}(Q)
\]
and therefore
\[
s_k\downarrow\eta-\lambda_{\min}(Q),
\]
the smallest scalar shift that achieves the target curvature margin \(\eta\).

For general sign patterns, the limiting comparison-matrix bound can be conservative because replacing \(q_{ij}\) by \(-|q_{ij}|\) removes favorable sign cancellation. The method is therefore a certificate, not a claim of universally accurate eigenvalue estimation.

## Reproducibility check

`artifacts/verify_convexification.py` contains two deterministic checks.

First, with eight Lanczos steps on
\[
Q=\operatorname{diag}(-1,0,1/14,\ldots,1/2)
\]
and a start whose component in the \(-1\) eigendirection is \(10^{-8}\), the smallest Ritz value is approximately
\[
-1.3709332\times10^{-6}.
\]
With \(\delta=10^{-2}\), the resulting shift is approximately \(0.01000137\), leaving
\[
\lambda_{\min}(Q+sI)\approx-0.98999863.
\]

Second, a sign-switchable tridiagonal example has
\[
\lambda_{\min}(Q)=\lambda_{\min}(C(Q))
\approx-0.869542209728.
\]
The certified sequence improves monotonically from
\[
L_0=-1.2
\]
to
\[
L_{99}\approx-0.869542215349.
\]
With target margin \(\eta=0.01\), the resulting shift gives
\[
\lambda_{\min}(Q+sI)
\approx0.010000005622.
\]

These computations support the formulas but are not substitutes for the analytic proofs above.

## Relation to prior work and originality boundary

Chen and Lu's PDNQP requires \(Q+\gamma^{-1}I\succ0\) for its strongly convex inner QPs and convergence statement, while its practical rule describes \(\widehat\lambda_Q\) only as a Lanczos estimate. The result above identifies the exact missing condition for a Ritz estimate to certify that assumption and supplies a factorization-free certified alternative.

The ingredients Rayleigh--Ritz, Gershgorin discs, diagonal scaling, comparison/Z-matrices, Perron--Frobenius, and Collatz--Wielandt are classical and are **not** claimed as new. Gershgorin-based Hessian regularization also exists in optimization software such as acados. The originality claim is restricted to the combination relevant to the PDNQP setting: the exact fixed-margin failure condition, a failure family for every prescribed finite Lanczos depth, and a source-compatible monotone sparse-matvec certificate whose limiting conservatism is characterized exactly by \(C(Q)\).

To the best of our knowledge, no inspected source states this correction-and-repair package for PDNQP.

## Limitations

- The result does **not** show that the numerical experiments reported by PDNQP used an insufficient shift. The inspected arXiv version does not specify enough detail about the Lanczos estimator to establish that.
- No public implementation linked from the inspected arXiv version was available for checking an implementation-specific safeguard. If the implementation computes a rigorous lower bound or performs an additional convexity check, the finite-Ritz counterexample does not apply to that implementation.
- The comparison-matrix certificate can be substantially conservative for matrices with favorable sign cancellation. It is exact only for the stated sign-switchable class and related cases.
- The sparse-matvec iteration is an exact-arithmetic certificate. Rigorous floating-point certification requires directed rounding or an explicit numerical safety allowance.
- This result restores the spectral condition required for strong convexity; it does not by itself prove the other hypotheses of the outer convergence theorem.

## References

1. Z. Chen and H. Lu, *PDNQP: A GPU-based Factorization-free Method for Large-scale Nonconvex Quadratic Programming*, arXiv:2609.19557v1, 2026. https://arxiv.org/abs/2609.19557v1
2. B. Hermans, A. Themelis, and P. Patrinos, *QPALM: A Proximal Augmented Lagrangian Method for Nonconvex Quadratic Programs*, Mathematical Programming Computation 14 (2022), 497--541. https://arxiv.org/abs/2010.02653
3. R. S. Varga, *Matrix Iterative Analysis*, 2nd ed., Springer, 2000. (Classical Gershgorin, nonnegative-matrix, and iterative-analysis background.)
4. acados documentation, Hessian regularization option `GERSHGORIN_LEVENBERG_MARQUARDT`. https://docs.acados.org/python_interface/
