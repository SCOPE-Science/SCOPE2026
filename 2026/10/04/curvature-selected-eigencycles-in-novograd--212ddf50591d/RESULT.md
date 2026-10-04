# Curvature-selected eigencycles in NovoGrad
## Finding

Consider one deterministic parameter layer with the SPD quadratic
\[
f(x)=\frac12 x^\top Hx,
\qquad
H=H^\top\succ0.
\]
Use the source NovoGrad momentum form with constant learning rate and no weight decay:
\[
v_t
=
\beta_2v_{t-1}
+
(1-\beta_2)\|Hx_t\|^2,
\]
\[
m_t
=
\beta_1m_{t-1}
+
\frac{Hx_t}{\sqrt{v_t+\varepsilon}},
\]
\[
x_{t+1}
=
x_t-\alpha m_t,
\]
where
\[
0\le\beta_1<1,
\qquad
0\le\beta_2<1,
\qquad
\alpha>0,
\qquad
\varepsilon\ge0.
\]

Let
\[
Hu=\lambda u,
\qquad
\|u\|=1.
\]
If
\[
\alpha\lambda
>
2(1+\beta_1)\sqrt{\varepsilon},
\]
define
\[
r_\lambda^2
=
\frac{\alpha^2}{4(1+\beta_1)^2}
-
\frac{\varepsilon}{\lambda^2}.
\]
Then NovoGrad has the exact nonzero period-two state orbit
\[
x_t=(-1)^t r_\lambda u,
\]
\[
v_t=\lambda^2r_\lambda^2,
\]
\[
m_t=(-1)^t\frac{2r_\lambda}{\alpha}u.
\]

Thus every curvature eigenmode above the epsilon-dependent existence threshold supports an exact oscillatory state. When
\[
\varepsilon=0,
\]
the orbit radius simplifies to
\[
r_\lambda
=
\frac{\alpha}{2(1+\beta_1)},
\]
which is independent of curvature and of the second-moment decay.

The striking part is the transverse selection law. Let
\[
Hw=\mu w,
\qquad
w\perp u.
\]
At the period-two orbit, the first-order perturbation of the scalar second moment caused by the \(w\)-mode vanishes because
\[
\langle Hu,Hw\rangle=0.
\]
Consequently the transverse position-momentum perturbation follows the same constant \(2\times2\) matrix at both phases of the orbit. Its characteristic polynomial is
\[
z^2
-
(1+\beta_1)
\left(
1-2\frac{\mu}{\lambda}
\right)z
+
\beta_1.
\]

The transverse mode is strictly Schur-stable exactly when
\[
0<\mu<\lambda.
\]
At
\[
\mu=\lambda,
\]
the polynomial factors as
\[
(z+1)(z+\beta_1),
\]
so the mode is neutral through the root \(-1\). If
\[
\mu>\lambda,
\]
one transverse root has modulus greater than one.

Therefore every eigencycle associated with a nonmaximal eigenvalue is transversely unstable: a larger-curvature eigenmode destabilizes it. An eigencycle in the top eigenspace has no unstable orthogonal curvature mode. If the top eigenvalue is repeated, directions inside that eigenspace are neutral, matching the fact that every unit vector in the eigenspace generates a cycle.

For
\[
0<\beta_1<1,
\]
there is also an exact relative-curvature rate plateau. The transverse roots are complex precisely when
\[
\left|
\frac{\mu}{\lambda}
-
\frac12
\right|
<
\frac{\sqrt{\beta_1}}{1+\beta_1}.
\]
Throughout this interval their common modulus is
\[
\sqrt{\beta_1}.
\]

The entire transverse polynomial depends only on the curvature ratio
\[
\mu/\lambda
\]
and the first-moment coefficient \(\beta_1\). Once the cycle exists, it is independent of
\[
\alpha,
\qquad
\beta_2,
\qquad
\varepsilon.
\]

## Assumptions and scope

