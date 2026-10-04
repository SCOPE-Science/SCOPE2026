# Exact epsilon-floor local stability law for diffGrad
## Finding

Consider source-form diffGrad on the deterministic scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]
Let
\[
0\le\beta_1,\beta_2<1,
\qquad
\alpha>0,
\qquad
\varepsilon>0.
\]
The source update uses
\[
g_t=\lambda x_t,
\]
\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\]
\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2,
\]
bias corrections
\[
\widehat m_t=\frac{m_t}{1-\beta_1^t},
\qquad
\widehat v_t=\frac{v_t}{1-\beta_2^t},
\]
and the diffGrad friction coefficient
\[
\xi_t
=
\frac{1}
{1+\exp(-|g_{t-1}-g_t|)}.
\]
The parameter update is
\[
x_{t+1}
=
x_t
-
\alpha
\frac{\xi_t\widehat m_t}
{\sqrt{\widehat v_t}+\varepsilon}.
\]

The zero trajectory is an exact reference orbit. Its limiting first-order dynamics are governed by
\[
\chi
=
\frac{\alpha\lambda}{2\varepsilon}.
\]
The two optimization eigenvalues are the roots of
\[
r^2
-
\left[
1+\beta_1-(1-\beta_1)\chi
\right]r
+
\beta_1
=
0.
\]
The second-moment direction contributes eigenvalue
\[
\beta_2,
\]
and the one-step gradient-memory coordinate needed by the friction coefficient contributes eigenvalue
\[
0.
\]

Consequently, the strict asymptotic local-stability frontier is
\[
0
<
\frac{\alpha\lambda}{\varepsilon}
<
\frac{4(1+\beta_1)}{1-\beta_1}.
\]
At equality in the upper condition, the optimization roots are
\[
-1
\quad\text{and}\quad
-\beta_1,
\]
so the linearized boundary is sharp.

The defining gradient-difference mechanism does not enter this first-order spectrum. Near the zero orbit,
\[
\xi_t
=
\frac12
+
O\!\left(
|g_t-g_{t-1}|
\right).
\]
Because the friction coefficient multiplies \(\widehat m_t\), whose leading term is already first order, the nonconstant part of \(\xi_t\) contributes only second-order terms to the parameter update. Thus the entire first-order optimization block is EMA-style heavy-ball momentum with effective step
\[
\frac{\alpha}{2\varepsilon}.
\]

This has an exact consequence relative to the same epsilon-floor momentum block without diffGrad friction. Removing the factor \(\xi_t\) gives the usual frozen Adam or EMA-heavy-ball local threshold
\[
\frac{\alpha\lambda}{\varepsilon}
<
\frac{2(1+\beta_1)}{1-\beta_1}.
\]
diffGrad's floor value
\[
\xi_\star=\frac12
\]
therefore doubles that local curvature ceiling, but the derivative of the gradient-difference mechanism itself supplies no additional first-order stabilization.

There is also an exact momentum-controlled oscillatory plateau. For
\[
0<\beta_1<1,
\]
the two optimization eigenvalues are nonreal exactly when
\[
\frac{2(1-\sqrt{\beta_1})}
{1+\sqrt{\beta_1}}
<
\frac{\alpha\lambda}{\varepsilon}
<
\frac{2(1+\sqrt{\beta_1})}
{1-\sqrt{\beta_1}}.
\]
Throughout this interval, both roots have modulus
\[
\sqrt{\beta_1}.
\]

For the common value
\[
\beta_1=0.9,
\]
the strict diffGrad ceiling is
\[
\frac{\alpha\lambda}{\varepsilon}<76,
\]
whereas the corresponding unfactored EMA-momentum ceiling is
\[
\frac{\alpha\lambda}{\varepsilon}<38.
\]
The source paper uses an epsilon of approximately
\[
10^{-7}
\]
and describes learning rates around
\[
10^{-3}
\]
in its experiments, so the epsilon floor is not merely formal: it determines the eventual local scale once the adaptive second moment has collapsed sufficiently close to a deterministic stationary point.

## Assumptions and scope

The theorem uses the update convention stated in the defining diffGrad paper: epsilon is outside the square root in the diffGrad denominator.

The statement is deterministic and scalar. It classifies the strict asymptotic local stability of the zero reference orbit for the bias-corrected recurrence. The bias corrections make the finite-time map nonautonomous, but their coefficients converge exponentially to one.

The upper equality case has a limiting root at \(-1\). No nonlinear conclusion is claimed at that boundary.

The theorem is local. It does not exclude nonzero cycles or other global dynamics outside the local stable regime. In particular, known Adam analyses show that adaptive-moment methods can possess nontrivial cycles on scalar quadratics.

## Proof

Augment the state with the previous parameter value so that the gradient-difference coefficient is Markovian:
\[
z_t
=
(x_t,m_{t-1},v_{t-1},x_{t-1}).
\]
The zero sequence is an exact reference orbit.

First consider the friction coefficient. Since
\[
g_t-g_{t-1}
=
\lambda(x_t-x_{t-1}),
\]
and
\[
\frac{1}{1+e^{-u}}
=
\frac12+\frac{u}{4}+O(u^3)
\]
for \(u\ge0\) near zero,
\[
\xi_t
=
\frac12
+
O\!\left(
|x_t-x_{t-1}|
\right).
\]
This function is not differentiable by itself across the absolute value, but in the parameter update it is multiplied by \(m_t\). Hence
\[
\left(\xi_t-\frac12\right)m_t
=
O(\|z_t\|^2),
\]
so its nonconstant part has no first-order contribution.

