# Exact stationary covariance and stability factorization for constant-template STORM
## Finding

Consider
\[
f(x,\xi)=\frac{\lambda}{2}x^2+\xi x,
\qquad
\lambda>0,
\]
with iid samples satisfying
\[
\mathbb E[\xi]=0,
\qquad
\operatorname{Var}(\xi)=\sigma^2<\infty.
\]
The population objective is
\[
F(x)=\frac{\lambda}{2}x^2,
\]
whose unique minimizer is \(x^\star=0\).

Use the constant-parameter corrected-momentum template underlying STORM:
\[
x_{t+1}=x_t-\eta d_t,
\]
\[
d_{t+1}
=
\nabla f(x_{t+1},\xi_{t+1})
+
(1-a)\left[d_t-\nabla f(x_t,\xi_{t+1})\right],
\]
with
\[
0<a\le1,
\qquad
\eta>0.
\]
Define
\[
s=\eta\lambda,
\qquad
u_t=\frac{d_t}{\lambda},
\qquad
\varepsilon_t=\frac{\xi_t}{\lambda},
\qquad
e_t=u_t-x_t.
\]
Then the update is exactly
\[
x_{t+1}=(1-s)x_t-se_t,
\]
\[
e_{t+1}=(1-a)e_t+a\varepsilon_{t+1}.
\]
Thus the deterministic modes factor completely: their eigenvalues are
\[
1-s
\quad\text{and}\quad
1-a.
\]

For \(0<a\le1\), convergence to a unique finite stationary covariance holds exactly for
\[
0<s<2.
\]
The step-stability interval is therefore identical to scalar constant-step SGD.

Inside this interval, the normalized estimator error has stationary variance
\[
\operatorname{Var}(e)
=
\frac{a}{2-a}\frac{\sigma^2}{\lambda^2},
\]
so
\[
\operatorname{Var}(d-\nabla F(x))
=
\frac{a}{2-a}\sigma^2.
\]
This estimator-error floor is independent of the learning rate.

The stationary iterate variance is
\[
\operatorname{Var}(x)
=
\frac{\sigma^2}{\lambda^2}
\frac{
a s(2-a-s+as)
}{
(2-a)(2-s)(a+s-as)
}.
\]

For plain constant-step SGD on the same oracle,
\[
x_{t+1}=(1-s)x_t-s\varepsilon_{t+1},
\]
and
\[
\operatorname{Var}_{\rm SGD}(x)
=
\frac{\sigma^2}{\lambda^2}\frac{s}{2-s}.
\]
Hence
\[
R(a,s)
=
\frac{\operatorname{Var}_{\rm STORM}(x)}
{\operatorname{Var}_{\rm SGD}(x)}
=
\frac{
a(2-a-s+as)
}{
(2-a)(a+s-as)
}.
\]
If
\[
0<a<1,
\qquad
0<s<2,
\]
then
\[
1-R(a,s)
=
\frac{2s(1-a)}
{(2-a)(a+s-as)}
>0.
\]
So corrected momentum strictly lowers the stationary iterate variance while retaining the full SGD stability interval.

For fixed \(s\in(0,2)\), the ratio is strictly increasing in \(a\), because
\[
\frac{\partial R}{\partial a}
=
\frac{
2s\left[1-(s-1)(1-a)^2\right]
}{
(2-a)^2(a+s-as)^2
}
>0.
\]
As \(a\downarrow0\),
\[
\operatorname{Var}(x)
=
\frac{\sigma^2}{\lambda^2}
\left[\frac{a}{2}+O(a^2)\right],
\]
but the memory eigenvalue \(1-a\) approaches one. The exact benchmark therefore exposes a noise-floor versus memory-speed tradeoff.

## Assumptions and scope

The theorem concerns the constant-parameter corrected-momentum template presented in the STORM paper before its adaptive parameter schedule. The published STORM algorithm uses time-varying learning rates and momentum weights; this result does not claim to analyze that adaptive schedule.

The stochastic gradient is
\[
\nabla f(x,\xi)=\lambda x+\xi.
\]
The same sample is used at the current and preceding iterate in the correction term. This common-random-number coupling is essential for the exact error decoupling.

The sample gradients are not uniformly bounded over all \(x\). The statement is a direct exact analysis of the update itself, not an application of the bounded-gradient adaptive theorem.

Finite-second-moment stationarity means that the mean converges to zero and the covariance converges to the unique stationary covariance for finite-second-moment initial data. When \(\sigma^2>0\), the iterate does not converge to zero in mean square.

## Proof

Since
\[
\nabla f(x,\xi)=\lambda x+\xi,
\]
the corrected-momentum update gives
\[
\begin{aligned}
d_{t+1}
&=
\lambda x_{t+1}+\xi_{t+1}
+
(1-a)
\left[d_t-\lambda x_t-\xi_{t+1}\right]\\
&=
a\lambda x_t+(1-a-s)d_t+a\xi_{t+1}.
\end{aligned}
\]
After dividing by \(\lambda\),
\[
u_{t+1}
=
a x_t+(1-a-s)u_t+a\varepsilon_{t+1}.
\]
Subtracting
\[
x_{t+1}=x_t-su_t
\]
yields
\[
e_{t+1}=(1-a)e_t+a\varepsilon_{t+1}.
\]
Also,
\[
x_{t+1}
=
x_t-s(x_t+e_t)
=
(1-s)x_t-se_t.
\]

