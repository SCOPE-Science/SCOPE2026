# Sharp Armijo contraction and minimax tuning on scalar Prox-SAM quadratics
## Finding

Consider the deterministic full-sample regime of the variable-metric proximal stochastic gradient method with additional sampling (Prox-SAM), specialized to
\[
H(x)=\frac{\lambda}{2}(x-x^\star)^2,
\qquad
R\equiv0,
\qquad
\lambda>0.
\]

Let the scalar metric be \(s_k>0\), the learning rate be \(\alpha_k>0\), and define the raw scaled curvature
\[
r_k=\frac{\alpha_k\lambda}{s_k}.
\]
The source algorithm computes the proximal-gradient direction first and then applies an independent Armijo relaxation \(t_k\in\{1,\beta,\beta^2,\ldots\}\), with
\[
\eta,\beta\in(0,1).
\]

For every nonstationary iterate, the Armijo test is equivalent to the single scalar inequality
\[
t_kr_k\le2-\eta.
\]
Therefore the accepted effective step
\[
u_k=t_kr_k
\]
obeys
\[
u_k=r_k
\quad\text{if}\quad
r_k\le2-\eta,
\]
and, whenever backtracking occurs,
\[
\beta(2-\eta)<u_k\le2-\eta.
\]

Assume only the source lower learning-rate bound and upper metric bound,
\[
\alpha_k\ge\alpha_{\min}>0,
\qquad
s_k\le\mu,
\]
and set
\[
r_0=\frac{\alpha_{\min}\lambda}{\mu}.
\]
Then every nonstationary iteration satisfies
\[
\frac{|x_{k+1}-x^\star|}{|x_k-x^\star|}
\le
q(\eta;r_0,\beta)
:=
\max\left\{
1-\min\{r_0,\beta(2-\eta)\},
1-\eta
\right\}
<1.
\]

Hence the full-sample scalar quadratic specialization is globally Q-linearly convergent even if the raw learning rates and metrics vary arbitrarily within the source bounds.

Moreover, if one retains only the lower raw-curvature information \(r_k\ge r_0\), the contraction envelope is sharp, and its exact minimax Armijo parameter is
\[
\eta_{\mathrm{opt}}
=
\min\left\{
r_0,\frac{2\beta}{1+\beta}
\right\}.
\]
The corresponding optimal worst-case factor is
\[
q_{\mathrm{opt}}
=
1-
\min\left\{
r_0,\frac{2\beta}{1+\beta}
\right\}.
\]

In the regime
\[
r_0\ge\frac{2\beta}{1+\beta},
\]
the optimally balanced value is
\[
\eta_{\mathrm{opt}}=\frac{2\beta}{1+\beta},
\qquad
q_{\mathrm{opt}}=\frac{1-\beta}{1+\beta}.
\]
For the source experimental choice \(\beta=1/2\), this balance occurs at
\[
\eta_{\mathrm{opt}}=\frac23,
\qquad
q_{\mathrm{opt}}=\frac13,
\]
provided the raw-curvature lower bound is at least \(2/3\).

## Assumptions and scope

The result concerns the deterministic full-sample specialization \(N_k=N\), for which the source states that its first four steps reduce to a deterministic variable-metric proximal-gradient method with line search.

The objective is one-dimensional and quadratic, and the nonsmooth regularizer is zero. The result therefore does not claim the same exact factor for multidimensional, nonsmooth, or stochastic phases of the method.

The source imposes
\[
0<\alpha_{\min}\le\alpha_k\le\alpha_{\max}
\]
and uniformly bounded positive-definite metrics. In one dimension, the upper metric bound gives the positive lower raw-curvature bound \(r_0\).

The sharpness statement is for the information class in which only \(r_k\ge r_0\) is used. A finite upper bound on \(r_k\) can improve the worst-case factor if it excludes one of the extremizing accepted-step values.

## Proof

Write
\[
e_k=x_k-x^\star.
\]
For
\[
f(x)=\frac{\lambda}{2}e^2,
\]
the gradient is
\[
\nabla f(x_k)=\lambda e_k.
\]
With scalar metric \(s_k\), the source proximal-gradient point is
\[
v_k=x_k-\frac{\alpha_k}{s_k}\lambda e_k,
\]
so the trial direction is
\[
d_k=v_k-x_k=-r_ke_k.
\]

For \(R\equiv0\), the source model-decrease quantity is
\[
q_k
=
d_k\nabla f(x_k)
+
\frac{s_k}{2\alpha_k}d_k^2.
\]
Substitution gives
\[
q_k
=
-r_k\lambda e_k^2
+
\frac12r_k\lambda e_k^2
=
-\frac12r_k\lambda e_k^2.
\]

The Armijo test at relaxation \(t>0\) is
\[
f(x_k+td_k)
\le
f(x_k)+\eta t q_k.
\]
Since
\[
x_k+td_k-x^\star=(1-tr_k)e_k,
\]
the test becomes
\[
\frac{\lambda e_k^2}{2}(1-tr_k)^2
\le
\frac{\lambda e_k^2}{2}(1-\eta tr_k).
\]
For \(e_k\ne0\), canceling the positive factor and expanding yields
\[
-2tr_k+t^2r_k^2\le-\eta tr_k.
\]
Because \(t>0\) and \(r_k>0\), this is equivalent to
\[
tr_k\le2-\eta.
\]

