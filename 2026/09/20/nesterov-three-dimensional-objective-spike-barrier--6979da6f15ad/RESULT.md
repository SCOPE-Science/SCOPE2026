# Three-dimensional onset of objective spikes in exact-parameter Nesterov acceleration

Same-model review: passed. Independent audit: not yet performed.

## Setting

Consider the real strongly convex quadratic
\[
f(x)=\tfrac12(x-x_*)^T A(x-x_*),\qquad A\succ0,
\]
with exact spectral endpoints \(\mu=\lambda_{\min}(A)\),
\(L=\lambda_{\max}(A)\), and \(\kappa=L/\mu\). Translate so that \(x_*=0\).
For \(\kappa>1\), set
\[
q=\sqrt{\mu/L}=\kappa^{-1/2},\qquad
\beta=\frac{1-q}{1+q}.
\]
We study the classical strongly-convex Nesterov iteration with exact spectral
calibration and standard zero-momentum initialization:
\[
y_0=x_0,\qquad
x_{k+1}=y_k-L^{-1}Ay_k,\qquad
y_{k+1}=x_{k+1}+\beta(x_{k+1}-x_k).
\]
Equivalently,
\[
x_1=(I-A/L)x_0,
\]
and for \(k\ge1\),
\[
x_{k+1}=(I-A/L)\bigl((1+\beta)x_k-\beta x_{k-1}\bigr).
\]
All statements below are in exact arithmetic and concern the objective values
\(f(x_k)\).

## Main result

### Theorem 1: two-point spectra are objective-monotone

If \(\sigma(A)\subseteq\{\mu,L\}\), then both \(\|x_k\|_2\) and
\(f(x_k)\) are nonincreasing for every initial point. Consequently, every
\(2\times2\) SPD quadratic with exact condition number \(\kappa>1\) has a
monotone objective trajectory under the iteration above. For \(\kappa=1\),
the first gradient step reaches the minimizer exactly.

### Theorem 2: dimension three is sufficient and sharp

For every \(\kappa>1\), there is a \(3\times3\) SPD quadratic with exact
condition number \(\kappa\) for which the objective increases. More strongly,
for one fixed such matrix and fixed \(\kappa\), the local ratio
\(f(x_3)/f(x_2)\) is unbounded over nonstationary initial points.

After scaling \(L=1\), take
\[
A=\operatorname{diag}\!\left(q^2,\frac{1+q}{2},1\right),
\qquad x_0=(\varepsilon,1,0)^T,\quad \varepsilon>0.
\]
Then \(x_2\ne0\) for every \(\varepsilon>0\), but
\[
\frac{f(x_3)}{f(x_2)}\longrightarrow\infty
\qquad(\varepsilon\downarrow0).
\]
Hence three is the minimum dimension in which objective nonmonotonicity can
occur under exact endpoint calibration and standard initialization. At least three
distinct curvature modes are therefore necessary, and the explicit construction
shows that three can suffice. There is no finite bound depending only on \(\kappa\) for the one-step relative
objective increase \(f(x_{k+1})/f(x_k)\), even when dimension is fixed at three.

## Proof

Diagonalize \(A\). For a normalized eigenvalue \(t=\lambda/L\), let
\(p_k(t)\) be the scalar multiplier taking the initial component to the
\(k\)-th iterate. Then
\[
p_0(t)=1,\qquad p_1(t)=1-t,
\]
and
\[
p_{k+1}(t)=(1-t)\bigl((1+\beta)p_k(t)-\beta p_{k-1}(t)\bigr).
\]

At the upper endpoint \(t=1\),
\[
p_k(1)=0\qquad(k\ge1).
\]
At the lower endpoint \(t=q^2\), the recurrence has a repeated root
\(1-q\), and direct induction gives
\[
\boxed{p_k(q^2)=(1+kq)(1-q)^k.}
\]
Moreover,
\[
\frac{p_{k+1}(q^2)}{p_k(q^2)}
=(1-q)\frac{1+(k+1)q}{1+kq}<1,
\]
because
\[
1+kq-(1-q)(1+(k+1)q)=(k+1)q^2>0.
\]
Thus every modal magnitude decreases when the spectrum contains only the two
endpoints, proving Theorem 1.

For the dimension-three construction, compute
\[
p_2(t)=(1-t)\bigl(1-(1+\beta)t\bigr).
\]
It has the interior zero
\[
t_* = \frac{1}{1+\beta}=\frac{1+q}{2}\in(q^2,1).
\]
At this curvature,
\[
p_1(t_*)=\frac{1-q}{2},\qquad p_2(t_*)=0,
\]
while momentum revives the mode one step later:
\[
\boxed{p_3(t_*)=-\frac{(1-q)^3}{4(1+q)}\ne0.}
\]
For the low-curvature endpoint,
\[
p_2(q^2)=(1+2q)(1-q)^2,
\qquad
p_3(q^2)=(1+3q)(1-q)^3.
\]
Therefore, with \(r=1-q\),
\[
f(x_2)=\frac12 q^2\varepsilon^2(1+2q)^2r^4,
\]
and
\[
f(x_3)=\frac12\left[
q^2\varepsilon^2(1+3q)^2r^6
+\frac{1+q}{2}\frac{r^6}{16(1+q)^2}
\right].
\]
In particular,
\[
\boxed{
\frac{f(x_3)}{f(x_2)}
\sim
\frac{(1-q)^2}{32q^2(1+q)(1+2q)^2}\,\varepsilon^{-2}
}
\qquad(\varepsilon\downarrow0),
\]
which proves Theorem 2. The denominator remains positive for every
\(\varepsilon>0\), so the divergence is not an artifact of dividing by an
exactly zero objective value.

