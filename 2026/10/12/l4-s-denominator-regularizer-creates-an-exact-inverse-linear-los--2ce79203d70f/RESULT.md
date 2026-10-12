# L4's denominator regularizer creates an exact inverse-linear loss tail
## Finding

The practical L4 rule adds a tiny constant to the denominator of its loss-based step for numerical stability. On the simplest convex quadratic, that constant eventually changes the asymptotic convergence class.

Consider
\[
L(x)=\frac12\lambda x^2,
\qquad
\lambda>0,
\]
and apply the practical L4 meta-algorithm with the SGD choice
\[
v=g=\nabla L=\lambda x.
\]
Use parameters
\[
0<\alpha\le2,
\qquad
0\le\gamma<1,
\qquad
0<\gamma_0\le1,
\qquad
\tau>0,
\qquad
\varepsilon>0.
\]

Let \(S_t\) be the stored minimum-loss state before the clamp at step \(t\), let
\[
M_t=\min\{S_t,L(x_t)\},
\]
and initialize
\[
S_0=\gamma_0L(x_0).
\]
After the L4 step, the source forgetting rule sets
\[
S_{t+1}=\left(1+\frac1\tau\right)M_t.
\]

Define
\[
q_t=\frac{M_t}{L(x_t)}\in(0,1].
\]
The parameter update has the exact form
\[
x_{t+1}=c_t x_t,
\]
where
\[
c_t
=
1-
\frac\alpha2(1-\gamma q_t)
\frac{\lambda^2x_t^2}{\lambda^2x_t^2+\varepsilon}.
\]
Under the stated parameter range,
\[
0<c_t<1.
\]
Therefore
\[
q_{t+1}
=
\min\left\{
1,
\left(1+\frac1\tau\right)
\frac{q_t}{c_t^2}
\right\}.
\]

As long as \(q_t<1\), this gives
\[
q_{t+1}>
\left(1+\frac1\tau\right)q_t.
\]
Hence the minimum-loss tracker reaches
\[
\boxed{q_t=1}
\]
after finitely many steps. More precisely, with \(q_0=\gamma_0\), lock occurs no later than
\[
\boxed{
N
=
\left\lceil
\frac{\log(1/\gamma_0)}
{\log(1+1/\tau)}
\right\rceil.
}
\]
Once \(q_t=1\), the inequality \(c_t^2<1\) makes the next clamp select the new current loss again, so the tracker remains locked forever.

After lock, set
\[
A=\frac{\alpha(1-\gamma)}2
\]
and
\[
z_t=\frac{\lambda^2x_t^2}{\varepsilon}.
\]
Then the exact scalar recurrence is
\[
\boxed{
z_{t+1}
=
z_t
\left(
1-A\frac{z_t}{1+z_t}
\right)^2.
}
\]
It has the sharp asymptotic law
\[
\boxed{
tz_t\longrightarrow\frac1{2A}.
}
\]
Because
\[
L(x_t)=\frac{\varepsilon}{2\lambda}z_t,
\]
we obtain
\[
\boxed{
tL(x_t)
\longrightarrow
\frac{\varepsilon}
{2\alpha(1-\gamma)\lambda}.
}
\]
Thus every fixed positive denominator regularizer produces an exact inverse-linear late loss tail on this scalar quadratic.

The contrast with the unregularized denominator is singular. If one formally sets
\[
\varepsilon=0,
\]
then after target lock
\[
x_{t+1}
=
\left[1-\frac{\alpha(1-\gamma)}2\right]x_t
\]
and therefore
\[
\boxed{
\frac{L(x_{t+1})}{L(x_t)}
=
\left[1-\frac{\alpha(1-\gamma)}2\right]^2.
}
\]
For a positive factor this is geometric convergence; at the endpoint where the factor vanishes, the minimizer is reached in one step.

With the source defaults
\[
\alpha=0.15,
\qquad
\gamma=0.9,
\qquad
\gamma_0=0.75,
\qquad
\tau=1000,
\qquad
\varepsilon=10^{-12},
\]
the universal tracker-lock bound is
\[
N\le288,
\]
and the exact asymptotic constant is
\[
\boxed{
tL(x_t)
\longrightarrow
\frac{3.333333\ldots\times10^{-11}}{\lambda}.
}
\]

## Assumptions and scope

The theorem uses the practical L4 minimum-loss tracker, optimism factor, forgetting rule, and denominator regularizer from the defining algorithm, specialized to the SGD direction \(v=g=\nabla L\).

The loss is deterministic, scalar, nonnegative, and quadratic. The result is not a stochastic-noise theorem and does not analyze L4Mom or L4Adam's additional moving-average states.

The condition \(0<\alpha\le2\) is a sufficient source-relevant range that keeps every scalar update factor strictly between zero and one when \(\varepsilon>0\). The source default \(\alpha=0.15\) lies well inside this range.