The backtracking starts at \(t=1\) and repeatedly multiplies by \(\beta\). If
\[
r_k\le2-\eta,
\]
the full trial is accepted and \(u_k=r_k\). Otherwise, minimality of the accepted backtracking index gives
\[
u_k=\beta^{m_k}r_k\le2-\eta
\]
while the preceding trial failed:
\[
\frac{u_k}{\beta}>2-\eta.
\]
Hence
\[
\beta(2-\eta)<u_k\le2-\eta.
\]

Since
\[
e_{k+1}=(1-u_k)e_k,
\]
the contraction factor is \(|1-u_k|\). The source bounds imply
\[
r_k\ge r_0.
\]
Thus every accepted effective step satisfies
\[
u_k\ge\min\{r_0,\beta(2-\eta)\}
\]
and
\[
u_k\le2-\eta<2.
\]
On this interval, the maximum of \(|1-u|\) occurs at an endpoint, giving
\[
|1-u_k|
\le
\max\left\{
1-\min\{r_0,\beta(2-\eta)\},
1-\eta
\right\}.
\]
Both terms are strictly below one.

For sharpness under the sole lower bound \(r\ge r_0\), three extremal mechanisms are available. If \(r_0\le2-\eta\), taking \(r=r_0\) gives the no-backtracking value \(u=r_0\). Taking a raw step at an accepted boundary gives \(u=2-\eta\). Taking a rejected raw step arbitrarily close above such a boundary makes the next accepted value approach \(\beta(2-\eta)\). Therefore the displayed envelope cannot be reduced without using additional raw-step information.

It remains to optimize over \(\eta\). Put
\[
h=\frac{2\beta}{1+\beta}.
\]
If \(r_0\le h\), choosing \(\eta=r_0\) gives
\[
r_0\le\beta(2-\eta),
\]
so both competing factors are at most \(1-r_0\), and no smaller value is possible because the no-backtracking endpoint \(u=r_0\) is allowed.

If \(r_0\ge h\), choose \(\eta=h\). Then
\[
\beta(2-h)=h,
\]
so the backtracking lower endpoint and the Armijo upper endpoint are equioscillating:
\[
1-\beta(2-h)=1-h.
\]
For \(\eta<h\), the term \(1-\eta\) is larger; for \(\eta>h\), the term \(1-\beta(2-\eta)\) is larger. Hence \(h\) is the unique minimizer in this regime.

Combining the two cases proves
\[
\eta_{\mathrm{opt}}=\min\{r_0,h\},
\qquad
q_{\mathrm{opt}}=1-\min\{r_0,h\}.
\]

## Verification

The standalone script `artifacts/verify_armijo_scalar.py` symbolically checks the reduction of the source Armijo inequality and numerically verifies the accepted-step bands and the minimax formula over dense grids of raw scaled curvatures.

The universal statement is proved analytically above. Grid computations are supporting evidence and are not used as an exhaustive proof.

## Relationship to prior work

The primary Prox-SAM paper separates the raw learning rate \(\alpha_k\) from a backtracking relaxation \(t_k\), proves that the line search is well defined, and proves qualitative full-sample convergence under standard variable-metric assumptions. It does not give the scalar quadratic accepted-step law, the explicit global Q-linear factor above, or the minimax choice of \(\eta\).

The deterministic variable-metric line-search framework cited by the source proves convergence and an \(O(1/k)\) convex function-value bound under broader assumptions. It does not state the one-dimensional sharp backtracking envelope or the balance
\[
\eta=\frac{2\beta}{1+\beta}.
\]

General stochastic Armijo literature provides expected complexity guarantees under probabilistic accuracy conditions. Those results do not imply the exact effective-step interval or the source-specific minimax tuning rule derived here.

Targeted searches using the source title, Prox-SAM name, scalar-quadratic terminology, Armijo relaxation parameters, variable-metric backtracking, and exact-contraction terminology did not locate an equivalent statement.

## Limitations

The exact rate concerns a scalar full-sample quadratic with \(R\equiv0\). It is a diagnostic model for the interaction between \(\alpha_k\), \(s_k\), \(t_k\), \(\eta\), and \(\beta\), not a general stochastic complexity theorem.

The sharp minimax envelope deliberately discards the source upper raw-curvature bound. When a useful finite upper bound is included, a smaller exact worst-case factor may be obtained by excluding inaccessible backtracking cells.

No claim is made that the minimax \(\eta\) is optimal for wall-clock performance on the source machine-learning experiments, where stochastic sampling costs and nonquadratic geometry also matter.

## References

1. N. Krklec Jerinkić, F. Porta, V. Ruggiero, I. Trombini, *Variable metric proximal stochastic gradient methods with additional sampling*, first public 23 January 2025; Computational Optimization and Applications 93, 157--207, DOI: 10.1007/s10589-025-00720-w.
2. S. Bonettini, I. Loris, F. Porta, M. Prato, *Variable Metric Inexact Line-Search-Based Methods for Nonsmooth Optimization*, SIAM Journal on Optimization 26, 891--921, DOI: 10.1137/15M1019325.
3. C. Paquette, K. Scheinberg, *A Stochastic Line Search Method with Expected Complexity Analysis*, SIAM Journal on Optimization 30, 349--376, DOI: 10.1137/18M1216250.
