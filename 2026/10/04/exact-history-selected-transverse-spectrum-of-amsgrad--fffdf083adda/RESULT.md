# Exact history-selected transverse spectrum of AMSGrad
## Finding

Consider constant-step source-form AMSGrad on the unconstrained scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]
Let
\[
\alpha>0,
\qquad
0\le\beta_1<1,
\qquad
0\le\beta_2<1,
\]
and use the AMSGrad state equations
\[
g_t=\lambda x_t,
\]
\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\]
\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2,
\]
\[
\widehat v_t=\max(\widehat v_{t-1},v_t),
\]
\[
x_{t+1}=x_t-\alpha\frac{m_t}{\sqrt{\widehat v_t}}.
\]

The maximum-memory state creates a continuum of optimizer-state equilibria:
\[
\mathcal E
=
\left\{
(x,m,v,\widehat v)=(0,0,0,V):V>0
\right\}.
\]
The parameter is at the minimizer on every point of this manifold, but the retained AMSGrad memory \(V\) can differ.

Fix one leaf \(V>0\). In a neighborhood where the maximum is inactive, so that the stored maximum remains \(V\), define
\[
c
=
\frac{\alpha(1-\beta_1)\lambda}{\sqrt V}.
\]
The Jacobian has four eigenvalues. One is
\[
1,
\]
corresponding to neutral motion along the memory manifold. One is
\[
\beta_2,
\]
coming from relaxation of the current second moment. The remaining position-momentum pair is given exactly by
\[
r^2
-
(1+\beta_1-c)r
+
\beta_1
=0.
\]

Therefore \(\mathcal E\) is locally transversely asymptotically stable at memory level \(V\) if and only if
\[
0<c<2(1+\beta_1).
\]
Equivalently,
\[
V
>
V_{\mathrm{crit}}
:=
\left[
\frac{\alpha(1-\beta_1)\lambda}
{2(1+\beta_1)}
\right]^2.
\]
At the exact boundary
\[
V=V_{\mathrm{crit}},
\]
the position-momentum roots are
\[
-1
\qquad\text{and}\qquad
-\beta_1.
\]
For
\[
0<V<V_{\mathrm{crit}},
\]
one position-momentum root has modulus greater than one.

For
\[
0<\beta_1<1,
\]
there is also an exact damping plateau. The position-momentum roots are complex exactly when
\[
(1-\sqrt{\beta_1})^2
<
c
<
(1+\sqrt{\beta_1})^2.
\]
Throughout this whole interval their common modulus is
\[
\sqrt{\beta_1}.
\]
In terms of the stored maximum, the plateau is
\[
\frac{\alpha^2(1-\beta_1)^2\lambda^2}
{(1+\sqrt{\beta_1})^4}
<
V
<
\frac{\alpha^2(1-\beta_1)^2\lambda^2}
{(1-\sqrt{\beta_1})^4}.
\]

For still larger memory,
\[
V\to\infty,
\]
one position-momentum eigenvalue tends to \(1\) while the other tends to \(\beta_1\). Thus an extremely large historical maximum remains stable but makes the parameter dynamics arbitrarily slow.

This gives an exact local interpretation of AMSGrad's long-term memory. The retained maximum does not merely make the coordinate learning rate nonincreasing. It selects the local constant-step spectrum: too little stored curvature memory is unstable, an intermediate interval has a momentum-controlled rate plateau, and excessive memory over-damps the parameter dynamics.

## Assumptions and scope

The theorem uses Algorithm 2 in the defining AMSGrad work, on an unconstrained scalar problem, with constant step size and constant first-moment coefficient. The source algorithm allows a step-size sequence and notes that constant first-moment coefficients are typical in practice; constant steps are also used in its neural-network experiments.

The result is local to the open branch on which the running maximum is inactive. This is the relevant branch around every equilibrium with \(V>0\), because the current second moment equals zero at the equilibrium and is therefore strictly below the stored maximum.

The neutral eigenvalue \(1\) is not hidden or discarded: it is the tangent direction of the equilibrium manifold itself. “Transversely stable” means that parameter, first-moment, and current-second-moment perturbations decay while the stored historical maximum approaches a nearby constant leaf.

The source theoretical AMSGrad update does not include a denominator epsilon. Variants that use \(\sqrt{\widehat v}+\varepsilon\) have a shifted threshold.

The theorem does not claim that every positive value of \(V\) is reached from the standard zero-memory initialization by one prescribed trajectory. It classifies the local dynamics at every optimizer state allowed by AMSGrad's retained maximum memory.

## Proof

Use the state coordinates
\[
(x_t,m_{t-1},v_{t-1},\widehat v_{t-1}).
\]
At
\[
(0,0,0,V),
\qquad
V>0,
\]
the next gradient, moments, and parameter are all zero, while the maximum remains \(V\). This proves that \(\mathcal E\) is an equilibrium manifold.

