# Exact stationary nullcline regressions and speed-defect budget in FitzHugh–Nagumo
## Finding
Consider the autonomous FitzHugh–Nagumo oscillator
\[
\dot v=v-\frac{v^3}{3}-w+I,
\qquad
\dot w=\varepsilon(v+a-bw),
\]
with
\[
\varepsilon>0,
\qquad
b>0,
\qquad
a,I\in\mathbb R.
\]
Define the cubic voltage nullcline function
\[
F(v)=v-\frac{v^3}{3}+I.
\]

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the exact conditional laws
\[
\boxed{\mathbb E_\mu[w\mid v]=F(v)}
\]
and
\[
\boxed{\mathbb E_\mu[v\mid w]=bw-a}.
\]
Thus the two deterministic nullclines are not merely phase-plane curves: each is exactly a stationary conditional regression of the opposite coordinate.

The conditional residuals are the coordinate speeds,
\[
w-F(v)=-\dot v
\]
and
\[
v-(bw-a)=\frac{\dot w}{\varepsilon}.
\]
Consequently,
\[
\boxed{
\operatorname{Var}_\mu(w)-\operatorname{Var}_\mu(F(v))
=
\mathbb E_\mu[\dot v^2]
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(v)-b^2\operatorname{Var}_\mu(w)
=
\frac{1}{\varepsilon^2}\mathbb E_\mu[\dot w^2]
}.
\]
Combining them gives the exact two-speed budget
\[
\boxed{
\operatorname{Var}_\mu(v)-b^2\operatorname{Var}_\mu(F(v))
=
\frac{1}{\varepsilon^2}\mathbb E_\mu[\dot w^2]
+b^2\mathbb E_\mu[\dot v^2]
}.
\]

Each of the two individual defects vanishes exactly for probability measures supported on the equilibrium set. Hence every compact invariant probability measure that is not supported on equilibria satisfies both strict inequalities
\[
\operatorname{Var}_\mu(w)>\operatorname{Var}_\mu(F(v))
\]
and
\[
\operatorname{Var}_\mu(v)>b^2\operatorname{Var}_\mu(w).
\]
It also gives positive stationary mass to both sides of both nullclines:
\[
\mu\{w<F(v)\}>0,
\qquad
\mu\{w>F(v)\}>0,
\]
and
\[
\mu\{v>bw-a\}>0,
\qquad
\mu\{v<bw-a\}>0.
\]

For the standard parameter values
\[
a=\frac{7}{10},
\qquad
b=\frac45,
\qquad
\varepsilon=\frac{2}{25},
\]
used in a standard reference normalization, the recovery-speed defect becomes
\[
\operatorname{Var}(v)-\frac{16}{25}\operatorname{Var}(w)
=
\frac{625}{4}\mathbb E[\dot w^2],
\]
and the combined budget is
\[
\operatorname{Var}(v)-\frac{16}{25}\operatorname{Var}(F(v))
=
\frac{625}{4}\mathbb E[\dot w^2]
+
\frac{16}{25}\mathbb E[\dot v^2].
\]

## Assumptions and scope
The measure \(\mu\) is invariant for the autonomous flow and supported on a compact subset of \(\mathbb R^2\). Compact support guarantees integrability of the coordinate, cubic, and antiderivative test functions used below.

The normalization is the standard two-variable form
\[
\dot v=v-\frac{v^3}{3}-w+I,
\qquad
\dot w=\varepsilon(v+a-bw),
\]
with voltage-like fast variable \(v\) and recovery variable \(w\). Other common FitzHugh–Nagumo normalizations are related by affine rescaling and replacement of the cubic by an equivalent cubic polynomial; the proof mechanism persists, but the claim here is stated only for the displayed equations.

The equilibrium set is the finite set of solutions of
\[
w=F(v),
\qquad
v+a-bw=0,
\]
equivalently the real roots of
\[
\frac b3v^3+(1-b)v+a-bI=0.
\]
Depending on parameters there can be one or three real equilibria.

The earliest verified public source date for the FitzHugh model is 1 July 1961. The original article introduces the two-variable excitable-oscillatory model and describes regimes with a stable singular point or a limit cycle. A later detailed mathematical treatment writes an equivalent cubic two-dimensional FitzHugh–Nagumo system and proves boundedness and a rich bifurcation structure.

