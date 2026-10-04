# Exact stationary nullcline regressions and speed defects in the Morris–Lecar oscillator
## Finding
Consider the standard two-dimensional Morris–Lecar system
\[
C\dot V
=
F(V)-g_K(V-V_K)W,
\]
\[
\dot W
=
q(V)\bigl(W_\infty(V)-W\bigr),
\]
where
\[
F(V)
=
I_{\rm app}
-g_L(V-V_L)
-g_{Ca}M_\infty(V)(V-V_{Ca}),
\]
with
\[
C>0,\qquad
g_K>0,\qquad
q(V)>0.
\]

For the classical sigmoid formulation,
\[
M_\infty(V)
=
\frac12
\left[
1+\tanh\!\left(\frac{V-V_1}{V_2}\right)
\right],
\]
\[
W_\infty(V)
=
\frac12
\left[
1+\tanh\!\left(\frac{V-V_3}{V_4}\right)
\right],
\]
and
\[
q(V)
=
\frac{\phi}{\tau_W(V)},
\qquad
\tau_W(V)
=
\frac{1}{
\cosh\!\left(\frac{V-V_3}{2V_4}\right)
},
\]
with
\[
\phi>0,\qquad V_2>0,\qquad V_4>0.
\]
Thus \(W_\infty\) is strictly increasing.

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the exact voltage-fiber current calibration
\[
\boxed{
\mathbb E_\mu[
g_K(V-V_K)W\mid V
]
=
F(V)
}.
\]

Define
\[
Z
=
\mathbb E_\mu[q(V)]
>0
\]
and the rate-tilted probability measure
\[
d\nu
=
\frac{q(V)}{Z}\,d\mu.
\]
Then the recovery gate satisfies the exact tilted conditional law
\[
\boxed{
\mathbb E_\nu[
W_\infty(V)\mid W
]
=
W
}.
\]

These two nullcline regressions have exact fluctuation defects:
\[
\boxed{
\operatorname{Var}_\mu(
g_K(V-V_K)W
)
-
\operatorname{Var}_\mu(F(V))
=
C^2\mathbb E_\mu[\dot V^2]
}
\]
and
\[
\boxed{
\operatorname{Var}_\nu(W_\infty(V))
-
\operatorname{Var}_\nu(W)
=
\frac{
\mathbb E_\mu[\dot W^2/q(V)]
}{
\mathbb E_\mu[q(V)]
}
}.
\]

For the usual rate
\[
q(V)=\frac{\phi}{\tau_W(V)},
\]
the second identity is equivalently
\[
\operatorname{Var}_\nu(W_\infty(V))
-
\operatorname{Var}_\nu(W)
=
\frac{
\mathbb E_\mu[\tau_W(V)\dot W^2]
}{
\phi^2\mathbb E_\mu[\tau_W(V)^{-1}]
}.
\]

Each defect vanishes exactly for probability measures supported on the equilibrium set.

Consequently every compact stationary state that is not equilibrium-supported has both defects strictly positive. It gives positive mass to both sides of both phase-plane nullclines
\[
F(V)=g_K(V-V_K)W
\]
and
\[
W=W_\infty(V).
\]
In particular every nonconstant periodic orbit crosses both nullclines.

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the autonomous Morris–Lecar flow and supported on a compact subset of the phase plane.

The theorem is stated for the standard two-dimensional reduced model with constant applied current. The only structural hypotheses needed for the first regression are
\[
C>0,\qquad g_K>0.
\]
For the second regression and equality classification we assume
\[
q(V)>0
\]
throughout the compact voltage range and that \(W_\infty\) is strictly increasing. These properties hold for the standard hyperbolic-function parametrization with
\[
\phi>0,\qquad V_4>0.
\]

The first regression is deliberately written without dividing by
\[
V-V_K.
\]
Thus it remains valid even if an invariant state charges the potassium reversal voltage. Away from
\[
V=V_K,
\]
it can be written as
\[
\mathbb E_\mu[W\mid V]
=
\frac{F(V)}{g_K(V-V_K)}.
\]

The earliest verified public date for the Morris–Lecar paper is 1 July 1981. The original article studies oscillatory and bistable behavior in a two-conductance barnacle muscle model. A later authoritative model description writes the reduced equations in the exact voltage–recovery form used here.

A same-family bifurcation article lists primary MSC \(34C15\); this result is classified accordingly.

## Proof
Let \(L\) be the generator of the Morris–Lecar flow.

