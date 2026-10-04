# Exact curvature-clipping phase diagram for capped SPS on scalar quadratics
## Finding

Consider the finite sum
\[
f(x)=\frac1n\sum_{i=1}^n f_i(x),
\qquad
f_i(x)=\frac{a_i}{2}(x-b_i)^2,
\qquad
a_i>0.
\]
Each component minimum is
\[
f_i^\star=0,
\]
and the minimizer of the average objective is
\[
x^\star
=
\frac{\sum_{i=1}^n a_i b_i}{\sum_{i=1}^n a_i}.
\]

At every iteration sample \(i\) uniformly and use the bounded stochastic Polyak stepsize
\[
\gamma_i(x)
=
\min\left\{
\frac{f_i(x)-f_i^\star}
{c\,|f_i'(x)|^2},
\gamma_b
\right\},
\qquad
c\ge\frac12,
\qquad
\gamma_b>0.
\]
Put
\[
q=\frac{1}{2c},
\qquad
r_i=\min\{q,a_i\gamma_b\}.
\]
Then the update is exactly
\[
x^+=(1-r_i)x+r_i b_i.
\]
The formula extends continuously through \(x=b_i\), where the sampled gradient is zero and the iterate remains unchanged.

Because
\[
0<r_i\le1,
\]
every sampled affine map contracts differences by at most
\[
1-r_{\min}<1,
\qquad
r_{\min}=\min_i r_i.
\]
Hence the Markov chain has a unique stationary law and converges to it geometrically from every deterministic initial condition.

Its stationary mean is
\[
m
=
\frac{\sum_i r_i b_i}{\sum_i r_i},
\]
and its stationary variance is
\[
V
=
\frac{
\sum_i r_i^2(b_i-m)^2
}{
2\sum_i r_i-\sum_i r_i^2
}.
\]

These formulas reveal an exact interpretation of the cap. Since
\[
r_i
=
\gamma_b
\min\left\{
a_i,\frac{q}{\gamma_b}
\right\},
\]
the stationary mean is the minimizer of the clipped-curvature surrogate
\[
\widetilde f_{\gamma_b}(x)
=
\frac1{2n}
\sum_{i=1}^n
\min\left\{
a_i,\frac{q}{\gamma_b}
\right\}
(x-b_i)^2.
\]
Thus the upper stepsize bound is not merely a stability safeguard on this family: it determines which component curvatures are retained in the long-run target.

There are three exact regimes.

If
\[
0<\gamma_b\le\frac{q}{a_{\max}},
\]
then every component is cap-active:
\[
r_i=a_i\gamma_b.
\]
Consequently,
\[
m=x^\star.
\]
The stationary variance is
\[
V
=
\gamma_b
\frac{
\sum_i a_i^2(b_i-x^\star)^2
}{
2\sum_i a_i-\gamma_b\sum_i a_i^2
}.
\]
On this regime, capped SPS is exactly ordinary constant-step SGD with step \(\gamma_b\) on the sampled quadratics.

If
\[
\gamma_b\ge\frac{q}{a_{\min}},
\]
then no component is cap-active:
\[
r_i=q.
\]
The stationary mean becomes the unweighted component-center average
\[
m=\bar b=\frac1n\sum_i b_i,
\]
and the stationary variance is
\[
V
=
\frac{q}{2-q}
\frac1n
\sum_i(b_i-\bar b)^2.
\]
Both quantities are then independent of the curvatures \(a_i\). In particular, when
\[
c=\frac12,
\]
one has \(q=1\), so each update sets
\[
x^+=b_i
\]
exactly and the stationary law is the empirical distribution of the component minimizers.

Between those regimes, only the largest curvatures are clipped. The stationary target continuously interpolates between the true curvature-weighted minimizer and the curvature-blind center average through the clipped weights
\[
\min\left\{
a_i,\frac{q}{\gamma_b}
\right\}.
\]

For the two-component family
\[
b_1=1,
\qquad
b_2=-1,
\qquad
a_1>a_2>0,
\]
the true minimizer is
\[
x^\star=\frac{a_1-a_2}{a_1+a_2}.
\]
The exact stationary mean is
\[
m(\gamma_b)=
\begin{cases}
x^\star,
&
0<\gamma_b\le q/a_1,
\\[4pt]
\dfrac{q-a_2\gamma_b}{q+a_2\gamma_b},
&
q/a_1<\gamma_b<q/a_2,
\\[10pt]
0,
&
\gamma_b\ge q/a_2.
\end{cases}
\]
The middle branch decreases strictly from \(x^\star\) to \(0\). Therefore loosening the cap causes a sharp, fully explicit loss of objective consistency before reaching the completely curvature-blind regime.

Finally, since
\[
f(x)-f(x^\star)
=
\frac{\bar a}{2}(x-x^\star)^2,
\qquad
\bar a=\frac1n\sum_i a_i,
\]
the exact stationary expected suboptimality is
\[
\mathbb E[f(X_\infty)-f(x^\star)]
=
\frac{\bar a}{2}
\left[
(m-x^\star)^2+V
\right].
\]
This separates the cap-induced target bias from the irreducible constant-step sampling variance.

## Assumptions and scope

The theorem is one-dimensional, uses uniform independent component sampling, exact knowledge of each \(f_i^\star\), and the bounded SPS rule with fixed \(c\) and fixed cap \(\gamma_b\).

The restriction \(c\ge1/2\) is the strongly convex parameter range emphasized in the defining SPS work and ensures \(q\le1\), so each component map is a convex combination of the current iterate and its component minimizer.

The result concerns the stationary law of constant-parameter SPS with a fixed cap. It is distinct from decreasing-cap or decreasing-\(c_k\) schemes designed for exact convergence.

The uncapped curvature-blind target is not claimed as new. Later work on SPS dynamics already identified curvature cancellation and convergence toward the unweighted average of component minimizers in one-dimensional quadratics under decreasing steps. The novelty-bearing statement here is the exact fixed-cap curvature-clipping phase diagram and stationary bias-variance law.

## Proof

For
\[
f_i(x)=\frac{a_i}{2}(x-b_i)^2,
\]
one has
\[
f_i'(x)=a_i(x-b_i).
\]
Whenever \(x\ne b_i\),
\[
\frac{f_i(x)-f_i^\star}
{c\,|f_i'(x)|^2}
=
\frac{1}{2ca_i}.
\]
Hence
\[
a_i\gamma_i(x)
=
\min\left\{
\frac{1}{2c},
a_i\gamma_b
\right\}
=
r_i,
\]
and
\[
x^+
=
x-\gamma_i a_i(x-b_i)
=
(1-r_i)x+r_i b_i.
\]
At \(x=b_i\), both the gradient update and the affine formula leave \(x\) fixed.

For two trajectories driven by the same sampled indices,
\[
|x_{k+1}-y_{k+1}|
=
(1-r_{i_k})|x_k-y_k|
\le
(1-r_{\min})|x_k-y_k|.
\]
Thus the random affine system is uniformly contractive and has a unique invariant probability law.

Let \(X\) have the stationary law and let \(I\) be an independent uniform component index. Then
\[
X\overset d=(1-r_I)X+r_I b_I.
\]
Taking expectations gives
\[
m
=
(1-\bar r)m
+
\frac1n\sum_i r_i b_i,
\qquad
\bar r=\frac1n\sum_i r_i,
\]
so
\[
m=\frac{\sum_i r_i b_i}{\sum_i r_i}.
\]

Write
\[
Y=X-m.
\]
Since
\[
\sum_i r_i(b_i-m)=0,
\]
the centered recursion is
\[
Y^+
=
(1-r_I)Y+r_I(b_I-m).
\]
At stationarity \(Y\) is independent of the fresh index and has zero mean. Therefore
\[
V
=
\frac1n\sum_i(1-r_i)^2V
+
\frac1n\sum_i r_i^2(b_i-m)^2.
\]
Rearranging gives
\[
V
=
\frac{
\sum_i r_i^2(b_i-m)^2
}{
2\sum_i r_i-\sum_i r_i^2
}.
\]
The denominator is positive because each \(r_i\in(0,1]\).

The clipped-curvature interpretation follows by factoring \(\gamma_b\) from \(r_i\). The all-capped and all-uncapped formulas are direct substitutions.

For the two-component example, the cap thresholds are
\[
\frac{q}{a_1}
<
\frac{q}{a_2}.
\]
Below the first threshold,
\[
(r_1,r_2)=\gamma_b(a_1,a_2).
\]
Between the thresholds,
\[
(r_1,r_2)=(q,a_2\gamma_b).
\]
Above the second threshold,
\[
(r_1,r_2)=(q,q).
\]
Substitution into
\[
m=\frac{r_1-r_2}{r_1+r_2}
\]
gives the displayed phase diagram. On the mixed branch,
\[
\frac{\mathrm d m}{\mathrm d\gamma_b}
=
-\frac{2qa_2}{(q+a_2\gamma_b)^2}<0.
\]

The objective-gap identity follows by completing the square in the average quadratic.

## Verification

The accompanying `verify.py` checks the SPS reduction, stationary moment equations, all-capped and all-uncapped formulas, the two-component phase boundaries, and deterministic finite-depth enumeration against the exact moment recursion.

The finite enumeration is a transcription guard only. Existence and uniqueness of the stationary law follow from uniform contraction, and its exact first two moments follow from the distributional fixed-point equations above.

## Relationship to prior work

Loizou, Vaswani, Laradji, and Lacoste-Julien introduced SPS and its bounded variant \(\mathrm{SPS}_{\max}\). Their definition uses the component optimal values and caps the adaptive step by \(\gamma_b\); the cap is described as essential for convergence to a small neighborhood in the non-interpolating setting. Their general theory bounds that neighborhood but does not give the exact stationary target or covariance on heterogeneous scalar quadratics.

Orvieto, Lacoste-Julien, and Loizou later identified a fundamental bias of SPS outside interpolation. Their one-dimensional quadratic analysis shows that the Polyak ratio cancels component curvature and, for decreasing scaling with a sufficiently loose cap, drives the method toward the unweighted average of component minimizers rather than the true curvature-weighted minimizer. That prior result covers the curvature-blind limiting target in the loose-cap regime.

The finite-cap regime is different. The same algebra shows that \(\gamma_b\) selectively clips large curvature weights rather than merely limiting the numerical size of the update. The inspected SPS-dynamics paper explicitly takes \(\gamma_b\) large enough to make the cap inactive in its counterexample and does not state the clipped-curvature stationary law or its phase thresholds.

Gower, Blondel, Gazagnadou, and Pedregosa give a variational interpretation of \(\mathrm{SPS}_{\max}\) and emphasize that its cap parameter still needs careful tuning outside interpolation. Their analysis motivates slack-based replacements, but the inspected text does not provide the exact quadratic cap-to-bias map above.

## Limitations

The exact phase diagram uses scalar quadratics. In multiple dimensions, component Hessians need not commute and a scalar cap no longer reduces the target to simple clipped curvature weights.

The stationary law is for fixed positive \(\gamma_b\). Tightening the cap over time changes the process and can recover exact convergence under different assumptions.

A tight cap removes target bias on this quadratic family because every component update becomes ordinary constant-step SGD, but it does not remove stationary sampling variance at a fixed positive cap.

The result assumes exact component minima \(f_i^\star\). Estimating or replacing them changes the affine map.

Equivalent random-affine calculations may exist in stochastic approximation under non-SPS terminology; this remains the principal originality risk.

## References

1. Nicolas Loizou, Sharan Vaswani, Issam Hadj Laradji, and Simon Lacoste-Julien, “Stochastic Polyak Step-size for SGD: An Adaptive Learning Rate for Fast Convergence,” arXiv:2002.10542v1, 2020.
2. Antonio Orvieto, Simon Lacoste-Julien, and Nicolas Loizou, “Dynamics of SGD with Stochastic Polyak Stepsizes: Truly Adaptive Variants and Convergence to Exact Solution,” arXiv:2205.04583v1, 2022.
3. Robert M. Gower, Mathieu Blondel, Nidham Gazagnadou, and Fabian Pedregosa, “Cutting Some Slack for SGD with Adaptive Polyak Stepsizes,” arXiv:2202.12328v1, 2022.
