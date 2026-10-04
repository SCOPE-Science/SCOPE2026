# Exact floor-limited local spectrum of Sophia on diagonal quadratics
## Finding

Consider the deterministic diagonal quadratic
\[
f(x)
=
\frac12\sum_{i=1}^d \lambda_i x_i^2,
\qquad
\lambda_i>0.
\]
Use Sophia with constant learning rate \(\eta>0\), first-moment coefficient
\[
0\le\beta_1<1,
\]
Hessian-EMA coefficient
\[
0\le\beta_2<1,
\]
refresh period \(k\ge1\), denominator parameters \(\gamma>0\) and \(\varepsilon>0\), clipping threshold \(1\), and zero weight decay. Assume the Hessian estimator is exact on this quadratic, so every refreshed diagonal estimate equals \(\lambda_i\) on coordinate \(i\).

At the \(j\)-th Hessian refresh, the source initialization and EMA rule give
\[
h_i^{(j)}
=
\lambda_i(1-\beta_2^j).
\]
Thus
\[
h_i^{(j)}\longrightarrow \lambda_i
\]
geometrically, independently of the optimization state.

Near the minimizer the elementwise clip is inactive. Define
\[
\chi_i
=
\frac{\eta\lambda_i}
{\max\{\gamma\lambda_i,\varepsilon\}}
=
\min\left\{
\frac{\eta}{\gamma},
\frac{\eta\lambda_i}{\varepsilon}
\right\}.
\]
The limiting local characteristic polynomial for coordinate \(i\) is
\[
r^2
-
\left[
1+\beta_1-(1-\beta_1)\chi_i
\right]r
+
\beta_1.
\]
Consequently, strict asymptotic local exponential stability is equivalent to
\[
0<\chi_i<
\frac{2(1+\beta_1)}{1-\beta_1}
\]
for every coordinate.

Because
\[
0<\chi_i\le\frac{\eta}{\gamma}
\]
for every positive curvature, Sophia is strictly locally stable for every diagonal SPD quadratic, regardless of the curvature magnitudes, exactly when
\[
0<
\frac{\eta}{\gamma}
<
\frac{2(1+\beta_1)}{1-\beta_1}.
\]
The Hessian-EMA parameter \(\beta_2\) and refresh period \(k\) do not appear in this limiting spectrum; on exact quadratics they control only the exponentially decaying preconditioner transient.

For
\[
0<\beta_1<1,
\]
define
\[
\chi_-
=
\frac{1-\sqrt{\beta_1}}
{1+\sqrt{\beta_1}},
\qquad
\chi_+
=
\frac{1+\sqrt{\beta_1}}
{1-\sqrt{\beta_1}}.
\]
Whenever
\[
\chi_-<
\frac{\eta}{\gamma}
<
\chi_+,
\]
every coordinate with
\[
\lambda_i
\ge
\lambda_{\rm plateau}
:=
\frac{\varepsilon\chi_-}{\eta}
\]
has a complex-conjugate optimization pair with exact modulus
\[
\sqrt{\beta_1}.
\]
Therefore the limiting local rate is exactly curvature independent above the explicit flat-curvature threshold \(\lambda_{\rm plateau}\).

Coordinates below this threshold satisfy
\[
\chi_i
=
\frac{\eta\lambda_i}{\varepsilon}
<
\chi_-.
\]
Their dominant root is real and positive:
\[
\rho_i
=
\frac{
T_i+\sqrt{T_i^2-4\beta_1}
}{2},
\qquad
T_i
=
1+\beta_1-(1-\beta_1)\chi_i.
\]
As \(\lambda_i\downarrow0\),
\[
\rho_i
=
1-\frac{\eta\lambda_i}{\varepsilon}
+
O\left(
\left(\frac{\eta\lambda_i}{\varepsilon}\right)^2
\right).
\]
Hence the denominator floor is the exact mechanism that restores curvature-dependent slowing in sufficiently flat directions.

