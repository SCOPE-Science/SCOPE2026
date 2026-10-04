# Fiberwise prey excess and nullcline calibration in the Rosenzweig–MacArthur oscillator
## Finding
Consider the dimensionless Rosenzweig–MacArthur predator–prey system
\[
\dot N=rN(1-N)-\frac{NP}{h+N},
\qquad
\dot P=\frac{NP}{h+N}-mP,
\]
with
\[
r>0,\qquad h>0,\qquad m>0.
\]
Here \(N\) is prey density and \(P\) is predator density.

Let \(\mu\) be a compactly supported invariant Borel probability measure whose support lies in the strictly positive quadrant. Then such a measure can exist only if
\[
m<\frac{1}{1+h}.
\]
Define the positive coexistence equilibrium by
\[
N_* = \frac{mh}{1-m},
\qquad
P_* = r(1-N_*)(h+N_*).
\]

Every such stationary state satisfies two exact nullcline regressions:
\[
\boxed{\mathbb E_\mu[P\mid N]=r(1-N)(h+N)}
\]
and
\[
\boxed{\mathbb E_\mu\!\left[\frac{N}{h+N}\,\middle|\,P\right]=m}.
\]
The second law is equivalently the fiberwise harmonic calibration
\[
\boxed{
\mathbb E_\mu\!\left[\frac{1}{h+N}\,\middle|\,P\right]
=
\frac{1}{h+N_*}
}.
\]

This harmonic identity has an exact conditional defect. For \(\mu\)-almost every predator density,
\[
\boxed{
\mathbb E_\mu[N\mid P]-N_*
=
\mathbb E_\mu\!\left[\frac{(N-N_*)^2}{h+N}\,\middle|\,P\right]
}.
\]
Since
\[
\frac{\dot P}{P}
=
\frac{N}{h+N}-m,
\]
the same identity can be written as
\[
\boxed{
\mathbb E_\mu[N\mid P]-N_*
=
\frac{1}{(1-m)^2}
\mathbb E_\mu\!\left[(h+N)\left(\frac{\dot P}{P}\right)^2\,\middle|\,P\right]
}.
\]
Thus every predator-density fiber is prey-enriched relative to the coexistence prey density, with equality on a fiber exactly when that fiber is concentrated at \(N=N_*\).

Averaging over \(P\) gives
\[
\boxed{
\mathbb E_\mu[N]-N_*
=
\mathbb E_\mu\!\left[\frac{(N-N_*)^2}{h+N}\right]
=
\frac{1}{(1-m)^2}
\mathbb E_\mu\!\left[(h+N)\left(\frac{\dot P}{P}\right)^2\right]
}.
\]
The right-hand side vanishes exactly at the coexistence equilibrium atom. Therefore every non-equilibrium compact stationary state has
\[
\mathbb E_\mu[N]>N_*.
\]

The two per-capita coordinate speeds also have exact variance defects:
\[
\boxed{
\operatorname{Var}_\mu\!\left(\frac{P}{h+N}\right)
-r^2\operatorname{Var}_\mu(N)
=
\mathbb E_\mu\!\left[\left(\frac{\dot N}{N}\right)^2\right]
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu\!\left(\frac{N}{h+N}\right)
=
\mathbb E_\mu\!\left[\left(\frac{\dot P}{P}\right)^2\right]
}.
\]
For every non-equilibrium stationary state both right-hand sides are strictly positive, so the state puts positive mass on both sides of both classical nullclines.

The classical fact that a Rosenzweig–MacArthur cycle has prey time average above the coexistence equilibrium is prior. The finding assessed here is the all-invariant-measures fiberwise strengthening and the exact conditional and global defect formulas.

## Assumptions and scope
The invariant measure is compactly supported in \((0,\infty)^2\). This gives positive lower bounds for \(N\) and \(P\) on the support, so logarithmic antiderivative tests are legitimate.

The displayed model is a standard nondimensional Rosenzweig–MacArthur system with logistic prey growth and a Holling type II response. The same normalization appears in later eco-epidemiological work, while an equivalent six-parameter dimensional form is
\[
\dot S=rS\left(1-\frac{S}{K}\right)-\frac{qXS}{H+S},
\qquad
\dot X=\frac{pXS}{H+S}-dX.
\]

The foundational predator–prey article was published on 1 July 1963. A classical mathematical treatment of logistic prey with saturating Michaelis–Menten predation is classified under MSC \(34C05\), and a later Rosenzweig–MacArthur trajectory paper explicitly lists primary MSC \(34C05\). The present result is classified accordingly.

