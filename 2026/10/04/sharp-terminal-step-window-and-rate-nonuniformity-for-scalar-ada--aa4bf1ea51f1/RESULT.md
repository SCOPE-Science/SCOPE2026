# Sharp terminal-step window and rate nonuniformity for scalar AdaGrad-Norm
## Finding

Consider deterministic AdaGrad-Norm on
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0,
\]
with
\[
b_0>0,
\qquad
\eta>0,
\qquad
x_0\ne0.
\]
The iteration is
\[
b_{t+1}^2=b_t^2+\lambda^2x_t^2,
\]
\[
x_{t+1}
=
\left(
1-\frac{\eta\lambda}{b_{t+1}}
\right)x_t.
\]

Then \(b_t\) converges to a finite limit \(b_\infty\), \(x_t\to0\), and every nontrivial trajectory satisfies the strict terminal inequality
\[
b_\infty>\frac{\eta\lambda}{2}.
\]
Equivalently, the limiting normalized effective gradient-descent step
\[
\theta_\infty
=
\frac{\eta\lambda}{b_\infty}
\]
always belongs to
\[
0<\theta_\infty<2.
\]
Thus scalar AdaGrad-Norm self-stabilizes into exactly the open scalar gradient-descent stability window.

Unless the method reaches \(x=0\) in finite time,
\[
\lim_{t\to\infty}
\frac{|x_{t+1}|}{|x_t|}
=
\left|1-\theta_\infty\right|
<1.
\]
So the terminal accumulator determines the exact asymptotic linear factor. If \(\theta_\infty<1\), the tail is sign-preserving; if \(\theta_\infty>1\), the tail alternates sign; if \(\theta_\infty=1\) and the minimizer is not hit earlier, the ratio limit is zero.

The stable terminal window is sharp over initializations and hyperparameters:
\[
\inf \theta_\infty=0,
\qquad
\sup \theta_\infty=2.
\]
Neither endpoint is attained by a nontrivial trajectory. Consequently,
\[
\sup
\left|1-\theta_\infty\right|
=
1.
\]
Parameter-robust convergence therefore does not imply a uniform asymptotic contraction factor bounded away from one.

The central point
\[
\theta_\infty=1
\]
is attainable exactly by finite annihilation. In particular, one-step annihilation occurs when
\[
b_0^2+\lambda^2x_0^2
=
\eta^2\lambda^2.
\]
Then
\[
b_1=\eta\lambda,
\qquad
x_1=0.
\]

There is also an explicit finite bound on the potentially noncontractive startup. Define
\[
M
=
\#\left\{
t\ge0:
b_{t+1}\le\frac{\eta\lambda}{2}
\right\}.
\]
Because \(b_t\) is nondecreasing, these indices form an initial segment. Their number satisfies
\[
M
\le
\left\lfloor
\frac{
\left(\eta^2\lambda^2/4-b_0^2\right)_+
}{
\lambda^2x_0^2
}
\right\rfloor.
\]
After this initial segment,
\[
|x_{t+1}|<|x_t|
\]
at every nonzero step.

## Assumptions and scope

The objective is a deterministic one-dimensional positive quadratic. The result uses the scalar AdaGrad-Norm convention in which the current gradient is first added to the accumulator and the resulting \(b_{t+1}\) is used in the same iteration.

The initial point is assumed nonoptimal. If \(x_0=0\), the algorithm is already stationary and no stability restriction on the unused effective step is meaningful.

The theorem concerns the exact asymptotic behavior of one curvature mode. It does not claim that a multidimensional AdaGrad-Norm trajectory has a single modal contraction factor, because all coordinates share the same accumulator.

The literature already proves robust convergence, bounded accumulators, a descent threshold near \(b>\eta L/2\), and linear convergence under strongly convex assumptions. Those facts are not claimed as new. The novelty-bearing part is the sharp scalar terminal-step phase portrait: both edges of the open stable interval are approachable, the exact tail factor follows from the terminal accumulator, there is no hyperparameter-uniform contraction rate, and the pre-threshold noncontractive phase has an explicit count bound.