## Proof
Let \(L\) be the generator.

For any continuous function \(\phi\) on the compact \(v\)-range of the support, choose a continuously differentiable antiderivative \(H\) with
\[
H'(v)=\phi(v).
\]
Then
\[
LH
=
\phi(v)\bigl(F(v)-w\bigr).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(v)(F(v)-w)]=0
\]
for every continuous \(\phi\). Therefore
\[
\mathbb E_\mu[w\mid v]=F(v).
\]

Likewise, for any continuous function \(\psi\) on the compact \(w\)-range, choose an antiderivative \(K\) satisfying
\[
K'(w)=\psi(w).
\]
Then
\[
LK
=
\varepsilon\psi(w)(v+a-bw).
\]
Stationarity gives
\[
\mathbb E_\mu[\psi(w)(v+a-bw)]=0,
\]
so
\[
\mathbb E_\mu[v\mid w]=bw-a.
\]

The first conditional expectation makes \(F(v)\) the orthogonal projection of \(w\) onto functions of \(v\). Hence the law of total variance gives
\[
\operatorname{Var}_\mu(w)
=
\operatorname{Var}_\mu(F(v))
+
\mathbb E_\mu[(w-F(v))^2].
\]
Because
\[
w-F(v)=-\dot v,
\]
we obtain
\[
\operatorname{Var}_\mu(w)-\operatorname{Var}_\mu(F(v))
=
\mathbb E_\mu[\dot v^2].
\]

The second conditional expectation similarly gives
\[
\operatorname{Var}_\mu(v)
=
b^2\operatorname{Var}_\mu(w)
+
\mathbb E_\mu[(v+a-bw)^2].
\]
Using
\[
v+a-bw=\frac{\dot w}{\varepsilon}
\]
yields
\[
\operatorname{Var}_\mu(v)-b^2\operatorname{Var}_\mu(w)
=
\frac1{\varepsilon^2}\mathbb E_\mu[\dot w^2].
\]
Substitution of the first identity into the second gives the two-speed budget.

We now classify equality. Suppose first that
\[
\mathbb E_\mu[\dot v^2]=0.
\]
The continuous function \(\dot v\) then vanishes on \(\operatorname{supp}\mu\). The support of an invariant probability measure is invariant under the flow, so along every trajectory in the support,
\[
\dot v=0
\]
for all time. Thus \(v\) is constant and
\[
w=F(v)
\]
is constant as well. Therefore \(\dot w=0\), so every support point is an equilibrium. Conversely every probability measure supported on equilibria has zero defect.

The same argument starts from
\[
\mathbb E_\mu[\dot w^2]=0.
\]
Then \(w\) is constant along each support trajectory and
\[
v=bw-a
\]
is constant, so again the trajectory is an equilibrium. Hence either individual defect vanishes exactly for equilibrium-supported measures.

Finally consider a measure not supported on equilibria. Both squared-speed expectations are then strictly positive. Invariance of the coordinate functions gives
\[
\mathbb E_\mu[\dot v]=0,
\qquad
\mathbb E_\mu[\dot w]=0.
\]
A nonzero square-integrable random variable with mean zero must take both positive and negative values on sets of positive measure. Therefore \(\dot v\) has both signs, equivalently \(w-F(v)\) has both signs, and \(\dot w\) has both signs, equivalently \(v-(bw-a)\) has both signs. This proves the two-sided nullcline crossing statement.

## Verification
The accompanying checker verifies the polynomial vector-field identities and the exact standard-parameter coefficients.

It checks
\[
\dot v=F(v)-w,
\qquad
\frac{\dot w}{\varepsilon}=v+a-bw,
\]
and the equilibrium polynomial
\[
\frac b3v^3+(1-b)v+a-bI=0.
\]

For
\[
b=\frac45,
\qquad
\varepsilon=\frac{2}{25},
\]
it confirms exactly
\[
b^2=\frac{16}{25},
\qquad
\varepsilon^{-2}=\frac{625}{4}.
\]

The stored checker output is `VERIFY_OK`.

