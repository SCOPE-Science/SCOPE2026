# Amos can stall away from a scalar quadratic minimizer because its self-generated steps are summable
## Finding

Amos couples Adam-style gradient normalization to two internally generated decay factors. The defining paper motivates those factors heuristically and emphasizes that no externally specified terminal training horizon is required.

On a deterministic scalar quadratic, the memoryless second-moment endpoint of the published algorithm exposes a sharp obstruction: the self-generated normalized-gradient displacement becomes summable, so sufficiently large initial states never reach the minimizer.

Consider
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]
Run source-form Amos Algorithm 1 with no optional momentum and no gradient clipping. Choose
\[
\beta=0,
\qquad
0<\xi\le1,
\qquad
\eta>0,
\qquad
b_0=0,
\]
where \(\xi\) is Amos's global learning-rate parameter and \(\eta\) is its model-oriented scale parameter.

As long as
\[
x_t>0,
\]
the scalar gradient is
\[
g_t=\lambda x_t>0.
\]
At \(\beta=0\), the bias-corrected second-moment estimate is exactly
\[
\widehat v_t=g_t^2.
\]
Thus the normalized gradient loses all dependence on both the curvature and the magnitude of the state:
\[
\frac{g_t}{\sqrt{\widehat v_t}}=1.
\]

Write the source decay factors as
\[
c_t=
\left(
1+\frac{\sqrt{\xi}}{4}b_t
\right)^{-1/2},
\qquad
d_t=
\left(
1+\frac{\sqrt{\xi\eta}}{4}b_t
\right)^{-1}.
\]
The adaptive regularization coefficient is then
\[
\gamma_t=c_t\xi^2.
\]

Consequently the exact positive-branch recurrence is
\[
\boxed{
b_{t+1}
=
b_t+\xi^2c_t(1+b_t)
}
\]
and
\[
\boxed{
x_{t+1}
=
(1-r_t)x_t-s_t,
}
\]
where
\[
r_t=\frac{\xi^2}{2}c_td_t,
\qquad
s_t=\xi\eta d_t.
\]

The decay buffer has the exact asymptotic law
\[
\boxed{
\frac{b_t}{t^2}\longrightarrow\xi^{7/2}.
}
\]
Therefore
\[
c_t\sim\frac{2}{\xi^2t},
\qquad
d_t\sim\frac{4}{\xi^4\sqrt{\eta}\,t^2},
\]
and hence
\[
\boxed{
r_t\sim
\frac{4}{\xi^4\sqrt{\eta}\,t^3},
\qquad
s_t\sim
\frac{4\sqrt{\eta}}{\xi^3t^2}.
}
\]

Both sequences are summable:
\[
\sum_{t=0}^{\infty}r_t<\infty,
\qquad
\sum_{t=0}^{\infty}s_t<\infty.
\]

Because
\[
0<\xi\le1,
\]
we have
\[
0\le r_t\le\frac{\xi^2}{2}\le\frac12.
\]
Define
\[
P_0=1,
\qquad
P_t=\prod_{j=0}^{t-1}(1-r_j).
\]
Then
\[
P_t\downarrow P_\infty>0.
\]

Now define the finite positive threshold
\[
\boxed{
X_\star
=
\sum_{k=0}^{\infty}
\frac{s_k}{P_{k+1}}.
}
\]
For every initialization
\[
x_0>X_\star,
\]
the exact solution of the affine recurrence is
\[
x_t
=
P_t
\left(
x_0-
\sum_{k=0}^{t-1}
\frac{s_k}{P_{k+1}}
\right).
\]
Every bracket is positive, so this solution is self-consistent with the assumed positive-gradient branch. Taking the limit gives
\[
\boxed{
x_t
\longrightarrow
P_\infty(x_0-X_\star)>0.
}
\]

Thus source-form Amos can converge to a nonstationary point on a one-dimensional strongly convex quadratic.

The boundary is exact for the positive branch. If
\[
x_0=X_\star,
\]
then
\[
x_t
=
P_t
\sum_{k=t}^{\infty}
\frac{s_k}{P_{k+1}}
>0
\]
and
\[
x_t\longrightarrow0.
\]
If
\[
0<x_0<X_\star,
\]
the increasing partial sums in the exact representation eventually exceed \(x_0\), so the trajectory cannot remain on the positive branch forever.

## Assumptions and scope

The theorem uses the equations of source-form Amos Algorithm 1.

The second-moment parameter is the allowed endpoint
\[
\beta=0.
\]
This is deliberately a memoryless slice that isolates the optimizer's self-generated decay mechanism. It is not the paper's default
\[
\beta=0.999.
\]

The global learning-rate is constant and satisfies
\[
0<\xi\le1.
\]
The model-oriented scale satisfies
\[
\eta>0.
\]

Optional gradient clipping and optional momentum are disabled.

The objective is deterministic and scalar. The source paper is designed for noisy deep-learning gradients; this theorem therefore identifies a boundary behavior of the stated optimizer rather than a claim about its default large-model training regime.

The source algorithm as printed has no additive denominator regularizer in the displayed normalized-gradient formula. Implementations that add one are different dynamical systems near a zero gradient.

## Proof

At
\[
\beta=0,
\]
the source second-moment update gives
\[
v_t=g_t^2,
\]
and bias correction leaves
\[
\widehat v_t=g_t^2.
\]
For
\[
x_t>0,
\]
the normalized gradient is therefore one.

In one scalar coordinate,
\[
\operatorname{M}_2(g_t)^2=g_t^2,
\]
so the source adaptive regularization coefficient becomes
\[
\gamma_t
=
c_t\frac{\xi^2}{\widehat v_t}g_t^2
=
c_t\xi^2.
\]
Substitution into the source buffer and parameter updates gives the displayed recurrences.