The recurrence is the original NovoGrad ordering: a layerwise scalar second moment normalizes the current gradient before that normalized gradient is accumulated into momentum. The theorem does not use the optional Adam-like gradient-averaging variant that multiplies the new normalized gradient by \(1-\beta_1\).

Weight decay is set to zero. A nonzero decay term changes both the exact cycle and its transverse matrix.

The result is a deterministic constant-step statement. The source experiments use learning-rate schedules, so this theorem is not a claim that trained networks settle onto these cycles.

The exact orbit is a state-space orbit of the autonomous recurrence. Source initialization need not place the method exactly on that orbit.

The theorem classifies orthogonal transverse eigenmodes. It does not claim radial stability of the period-two orbit along its generating eigenvector.

## Proof

Fix an eigenpair
\[
Hu=\lambda u.
\]
Seek a sign-alternating orbit of the form
\[
x_t=s_t r u,
\qquad
s_t=(-1)^t,
\qquad
r>0.
\]
Since the gradient norm is constant,
\[
\|Hx_t\|^2
=
\lambda^2r^2.
\]
Hence
\[
v_t=\lambda^2r^2
\]
is invariant for every
\[
0\le\beta_2<1.
\]

To flip position sign in one step, the momentum must satisfy
\[
m_t
=
\frac{x_t-x_{t+1}}{\alpha}
=
s_t\frac{2r}{\alpha}u.
\]
The previous momentum is therefore
\[
m_{t-1}
=
-s_t\frac{2r}{\alpha}u.
\]
Let
\[
D
=
\sqrt{\lambda^2r^2+\varepsilon}.
\]
The momentum recurrence becomes
\[
s_t\frac{2r}{\alpha}u
=
-\beta_1s_t\frac{2r}{\alpha}u
+
s_t\frac{\lambda r}{D}u.
\]
After cancelling
\[
s_t r u,
\]
one gets
\[
D
=
\frac{\alpha\lambda}{2(1+\beta_1)}.
\]
Squaring gives
\[
r^2
=
\frac{\alpha^2}{4(1+\beta_1)^2}
-
\frac{\varepsilon}{\lambda^2}.
\]
A nonzero real cycle exists exactly under the displayed strict threshold.

Now perturb the cycle in an orthogonal eigenmode
\[
Hw=\mu w.
\]
Write the transverse position and previous-momentum components as
\[
y_t w
\qquad\text{and}\qquad
n_{t-1}w.
\]
Because
\[
\langle Hu,Hw\rangle=0,
\]
the derivative of
\[
\|Hx\|^2
\]
in the \(w\)-direction vanishes at the base cycle. A perturbation of the scalar second moment therefore does not enter the transverse gradient component to first order.

The normalized transverse gradient is simply
\[
\frac{\mu y_t}{D}w.
\]
Hence
\[
n_t
=
\beta_1n_{t-1}
+
\frac{\mu}{D}y_t,
\]
\[
y_{t+1}
=
y_t-\alpha n_t.
\]
Thus
\[
\begin{bmatrix}
y_{t+1}\\
n_t
\end{bmatrix}
=
\begin{bmatrix}
1-\alpha\mu/D&-\alpha\beta_1\\
\mu/D&\beta_1
\end{bmatrix}
\begin{bmatrix}
y_t\\
n_{t-1}
\end{bmatrix}.
\]
Using
\[
D
=
\frac{\alpha\lambda}{2(1+\beta_1)},
\]
the trace is
\[
(1+\beta_1)
\left(
1-2\frac{\mu}{\lambda}
\right),
\]
and the determinant is
\[
\beta_1.
\]
This proves the stated characteristic polynomial.

For a real monic quadratic
\[
z^2-Tz+\beta_1,
\]
the Jury conditions are
\[
1-\beta_1>0,
\]
\[
1-T+\beta_1>0,
\]
\[
1+T+\beta_1>0.
\]
The first holds by assumption. The second reduces to
\[
2(1+\beta_1)\frac{\mu}{\lambda}>0.
\]
The third reduces to
\[
2(1+\beta_1)
\left(
1-\frac{\mu}{\lambda}
\right)>0.
\]
Since the quadratic is SPD, the first is automatic, and the second is exactly
\[
\mu<\lambda.
\]

