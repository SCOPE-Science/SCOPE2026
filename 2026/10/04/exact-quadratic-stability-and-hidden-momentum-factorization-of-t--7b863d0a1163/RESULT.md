# Exact quadratic stability and hidden-momentum factorization of the 2018 PID optimizer
## Finding

Consider the recurrence printed in the 2018 PID-optimizer paper on
\[
f(x)=\frac12x^\top Hx,\qquad H\succ0:
\]
\[
V_{t+1}=\beta V_t-\eta Hx_t,
\]
\[
D_{t+1}=\beta D_t+(1-\beta)H(x_t-x_{t-1}),
\]
\[
x_{t+1}=x_t+V_{t+1}+\kappa D_{t+1},
\]
where
\[
0\le\beta<1,\qquad \eta>0,\qquad \kappa\ge0.
\]

For a curvature eigenvalue \(\lambda>0\), put
\[
s=\eta\lambda,\qquad q_\lambda=\beta+(1-\beta)\kappa\lambda.
\]
The full four-state modal characteristic polynomial factors exactly as
\[
\chi_\lambda(z)=
z(z-\beta)
\left[z^2-(1+q_\lambda-s)z+q_\lambda\right].
\]
Thus two roots are passive, \(0\) and \(\beta\), while the active pair has exactly the heavy-ball form with a curvature-dependent effective momentum product \(q_\lambda\).

The scalar mode is Schur stable if and only if
\[
\kappa\lambda<1
\]
and
\[
0<\eta\lambda<
2\left[1+\beta+(1-\beta)\kappa\lambda\right].
\]
Consequently, when the spectrum of \(H\) lies in \([\mu,L]\), all modes are stable if and only if
\[
\kappa L<1
\]
and
\[
\eta L<
2\left[1+\beta+(1-\beta)\kappa L\right].
\]

Because \(\kappa L<1\), the right-hand side can approach but never reach \(4\). Hence
\[
\eta L<4
\]
is the sharp absolute supremum of the stable stepsize range over admissible derivative gains.

For a fixed mode, the exact best asymptotic state factor over \(\eta\) is
\[
\sqrt{q_\lambda},
\]
and it is attained exactly on
\[
(1-\sqrt{q_\lambda})^2
\le
\eta\lambda
\le
(1+\sqrt{q_\lambda})^2.
\]
Therefore derivative gain has an exact stability-versus-rate tradeoff: increasing \(\kappa\) enlarges the scalar stepsize ceiling but raises the best attainable modal factor whenever \(\kappa>0\).

## Assumptions and scope

The theorem concerns the recurrence printed in the 2018 paper. The source-associated public implementation is algebraically different: it applies the current gradient directly together with weighted integral and derivative buffers. The theorem is therefore not an implementation-level claim.

The objective is a deterministic SPD quadratic and all coefficients are constant. Arbitrary initial values of \(x_t\), \(x_{t-1}\), \(V_t\), and \(D_t\) are allowed. The result concerns asymptotic linear stability, not transient objective monotonicity.

A 2020 follow-up describes the earlier method as an integral-derivative construction and proposes a different complete PID optimizer. That later recurrence and its derivative-noise controls are outside this claim.

## Proof

Fix an eigendirection of \(H\) with eigenvalue \(\lambda\). Define
\[
s=\eta\lambda,\qquad a=(1-\beta)\kappa\lambda.
\]
For
\[
\xi_t=
\begin{bmatrix}
x_t\\x_{t-1}\\V_t\\D_t
\end{bmatrix},
\]
the modal update is
\[
\xi_{t+1}=M_\lambda\xi_t,
\]
where
\[
M_\lambda=
\begin{bmatrix}
1-s+a&-a&\beta&\kappa\beta\\
1&0&0&0\\
-s&0&\beta&0\\
(1-\beta)\lambda&-(1-\beta)\lambda&0&\beta
\end{bmatrix}.
\]
Direct determinant expansion gives
\[
\det(zI-M_\lambda)
=
z(z-\beta)
\left[z^2-(1+\beta+a-s)z+\beta+a\right].
\]
Since
\[
q_\lambda=\beta+a,
\]
this is the claimed factorization.

