# A hidden constraint invariant doubles the scalar feasibility exponent in undamped ELR flow
## Finding

Consider
\[
\min_{x\in\mathbb R} 0
\qquad\text{subject to}\qquad
x=0.
\]
Use the undamped Euclidean specialization of the coupled Euler--Lagrange primal--dual flow with augmented-Lagrangian penalty
\[
\mu>0.
\]
Let
\[
z_x=x+e^{-a_t}\dot x,
\qquad
z_\lambda=\lambda+e^{-a_t}\dot\lambda,
\]
and impose the exact ideal scaling
\[
e^{a_t}=\dot b_t>0.
\]
Set
\[
s=e^{b_t}.
\]

Then the quantity
\[
I=sx-z_\lambda
\]
is constant along every trajectory.

Writing
\[
w=sx=z_\lambda+I,
\]
the four-dimensional primal--dual flow collapses, for feasibility purposes, to the scalar nonautonomous oscillator
\[
\frac{d^2w}{ds^2}
+
\left(1+\frac{\mu}{s}\right)w
=
I.
\]
Every solution of this equation is bounded on
\[
s\ge s_0>0.
\]
Therefore
\[
|x(t)|
=
\frac{|w(e^{b_t})|}{e^{b_t}}
=
O(e^{-b_t}).
\]

This is a full exponent faster than the generic undamped feasibility conclusion obtained by taking the square root of
\[
\|r(x(t))\|^2=O(e^{-b_t}).
\]
No Rayleigh friction is needed on this scalar constraint mode.

The exponent is also sharp within the same model. If
\[
I=0
\]
and the trajectory is nonzero, then
\[
\limsup_{t\to\infty}e^{b_t}|x(t)|>0.
\]
Hence the feasibility error is generally not
\[
o(e^{-b_t}).
\]

The mechanism is not dissipation of the lookahead variable. On the sharp family,
\[
z_\lambda=sx
\]
retains a nonvanishing oscillatory amplitude while the primal position gains the extra factor
\[
s^{-1}=e^{-b_t}.
\]
The faster feasibility rate comes from an exact position--lookahead invariant.

## Assumptions and scope

The objective is identically zero, the affine constraint is scalar and nondegenerate, the primal and multiplier Bregman generators are Euclidean quadratics, and the Rayleigh friction coefficient is zero.

The augmented-Lagrangian penalty is any fixed
\[
\mu>0.
\]
The scaling function satisfies
\[
e^{a_t}=\dot b_t>0,
\]
so
\[
s=e^{b_t}
\]
is a valid increasing time variable. No special choice such as polynomial or exponential \(b_t\) is required.

The result concerns this exact scalar constraint mode. It is not asserted for multiple coupled constraints, non-Euclidean mirror maps, nonlinear constraints, or arbitrary objective curvature.

## Proof

For the Euclidean mirror maps, the source first-order flow becomes
\[
\dot x=e^{a_t}(z_x-x),
\]
\[
\dot z_x=-e^{a_t+b_t}(\mu x+z_\lambda),
\]
\[
\dot\lambda=e^{a_t}(z_\lambda-\lambda),
\]
\[
\dot z_\lambda=e^{a_t+b_t}z_x.
\]

Because
\[
s=e^{b_t},
\qquad
\dot s=e^{a_t}s,
\]
division by \(\dot s\) gives
\[
\frac{dx}{ds}=\frac{z_x-x}{s},
\qquad
\frac{dz_x}{ds}=-(\mu x+z_\lambda),
\]
\[
\frac{d\lambda}{ds}=\frac{z_\lambda-\lambda}{s},
\qquad
\frac{dz_\lambda}{ds}=z_x.
\]

Now
\[
\frac{d}{ds}(sx-z_\lambda)
=
x+s\frac{dx}{ds}-\frac{dz_\lambda}{ds}
=
x+(z_x-x)-z_x
=
0.
\]
Thus
\[
I=sx-z_\lambda
\]
is invariant.

Let
\[
w=sx=z_\lambda+I.
\]
Then
\[
w'=\frac{dz_\lambda}{ds}=z_x
\]
and
\[
w''
=
\frac{dz_x}{ds}
=
-(\mu x+z_\lambda)
=
I-\left(1+\frac{\mu}{s}\right)w.
\]
Hence
\[
w''+q(s)w=I,
\qquad
q(s)=1+\frac{\mu}{s}.
\]

