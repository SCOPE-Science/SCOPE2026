# The discrete PID optimizer is curvature-dependent heavy ball on quadratics
## Finding

Consider the discrete PID optimizer introduced for deep-network training, specialized to the deterministic symmetric positive-definite quadratic
\[
f(x)=\frac12x^\top Hx,
\qquad
0<\mu I\preceq H\preceq LI.
\]
The source recurrences are
\[
V_{t+1}=\alpha V_t-rHx_t,
\]
\[
D_{t+1}=\alpha D_t+(1-\alpha)H(x_t-x_{t-1}),
\]
\[
x_{t+1}=x_t+V_{t+1}+K_dD_{t+1},
\]
with
\[
0<\alpha<1,
\qquad
r>0,
\qquad
K_d\ge0.
\]

After the first update, the two auxiliary states can be eliminated exactly:
\[
\boxed{
x_{t+1}
=
(I-rH)x_t
+
\bigl[\alpha I+K_d(1-\alpha)H\bigr](x_t-x_{t-1}).
}
\]
Thus every Hessian eigenmode of curvature
\[
\lambda
\]
is exactly a heavy-ball recurrence with curvature-dependent momentum
\[
\boxed{
\beta(\lambda)
=
\alpha+K_d(1-\alpha)\lambda.
}
\]

For all eigenvalues in
\[
[\mu,L],
\]
the induced parameter recurrence is asymptotically Schur stable if and only if
\[
\boxed{K_dL<1}
\]
and
\[
\boxed{
0<rL
<
2\bigl[1+\alpha+K_d(1-\alpha)L\bigr].
}
\]

The first condition is a hard derivative-gain ceiling. If
\[
K_dL\ge1,
\]
then the highest-curvature mode is not asymptotically stable for **any** positive learning rate.

The modewise characteristic roots have product
\[
\beta(\lambda).
\]
Therefore every positive learning rate obeys
\[
\rho_\lambda
\ge
\sqrt{\beta(\lambda)}.
\]
This lower bound is sharp. Choosing
\[
r\lambda=1+\beta(\lambda)
\]
makes the characteristic polynomial
\[
z^2+\beta(\lambda),
\]
so both roots have modulus
\[
\sqrt{\beta(\lambda)}.
\]
Hence the exact best asymptotic contraction factor attainable on an isolated quadratic mode, after optimizing the learning rate, is
\[
\boxed{
\inf_{r>0}\rho_\lambda
=
\sqrt{\alpha+K_d(1-\alpha)\lambda}.
}
\]
For every
\[
K_d>0,
\]
this best possible modal rate floor increases strictly with curvature.

There is also an exact loss-scale consequence. Replace the objective by
\[
\widetilde f=c f,
\qquad c>0.
\]
Its Hessian is
\[
cH.
\]
The hard stability condition becomes
\[
K_dcL<1.
\]
Thus, for any fixed positive derivative gain, multiplying the loss by a sufficiently large positive constant makes the high-curvature mode unstable regardless of how small the positive learning rate is chosen.

The derivative state is therefore not an independent damping channel on a fixed quadratic Hessian. After elimination, it is exactly a positive momentum increment that grows linearly with curvature.

## Assumptions and scope

The theorem concerns the discrete PID optimizer recurrences printed in the defining and extended deep-learning papers.

The objective is deterministic and quadratic with a constant SPD Hessian. The result concerns the exact linear recurrence in this model, not a stochastic minibatch approximation.

The momentum and derivative moving averages use the same source coefficient
\[
\alpha.
\]
The derivative gain is nonnegative.

The second-order parameter recurrence holds from the first completed source update onward. The auxiliary states have their own homogeneous factor
\[
\alpha,
\]
which is stable because
\[
0<\alpha<1.
\]
When the parameter recurrence converges, the driven auxiliary states converge as well.

No claim is made that a positive derivative gain is always harmful in nonlinear or stochastic training. It can change transient root geometry for a fixed learning rate. The theorem identifies its exact fixed-Hessian interpretation and stability constraints.

## Proof

From the preceding source parameter update,
\[
x_t=x_{t-1}+V_t+K_dD_t.
\]
Therefore
\[
V_t+K_dD_t=x_t-x_{t-1}.
\]

Substituting the source updates gives
\[
\begin{aligned}
x_{t+1}
&=
x_t+\alpha V_t-rHx_t
+K_d\left[\alpha D_t+(1-\alpha)H(x_t-x_{t-1})\right]\\
&=
x_t-rHx_t
+\alpha(V_t+K_dD_t)
+K_d(1-\alpha)H(x_t-x_{t-1})\\
&=
(I-rH)x_t
+\left[\alpha I+K_d(1-\alpha)H\right](x_t-x_{t-1}).
\end{aligned}
\]

Diagonalize
\[
H=Q\Lambda Q^\top.
\]
An eigenmode of curvature
\[
\lambda
\]
obeys
\[
u_{t+1}
=
\left[1-r\lambda+\beta(\lambda)\right]u_t
-
\beta(\lambda)u_{t-1},
\]
where
\[
\beta(\lambda)=\alpha+K_d(1-\alpha)\lambda.
\]
Its characteristic polynomial is
\[
z^2-
\left[1-r\lambda+\beta(\lambda)\right]z
+
\beta(\lambda).
\]