## Proof

Scale the variables by
\[
r_t=\frac{b_t}{\eta\lambda},
\qquad
z_t=\frac{x_t}{\eta}.
\]
Then the dynamics become parameter free:
\[
r_{t+1}^2=r_t^2+z_t^2,
\]
\[
z_{t+1}
=
\left(
1-\frac1{r_{t+1}}
\right)z_t.
\]

First, \(r_t\) is nondecreasing. We show it is bounded.

If \(r_t<1\) for every \(t\), boundedness is immediate. Otherwise, let \(T\) be the first index with
\[
r_T\ge1.
\]
For \(t\ge T\), put
\[
A_t=z_t^2.
\]
Then
\[
r_{t+1}-r_t
=
\frac{A_t}{r_{t+1}+r_t},
\]
while
\[
A_t-A_{t+1}
=
A_t
\left(
\frac{2}{r_{t+1}}
-
\frac{1}{r_{t+1}^2}
\right).
\]
Since
\[
r_{t+1}\ge r_t\ge1,
\]
one has
\[
A_t-A_{t+1}
\ge
r_{t+1}-r_t.
\]
Therefore
\[
r_{N+1}-r_T
\le
A_T-A_{N+1}
\le
A_T
\]
for every \(N\ge T\). Hence \(r_t\) is bounded and has a finite limit \(r_\infty\).

Because
\[
z_t^2
=
r_{t+1}^2-r_t^2,
\]
convergence of \(r_t\) implies
\[
z_t\to0.
\]

Now suppose, toward a contradiction, that
\[
r_\infty\le\frac12.
\]
Monotonicity then gives
\[
r_{t+1}\le\frac12
\]
for every \(t\). Hence
\[
\left|
1-\frac1{r_{t+1}}
\right|
\ge1,
\]
so
\[
|z_{t+1}|\ge|z_t|.
\]
Since \(z_0\ne0\), this contradicts \(z_t\to0\). Therefore
\[
r_\infty>\frac12.
\]
Returning to the original variables gives
\[
b_\infty>\frac{\eta\lambda}{2}
\]
and
\[
0<
\theta_\infty=\frac1{r_\infty}
<2.
\]

If no iterate reaches zero, division by \(z_t\) is valid and
\[
\frac{|z_{t+1}|}{|z_t|}
=
\left|
1-\frac1{r_{t+1}}
\right|.
\]
Taking limits yields
\[
\lim_{t\to\infty}
\frac{|x_{t+1}|}{|x_t|}
=
\left|
1-\frac1{r_\infty}
\right|
=
|1-\theta_\infty|.
\]

Finite termination occurs precisely when, for some nonzero \(z_t\),
\[
r_{t+1}=1.
\]
For one-step termination this is
\[
r_1^2=r_0^2+z_0^2=1,
\]
which is exactly
\[
b_0^2+\lambda^2x_0^2=\eta^2\lambda^2.
\]

To bound the startup phase, observe that whenever
\[
r_{t+1}\le\frac12,
\]
one has
\[
|z_{t+1}|\ge|z_t|.
\]
Because \(r_t\) is nondecreasing, all such indices occur consecutively from the start. If there are \(M\) of them, then
\[
r_M^2
=
r_0^2+\sum_{t=0}^{M-1}z_t^2
\ge
r_0^2+Mz_0^2.
\]
Also
\[
r_M\le\frac12.
\]
Therefore
\[
M
\le
\frac{1/4-r_0^2}{z_0^2}
\]
whenever the numerator is positive, and \(M=0\) otherwise. This gives the displayed bound in the original variables.

It remains to show that the terminal interval is sharp.

For the lower edge, choose \(r_0=R>1\) and any nonzero \(z_0\). Since
\[
r_\infty\ge r_0=R,
\]
one has
\[
\theta_\infty\le\frac1R.
\]
Letting \(R\to\infty\) gives
\[
\inf\theta_\infty=0.
\]