The limiting case \(\varepsilon=0\) is also informative: \(x_2=0\) exactly
but \(x_3\ne0\) if the recurrence is continued. A practical method that tests
for a zero gradient would terminate at \(x_2\); the positive-\(\varepsilon\)
family above removes that stopping-rule issue.

## Comparison with nonaccelerated gradient descent

With the same exact \(L\), gradient descent satisfies
\[
f(x_{k+1})\le (1-\mu/L)^2 f(x_k)
\]
for every SPD quadratic, so it is stepwise objective-monotone. Classical
Nesterov acceleration improves the global condition-number dependence of
first-order convergence from the gradient-descent scale \(\kappa\) to the
accelerated scale \(\sqrt\kappa\), but the theorem above shows that this does
not imply any finite local objective-ratio control once an interior curvature
mode is present. Objective-based restart or monotonicity safeguards address a
real behavior even in exact SPD quadratics with perfectly calibrated spectral
parameters.

## Relation to prior literature

Nesterov's classical analysis supplies the strongly-convex accelerated method
and its global rate. O'Donoghue and Candes (2015) document oscillatory behavior
of accelerated schemes and motivate function-value and gradient restart tests.
Hagedorn and Jarre (2024) give a theorem-level spectral analysis of fixed-step
Nesterov and Polyak methods on strongly convex quadratics; their Nesterov section
uses the corresponding two-state modal matrix and establishes iteration-complexity
bounds, while their explicit low-dimensional nonmonotonic examples concern
iterate-distance/momentum behavior rather than the minimum dimension for
objective increase proved here. Bach (2026) studies asymptotic Nesterov behavior
for quadratic problems by z-transforms, including oscillatory regimes, under a
different time-varying acceleration setting.

Searches over objective/function-value monotonicity, overshoot, restart,
quadratic spectral recurrences, iteration-polynomial roots, low-dimensional
examples, and recent acceleration analyses did not locate the exact combination
proved here: endpoint-spectrum objective monotonicity, the sharp dimension-three
onset, the explicit interior annihilation/revival curvature, and an unbounded
positive-denominator local objective ratio for fixed \(\kappa\). Accordingly,
originality is claimed only to the best of our knowledge.

## Scientific limitations

The result assumes exact real arithmetic, an unconstrained SPD quadratic,
exact knowledge of the true spectral endpoints \(\mu,L\), the classical
strongly-convex constant momentum \(\beta=(\sqrt\kappa-1)/(\sqrt\kappa+1)\),
and the standard zero-momentum initialization. Loose spectral bounds can alter
the two-dimensional conclusion. The result does not cover the convex
non-strongly-convex time-varying Nesterov coefficient rule, FISTA, heavy-ball, composite
objectives, adaptive or restarted variants, stochastic/inexact gradients, or
finite precision. The unbounded quantity is the local relative ratio
\(f(x_{k+1})/f(x_k)\), created by an arbitrarily small denominator; it does not
imply divergence or unbounded absolute objective values, and it is fully
compatible with the usual global accelerated convergence guarantees.

Historical acceleration, semi-iterative, and polynomial-iteration literature is
broad. Although the most relevant accessible classical and current sources were
checked, an equivalent observation may exist under different terminology.

## Reproducibility

`artifacts/verify.py` deterministically checks the endpoint formulas, rotated
endpoint-spectrum examples, the interior annihilation/revival identity, and the
\(\varepsilon^{-2}\) asymptotic. `artifacts/verification.txt` records the
verified output.

## References

- Y. Nesterov, *Introductory Lectures on Convex Optimization: A Basic Course*, Springer, 2004. https://doi.org/10.1007/978-1-4419-8853-9
- B. O'Donoghue and E. Candes, "Adaptive Restart for Accelerated Gradient Schemes," *Foundations of Computational Mathematics* 15, 715-732 (2015). https://doi.org/10.1007/s10208-013-9150-3
- M. Hagedorn and F. Jarre, "Iteration Complexity of Fixed-Step Methods by Nesterov and Polyak for Convex Quadratic Functions," *Journal of Optimization Theory and Applications* 202, 456-474 (2024). https://doi.org/10.1007/s10957-023-02261-w
- F. Bach, "On the Effectiveness of the z-Transform Method in Quadratic Optimization," *Journal of Machine Learning Research* 27(180), 1-43 (2026). https://www.jmlr.org/papers/v27/25-1621.html