For a real monic quadratic
\[
z^2+a_1z+a_2,
\]
the strict Jury conditions are
\[
1+a_1+a_2>0,
\qquad
1-a_1+a_2>0,
\qquad
1-a_2>0.
\]
They become
\[
r\lambda>0,
\]
\[
r\lambda<2\left[1+\beta(\lambda)\right],
\]
and
\[
\beta(\lambda)<1.
\]

Because
\[
K_d\ge0,
\]
the modal momentum is increasing in
\[
\lambda.
\]
Thus
\[
\beta(\lambda)<1
\quad\text{for every }\lambda\in[\mu,L]
\]
is equivalent to
\[
\alpha+K_d(1-\alpha)L<1.
\]
Since
\[
\alpha<1,
\]
this is exactly
\[
K_dL<1.
\]

The other nontrivial Jury inequality is
\[
r
<
2\left[\frac{1+\alpha}{\lambda}+K_d(1-\alpha)\right].
\]
Its right-hand side decreases with
\[
\lambda,
\]
so the worst curvature is again
\[
L.
\]
This gives
\[
rL
<
2\left[1+\alpha+K_d(1-\alpha)L\right].
\]

For the rate statement, the two characteristic roots have product
\[
\beta(\lambda)\ge0.
\]
Hence their maximum modulus is at least
\[
\sqrt{\beta(\lambda)}.
\]
If
\[
r\lambda=1+\beta(\lambda),
\]
the linear coefficient vanishes and the roots are
\[
\pm i\sqrt{\beta(\lambda)}.
\]
This attains the lower bound and proves the exact modal optimum.

Finally, objective scaling by
\[
c>0
\]
replaces every curvature by
\[
c\lambda.
\]
Substitution into the already proved hard gain condition gives
\[
K_dcL<1.
\]
This condition is independent of the learning rate.

## Verification

The accompanying `verify.py` reconstructs the source three-state recurrence directly on diagonal SPD quadratics.

It verifies, after the first update, exact agreement between the full PID parameter trajectory and the eliminated second-order recurrence. It compares the strict Jury inequalities with direct characteristic-root calculations over random curvatures and parameters, and checks the all-spectrum endpoint reduction.

It also checks the hard boundary
\[
K_dL=1,
\]
the sharp modal rate floor
\[
\sqrt{\alpha+K_d(1-\alpha)\lambda},
\]
and the loss-rescaling instability mechanism.

These finite computations are transcription guards only. The mode reduction and exact stability region are proved analytically above.

## Relationship to prior work

An, Wang, Sun, Xu, Dai, and Zhang introduced the discrete PID optimizer by adding a filtered gradient-difference term to SGD with momentum. Their printed recurrence is exactly the three-state rule analyzed here. The derivative channel is motivated as “future” gradient information intended to reduce overshoot, and the derivative gain is initialized through a continuous-time Laplace-transform and Ziegler--Nichols heuristic.

The later journal extension retains the same discrete optimizer. Its ablation study reports that larger derivative gains can make validation behavior more unstable and concludes that the relation among optimal PID hyperparameters remains a subject for further study. The inspected full text does not eliminate the discrete states on a constant Hessian or state the hard condition
\[
K_dL<1.
\]

Shi, Zhang, Wang, Cheng, and Lu later revisit the optimizer and emphasize that derivative information is vulnerable to high-frequency stochastic noise, motivating a modified PID construction. That is a different algorithmic response and does not imply the exact deterministic quadratic reduction above.

Classical heavy-ball and Jury theory supplies the final second-order stability test once the optimizer-specific elimination has been found. The new statement is the exact identification
\[
\beta(\lambda)=\alpha+K_d(1-\alpha)\lambda,
\]
together with the resulting sharp all-spectrum gain ceiling, learning-rate interval, exact modal rate floor, and loss-scale sensitivity for this published optimizer.

Focused searches for the deep-learning PID optimizer together with quadratic Schur stability, curvature-dependent momentum, Hessian eigenmodes, loss scaling, and the condition
\[
K_dL<1
\]
did not identify an implication-equivalent published statement.

## Limitations

The finding is a deterministic constant-Hessian benchmark.

It does not assess the reported empirical deep-learning results, nor does it equate transient overshoot with asymptotic spectral radius.

The exact reduction uses the source choice of a common filter coefficient
\[
\alpha
\]
for the momentum and derivative moving averages.

On a nonlinear objective the Hessian changes with the iterate, so the curvature-dependent momentum interpretation becomes local rather than globally exact.

## References

1. Wangpeng An, Haoqian Wang, Qingyun Sun, Jun Xu, Qionghai Dai, and Lei Zhang, “A PID Controller Approach for Stochastic Optimization of Deep Networks,” CVPR 2018, DOI:10.1109/CVPR.2018.00889.
2. Haoqian Wang, Yi Luo, Wangpeng An, Qingyun Sun, Jun Xu, and Lei Zhang, “PID Controller-Based Stochastic Optimization Acceleration for Deep Neural Networks,” IEEE Transactions on Neural Networks and Learning Systems, DOI:10.1109/TNNLS.2019.2963066.
3. Lei Shi, Yifan Zhang, Wanguo Wang, Jian Cheng, and Hanqing Lu, “Rethinking The PID Optimizer For Stochastic Optimization Of Deep Networks,” ICME 2020, DOI:10.1109/ICME46284.2020.9102970.