Take any continuous function \(\varphi\) on the compact voltage range and choose a continuously differentiable antiderivative \(H\) satisfying
\[
H'(V)=\varphi(V).
\]
Then
\[
LH
=
\frac{\varphi(V)}{C}
\left[
F(V)-g_K(V-V_K)W
\right].
\]
Invariance gives
\[
\mathbb E_\mu[
\varphi(V)
(
F(V)-g_K(V-V_K)W
)
]
=
0
\]
for every such \(\varphi\). Hence
\[
\mathbb E_\mu[
g_K(V-V_K)W\mid V
]
=
F(V).
\]

Set
\[
A
=
g_K(V-V_K)W,
\qquad
B
=
F(V).
\]
The conditional law is
\[
\mathbb E_\mu[A\mid V]=B.
\]
Therefore
\[
\mathbb E_\mu[A]=\mathbb E_\mu[B]
\]
and
\[
\mathbb E_\mu[AB]
=
\mathbb E_\mu[B^2].
\]
Since
\[
A-B=-C\dot V,
\]
expansion gives
\[
C^2\mathbb E_\mu[\dot V^2]
=
\mathbb E_\mu[(A-B)^2]
=
\operatorname{Var}_\mu(A)
-
\operatorname{Var}_\mu(B).
\]

For the gate variable, take any continuous function \(\psi\) on the compact \(W\)-range and choose an antiderivative \(K\) with
\[
K'(W)=\psi(W).
\]
Then
\[
LK
=
\psi(W)q(V)(W_\infty(V)-W).
\]
Invariance yields
\[
\mathbb E_\mu[
\psi(W)q(V)(W_\infty(V)-W)
]
=
0.
\]
Dividing by the positive normalizing constant
\[
Z=\mathbb E_\mu[q(V)]
\]
gives
\[
\mathbb E_\nu[
\psi(W)(W_\infty(V)-W)
]
=
0
\]
for every \(\psi\), hence
\[
\mathbb E_\nu[
W_\infty(V)\mid W
]
=
W.
\]

The conditional-variance decomposition under \(\nu\) now gives
\[
\operatorname{Var}_\nu(W_\infty(V))
=
\operatorname{Var}_\nu(W)
+
\mathbb E_\nu[
(W_\infty(V)-W)^2
].
\]
Because
\[
\dot W
=
q(V)(W_\infty(V)-W),
\]
we have
\[
\mathbb E_\nu[
(W_\infty(V)-W)^2
]
=
\frac{
\mathbb E_\mu[
q(V)(W_\infty(V)-W)^2
]
}{
Z
}
=
\frac{
\mathbb E_\mu[\dot W^2/q(V)]
}{
\mathbb E_\mu[q(V)]
}.
\]

We classify equality.

If the voltage defect vanishes, then
\[
\dot V=0
\]
on the invariant support. Along each support trajectory, \(V\) is constant, say \(V_0\). The gate equation becomes the scalar linear equation
\[
\dot W
=
q(V_0)
\bigl(
W_\infty(V_0)-W
\bigr).
\]
Every nonconstant solution of this equation is unbounded in backward time. A trajectory in a compact invariant support is bounded and complete, so
\[
W=W_\infty(V_0)
\]
and the trajectory is an equilibrium.

If the gate defect vanishes, then
\[
W_\infty(V)=W
\]
almost surely under \(\nu\). Since
\[
q(V)>0,
\]
the measures \(\mu\) and \(\nu\) have the same null sets on the compact support, so
\[
\dot W=0
\]
on the support. Thus \(W\) is constant along every support trajectory. Because \(W_\infty\) is strictly increasing,
\[
W_\infty(V)=W
\]
forces \(V\) to be constant as well. Hence the support again consists of equilibria.

Conversely, any probability measure supported on equilibria makes both defects vanish.

Finally, for an invariant measure,
\[
\mathbb E_\mu[\dot V]=0,
\qquad
\mathbb E_\mu[\dot W]=0.
\]
For a non-equilibrium-supported measure, both mean-square speeds are positive. Therefore each derivative has positive mass on both signs. Since
\[
C\dot V
=
F(V)-g_K(V-V_K)W
\]
and
\[
\dot W
=
q(V)(W_\infty(V)-W),
\qquad
q(V)>0,
\]
the measure lies on both sides of both nullclines.

## Verification
The accompanying checker validates the algebra behind both variance defects using exact rational arithmetic.

For an abstract conditional regression
\[
\mathbb E[A\mid B]=B,
\]
it checks that the moment consequences
\[
\mathbb E[A]=\mathbb E[B],
\qquad
\mathbb E[AB]=\mathbb E[B^2]
\]
make
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B)
\]
an exact identity.

