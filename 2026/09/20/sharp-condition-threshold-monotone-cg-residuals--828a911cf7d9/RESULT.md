# Sharp condition-number threshold for monotone exact-CG residuals

**Same-model review: passed. Independent audit: not yet performed.**

## Statement

Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite with
\[
0<\mu=\lambda_{\min}(A)\le \lambda_{\max}(A)=L,
\qquad
\kappa=\frac{L}{\mu}.
\]
Run the standard conjugate-gradient method in exact arithmetic,
\[
r_k=b-Ax_k,\qquad
p_0=r_0,\qquad
p_k=r_k+\beta_{k-1}p_{k-1},
\]
with
\[
\alpha_k=\frac{r_k^Tr_k}{p_k^TAp_k},
\qquad
\beta_{k-1}=\frac{\|r_k\|_2^2}{\|r_{k-1}\|_2^2},
\qquad
r_{k+1}=r_k-\alpha_kAp_k.
\]

For every nonterminal step, define
\[
d_k:=\frac{\|p_k\|_2^2}{\|r_k\|_2^2},
\qquad
K:=\frac{L+\mu}{2\sqrt{L\mu}}
=\frac{\kappa+1}{2\sqrt{\kappa}}.
\]
Then
\[
\boxed{
\frac{\|r_{k+1}\|_2^2}{\|r_k\|_2^2}
\le \frac{K^2}{d_k}-1
\le K^2-1
}
\tag{1}
\]
and hence
\[
\boxed{
\frac{\|r_{k+1}\|_2}{\|r_k\|_2}
\le
\frac{L-\mu}{2\sqrt{L\mu}}
=
\frac{\kappa-1}{2\sqrt{\kappa}}.
}
\tag{2}
\]

The global factor in (2) is sharp for every fixed SPD matrix \(A\): if
\(u_\mu,u_L\) are unit eigenvectors corresponding to \(\mu,L\), then the
initial residual
\[
r_0=\sqrt L\,u_\mu+\sqrt\mu\,u_L
\tag{3}
\]
attains equality at the first CG step.

Consequently, for a fixed SPD matrix \(A\), the following are equivalent:

1. for every right-hand side \(b\), every initial guess \(x_0\), and every
   exact-CG step that exists,
   \[
   \|r_{k+1}\|_2\le \|r_k\|_2;
   \]
2. its spectral condition number satisfies
   \[
   \boxed{\kappa_2(A)\le 3+2\sqrt2.}
   \tag{4}
   \]

Thus \(3+2\sqrt2\approx5.8284271247\) is the exact universal
condition-number threshold for monotone Euclidean CG residuals. If
\(\kappa>3+2\sqrt2\), the endpoint construction (3) gives a first-step
residual increase. At the threshold equality can occur at the first step,
while every later nonterminal step following a nonterminal predecessor is
strictly decreasing.

There is also an observable history refinement:
\[
d_0=1,\qquad
d_k=1+\beta_{k-1}d_{k-1}.
\tag{5}
\]
In particular,
\[
d_k\ge \frac{K^2}{2}
\quad\Longrightarrow\quad
\|r_{k+1}\|_2\le \|r_k\|_2.
\tag{6}
\]

For fixed SPD preconditioning \(M\), the same statements hold for PCG after
replacing \(A\) by
\[
H=M^{-1/2}AM^{-1/2}
\]
and replacing the Euclidean residual norm by
\[
\|r\|_{M^{-1}}=(r^TM^{-1}r)^{1/2}.
\]
Hence the exact PCG threshold in this natural residual norm is
\(\kappa_2(H)\le3+2\sqrt2\).

## Proof