The asymptotic tail becomes visible only when \(\lambda^2x_t^2\) is comparable with or below \(\varepsilon\). For the source default \(\varepsilon=10^{-12}\), this is an extremely late, small-loss regime unless \(\lambda\) is also small.

## Proof

At step \(t\), write
\[
M_t=q_tL(x_t)
=
\frac12q_t\lambda x_t^2.
\]
The practical L4-SGD update is
\[
x_{t+1}
=
x_t-
\alpha
\frac{L(x_t)-\gamma M_t}
{\lambda^2x_t^2+\varepsilon}
\lambda x_t.
\]
Substitution yields
\[
x_{t+1}=c_tx_t
\]
with the stated \(c_t\). Since \(q_t\le1\), \(\gamma<1\), \(\varepsilon>0\), and \(\alpha\le2\), one has
\[
0<c_t<1.
\]
Thus
\[
L(x_{t+1})=c_t^2L(x_t).
\]
The source forgetting rule gives
\[
S_{t+1}=\left(1+\frac1\tau\right)M_t.
\]
The next clamp therefore gives
\[
q_{t+1}
=
\min\left\{
1,
\left(1+\frac1\tau\right)
\frac{q_t}{c_t^2}
\right\}.
\]
Since \(c_t^2<1\), any unlocked state grows by a factor larger than \(1+1/\tau\), proving finite lock and the displayed bound. Once locked, the same inequality makes the new current loss strictly smaller than the forgotten old reference, so lock is invariant.

After lock, \(q_t=1\), and the update reduces to
\[
x_{t+1}
=
x_t
\left[
1-A
\frac{\lambda^2x_t^2}
{\lambda^2x_t^2+\varepsilon}
\right].
\]
With \(z_t=\lambda^2x_t^2/\varepsilon\), this gives the displayed recurrence. The sequence \(z_t\) is positive and strictly decreasing. Its only possible limit is zero.

Set
\[
w_t=\frac1{z_t}.
\]
A direct calculation gives
\[
w_{t+1}-w_t
=
A
\frac{2+(2-A)z_t}
{[1+(1-A)z_t]^2}.
\]
Since \(z_t\to0\),
\[
w_{t+1}-w_t\to2A.
\]
Stolz--Cesaro therefore gives
\[
\frac{w_t}{t}\to2A,
\]
which is equivalent to
\[
tz_t\to\frac1{2A}.
\]
Multiplying by \(\varepsilon/(2\lambda)\) proves the loss limit.

## Verification

The accompanying `verify.py` reconstructs the practical L4 minimum-loss state, clamp, forgetting rule, SGD direction, and positive denominator regularizer.

It checks the finite tracker-lock bound over deterministic parameter grids, verifies the exact post-lock recurrence, confirms convergence of the scaled loss to the proved asymptotic constant, and checks the geometric post-lock law when the denominator regularizer is formally removed.

The computations are transcription guards. Finite tracker lock and the asymptotic constant are proved analytically above.

## Relationship to prior work

Rolínek and Martius introduce L4 as a practical loss-based stepsize meta-algorithm. The first public version already contains the minimum-loss clamp, optimism factor, forgetting timescale, denominator regularizer, and the defaults used here. The paper explicitly describes the denominator constant as a numerical-stability device and states that its practical heuristics and regularizers lose some exact properties of the simplified core rule.

The defining source also states that its motivation is closely related to Polyak's loss-based stepsize and explicitly declines to claim theoretical guarantees for L4. The inspected full text does not analyze the practical scalar quadratic recurrence, finite lock of the minimum-loss tracker, or the denominator-induced inverse-linear tail.

Later stochastic Polyak-stepsize theory proves convergence guarantees for methods that use optimal component losses or related lower-bound information. That theory establishes the broader importance of loss-based stepsizes but does not supply the practical L4 state recursion formed by its optimism, forgetting, and additive denominator regularizer.

A focused published-record comparison found a sharp quadratic result for scaled Polyak steps without L4's practical minimum-loss state or additive denominator constant. It does not imply the asymptotic law here.

## Limitations

The theorem does not cover momentum or Adam update directions.

It does not model minibatch fluctuations in the observed loss or gradient.

The exact inverse-linear regime is asymptotic and may begin below practically relevant numerical scales when \(\varepsilon\) is extremely small.

The theorem identifies a mathematical effect of the regularizer; it does not claim that the source default should be changed in practical deep-learning workloads.

## References

1. Michal Rolínek and Georg Martius, “L4: Practical loss-based stepsize adaptation for deep learning,” arXiv:1802.05074v1, first submitted 2018-02-14; NeurIPS 2018.
2. Nicolas Loizou, Sharan Vaswani, Issam Hadj Laradji, and Simon Lacoste-Julien, “Stochastic Polyak Step-size for SGD: An Adaptive Learning Rate for Fast Convergence,” Proceedings of AISTATS 2021, PMLR 130.
