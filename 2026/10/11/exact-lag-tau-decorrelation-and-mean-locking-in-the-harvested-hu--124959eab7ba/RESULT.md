# Exact lag-\(\tau\) decorrelation and mean locking in the harvested Hutchinson–Wright equation
## Finding
Consider the harvested Hutchinson–Wright delay equation
\[
\dot x(t)
=
r x(t)
\left(
1-\frac{x(t-\tau)}{K}
\right)
-\delta x(t),
\]
where
\[
r>0,
\qquad
K>0,
\qquad
\tau>0,
\qquad
\delta\ge0.
\]
Let
\[
\mathcal C_+
=
C([-\tau,0],(0,\infty))
\]
be the strictly positive history space, and let \(\mu\) be a compactly supported invariant Borel probability measure for the solution semiflow on \(\mathcal C_+\).

For a history \(\varphi\), write
\[
X_0(\varphi)=\varphi(0),
\qquad
X_{-\tau}(\varphi)=\varphi(-\tau),
\]
and define
\[
K_\delta
=
K\left(1-\frac{\delta}{r}\right).
\]
Then the delayed population has the exact stationary regression
\[
\boxed{
\mathbb E_\mu[X_{-\tau}\mid X_0]
=
K_\delta
}.
\]

Because \(X_{-\tau}>0\) almost surely, the existence of such a stationary state forces
\[
\boxed{
\delta<r
}.
\]
In that regime, invariance under a time shift of length \(\tau\) gives equality of the one-time marginals of \(X_{-\tau}\) and \(X_0\). Consequently
\[
\boxed{
\mathbb E_\mu[X_0]
=
K_\delta
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(X_0,X_{-\tau})
=
0
}.
\]

The per-capita growth rate is
\[
\frac{\dot x(0)}{X_0}
=
\frac rK
\left(
K_\delta-X_{-\tau}
\right).
\]
Therefore the stationary population variance is exactly the mean-square logarithmic-growth activity:
\[
\boxed{
\operatorname{Var}_\mu(X_0)
=
\frac{K^2}{r^2}
\mathbb E_\mu
\left[
\left(
\frac{\dot x(0)}{X_0}
\right)^2
\right]
}.
\]

The right-hand side vanishes exactly for the invariant atom supported on the constant positive equilibrium history
\[
x(t)\equiv K_\delta.
\]
Thus every other compact positive stationary state has positive variance. Its lag-\(\tau\) Pearson correlation is therefore defined and satisfies
\[
\boxed{
\operatorname{Corr}_\mu(X_0,X_{-\tau})
=
0
}.
\]

Every non-equilibrium compact stationary state also places positive mass on both sides of the positive equilibrium level:
\[
\boxed{
\mu\{X_0<K_\delta\}>0,
\qquad
\mu\{X_0>K_\delta\}>0
}.
\]
Hence every nonconstant positive periodic orbit crosses
\[
x=K_\delta
\]
at least twice per least period.

The mean-locking law has a direct harvesting consequence. Whenever compact positive stationary states exist at two harvesting rates \(\delta_1<\delta_2<r\), their means differ by
\[
\mathbb E_{\mu_{\delta_1}}[X_0]
-
\mathbb E_{\mu_{\delta_2}}[X_0]
=
\frac{K}{r}
(\delta_2-\delta_1)
>0.
\]
Thus proportional harvesting cannot create a stationary-mean hydra effect in the harvested Hutchinson–Wright model, even when delay destabilizes the equilibrium and produces sustained oscillation.

## Assumptions and scope
Compact support is taken in the strictly positive history space \(\mathcal C_+\). A compact subset of \(\mathcal C_+\) is uniformly bounded away from zero, which makes the logarithmic current-coordinate generator tests used below regular.

No ergodicity assumption is required. The result applies to positive equilibrium measures, normalized measures on positive periodic solutions, and arbitrary compact invariant mixtures.