The checker confirms only algebraic certificates. The conditional-expectation statements, variance decompositions, equality rigidity, and sign-crossing conclusions are analytic consequences of stationarity and invariant support and are not inferred from finite simulations.

## Relationship to prior work
FitzHugh's 1961 article introduced the planar excitable-oscillatory model as a Bonhoeffer–van der Pol generalization, with two state variables representing excitability and refractoriness. Nagumo, Arimoto, and Yoshizawa built the related active pulse-transmission circuit the following year.

A complete mathematical preprint later published as *FitzHugh–Nagumo Revisited* studies an equivalent cubic two-dimensional system in detail. It proves forward boundedness, classifies equilibria and Hopf bifurcations, and studies homoclinic and saddle-node phenomena. Full-text searches of that source for `average`, `moment`, `invariant measure`, and `conditional` returned no matching stationary-statistical formulation. Its results do not implication-wise give either nullcline conditional regression or the two-speed variance budget.

A recent full article on dynamic homeostasis uses a standard FitzHugh–Nagumo relaxation oscillator and studies how the period-average of the slow variable changes with input. It emphasizes that the slow-variable average is approximately insensitive over an oscillatory parameter range, while the fast-variable average is not. That parameter-sweep statement is different from the exact fixed-parameter identities here, which condition on the instantaneous opposite coordinate and hold for every compact invariant measure rather than one attracting relaxation cycle.

A standard reference presentation writes exactly
\[
\dot v=v-\frac{v^3}{3}-w+I,
\qquad
\dot w=0.08(v+0.7-0.8w),
\]
and identifies the cubic and linear nullclines as the organizing geometry of the model. The accepted theorem turns those same nullclines into exact stationary regression functions and quantifies their residuals by the physical coordinate speeds.

Mathematical FitzHugh–Nagumo and piecewise-linear FitzHugh–Nagumo literature includes primary MSC \(34C05\), supporting the ordinary-differential-equation dynamical classification used here.

## Limitations
The theorem concerns compactly supported invariant probability measures for the autonomous planar oscillator. It does not treat stochastic forcing, spatial diffusion, delay, or time-dependent input.

The conditional laws determine only the first conditional moment of the opposite coordinate. They do not determine the full invariant density or the period of a limit cycle.

The equality classification permits arbitrary probability mixtures of equilibrium atoms when several equilibria exist.

The recent dynamic-homeostasis literature studies approximate parameter insensitivity of cycle averages; no contradiction is implied because the accepted theorem is a fixed-parameter exact disintegration.

Because the generator argument is short, an equivalent observation could occur incidentally in unindexed neuroscience or oscillator literature. No novelty is claimed for the FitzHugh–Nagumo equations, nullclines, equilibrium structure, boundedness, Hopf bifurcations, or existence of periodic solutions.

## References
1. R. FitzHugh, “Impulses and Physiological States in Theoretical Models of Nerve Membrane,” *Biophysical Journal* 1, 445–466 (1961), DOI 10.1016/S0006-3495(61)86902-6.
2. J. Nagumo, S. Arimoto, and S. Yoshizawa, “An Active Pulse Transmission Line Simulating Nerve Axon,” *Proceedings of the IRE* 50, 2061–2070 (1962), DOI 10.1109/JRPROC.1962.288235.
3. T. Kostova, R. Ravindran, and M. E. Schonbek, “FitzHugh–Nagumo Revisited: Types of Bifurcations, Periodical Forcing and Stability Regions by a Lyapunov Functional,” *International Journal of Bifurcation and Chaos* 14, 913–925 (2004), DOI 10.1142/S0218127404009685.
4. A. Tonnelier, “The McKean's Caricature of the FitzHugh–Nagumo Model I. The Space-Clamped System,” *SIAM Journal on Applied Mathematics* 63, 459–484 (2003), DOI 10.1137/S0036139901393500.
5. E. M. Izhikevich and R. FitzHugh, “FitzHugh–Nagumo model,” *Scholarpedia* 1(9), 1349 (2006), DOI 10.4249/scholarpedia.1349.
6. “Dynamic Homeostasis in Relaxation and Bursting Oscillations,” *SIAM Journal on Life Sciences* (2026), DOI 10.1137/25M1779309.
