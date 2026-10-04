# Neutral accumulator manifold and exact transverse-stability threshold for Yogi
## Finding

Consider constant-step Yogi on
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0,
\]
with
\[
0<\beta_1,\beta_2<1,
\qquad
\eta>0,
\qquad
\varepsilon>0.
\]
Using the defining update,
\[
g=\lambda x,
\]
\[
m^+=\beta_1m+(1-\beta_1)g,
\]
\[
v^+
=
v-(1-\beta_2)\operatorname{sign}(v-g^2)g^2,
\]
\[
x^+
=
x-\eta\frac{m^+}{\sqrt{v^+}+\varepsilon},
\]
the objective minimizer does not correspond to one isolated optimizer state. Instead,
\[
\mathcal E
=
\left\{
(0,0,V):V\ge0
\right\}
\]
is a full ray of fixed states.

For every
\[
V>0,
\]
there is a neighborhood of \((0,0,V)\) in which
\[
v>\lambda^2x^2,
\]
so the sign branch is fixed and the map is smooth. The Jacobian there has one tangent eigenvalue
\[
1
\]
along the accumulator direction and a two-dimensional transverse block
\[
J_V^{\perp}
=
\begin{bmatrix}
1-h_V(1-\beta_1)\lambda&-h_V\beta_1\\
(1-\beta_1)\lambda&\beta_1
\end{bmatrix},
\]
where
\[
h_V=\frac{\eta}{\sqrt V+\varepsilon}.
\]
Define
\[
\chi_V
=
h_V\lambda
=
\frac{\eta\lambda}{\sqrt V+\varepsilon}.
\]
The transverse characteristic polynomial is
\[
r^2
-
\left[
1+\beta_1-(1-\beta_1)\chi_V
\right]r
+
\beta_1.
\]

The equilibrium ray is locally normally attracting at \((0,0,V)\) exactly when
\[
0<\chi_V<
\frac{2(1+\beta_1)}{1-\beta_1}.
\]
Equivalently, define
\[
q_\star
=
\frac{\eta\lambda(1-\beta_1)}{2(1+\beta_1)}.
\]
If
\[
q_\star\le\varepsilon,
\]
then every point with \(V>0\) is transversely stable. If
\[
q_\star>\varepsilon,
\]
the sharp accumulator threshold is
\[
V_c=(q_\star-\varepsilon)^2,
\]
and normal attraction holds exactly for
\[
V>V_c.
\]
At
\[
V=V_c>0,
\]
the transverse roots are
\[
-1
\quad\text{and}\quad
-\beta_1,
\]
so the boundary is sharp. For
\[
0<V<V_c,
\]
one transverse root has modulus greater than one.

The second-moment parameter \(\beta_2\) is absent from this first-order spectrum. Its only appearance near the equilibrium ray is in the quadratic drift
\[
v^+-v
=
-(1-\beta_2)\lambda^2x^2
\]
on the local branch. Thus \(\beta_2\) affects the nonlinear motion of the accumulator but not the first-order transverse stability threshold.

The same formula gives a precise initialization tradeoff. As
\[
V\to\infty,
\qquad
\chi_V\to0,
\]
and the larger transverse eigenvalue tends to \(1\). Therefore an arbitrarily large residual or initialized accumulator can make the local effective step arbitrarily small and the local convergence arbitrarily slow, even though it is transversely stable.

The fixed-state ray also means that no point \((0,0,V)\) with \(V>0\) is an asymptotically stable fixed point of the full optimizer state: perturbations purely along the \(v\)-direction remain on the equilibrium ray. The correct local object is a normally attracting or normally repelling invariant manifold, not an isolated optimizer equilibrium.

## Assumptions and scope

The result uses the Yogi update stated in its defining paper, without bias correction, weight decay, or a learning-rate schedule. The paper itself presents this non-debiased recurrence in Algorithm 2.

The theorem is deterministic and scalar. It concerns local dynamics near positive accumulator levels \(V>0\). The endpoint \(V=0\) is nonsmooth because both the square root and the sign branch meet there, so no differentiable fixed-point claim is made at that endpoint.

The theorem classifies first-order transverse stability, not global convergence from the paper's default state \(v_0=0\). The accumulator may move nonlinearly before a trajectory enters a neighborhood of a positive limiting level.

## Proof

At
\[
x=0,
\qquad
m=0,
\]
one has
\[
g=0,
\qquad
m^+=0,
\qquad
v^+=v,
\qquad
x^+=0.
\]
Hence every nonnegative \(V\) gives a fixed state \((0,0,V)\).