Exact CG gives mutual Euclidean orthogonality of the residuals and
\(A\)-conjugacy of the search directions. Since
\[
p_k=r_k+\beta_{k-1}p_{k-1}
\]
and \(p_{k-1}^TAp_k=0\),
\[
r_k^TAp_k=p_k^TAp_k.
\]
Therefore
\[
\begin{aligned}
\|r_{k+1}\|_2^2
&=\|r_k-\alpha_kAp_k\|_2^2\\
&=\|r_k\|_2^2
-2\alpha_k r_k^TAp_k
+\alpha_k^2\|Ap_k\|_2^2\\
&=-\|r_k\|_2^2
+\frac{\|r_k\|_2^4\|Ap_k\|_2^2}{(p_k^TAp_k)^2},
\end{aligned}
\]
so
\[
\frac{\|r_{k+1}\|_2^2}{\|r_k\|_2^2}
=
-1+
\frac{\|r_k\|_2^2\|Ap_k\|_2^2}{(p_k^TAp_k)^2}.
\tag{7}
\]

We next use the Kantorovich inequality in a form included here for
completeness. For any nonzero \(p\), put \(y=A^{1/2}p\). Then
\[
\frac{\|p\|_2^2\|Ap\|_2^2}{(p^TAp)^2}
=
\frac{(y^TA^{-1}y)(y^TAy)}{(y^Ty)^2}.
\]
If \(a=(y^TAy)/(y^Ty)\) and
\(c=(y^TA^{-1}y)/(y^Ty)\), the pointwise spectral inequality
\[
\lambda+\frac{\mu L}{\lambda}\le \mu+L,
\qquad \lambda\in[\mu,L],
\]
implies \(a+\mu Lc\le\mu+L\). Hence by AM-GM,
\[
\mu L\,ac\le\frac{(\mu+L)^2}{4},
\]
and therefore
\[
\frac{\|p\|_2^2\|Ap\|_2^2}{(p^TAp)^2}
\le
\frac{(L+\mu)^2}{4L\mu}=K^2.
\tag{8}
\]
Combining (7) and (8) with
\(\|r_k\|_2^2/\|p_k\|_2^2=1/d_k\) gives the first inequality in (1);
\(d_k\ge1\) gives the second and proves (2).

To verify \(d_k\ge1\) and (5), exact-CG orthogonality gives
\(r_k^Tp_{k-1}=0\). Therefore
\[
\|p_k\|_2^2
=
\|r_k\|_2^2+\beta_{k-1}^2\|p_{k-1}\|_2^2,
\]
and division by \(\|r_k\|_2^2\), using
\(\beta_{k-1}=\|r_k\|_2^2/\|r_{k-1}\|_2^2\), yields
\[
d_k=1+\beta_{k-1}d_{k-1}.
\]
Equation (6) follows immediately from (1). Since the left side of (1) is
nonnegative, the same estimate also implies \(d_k\le K^2\) at every
nonterminal exact-CG state.

For sharpness, use (3). Since the extreme eigenvectors are orthonormal,
\[
\|r_0\|_2^2=L+\mu,\qquad
r_0^TAr_0=2L\mu,\qquad
\|Ar_0\|_2^2=L\mu(L+\mu).
\]
Because \(p_0=r_0\), substitution into (7) gives
\[
\frac{\|r_1\|_2^2}{\|r_0\|_2^2}
=
\frac{(L-\mu)^2}{4L\mu},
\]
which is equality in (2). Every prescribed \(r_0\) is realizable for any
chosen \(x_0\) by taking \(b=Ax_0+r_0\).

It remains to solve when the sharp factor is at most one:
\[
\frac{\kappa-1}{2\sqrt\kappa}\le1
\iff
\kappa^2-6\kappa+1\le0.
\]
Since \(\kappa\ge1\), this is exactly
\(\kappa\le3+2\sqrt2\), proving (4). At the threshold \(K^2=2\).
For a later nonterminal step \(k\ge1\) following a nonterminal predecessor,
\(\beta_{k-1}>0\), so (5) gives \(d_k>1\), and (1) is then strictly below
one.