## Proof
Let \(L\) denote the generator of the flow.

Take any continuous function \(\phi\) on the compact prey range. Choose a continuously differentiable antiderivative \(H\) satisfying
\[
H'(N)=\frac{\phi(N)}{N}.
\]
Then
\[
LH
=
\phi(N)
\left[
r(1-N)-\frac{P}{h+N}
\right].
\]
Invariance gives
\[
\mathbb E_\mu\!\left[
\phi(N)
\left(
r(1-N)-\frac{P}{h+N}
\right)
\right]=0
\]
for every \(\phi\). Hence
\[
\mathbb E_\mu\!\left[\frac{P}{h+N}\,\middle|\,N\right]
=r(1-N),
\]
and therefore
\[
\mathbb E_\mu[P\mid N]
=r(1-N)(h+N).
\]
Because \(P>0\) on the support, this forces
\[
N<1
\]
almost surely and hence
\[
\operatorname{supp}\mu\subseteq\{N\le1\}.
\]

Now take a continuous function \(\psi\) on the compact predator range and choose \(K\) with
\[
K'(P)=\frac{\psi(P)}{P}.
\]
Then
\[
LK
=
\psi(P)
\left[
\frac{N}{h+N}-m
\right].
\]
Stationarity yields
\[
\mathbb E_\mu\!\left[\frac{N}{h+N}\,\middle|\,P\right]
=m.
\]
Since \(0<N<1\) almost surely and \(N/(h+N)\) is strictly increasing,
\[
0<m<\frac{1}{1+h}.
\]
Thus \(N_*\) and \(P_*\) above are positive.

Using
\[
\frac{N}{h+N}
=
1-\frac{h}{h+N}
\]
and
\[
1-m
=
\frac{h}{h+N_*},
\]
the predator-fiber law is exactly
\[
\mathbb E_\mu\!\left[\frac{1}{h+N}\,\middle|\,P\right]
=
\frac{1}{h+N_*}.
\]

Set
\[
Y=h+N,
\qquad
Y_*=h+N_*.
\]
Then
\[
\frac{(N-N_*)^2}{h+N}
=
\frac{(Y-Y_*)^2}{Y}
=
Y-2Y_*+\frac{Y_*^2}{Y}.
\]
Taking the conditional expectation given \(P\) and using the harmonic law gives
\[
\mathbb E_\mu\!\left[\frac{(N-N_*)^2}{h+N}\,\middle|\,P\right]
=
\mathbb E_\mu[N\mid P]-N_*.
\]

Furthermore,
\[
\frac{\dot P}{P}
=
\frac{N}{h+N}-m
=
\frac{h(N-N_*)}{(h+N)(h+N_*)}.
\]
Therefore
\[
(h+N)\left(\frac{\dot P}{P}\right)^2
=
(1-m)^2\frac{(N-N_*)^2}{h+N},
\]
which proves the speed-weighted version of the conditional defect.

For the prey variance law, define
\[
A=\frac{P}{h+N},
\qquad
B=r(1-N).
\]
The first conditional law is \(\mathbb E[A\mid N]=B\), while
\[
A-B=-\frac{\dot N}{N}.
\]
Conditional orthogonality gives
\[
\operatorname{Var}(A)-\operatorname{Var}(B)
=
\mathbb E[(A-B)^2],
\]
which is the first displayed variance defect.

For the predator equation,
\[
C=\frac{N}{h+N}
\]
has conditional mean \(m\) given \(P\). Hence its global mean is \(m\), and
\[
\operatorname{Var}(C)
=
\mathbb E[(C-m)^2]
=
\mathbb E\!\left[\left(\frac{\dot P}{P}\right)^2\right].
\]

If the global prey-excess defect vanishes, then \(N=N_*\) almost surely. Invariance of the support and the prey equation then force \(P=P_*\), so \(\mu\) is the coexistence equilibrium atom. The same conclusion follows if either per-capita speed defect vanishes. Conversely the equilibrium atom makes all defects zero.

For a non-equilibrium stationary state, each per-capita speed has zero mean by stationarity of \(\log N\) and \(\log P\), but positive mean square. Therefore each speed takes both signs on sets of positive measure, which is exactly two-sided crossing of the prey and predator nullclines.

## Verification
The accompanying checker uses exact symbolic polynomial arithmetic after clearing the positive denominator \(h+N\), together with exact rational test values for the conditional-defect algebra.