For the source value
\[
\beta_1=0.96,
\]
one has
\[
\chi_-\approx0.0102051443,
\qquad
\chi_+\approx97.98979486,
\]
and the stability ceiling is
\[
98.
\]
With the source value
\[
\varepsilon=10^{-12}
\]
and a constant learning rate
\[
\eta=6\times10^{-4},
\]
the plateau threshold is approximately
\[
1.7008574\times10^{-11}.
\]
The source peak learning-rate and \(\gamma\) choices for the 125M model give
\[
\eta/\gamma=0.06
\]
for Sophia-H and
\[
\eta/\gamma=0.012
\]
for Sophia-G, both inside the exact plateau interval. This numerical comparison is illustrative only because the training runs use learning-rate schedules rather than a constant learning rate.

## Assumptions and scope

The result concerns the source Sophia update with exact diagonal Hessian information on a deterministic diagonal quadratic. Weight decay is set to zero to isolate the curvature-normalized optimization dynamics.

The Hessian estimator is exact, but its exponential moving average and refresh period are kept. Since the true diagonal Hessian is constant, the Hessian state is an explicit deterministic transient.

The theorem is local because Sophia clips the preconditioned momentum outside a neighborhood of the minimizer. Since the denominator is at least \(\varepsilon>0\), the clip is inactive in a sufficiently small neighborhood, where the stated linear dynamics are exact.

The stability statement is strict and asymptotic. Equality at a unit-modulus boundary is not called exponentially stable.

The diagonal assumption is essential for coordinatewise decoupling. A rotated Hessian together with a diagonal preconditioner does not reduce to these scalar modes.

## Proof

For coordinate \(i\), the exact Hessian estimator returns \(\lambda_i\) at every Hessian refresh. Starting from the source initialization, the refresh-indexed EMA satisfies
\[
h_i^{(j)}
=
\beta_2 h_i^{(j-1)}
+
(1-\beta_2)\lambda_i,
\qquad
h_i^{(0)}=0.
\]
Thus
\[
h_i^{(j)}
=
\lambda_i(1-\beta_2^j).
\]

Let
\[
m_{i,t}
=
\beta_1m_{i,t-1}
+
(1-\beta_1)\lambda_i x_{i,t}.
\]
Inside the unclipped neighborhood,
\[
x_{i,t+1}
=
x_{i,t}
-
\eta\frac{m_{i,t}}
{\max\{\gamma h_{i,t},\varepsilon\}}.
\]
As \(t\to\infty\), the denominator converges geometrically to
\[
d_i
=
\max\{\gamma\lambda_i,\varepsilon\}.
\]

Scale the momentum by curvature:
\[
u_{i,t}
=
\frac{m_{i,t}}{\lambda_i}.
\]
The limiting map from
\[
(x_{i,t},u_{i,t-1})
\]
to
\[
(x_{i,t+1},u_{i,t})
\]
is
\[
\begin{bmatrix}
x_{i,t+1}\\
u_{i,t}
\end{bmatrix}
=
A(\chi_i)
\begin{bmatrix}
x_{i,t}\\
u_{i,t-1}
\end{bmatrix},
\]
where
\[
A(\chi)
=
\begin{bmatrix}
1-(1-\beta_1)\chi&-\beta_1\chi\\
1-\beta_1&\beta_1
\end{bmatrix}.
\]
Its determinant and trace are
\[
\det A(\chi)=\beta_1,
\]
\[
\operatorname{tr}A(\chi)
=
1+\beta_1-(1-\beta_1)\chi.
\]
This gives the stated characteristic polynomial.

For a real monic quadratic
\[
r^2-Tr+\beta_1,
\]
the strict second-order Jury conditions are
\[
1-\beta_1>0,
\]
\[
1-T+\beta_1>0,
\]
and
\[
1+T+\beta_1>0.
\]
Substituting the trace yields exactly
\[
\chi>0
\]
and
\[
\chi<
\frac{2(1+\beta_1)}{1-\beta_1}.
\]
This proves the modewise stability frontier.

The actual local coefficient matrices converge geometrically to \(A(\chi_i)\), because the Hessian EMA does. In the strict stable region, choose an induced norm in which the limiting matrix has norm below one; all sufficiently late local matrices remain contractions in that norm. In the strict unstable region, the limiting matrix has a hyperbolic expanding mode, and a geometrically summable coefficient perturbation preserves an expanding local solution. Hence the strict limiting Schur boundary is also the strict asymptotic local exponential-stability boundary.