To determine the decay rate, put
\[
p=\frac{\sqrt{\xi}}4.
\]
Then
\[
b_{t+1}-b_t
=
\xi^2\frac{1+b_t}{\sqrt{1+pb_t}}.
\]
The sequence is strictly increasing. It cannot be bounded, because a finite upper bound would leave its increments bounded below by a positive constant. Hence
\[
b_t\longrightarrow\infty.
\]

Moreover,
\[
\frac{b_{t+1}-b_t}{\sqrt{b_t}}
\longrightarrow
\frac{\xi^2}{\sqrt p}
=
2\xi^{7/4}.
\]
Since the increment is
\[
O(\sqrt{b_t}),
\]
we also have
\[
\frac{b_{t+1}}{b_t}\longrightarrow1.
\]
Therefore
\[
\sqrt{b_{t+1}}-\sqrt{b_t}
=
\frac{b_{t+1}-b_t}
{\sqrt{b_{t+1}}+\sqrt{b_t}}
\longrightarrow
\xi^{7/4}.
\]
By Stolz--Cesaro,
\[
\frac{\sqrt{b_t}}t
\longrightarrow
\xi^{7/4},
\]
which proves
\[
\frac{b_t}{t^2}
\longrightarrow
\xi^{7/2}.
\]

Substitution into the definitions of \(c_t\) and \(d_t\) gives their displayed asymptotics, and then the asymptotics of \(r_t\) and \(s_t\). In particular both series converge.

Because
\[
c_t\le1
\quad\text{and}\quad
d_t\le1,
\]
we have
\[
0\le r_t\le\xi^2/2\le1/2.
\]
A standard infinite-product criterion now gives
\[
P_\infty>0
\]
from
\[
\sum_t r_t<\infty.
\]
Since
\[
P_{k+1}\ge P_\infty,
\]
the series defining \(X_\star\) is finite.

Finally, iterating
\[
x_{t+1}=(1-r_t)x_t-s_t
\]
gives
\[
\frac{x_t}{P_t}
=
x_0-
\sum_{k=0}^{t-1}
\frac{s_k}{P_{k+1}}.
\]
The threshold conclusions follow directly.

## Verification

The accompanying `verify.py` reconstructs the memoryless source-form recurrence and independently evaluates the buffer, decay factors, affine coefficients, and positive-branch solution.

It checks the predicted limits
\[
\frac{b_t}{t^2}\to\xi^{7/2},
\qquad
t\,c_t\to\frac2{\xi^2},
\]
\[
t^2d_t\to\frac4{\xi^4\sqrt\eta},
\qquad
t^3r_t\to\frac4{\xi^4\sqrt\eta},
\qquad
t^2s_t\to\frac{4\sqrt\eta}{\xi^3}.
\]

For the concrete parameter choice
\[
\xi=\eta=1,
\]
the numerical partial products stabilize near
\[
P_\infty\approx0.17236
\]
and the threshold series near
\[
X_\star\approx16.404.
\]
A trajectory initialized at
\[
x_0=20
\]
stays positive over the replay horizon and approaches a positive value, in agreement with the exact theorem.

The finite replay is not used to establish the infinite-time claim; that claim follows from the analytic asymptotics and infinite-product argument above.

## Relationship to prior work

Tian and Parikh introduce Amos, specify its normalized-gradient update, adaptive weight decay, buffer recurrence, and the default forms of \(c_t\) and \(d_t\). They explicitly derive the decay factors heuristically and state that a rigorous convergence proof is left to future work.

The source already observes that both decay factors tend to zero and heuristically derives
\[
d_t\sim\frac1{q b_t},
\qquad
c_t\sim\frac1{\sqrt{p b_t}}
\]
for constants \(p,q>0\). Those asymptotic forms are prior work and are not claimed as new here.

The new point is what happens when the published recurrence is closed exactly on a deterministic strongly convex quadratic at the allowed endpoint
\[
\beta=0.
\]
Gradient normalization makes the buffer autonomous, the source decay then forces the normalized-gradient displacement to be summable, and the resulting affine recurrence has the explicit threshold \(X_\star\) separating minimizer convergence on the boundary from a family of nonstationary limits above it.

The source's comparison with classical SGD is also important context: it recalls the familiar nonsummable
\[
1/t
\]
learning-rate scale, whereas this deterministic normalized-gradient slice of Amos generates a
\[
1/t^2
\]
gradient displacement. The generic fact that summable step mass can prevent reaching a minimizer is not claimed as novel; the contribution is the exact derivation of that mechanism from Amos's own coupled buffer and decay equations.

Focused searches for Amos deterministic quadratic convergence, summable self-generated learning rates, nonstationary limits, and the memoryless second-moment endpoint did not identify an implication-equivalent published statement.

## Limitations

The counterexample uses
\[
\beta=0,
\]
not the default second-moment memory.

It analyzes the printed source algorithm without an additional denominator regularizer.

It is one-dimensional and deterministic, and it disables optional momentum and clipping.

The result does not imply that default Amos training on stochastic deep-learning problems stalls.

The theorem classifies the positive-gradient branch and proves an exact threshold for remaining on that branch. It does not classify the later sign-changing dynamics for initial states below \(X_\star\).

## References

1. Ran Tian and Ankur P. Parikh, “Amos: An Adam-style Optimizer with Adaptive Weight Decay towards Model-Oriented Scale,” arXiv:2210.11693v1, first submitted 2022-10-21; revised as arXiv:2210.11693v2.