The passive roots \(0\) and \(\beta\) are strictly inside the unit disk. The active factor is
\[
p(z)=z^2-(1+q_\lambda-s)z+q_\lambda.
\]
For a real monic quadratic \(z^2-Tz+q\), the Jury conditions are
\[
1-q>0,\qquad 1-T+q>0,\qquad 1+T+q>0.
\]
They become
\[
1-q_\lambda>0,\qquad s>0,\qquad 2(1+q_\lambda)-s>0.
\]
Because
\[
1-q_\lambda=(1-\beta)(1-\kappa\lambda),
\]
the scalar stability region follows exactly.

For \(\lambda\in[\mu,L]\), the condition \(\kappa\lambda<1\) is worst at \(L\). The other condition is equivalent to
\[
\left[\eta-2(1-\beta)\kappa\right]\lambda<2(1+\beta).
\]
If the bracket is positive, the left side is largest at \(L\); if it is nonpositive, the inequality holds automatically for every positive \(\lambda\). Hence the top-curvature condition is necessary and sufficient for the whole interval.

Finally, the active roots have product \(q_\lambda\), so their larger modulus is at least \(\sqrt{q_\lambda}\). Equality is attained exactly when the discriminant is nonpositive:
\[
(1+q_\lambda-s)^2-4q_\lambda\le0,
\]
which is equivalent to
\[
(1-\sqrt{q_\lambda})^2\le s\le(1+\sqrt{q_\lambda})^2.
\]
Because
\[
0\le\beta\le q_\lambda<1,
\]
the passive root \(\beta\) does not exceed \(\sqrt{q_\lambda}\). Thus the same value is the exact minimum spectral factor of the full modal state.

## Verification

The accompanying `verify.py` reconstructs the four-state modal matrix from the printed equations. It compares \(\det(zI-M_\lambda)\) with the factored polynomial at real and complex test points, checks both sides of the scalar and interval stability boundaries, and verifies the rate-optimal plateau.

These finite checks are algebra and transcription guards. The determinant factorization and Jury argument establish the infinite-time claims.

## Relationship to prior work

The 2018 source introduces the controller-based optimizer, writes the moving-average gradient-difference recurrence analyzed here, and motivates the derivative channel as a way to reduce overshoot. Its control analysis uses transfer-function intuition and tuning rules; it also warns that an excessively large derivative coefficient makes the system fragile. The inspected source does not give the discrete quadratic factorization or the exact Schur region above.

The 2020 follow-up explicitly describes the earlier approach as using integral and derivative information and proposes a different complete PID optimizer designed to better handle derivative noise. Its publicly accessible primary description does not state the present SPD-quadratic factorization or rate tradeoff.

The source-associated public implementation was inspected separately. Its update uses the current gradient in addition to integral and derivative buffers, so it is not algebraically identical to the printed recurrence.

The active quadratic factor is related to heavy-ball dynamics only after the four-state factorization is exposed, and its effective momentum \(q_\lambda\) varies with curvature. Focused searches for the optimizer name, gradient-difference momentum, quadratic stability, characteristic polynomials, and exact Schur boundaries did not identify a statement covering the complete claim.

## Limitations

The theorem is for the printed 2018 recurrence only. It does not cover the source-associated implementation, the later three-gain PID formulation, low-pass derivative filtering, adaptive derivative clamping, or other controller-inspired optimizers.

Stochastic gradient noise is excluded. This is important because derivative channels can amplify high-frequency noise.

The rate statement is modal and asymptotic. It does not quantify transient overshoot or finite-budget behavior.

Equivalent state-space calculations may exist in older control or optimization literature under different coordinates; targeted searches cannot eliminate that residual risk.

## References

1. Wangpeng An, Haoqian Wang, Qingyun Sun, Jun Xu, Qionghai Dai, and Lei Zhang, “A PID Controller Approach for Stochastic Optimization of Deep Networks,” CVPR 2018, DOI:10.1109/CVPR.2018.00889.
2. Lei Shi, Yifan Zhang, Wanguo Wang, Jian Cheng, and Hanqing Lu, “Rethinking the PID Optimizer for Stochastic Optimization of Deep Networks,” ICME 2020, DOI:10.1109/ICME46284.2020.9102970.
3. Public implementation associated with the 2018 work, `tensorboy/PIDOptimizer`, file `pid.py`, current master branch inspected for recurrence comparison.