The identity
\[
\chi_i
=
\min\left\{
\frac{\eta}{\gamma},
\frac{\eta\lambda_i}{\varepsilon}
\right\}
\]
shows immediately that uniform stability over all positive diagonal curvatures is equivalent to the stated bound on \(\eta/\gamma\).

For the rate plateau, the two optimization roots are nonreal exactly when
\[
T_i^2<4\beta_1.
\]
Solving this inequality gives
\[
\chi_-<\chi_i<\chi_+.
\]
Their product is \(\beta_1\), so each has modulus \(\sqrt{\beta_1}\).

If
\[
\chi_-<\eta/\gamma<\chi_+,
\]
then \(\chi_i\le\eta/\gamma<\chi_+\). The lower plateau condition \(\chi_i\ge\chi_-\) is equivalent to
\[
\lambda_i
\ge
\frac{\varepsilon\chi_-}{\eta}.
\]
This proves the exact flat-curvature threshold.

For \(\chi_i<\chi_-\), the dominant root is the positive closed form displayed above. Expanding that root at \(\chi_i=0\) gives
\[
\rho_i=1-\chi_i+O(\chi_i^2),
\]
which yields the stated flat-curvature asymptotic.

## Verification

The accompanying `verify.py` reconstructs the mode matrix, checks its trace and determinant, verifies the exact Jury boundary and complex-root interval, checks the Hessian-EMA formula, and evaluates the source-parameter examples.

The script also compares the analytic spectral radius with direct roots over deterministic grids spanning both the denominator-floor and curvature-normalized regimes.

These computations are algebra and transcription guards. The infinite-time local claims follow from the exact mode calculation and the exponentially convergent Hessian-state transient.

## Relationship to prior work

Liu, Li, Hall, Liang, and Ma introduced Sophia as a diagonal-Hessian preconditioned optimizer with elementwise clipping. Their practical algorithm maintains exponential moving averages of gradients and diagonal Hessian estimates and divides the momentum by
\[
\max\{\gamma h_t,\varepsilon\}
\]
before clipping. The source emphasizes improved adaptation to heterogeneous curvatures.

The same paper proves a condition-number-independent runtime bound for a substantially simplified deterministic method. That theoretical method uses the full Hessian, removes the momentum state, and explicitly omits the practical max-with-\(\varepsilon\) because the convex Hessian is positive definite. It therefore does not state the spectrum of the practical momentum-Hessian recurrence or identify the denominator floor as an exact boundary for condition-number-independent local rates.

The source experiments use
\[
\beta_1=0.96,
\qquad
\beta_2=0.99,
\qquad
\varepsilon=10^{-12},
\qquad
k=10,
\]
with \(\gamma=0.01\) for Sophia-H and \(\gamma=0.05\) for Sophia-G. The exact formulas above explain why, on an ideal diagonal quadratic, \(\beta_2\) and \(k\) control only the Hessian-estimation transient while the limiting local spectrum is determined by \(\beta_1\), \(\eta/\gamma\), and the floor \(\varepsilon\).

Focused searches for Sophia local stability, scalar or diagonal quadratic spectra, denominator-floor thresholds, momentum eigenvalues, and exact rate plateaus did not identify a published statement equivalent to the result above.

## Limitations

The Hessian estimate is assumed exact. Stochastic estimator noise can couple the preconditioner state back into the optimization dynamics and requires a mean-square or random-product analysis.

The theorem is local. Saturated clipping can create nonlinear transients and possibly periodic behavior outside the unclipped neighborhood; none is classified here.

Weight decay is disabled. Decoupled weight decay changes the local polynomial and should be analyzed separately.

Learning-rate schedules make the local coefficients slowly time varying even after the Hessian state has converged. The constant-\(\eta\) theorem does not claim an exact scheduled-training rate.

The diagonal quadratic assumption gives exact mode separation. Off-diagonal curvature relative to the coordinatewise preconditioner can destroy the condition-number-free modal picture.

## References

1. Hong Liu, Zhiyuan Li, David Hall, Percy Liang, and Tengyu Ma, “Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training,” arXiv:2305.14342v1, 2023.
2. Hong Liu, Zhiyuan Li, David Hall, Percy Liang, and Tengyu Ma, “Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training,” ICLR 2024.