At
\[
\mu=\lambda,
\]
the trace is
\[
-(1+\beta_1),
\]
giving
\[
(z+1)(z+\beta_1).
\]

Finally, complex roots occur exactly when
\[
T^2<4\beta_1.
\]
Substituting the trace and solving yields
\[
\left|
\frac{\mu}{\lambda}
-
\frac12
\right|
<
\frac{\sqrt{\beta_1}}{1+\beta_1}.
\]
The product of the complex-conjugate roots is \(\beta_1\), so both have modulus \(\sqrt{\beta_1}\).

## Verification

The accompanying `verify.py` checks the exact period-two state equations for several parameter choices, verifies the transverse characteristic polynomial and Schur boundary, confirms the complex-root plateau, and compares the analytic transverse matrix with a finite-difference Jacobian of the full NovoGrad state map.

The finite-difference checks are transcription guards. Existence of the orbit and the transverse classification are proved symbolically above.

## Relationship to prior work

The earliest located public NovoGrad description appears in the Jasper preprint, which introduces a layerwise scalar second moment, uses it to normalize the current gradient before momentum accumulation, and updates the weights with that momentum. The later dedicated NovoGrad paper gives the same ordering in a standalone algorithm and motivates the method through robustness to gradient scale, memory savings, and layerwise normalization. Neither inspected source analyzes constant-step period-two state orbits or transverse Floquet behavior on SPD quadratics.

Normalized direction-preserving Adam is a close predecessor because it also replaces a vector's coordinatewise second moment by a scalar norm statistic. Its update is materially different: it forms an exponential first moment of the unnormalized projected gradient, bias-corrects both moments, divides the first moment by the scalar second moment, and explicitly renormalizes weights to a sphere. Those formulas do not imply the NovoGrad cycle or the relative-curvature transverse polynomial here.

Classical normalized-gradient literature studies the direction-only update
\[
x_{t+1}
=
x_t
-
\alpha_t
\frac{\nabla f(x_t)}
{\|\nabla f(x_t)\|}.
\]
The inspected saddle-evasion paper explicitly focuses its main analysis on continuous-time normalized gradient flow and identifies discrete-time stable-manifold questions as future work. It does not contain NovoGrad's momentum-plus-EMA state or the curvature-selection law above.

## Limitations

The theorem does not establish radial attraction of the cycle. A top-eigenvalue cycle can be transversely stable while remaining unstable or neutral in the generating eigendirection.

The result does not cover weight decay, gradient averaging, stochastic gradients, or time-varying learning rates.

The epsilon floor determines whether a given eigenmode's nonzero cycle exists, even though epsilon disappears from its transverse spectrum after existence is imposed.

The exact cycle is a diagnostic state of the autonomous optimizer, not a claim about typical network-training trajectories.

## References

1. Jason Li, Vitaly Lavrukhin, Boris Ginsburg, Ryan Leary, Oleksii Kuchaiev, Jonathan M. Cohen, Huyen Nguyen, and Ravi Teja Gadde, “Jasper: An End-to-End Convolutional Neural Acoustic Model,” arXiv:1904.03288v1, 2019.
2. Boris Ginsburg, Patrice Castonguay, Oleksii Hrinchuk, Oleksii Kuchaiev, Ryan Leary, Vitaly Lavrukhin, Jason Li, Huyen Nguyen, Yang Zhang, and Jonathan M. Cohen, “Stochastic Gradient Methods with Layer-wise Adaptive Moments for Training of Deep Networks,” arXiv:1905.11286, 2019.
3. Zijun Zhang, Lin Ma, Zongpeng Li, and Chuan Wu, “Normalized Direction-preserving Adam,” arXiv:1709.04546, 2017.
4. Ryan Murray, Brian Swenson, and Soummya Kar, “Revisiting Normalized Gradient Descent: Fast Evasion of Saddle Points,” arXiv:1711.05224, 2017.