Finally, standard fixed-preconditioner CG is ordinary CG applied to
\(H=M^{-1/2}AM^{-1/2}\). Its transformed residual is
\[
\widetilde r_k=M^{-1/2}r_k,
\]
so \(\|\widetilde r_k\|_2=\|r_k\|_{M^{-1}}\). Applying the theorem to
\(H\) gives the PCG statement.

## Context and prior literature

Hestenes and Stiefel's original CG paper already emphasized that residual
norms need not decrease monotonically and contains constructions of highly
nonmonotone residual histories. Meurant's exact-arithmetic treatment
explicitly studies conditions under which the CG residual norm oscillates.
Carson, Liesen and Strakoš give a modern discussion of prescribed residual
behavior and stress that such constructions do not simultaneously prescribe
an arbitrary spectrum.

A 2024 note by Gabriel H. Brown derives the exact first-step criterion
\[
\|r_0\|_2\|Ar_0\|_2
\ge \sqrt2\,r_0^TAr_0
\]
for a residual increase and gives \(\kappa\ge7\) as a simple sufficient
condition using a fixed endpoint mixture. The result above converts that
local vector criterion into the sharp condition-number-only threshold
\(3+2\sqrt2\), proves a sharp factor valid at every exact-CG step, supplies
the history-dependent refinement (1), and transfers the statement to PCG
in its natural residual norm.

No checked source stated the fixed-matrix equivalence (4), the sharp
all-step factor (2), or the history certificate (1). This originality claim
is to the best of our knowledge.

## Verification

`artifacts/verify_cg_residual_threshold.py` independently checks the sharp
two-eigenvector construction for several condition numbers, including the
threshold, and tests both inequalities in (1) on deterministic random SPD
examples. `artifacts/verification.txt` records the output.

The computation is supporting evidence only; the result is proved above.

## Limitations

- The theorem is for finite-dimensional real SPD matrices in exact
  arithmetic.
- It concerns the Euclidean norm of the exact CG residual. It does not claim
  monotonicity of recursively updated residuals in floating-point arithmetic.
- The PCG extension is for a fixed SPD preconditioner and the
  \(M^{-1}\)-norm of the residual; Euclidean PCG residual monotonicity is not
  asserted.
- The condition-number threshold is uniform over all right-hand sides and
  initial guesses for a fixed matrix. Particular initial residuals can be
  monotone far above the threshold.
- The result does not claim a new bound for the \(A\)-norm of the CG error,
  nor an iteration-complexity or implementation-performance improvement.
- Meurant's exact-arithmetic chapter was inspected through its available
  excerpt, which explicitly says it studies residual oscillation conditions,
  but its complete theorem-level text was not available for inspection.
  The complete relevant treatment in Liesen--Strakoš was also not inspected.
  These are the principal residual risks that an equivalent historical
  condition-number statement may already exist.
- The original Hestenes--Stiefel paper and later literature establish much
  more general nonmonotone residual phenomena; the claim here is only the
  sharp uniform condition-number boundary stated above.

## References

1. M. R. Hestenes and E. Stiefel, *Methods of conjugate gradients for
   solving linear systems*, Journal of Research of the National Bureau of
   Standards 49 (1952), 409--436.
   https://doi.org/10.6028/jres.049.044
2. G. Meurant, *The Lanczos and Conjugate Gradient Algorithms: From Theory
   to Finite Precision Computations*, Chapter 2, SIAM (2006).
   https://doi.org/10.1137/1.9780898718140.ch2
3. E. Carson, J. Liesen and Z. Strakoš, *Towards understanding CG and GMRES
   through examples*, Linear Algebra and its Applications 692 (2024),
   241--291.
   https://doi.org/10.1016/j.laa.2024.04.003
4. J. Liesen and Z. Strakoš, *Krylov Subspace Methods: Principles and
   Analysis*, Oxford University Press (2013).
   https://doi.org/10.1093/acprof:oso/9780199655410.001.0001
5. G. H. Brown, *Behavior of the conjugate gradient residual* (2024).
   https://ghbrown.net/posts/cg_residual/