Hutchinson's 1948 article introduced the delayed logistic population mechanism. Later work developed its local and global stability, periodic solutions, Hopf bifurcation, and the Wright-equation formulation. The harvested version is treated explicitly in the 2014 survey of delayed logistic population models, including the positive equilibrium
\[
K_\delta
=
K\left(1-\frac{\delta}{r}\right)
\]
and its delay-dependent stability changes.

Those equilibrium and bifurcation facts are prior work. The finding here is the all-invariant-measures conditional regression, the exact zero lag-\(\tau\) covariance, the logarithmic-growth activity identity, and their equality and crossing consequences.

The foundational publication has a verified day-resolved date of 13 October 1948. The inspected same-model mathematical treatment lists \(34K18\) first among its Mathematics Subject Classification codes; that primary classification is used here.

## Proof
Rewrite the equation as
\[
\dot x(t)
=
\frac rK x(t)
\left(
K_\delta-x(t-\tau)
\right).
\]

Because the support of \(\mu\) is compact in \(\mathcal C_+\), the current coordinate \(X_0\) is bounded above and bounded away from zero on the support.

Let \(\phi\) be any continuous function on the compact current-coordinate range. Choose a continuously differentiable function \(H\) on a neighborhood of that range satisfying
\[
H'(u)
=
\frac{K}{r u}\phi(u).
\]
For the history-space generator \(L\),
\[
L(H\circ X_0)
=
\phi(X_0)
\left(
K_\delta-X_{-\tau}
\right).
\]
Invariance gives
\[
\mathbb E_\mu
\left[
\phi(X_0)
\left(
K_\delta-X_{-\tau}
\right)
\right]
=
0
\]
for every continuous \(\phi\). Hence
\[
\mathbb E_\mu[X_{-\tau}\mid X_0]
=
K_\delta.
\]

Since \(X_{-\tau}>0\) almost surely, its conditional expectation is positive almost surely. Therefore
\[
K_\delta>0,
\]
which is equivalent to
\[
\delta<r.
\]

Let \(S_t\) denote the history semiflow. Invariance gives
\[
(S_\tau)_\#\mu=\mu.
\]
For every history whose trajectory is defined through time \(\tau\),
\[
X_{-\tau}(S_\tau\varphi)=X_0(\varphi).
\]
Thus \(X_{-\tau}\) and \(X_0\) have the same marginal distribution under \(\mu\).

Taking expectations in the conditional law gives
\[
\mathbb E[X_{-\tau}]=K_\delta,
\]
and equal marginals yield
\[
\mathbb E[X_0]=K_\delta.
\]
Multiplying the conditional law by \(X_0\) gives
\[
\mathbb E[X_0X_{-\tau}]
=
K_\delta\mathbb E[X_0]
=
K_\delta^2.
\]
Therefore
\[
\operatorname{Cov}(X_0,X_{-\tau})=0.
\]

Pointwise,
\[
\frac{\dot x(0)}{X_0}
=
\frac rK
(K_\delta-X_{-\tau}).
\]
Squaring and averaging gives
\[
\mathbb E
\left[
\left(
\frac{\dot x(0)}{X_0}
\right)^2
\right]
=
\frac{r^2}{K^2}
\operatorname{Var}(X_{-\tau}).
\]
Equal marginals give
\[
\operatorname{Var}(X_{-\tau})
=
\operatorname{Var}(X_0),
\]
which proves the activity identity.

Suppose
\[
\operatorname{Var}(X_0)=0.
\]
Then \(X_0=K_\delta\) almost surely. By invariance, for every rational \(t\ge0\), the current evaluation along the shifted history is again \(K_\delta\) almost surely. Taking the countable intersection over rational times and using continuity of trajectories shows that
\[
x(t)=K_\delta
\]
for all \(t\ge0\) on a full-measure set of histories.

For \(0\le t\le\tau\), the derivative is then zero, so the differential equation gives
\[
x(t-\tau)=K_\delta.
\]
Thus the entire initial history is constant. Hence \(\mu\) is the positive equilibrium atom. The converse is immediate.