For the upper edge, fix any
\[
\frac12<r_0<1
\]
and define
\[
q_0=\frac1{r_0}-1\in(0,1).
\]
If
\[
r_0^2+\frac{z_0^2}{1-q_0^2}<1,
\]
then induction gives
\[
r_t<1
\]
and
\[
|z_t|\le q_0^t|z_0|.
\]
Consequently,
\[
r_\infty^2
\le
r_0^2+\frac{z_0^2}{1-q_0^2}.
\]
Choose a sequence \(r_0\downarrow1/2\) and nonzero \(z_0\to0\) so fast that the second term vanishes. Then
\[
r_\infty\downarrow\frac12
\]
and therefore
\[
\theta_\infty\uparrow2.
\]
This proves
\[
\sup\theta_\infty=2.
\]
The same construction has \(r_t<1\) throughout, so it also realizes an alternating tail arbitrarily close to the oscillatory stability edge.

## Verification

The accompanying `verify.py` reconstructs the scaled recurrence, checks the one-step annihilation surface, verifies the startup-count inequality on a deterministic grid, tests the exact ratio limit, and constructs families approaching both sharp terminal-step endpoints.

The finite computations do not prove the infinite statements. Boundedness of the accumulator, strict terminal stability, the exact ratio limit, and endpoint sharpness are established analytically above.

## Relationship to prior work

Ward, Wu, and Bottou introduced AdaGrad-Norm as a single-scalar adaptive stepsize and proved deterministic and stochastic convergence guarantees robust to arbitrary positive hyperparameters. Their defining update is exactly the one used here, but their analysis does not give the sharp scalar set of attainable terminal effective steps.

Xie, Wu, and Ward later proved linear convergence under strong convexity and described a two-stage mechanism: the accumulator grows through a startup regime, eventually enters a descent regime after a threshold proportional to \(\eta L/2\), remains bounded, and approaches a constant. Those results cover the qualitative self-stabilization mechanism. The present scalar result does not claim that mechanism as new. It identifies the sharp terminal interval, its unattained but approachable endpoints, the exact asymptotic factor, and the resulting absence of any hyperparameter-uniform contraction rate.

Traoré and Pauwels proved sequential convergence of scalar and coordinatewise AdaGrad for smooth convex objectives and showed summability of squared gradients. Their full proof establishes convergence of the iterate sequence, but it does not classify the terminal normalized step on a scalar quadratic or the sharp endpoint families above.

Targeted searches for AdaGrad-Norm terminal accumulators, limiting effective steps, exact scalar quadratic factors, and terminal stability edges did not identify a source stating the sharp endpoint classification.

## Limitations

The terminal value \(b_\infty\) is history dependent; the theorem does not provide a closed-form formula for it from arbitrary initial data.

The sharp endpoint statement is over initializations and hyperparameters. It does not say that one fixed initialization can realize every point in the terminal interval.

The result is deterministic. Persistent stochastic gradient noise typically makes the accumulator grow without converging to a finite terminal constant.

The scalar factor does not directly extend to multiple curvatures because AdaGrad-Norm uses one shared accumulator.

The exact terminal classification may have an equivalent formulation in older adaptive-filter or stochastic-approximation literature under terminology unrelated to AdaGrad-Norm; this remains the principal originality risk.

## References

1. Rachel Ward, Xiaoxia Wu, and Leon Bottou, “AdaGrad stepsizes: Sharp convergence over nonconvex landscapes,” arXiv:1806.01811v1, 2018.
2. Yuege Xie, Xiaoxia Wu, and Rachel Ward, “Linear Convergence of Adaptive Stochastic Gradient Descent,” arXiv:1908.10525v1, 2019.
3. Cheik Traoré and Edouard Pauwels, “Sequential convergence of AdaGrad algorithm for smooth convex optimization,” arXiv:2011.12341v1, 2020.