To prove boundedness, define the instantaneous equilibrium
\[
r(s)=\frac{I}{q(s)}
=
\frac{Is}{s+\mu},
\qquad
v=w-r.
\]
Then
\[
v''+qv=f(s),
\qquad
f(s)=-r''(s)
=
\frac{2I\mu}{(s+\mu)^3}.
\]
Consider
\[
E(s)=\frac12v'(s)^2+\frac12q(s)v(s)^2.
\]
Since
\[
q'(s)=-\frac{\mu}{s^2}<0,
\]
we have
\[
E'
=
f v'
+
\frac12q'v^2
\le
|f|\,|v'|
\le
|f|\sqrt{2E}.
\]
Therefore
\[
\frac{d}{ds}\sqrt{E(s)}
\le
\frac{|f(s)|}{\sqrt2}.
\]
The forcing is integrable:
\[
\int_{s_0}^{\infty}|f(s)|\,ds
=
\frac{|I|\mu}{(s_0+\mu)^2}.
\]
Thus \(E\), \(v\), \(r\), and therefore \(w\) remain bounded for all \(s\ge s_0\). Since
\[
x=\frac{w}{s},
\]
this proves
\[
|x(t)|=O(e^{-b_t}).
\]

For sharpness, restrict to
\[
I=0.
\]
Then
\[
w''+q(s)w=0
\]
and
\[
E(s)=\frac12w'^2+\frac12q w^2
\]
satisfies
\[
E'=\frac12q'w^2\le0.
\]
Because
\[
w^2\le\frac{2E}{q}
\]
and \(q'<0\),
\[
E'
\ge
\frac{q'}{q}E.
\]
Hence every nonzero solution obeys
\[
E(s)
\ge
E(s_0)\frac{q(s)}{q(s_0)}
\ge
\frac{E(s_0)}{q(s_0)}
>
0.
\]

If \(w(s)\to0\), then
\[
w''(s)=-q(s)w(s)\to0.
\]
A function converging to zero with second derivative converging to zero must also have first derivative converging to zero: apply the mean-value formula on any fixed forward interval and then let the starting point tend to infinity. This would force
\[
E(s)\to0,
\]
contradicting the positive lower bound above. Therefore
\[
\limsup_{s\to\infty}|w(s)|>0.
\]
Since
\[
s|x|=|w|,
\]
the rate
\[
e^{-b_t}
\]
cannot be improved to little-\(o\) uniformly on this family.

## Verification

The standalone script `artifacts/verify_elr_scalar_invariant.py` integrates the transformed four-state flow and the reduced oscillator independently for several parameter choices. It checks conservation of
\[
sx-z_\lambda,
\]
agreement between the two representations, boundedness of \(w=sx\), and a nonvanishing scaled feasibility amplitude on a nonzero \(I=0\) trajectory.

These finite calculations are consistency checks only. The invariant, energy estimate, and sharpness argument above prove the all-parameter statement.

## Relationship to prior work

The recent coupled Euler--Lagrange--Rayleigh paper supplies the exact primal and multiplier mirror flows used here. Its general undamped theorem gives
\[
\|r(x(t))\|^2=O(e^{-b_t}),
\]
while its strengthened
\[
\|r(x(t))\|=O(e^{-b_t})
\]
statement is presented with additional friction and boundedness assumptions. The scalar invariant above is not used in that analysis and gives the strengthened feasibility exponent with zero Rayleigh friction.

Attouch, Chbani, Fadili, and Riahi study a different inertial augmented-Lagrangian system with viscous damping, extrapolation, and time scaling. Their method is second-order directly in the primal and multiplier variables and does not contain the same position/lookahead mirror pair, so its rate theory does not imply the invariant
\[
e^{b_t}x-z_\lambda.
\]

Zhao, Liao, He, Zhou, and Li develop accelerated primal--dual mirror dynamics for affine constraints and prove accelerated feasibility and objective rates by Lyapunov analysis. Their flow and scaling architecture differ from the coupled Euler--Lagrange lookahead system considered here; the inspected full text does not state the scalar invariant or the forced oscillator reduction above.

Targeted searches using the flow name, equality-constraint specialization, lookahead variables, the invariant form, scalar oscillator reduction, and full
\[
e^{-b_t}
\]
undamped feasibility rate returned no equivalent statement.

## Limitations

The result is modal and scalar. It does not show that the generic theorem can be strengthened to
\[
\|r(x(t))\|=O(e^{-b_t})
\]
for arbitrary affine constraints or general Bregman geometries.

The sharpness claim concerns the exponent inside this scalar family, not a minimax lower bound for all accelerated primal--dual continuous-time methods.

The transformed oscillator is elementary enough that an equivalent calculation may exist in older accelerated augmented-Lagrangian literature under different notation. No such statement was found in the closest full texts inspected, but this remains the main historical originality risk.

## References

1. C. Chang, M. Mesbahi, *Unifying Variational View of Accelerated Primal-Dual Methods*, arXiv:2609.09454v2, 2026.
2. H. Attouch, Z. Chbani, J. Fadili, H. Riahi, *Fast Convergence of Dynamical ADMM via Time Scaling of Damped Inertial Dynamics*, Journal of Optimization Theory and Applications 193, 704--736, 2022; arXiv:2103.12675.
3. Y. Zhao, X. Liao, X. He, M. Zhou, C. Li, *Accelerated Primal-Dual Mirror Dynamics for Centralized and Distributed Constrained Convex Optimization Problems*, Journal of Machine Learning Research 24, Article 343, 2023.