Fix \(V>0\). In a sufficiently small neighborhood,
\[
v>\lambda^2x^2,
\]
so
\[
v^+
=
v-(1-\beta_2)\lambda^2x^2.
\]
The derivative of this expression at \(x=0\) is
\[
\mathrm d v^+=\mathrm d v.
\]
Also,
\[
m^+
=
\beta_1m+(1-\beta_1)\lambda x.
\]
In the update for \(x^+\), differentiation of the denominator contributes no first-order term because
\[
m^+=0
\]
at the fixed state. Thus
\[
\mathrm d x^+
=
\mathrm d x
-
\frac{\eta}{\sqrt V+\varepsilon}\mathrm d m^+.
\]
This gives the stated block-triangular Jacobian with tangent eigenvalue \(1\) and transverse block \(J_V^\perp\).

The transverse block has determinant
\[
\beta_1
\]
and trace
\[
T_V
=
1+\beta_1-(1-\beta_1)\chi_V.
\]
For the real monic quadratic
\[
r^2-T_Vr+\beta_1,
\]
the Jury conditions are
\[
1-\beta_1>0,
\]
\[
1-T_V+\beta_1>0,
\]
\[
1+T_V+\beta_1>0.
\]
The first holds by assumption. The second is
\[
(1-\beta_1)\chi_V>0,
\]
and the third is
\[
2(1+\beta_1)-(1-\beta_1)\chi_V>0.
\]
This proves the exact normal-attraction interval.

Solving the upper inequality for \(V\) gives
\[
\sqrt V+\varepsilon
>
\frac{\eta\lambda(1-\beta_1)}{2(1+\beta_1)}.
\]
This is automatic for every \(V>0\) when the right-hand side is at most \(\varepsilon\); otherwise it is equivalent to \(V>V_c\).

At equality, the trace is
\[
-(1+\beta_1),
\]
so the characteristic polynomial factors as
\[
(r+1)(r+\beta_1).
\]
Below the threshold the final Jury inequality fails, proving transverse instability.

Finally, as \(V\to\infty\), \(\chi_V\to0\). The polynomial tends to
\[
(r-1)(r-\beta_1),
\]
so the transverse spectral radius tends to one.

## Verification

The accompanying `verify.py` reconstructs the Jacobian from the recurrence, checks the exact determinant and trace identities, tests the Jury threshold on both sides, verifies the \(-1\) boundary root, and confirms numerically that the transverse spectrum is independent of \(\beta_2\).

The script also checks the exact fixed-state ray directly. Numerical root calculations are transcription guards; the infinite family of equilibria and the sharp transverse threshold follow from the analytic formulas above.

## Relationship to prior work

Zaheer, Reddi, Sachan, Kale, and Kumar introduced Yogi as an additive alternative to EMA-based adaptive methods. Their paper explains that Yogi changes the second moment by an amount proportional to the current squared gradient and uses the sign only to choose whether the accumulator rises or falls. Their convergence theorem is a nonconvex stochastic stationarity bound and does not give a local deterministic optimizer-state stability classification.

The same paper explicitly remarks that initialization of both moments is important in practice and proposes initializing Yogi's second moment from a minibatch estimate of the initial squared gradient rather than always using zero. The invariant-ray calculation above identifies a precise deterministic mechanism behind that sensitivity: positive residual accumulator levels are genuine distinct equilibria of the optimizer state and have different transverse rates and even different transverse stability.

Contemporary implementations preserve Yogi's additive second-moment rule and often expose a nonzero initial accumulator. The inspected implementation documentation does not state the invariant equilibrium ray or the exact threshold \(V_c\).

Focused searches for Yogi fixed points, scalar quadratic stability, local Jacobians, accumulator initialization, and limit cycles did not identify a published statement equivalent to the fixed-manifold and transverse-threshold result.

## Limitations

The result does not prove that a trajectory starting from \(v_0=0\) converges to a positive \(V\), nor does it classify all global scalar trajectories.

The fixed-ray degeneracy is an optimizer-state statement. All points on the ray represent the same model parameter \(x=0\).

The local normal-stability threshold is insensitive to \(\beta_2\), but nonlinear basin geometry and the accumulated second-order drift can depend strongly on \(\beta_2\).

Different software implementations may add bias correction, use a nonzero accumulator by default, or combine Yogi with weight decay and schedules; those modifications require separate dynamics.

## References

1. Manzil Zaheer, Sashank J. Reddi, Devendra Sachan, Satyen Kale, and Sanjiv Kumar, “Adaptive Methods for Nonconvex Optimization,” NeurIPS 2018, paper identifier `90365351ccc7437a1309dc64e4db32a3`.
2. `pytorch-optimizer` Yogi documentation, describing the Yogi recurrence and a configurable nonzero `initial_accumulator`.