It verifies the equilibrium identities
\[
\frac{N_*}{h+N_*}=m
\]
and
\[
P_*=r(1-N_*)(h+N_*).
\]

It verifies algebraically that
\[
\frac{N}{h+N}-m
=
\frac{h(N-N_*)}{(h+N)(h+N_*)},
\]
and hence the speed-weighted defect coefficient \((1-m)^{-2}\).

It also verifies the abstract conditional-regression identity
\[
\operatorname{Var}(A)-\operatorname{Var}(B)
=
\mathbb E[(A-B)^2]
\]
from the required first- and second-moment relations.

The stored checker output is `VERIFY_OK`.

The invariant-measure disintegrations, strict-support implication, and equality classification are analytic arguments in `RESULT.md`; they are not inferred from finite simulations.

## Relationship to prior work
Rosenzweig and MacArthur introduced the graphical predator–prey framework in 1963 and analyzed stability in terms of predator and prey isoclines. The publisher record supplies the exact publication date. A complete primary full text was not obtained through the lawful routes inspected, so that source is used for provenance and date rather than blanket noncoverage.

Cheng's classical mathematical paper proves uniqueness of a limit cycle for logistic prey with saturating Michaelis–Menten predation. Its mathematical classification includes MSC \(34C05\). These orbit-existence and uniqueness results do not state the accepted fiberwise stationary laws.

Lundström and Söderbacka give a complete open mathematical treatment of the Rosenzweig–MacArthur system, write both its standard dimensional equations and a transformed two-dimensional form, and derive sharp estimates of the unique cycle's extrema. Targeted full-document searches did not locate conditional-expectation, average, or variance formulations matching the accepted theorem.

Bate and Hilker explicitly use the standard dimensionless system
\[
\dot N=rN(1-N)-\frac{NP}{h+N},
\qquad
\dot P=\frac{NP}{h+N}-mP
\]
in their disease-free background dynamics. They treat period averages by integrating per-capita equations and explicitly note, citing Armstrong and McGehee, that oscillatory Rosenzweig–MacArthur prey have a larger time-averaged density than the corresponding equilibrium. That global inequality is therefore prior and is not claimed as new here. Their complete article contains no conditional-expectation or invariant-measure formulation under the targeted searches performed.

The accepted result strengthens the prior mean-shift statement in two ways. It holds for every compact positive invariant probability measure, not only a single cycle, and it localizes the excess on every predator-density fiber through an exact nonnegative defect. It also supplies exact per-capita speed/variance identities for both coordinates.

## Limitations
The theorem requires compact support in the strictly positive quadrant. It does not apply directly to invariant measures supported on extinction boundaries.

It is stated for the standard dimensionless Rosenzweig–MacArthur system with constant parameters. Stochastic, delayed, spatial, disease-structured, or evolution-extended variants require separate analysis.

The theorem constrains conditional first moments and per-capita speed energies; it does not determine the full invariant density, cycle period, phase distribution, or extrema.

The global inequality \(\mathbb E[N]>N_*\) for a nonconstant oscillation is prior in the ecological literature. The originality claim is restricted to the all-invariant-measures fiberwise harmonic calibration, the exact conditional prey-excess identity, and the exact variance-speed defects.

A general consumer-resource argument may yield analogous identities in other models, so no universality beyond the displayed system is claimed.

## References
1. M. L. Rosenzweig and R. H. MacArthur, “Graphical Representation and Stability Conditions of Predator-Prey Interactions,” The American Naturalist 97, 209–223 (1963), DOI 10.1086/282272.
2. K.-S. Cheng, “Uniqueness of a Limit Cycle for a Predator-Prey System,” SIAM Journal on Mathematical Analysis 12, 541–548 (1981), DOI 10.1137/0512047.
3. R. A. Armstrong and R. McGehee, “Competitive Exclusion,” The American Naturalist 115, 151–170 (1980), DOI 10.1086/283553.
4. A. M. Bate and F. M. Hilker, “Predator-prey oscillations can shift when diseases become endemic,” Journal of Theoretical Biology 316, 1–8 (2013), DOI 10.1016/j.jtbi.2012.09.013.
5. N. L. P. Lundström and G. Söderbacka, “Estimates of Size of Cycle in a Predator-Prey System,” Differential Equations and Dynamical Systems 30, 131–159, first published online 2018, DOI 10.1007/s12591-018-0422-x.