Every non-equilibrium stationary state therefore has positive variance. Since its mean is exactly \(K_\delta\), it cannot be supported entirely in either closed half-line
\[
X_0\ge K_\delta
\quad\text{or}\quad
X_0\le K_\delta
\]
without being constant. Hence it gives positive mass to both strict sides.

For a nonconstant positive periodic orbit, normalized time measure over one least period is a compact invariant probability measure. Positive time spent on both sides of the equilibrium level and continuity force at least two crossings per least period.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the algebraic rewriting
\[
r\left(1-\frac{q}{K}\right)-\delta
=
\frac rK(K_\delta-q),
\]
the covariance consequence
\[
\mathbb E[X_0X_{-\tau}]=K_\delta^2,
\]
and the exact conversion from lag variance to logarithmic-growth activity.

For the exact test parameters
\[
r=2,
\qquad
K=3,
\qquad
\delta=\frac12,
\]
it checks
\[
K_\delta=\frac94.
\]

The conditional-expectation quantifier, equality classification, and periodic crossing conclusion are analytic arguments in this document and are not inferred from finite simulations.

The stored checker output is `VERIFY_OK`.

## Relationship to prior work
Hutchinson introduced the delayed logistic feedback mechanism in 1948. The original article is used here for model provenance and the verified publication date; a complete machine-readable copy was not available through the bounded access routes used for this review.

Classical work on the Hutchinson–Wright equation established stability changes and Hopf bifurcation of periodic solutions. Those results concern existence and stability of orbits rather than invariant-measure conditional moments.

The 2014 article *Delayed logistic population models revisited* is the decisive self-review. It writes the Hutchinson–Wright equation, treats proportional harvesting explicitly, identifies the positive equilibrium and its stability regimes, and presents numerical bifurcation diagrams. In its discussion of the harvested equation, the plotted time average is described as matching the positive equilibrium when stable and remaining very close to it when unstable. The complete inspected article does not state the exact conditional regression, the zero lag-\(\tau\) covariance, or the logarithmic-growth variance identity.

A complete modern open treatment of the Hutchinson equation reviews the equivalent Wright equation, the Hopf threshold, stable periodic solutions, and global dynamics. Its stated results concern orbit structure and stability, not the stationary conditional law above.

The present theorem turns the delayed feedback itself into an exact statistical calibration. It proves that the delayed population is conditionally centered at the positive equilibrium at every current population level, forcing exact decorrelation at the biological feedback lag and exact mean locking even in oscillatory stationary regimes.

## Limitations
The theorem concerns compactly supported invariant probability measures on strictly positive histories. It does not classify unbounded trajectories or measures that charge the extinction boundary.

The existence of a positive stationary state is not asserted for every parameter set with \(\delta<r\); the theorem gives constraints on any such state that exists.

The mean-locking corollary sharpens a numerical same-model observation, but the strongest originality claim is the conditional regression, lag-\(\tau\) decorrelation, and activity identity. Because these follow from a short logarithmic generator calculation, an equivalent formulation could remain in older unindexed delay-equation literature.

The result does not determine the oscillation period, full invariant distribution, or the number and stability of periodic solutions.

## References
1. G. E. Hutchinson, “Circular causal systems in ecology,” *Annals of the New York Academy of Sciences* 50, 221–246 (1948), DOI 10.1111/j.1749-6632.1948.tb39854.x.
2. N. D. Kazarinoff, Y.-H. Wan, and P. van den Driessche, “Hopf Bifurcation and Stability of Periodic Solutions of Differential-difference and Integro-differential Equations,” *IMA Journal of Applied Mathematics* 21, 461–477 (1978), DOI 10.1093/imamat/21.4.461.
3. E. Liz, “Delayed logistic population models revisited,” *Publicacions Matemàtiques*, Extra Volume, 309–331 (2014), DOI 10.5565/PUBLMAT_Extra14_17.
4. C. T. H. Baker and G. Röst, “Global dynamics of the delayed logistic equation,” *Journal of Dynamics and Differential Equations* (2019), DOI 10.1007/s00332-019-09577-w.