It also verifies the measure-tilt conversion
\[
\mathbb E_\nu[\Delta^2]
=
\frac{\mathbb E_\mu[q\Delta^2]}{\mathbb E_\mu[q]}
=
\frac{\mathbb E_\mu[\dot W^2/q]}{\mathbb E_\mu[q]}
\]
when
\[
\dot W=q\Delta.
\]

For the standard parametrization it verifies the algebraic conversion
\[
q=\frac{\phi}{\tau}
\]
to
\[
\frac{\mathbb E_\mu[\dot W^2/q]}{\mathbb E_\mu[q]}
=
\frac{
\mathbb E_\mu[\tau\dot W^2]
}{
\phi^2\mathbb E_\mu[\tau^{-1}]
}.
\]

The stored checker output is `VERIFY_OK`.

The equality classification and nullcline crossing are analytic consequences of compact invariant support, positivity of \(q\), and strict monotonicity of \(W_\infty\); they are not inferred from finite numerical experiments.

## Relationship to prior work
Morris and Lecar introduced the conductance-based oscillator in 1981 and analyzed damped and sustained voltage oscillations and bistability. The public bibliographic record and reduced-model repository establish the original model and its provenance. A complete primary full-text fetch was not stable in the inspected route, so no whole-document noncoverage claim is made for that paper.

Lecar's later model description writes the familiar two-dimensional reduction
\[
C\dot V
=
-I_{\rm ion}(V,W)+I_{\rm app},
\qquad
\dot W
=
\frac{W_\infty(V)-W}{T_W(V)},
\]
with an instantaneous calcium current and delayed potassium recovery. This is the normalization used in the present theorem.

Duan, Zhai, and Lu study Morris–Lecar excitability and bursting through fast–slow and two-parameter bifurcation analysis. Their article is classified primarily under \(34C15\). The accessible article page contains no invariant-measure, variance, or average statement.

Cirillo and Sepulchre use Morris–Lecar as the canonical two-dimensional conductance-based slow–fast model before adding a second slow current for rest–spike bistability. Their full open article emphasizes nullclines, critical manifolds, invariant manifolds, folds, and limit cycles. Targeted full-document searches did not locate invariant-measure, variance, or average identities of the kind proved here.

A recent probability-measure study uses the Morris–Lecar model as a test system and explicitly discusses approximating an invariant measure on a stable limit cycle. Its full Morris–Lecar section concerns stochastic transition paths and early-warning indicators; targeted searches did not locate the two conditional nullcline regressions or either exact stationary variance defect.

The accepted result therefore does not claim new phase portraits or bifurcation thresholds. It identifies the two classical nullclines as exact stationary regression objects—one under the physical stationary law and the other under the intrinsic gate-rate tilt—and quantifies their residual fluctuations exactly by coordinate speeds.

## Limitations
The theorem concerns compactly supported invariant probability measures for the autonomous two-dimensional model with constant applied current.

The second regression is taken under the rate-tilted probability measure
\[
d\nu\propto q(V)d\mu,
\]
not under the original stationary measure unless \(q\) is constant.

The result does not determine the period, firing frequency, phase response, bifurcation threshold, or full invariant density.

The original 1981 full text was not stably retrievable in the inspected route; the exact reduced equations were independently checked in later authoritative model descriptions and repositories.

Because the generator calculations are short, an equivalent stationary-moment observation could remain in unindexed computational-neuroscience literature.

## References
1. C. Morris and H. Lecar, “Voltage oscillations in the barnacle giant muscle fiber,” Biophysical Journal 35, 193–213 (1981), DOI 10.1016/S0006-3495(81)84782-0.
2. H. Lecar, “Morris-Lecar model,” Scholarpedia 2, 1333 (2007), DOI 10.4249/scholarpedia.1333.
3. L. Duan, D. Zhai, and Q. Lu, “Bifurcation and bursting in Morris-Lecar model for class I and class II excitability,” Proceedings of the 8th AIMS International Conference, 391–399 (2011), DOI 10.3934/proc.2011.2011.391.
4. G. I. Cirillo and R. Sepulchre, “The geometry of rest–spike bistability,” Journal of Mathematical Neuroscience 10, 13 (2020), DOI 10.1186/s13408-020-00090-z.
5. P. Zhang, T. Gao, J. Guo, and J. Duan, “Action functional as an early warning indicator in the space of probability measures via Schrödinger bridge,” Quantitative Biology 13, e86 (2025), DOI 10.1002/qub2.86.