Therefore the deterministic state matrix in \((x_t,e_t)\) is
\[
M=
\begin{bmatrix}
1-s&-s\\
0&1-a
\end{bmatrix}.
\]
Its eigenvalues are \(1-s\) and \(1-a\). Because \(0<a\le1\), Schur stability is equivalent to
\[
|1-s|<1,
\]
which is exactly
\[
0<s<2.
\]

Let
\[
\tau^2=\frac{\sigma^2}{\lambda^2}.
\]
At stationarity, writing
\[
E=\operatorname{Var}(e),
\]
the scalar autoregression gives
\[
E=(1-a)^2E+a^2\tau^2,
\]
hence
\[
E=\frac{a}{2-a}\tau^2.
\]

Let
\[
C=\operatorname{Cov}(x,e).
\]
Stationarity gives
\[
C=(1-a)\left[(1-s)C-sE\right],
\]
so
\[
C
=
-\frac{(1-a)sE}{a+s-as}.
\]

Finally, with
\[
V=\operatorname{Var}(x),
\]
one has
\[
V=(1-s)^2V+s^2E-2s(1-s)C.
\]
Substituting the preceding formulas yields
\[
V
=
\tau^2
\frac{
a s(2-a-s+as)
}{
(2-a)(2-s)(a+s-as)
}.
\]

The SGD stationary variance follows from its scalar autoregression. Dividing the two formulas produces \(R(a,s)\); direct subtraction gives the positive expression for \(1-R(a,s)\), and differentiation gives the displayed positive derivative. The small-\(a\) expansion follows directly from the exact rational formula.

## Verification

The accompanying `verify.py` checks the triangular state transformation, eigenvalue factorization, stationary Lyapunov equations, exact SGD comparison, positivity of the variance improvement, and the small-\(a\) asymptotic on deterministic rational test points.

Finite checks are algebra and transcription guards. The infinite-time stability and covariance statements follow analytically from the triangular recursion and exact Lyapunov equations.

## Relationship to prior work

Cutkosky and Orabona introduced the corrected-momentum template and STORM. Their momentum-and-variance-reduction discussion uses the same sample at the current and preceding iterate, derives a general estimator-error recurrence, and explicitly motivates a tradeoff between the momentum weight and learning rate. Their published STORM algorithm then makes both parameters adaptive. The inspected full text does not specialize the template to the additive-noise quadratic or give the exact stationary covariance, unchanged SGD stability interval, or closed variance ratio above.

Levy, Kavis, and Cevher later restated the corrected-momentum template in STORM+ and emphasized the learning-rate/momentum interplay. Their analysis again uses adaptive parameter choices and nonconvex stationarity rates; the inspected full text contains no quadratic stationary-covariance theorem.

Tran-Dinh, Pham, Phan, and Nguyen independently developed a closely related hybrid SARAH-SGD estimator slightly earlier in May 2019. Their basic estimator combines a recursive-difference sample with an independent fresh stochastic-gradient sample. That formulation is scientifically close, but its additional independent noise does not have the same cancellation law as STORM's same-sample corrected momentum.

## Limitations

The decoupling relies on additive gradient noise with deterministic curvature. Sample-dependent curvature or multiplicative noise makes the gradient-difference correction stochastic and requires a different moment analysis.

The result concerns constant parameters in the STORM template, not the adaptive schedule used to obtain the published nonconvex complexity guarantee.

The theorem is scalar. A deterministic common Hessian in higher dimensions can be analyzed mode by mode, but heterogeneous sample Hessians do not reduce to this calculation.

The stationary covariance is a long-run noise benchmark, not a finite-time oracle-complexity theorem. Sending \(a\) toward zero lowers the stationary variance while making the estimator-memory mode arbitrarily slow.

An equivalent covariance calculation may exist in older linear stochastic-approximation or signal-processing literature under terminology unrelated to STORM; this is the main residual originality risk.

## References

1. Ashok Cutkosky and Francesco Orabona, “Momentum-Based Variance Reduction in Non-Convex SGD,” arXiv:1905.10018v1, 2019.
2. Kfir Y. Levy, Ali Kavis, and Volkan Cevher, “STORM+: Fully Adaptive SGD with Momentum for Nonconvex Optimization,” arXiv:2111.01040v1, 2021.
3. Quoc Tran-Dinh, Nhan H. Pham, Dzung T. Phan, and Lam M. Nguyen, “Hybrid Stochastic Gradient Descent Algorithms for Stochastic Nonconvex Optimization,” arXiv:1905.05920v1, 2019.