Because
\[
v_t=0<V
\]
at the equilibrium, there is an open neighborhood in which
\[
\widehat v_t=\widehat v_{t-1}.
\]
On this branch, differentiation at the equilibrium gives
\[
m_t
=
\beta_1m_{t-1}
+
(1-\beta_1)\lambda x_t,
\]
and
\[
v_t
=
\beta_2v_{t-1}
+
O(x_t^2).
\]
The derivative of the parameter update with respect to \(\widehat v\) vanishes at the equilibrium because the multiplying first moment is zero there.

Hence the Jacobian is block diagonal up to the position-momentum block:
\[
J_V
=
\begin{bmatrix}
1-c & -\alpha\beta_1/\sqrt V & 0 & 0\\
(1-\beta_1)\lambda & \beta_1 & 0 & 0\\
0&0&\beta_2&0\\
0&0&0&1
\end{bmatrix}.
\]
The position-momentum block has trace
\[
1+\beta_1-c
\]
and determinant
\[
\beta_1.
\]
Its characteristic polynomial is therefore
\[
r^2-(1+\beta_1-c)r+\beta_1.
\]

For a real monic quadratic
\[
r^2-Tr+\beta_1,
\]
with
\[
0\le\beta_1<1,
\]
the Jury conditions for both roots to lie strictly inside the unit disk are
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
Substituting
\[
T=1+\beta_1-c
\]
reduces the last two conditions to
\[
c>0
\]
and
\[
c<2(1+\beta_1).
\]
Since \(\alpha\), \(\lambda\), and \(V\) are positive, the first is automatic. Solving the second for \(V\) gives the sharp threshold.

At
\[
c=2(1+\beta_1),
\]
the polynomial becomes
\[
(r+1)(r+\beta_1).
\]
For larger \(c\), the final Jury condition fails, so one root lies outside the unit disk.

For
\[
0<\beta_1<1,
\]
the two roots are complex exactly when the discriminant is negative:
\[
(1+\beta_1-c)^2<4\beta_1.
\]
This is equivalent to
\[
(1-\sqrt{\beta_1})^2<c<(1+\sqrt{\beta_1})^2.
\]
The product of the conjugate roots is \(\beta_1\), so each has modulus \(\sqrt{\beta_1}\).

Finally, as \(V\to\infty\), one has \(c\to0\), and the characteristic polynomial tends to
\[
(r-1)(r-\beta_1).
\]
This proves the slow-memory limit.

## Verification

The accompanying `verify.py` reconstructs the full four-state AMSGrad map on the inactive-maximum branch, compares a finite-difference Jacobian with the analytic matrix, checks the Jury boundary on both sides, verifies the complex-root modulus plateau, and confirms the neutral memory and \(\beta_2\) eigenvalues.

The numerical checks are transcription guards. The equilibrium manifold and all spectral statements are proved symbolically above.

## Relationship to prior work

Reddi, Kale, and Kumar introduced AMSGrad specifically to endow Adam with long-term memory. The defining source says that AMSGrad maintains the maximum of all past second-moment values and uses that maximum for normalization, making the coordinate learning rate nonincreasing. Its convergence analysis is an online-regret analysis with decaying theoretical step sizes; it does not classify constant-step local dynamics around a minimizer as a function of the retained maximum.

Phuong and Phong later identified a hyperparameter-handling issue in the original AMSGrad proof, reproduced the AMSGrad recurrence, and supplied corrected convergence arguments and a modified AdamX algorithm. Their inspected analysis concerns global regret inequalities rather than the local optimizer-state spectrum on a fixed maximum-memory branch.

A generic heavy-ball recurrence has a related quadratic characteristic polynomial once a preconditioner is fixed. That observation does not subsume the present statement: AMSGrad's nondecaying maximum creates a continuum of equilibrium leaves, contributes a neutral state direction, and makes the effective heavy-ball coefficient a retained historical quantity. The sharp threshold here is a condition on that memory state itself.

The earliest exact-dated public evidence located for the AMSGrad OpenReview paper is 2017-12-19: a public technical discussion on that date linked the OpenReview entry and explicitly named AMSGrad. The later arXiv posting is a revision/mirror and is not used as the first-public date.

## Limitations

The analysis is scalar and local. In multiple dimensions, each coordinate can retain a different maximum and interact through the objective Hessian.

The theorem does not determine the historical maximum selected by an arbitrary trajectory from standard initialization.

The source max operation is nonsmooth on the switching surface \(v=\widehat v\); the theorem applies to the open inactive branch around \(V>0\).

Very large memory stabilizes the linearized parameter dynamics but can also make them arbitrarily slow; the theorem does not optimize a global training schedule.

## References

1. Sashank J. Reddi, Satyen Kale, and Sanjiv Kumar, “On the Convergence of Adam and Beyond,” ICLR 2018, OpenReview `ryQu7f-RZ`; later arXiv mirror `1904.09237`.
2. Tran Thi Phuong and Le Trieu Phong, “On the Convergence Proof of AMSGrad and a New Version,” arXiv:1904.03590, 2019.
3. Public technical discussion dated 2017-12-19 linking OpenReview `ryQu7f-RZ` and explicitly identifying AMSGrad; used only as exact-date evidence of public availability.