Next,
\[
v_t
=
\beta_2v_{t-1}
+
O(x_t^2).
\]
At the zero orbit,
\[
\frac{m_t}
{\sqrt{\widehat v_t}+\varepsilon}
=
\frac{m_t}{\varepsilon}
+
o(\|z_t\|).
\]
Indeed, the difference from \(m_t/\varepsilon\) is bounded by a constant times
\[
|m_t|\sqrt{\widehat v_t},
\]
which is \(o(\|z_t\|)\) on the nonnegative second-moment state space.

The bias-corrected first moment contributes the time-dependent factor
\[
\frac{1}{1-\beta_1^t}.
\]
Thus the linearization of the \((x,m)\) block at time \(t\) is
\[
A_t
=
\begin{bmatrix}
1-h_t(1-\beta_1)\lambda&-h_t\beta_1\\
(1-\beta_1)\lambda&\beta_1
\end{bmatrix},
\]
where
\[
h_t
=
\frac{\alpha}
{2\varepsilon(1-\beta_1^t)}.
\]
As \(t\to\infty\),
\[
A_t\to A_\infty
\]
exponentially, with
\[
h_\infty
=
\frac{\alpha}{2\varepsilon}.
\]

The limiting block has determinant
\[
\det A_\infty=\beta_1
\]
and trace
\[
T
=
1+\beta_1-(1-\beta_1)\chi,
\qquad
\chi
=
\frac{\alpha\lambda}{2\varepsilon}.
\]
Its characteristic polynomial is
\[
r^2-Tr+\beta_1.
\]

The real second-order Jury conditions are
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
They reduce to
\[
\chi>0
\]
and
\[
\chi
<
\frac{2(1+\beta_1)}
{1-\beta_1}.
\]
Substituting the definition of \(\chi\) yields
\[
\frac{\alpha\lambda}{\varepsilon}
<
\frac{4(1+\beta_1)}
{1-\beta_1}.
\]

The remaining limiting state eigenvalues are \(\beta_2\) from the second moment and \(0\) from the shift that stores the previous parameter. Since both lie strictly inside the unit disk, the displayed inequality is the complete strict limiting linear frontier.

Because \(A_t-A_\infty\) decays exponentially and the nonlinear remainder is little-o of the state norm, strict Schur stability of the limiting Jacobian gives local exponential stability of the nonautonomous zero orbit after a finite transient. If the limiting optimization block has a root of modulus greater than one, the zero orbit is locally unstable. The unit-root boundary is excluded from both strict statements.

For the oscillatory plateau, the discriminant is negative exactly when
\[
T^2<4\beta_1.
\]
Solving this inequality for \(\chi\), and then multiplying by two to return to \(\alpha\lambda/\varepsilon\), gives the stated interval. The product of the roots is \(\beta_1\), so their common modulus is \(\sqrt{\beta_1}\).

## Verification

The accompanying `verify.py` reconstructs the limiting Jacobian, checks its determinant, trace, Jury threshold, unit-root boundary, and complex-root plateau. It also evaluates the full nonlinear source-form map at shrinking states to confirm that the friction variation and adaptive denominator contribute only higher-order remainders.

The finite computations are transcription checks. The stability frontier follows from the analytic linearization and Jury inequalities above.

## Relationship to prior work

Dubey, Chakraborty, Roy, Mukherjee, Singh, and Chaudhuri introduced diffGrad by multiplying Adam's bias-corrected first-moment update by the friction coefficient
\[
\xi_t
=
\frac{1}
{1+\exp(-|g_{t-1}-g_t|)}.
\]
They emphasize that the coefficient has minimum value \(1/2\) when the gradient does not change and argue experimentally that it reduces oscillations near optima. Their theorem is an online-regret bound with decaying learning rate and bounded-gradient assumptions. The inspected paper contains no quadratic local-stability calculation.

Cohen et al. later derived the sharp quadratic stability threshold for EMA-style heavy-ball momentum and used it to explain the adaptive edge of stability for frozen Adam. That result supplies the closest linear comparison: the threshold is
\[
\frac{2(1+\beta_1)}
{\eta(1-\beta_1)}
\]
in preconditioned curvature units. It does not analyze diffGrad's gradient-difference friction. The present calculation shows exactly how diffGrad modifies that boundary: only its floor value \(1/2\) survives at first order.

Bock and Weiß analyzed nonconvergence and limit cycles of bias-corrected Adam on scalar quadratics. Their full dynamical analysis establishes that local behavior need not determine global convergence for adaptive-moment methods, but it does not study diffGrad or the first-order disappearance of its gradient-difference sensitivity.

## Limitations

The result does not claim that diffGrad behaves like half-step Adam away from a stationary point. When consecutive gradients differ substantially, the friction coefficient can approach one and nonlinear behavior can differ strongly.

The theorem does not classify nonlinear cycles outside the stable local regime.

The scalar model has no coordinate coupling. In higher dimensions, the same first-order friction-floor argument applies coordinatewise to a diagonalized frozen-preconditioner model, but a general adaptive second-moment state need not commute with the Hessian.

The experimental numerical example only illustrates the scale of the formula; it is not a prediction of instability for a particular neural network.

## References

1. Shiv Ram Dubey, Soumendu Chakraborty, Swalpa Kumar Roy, Snehasis Mukherjee, Satish Kumar Singh, and Bidyut Baran Chaudhuri, “diffGrad: An Optimization Method for Convolutional Neural Networks,” arXiv:1909.11015v1, 2019.
2. Jeremy M. Cohen et al., “Adaptive Gradient Methods at the Edge of Stability,” arXiv:2207.14484v1, 2022.
3. Sebastian Bock and Martin Georg Weiß, “Non-Convergence and Limit Cycles in the Adam optimizer,” arXiv:2210.02070v1, 2022.
