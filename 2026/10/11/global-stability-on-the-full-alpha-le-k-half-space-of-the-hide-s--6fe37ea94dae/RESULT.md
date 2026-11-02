# Closed-boundary global stability and a cross-term-free certificate for the Hide–Skeldon–Acheson dynamo

## Theorem (including the equality boundary)

Consider the real system
\[
\dot x=x(y-1)-\beta z,\qquad
\dot y=\alpha(1-x^2)-ky,\qquad
\dot z=x-bz,
\]
with \(\alpha,\beta,b,k>0\). For every \(0<\alpha\le k\), the equilibrium
\[
E=(0,\alpha/k,0)
\]
is unique and **globally asymptotically stable**. A single globally proper positive-definite energy is
\[
V=\alpha x^2+(y-\alpha/k)^2+\alpha\beta z^2,
\]
with exact orbital derivative
\[
\boxed{\dot V=-\frac{2\alpha(k-\alpha)}{k}x^2
 -2k(y-\alpha/k)^2-2\alpha\beta b z^2.}
\]
At the equality boundary \(\alpha=k\), the derivative is only negative semidefinite, but LaSalle's largest-invariant-subset condition is strict enough to establish global attraction. The formula also gives a uniformly valid proof of the already published strict-interior stability statement \(\alpha<k\).

## Proof

Differentiation gives
\[
\begin{aligned}
\dot V={}&2\alpha x[x(y-1)-\beta z]
+2(y-\alpha/k)[\alpha(1-x^2)-ky]
+2\alpha\beta z(x-bz).
\end{aligned}
\]
The \(xz\) terms cancel because the last weight is \(\alpha\beta\). The cubic terms \(2\alpha x^2y\) cancel as well, yielding the boxed formula identically. Since \(\alpha,\beta>0\), \(V\) is strictly positive away from \(E\) and coercive on \(\mathbb R^3\). Every positive-time orbit remains in a compact sublevel of \(V\), and the polynomial ODE therefore has a forward solution for all time.

When \(0<\alpha<k\), all three coefficients in \(-\dot V\) are positive, so Lyapunov's direct method proves global asymptotic stability. When \(\alpha=k\), \(\dot V=0\) exactly on \(S=\{y=1,z=0\}\). If a forward trajectory remains in \(S\), \(z\equiv0\) implies \(0=\dot z=x\), and then \(x\equiv0\); thus its sole invariant trajectory is the equilibrium \((0,1,0)\). Compact forward invariance and LaSalle's principle imply convergence to that equilibrium from every initial condition.

Uniqueness of the equilibrium for \(\alpha\le k\) also follows directly: an equilibrium with \(x\ne0\) would require, after eliminating \(z=x/b\) and \(y=\alpha(1-x^2)/k\),
\[
\alpha(1-x^2)/k=1+\beta/b,
\]
which contradicts \(\alpha/k\le1\). This completes the proof.

## The precise relation to the literature

X. Li, *New insights to the Hide–Skeldon–Acheson dynamo*, Discrete and Continuous Dynamical Systems–B **27** (2022), 6257–6267, DOI:10.3934/dcdsb.2021315, **Theorem 2.2**, already **states** global uniform asymptotic stability for the entire strict region \(k>\alpha\) without any extra hypothesis on \(b\) or \(\beta\). That strict-interior statement is therefore **prior coverage**, not a new stronger parameter theorem.

There is a technical issue in its printed proof. The energy with a unit \(z^2\) weight used there gives
\[
\dot W=-\frac{\alpha(k-\alpha)}k x^2
-k(y-\alpha/k)^2-bz^2+(1-\alpha\beta)xz,
\quad
W=\tfrac12[\alpha x^2+(y-\alpha/k)^2+z^2].
\]
The stated conclusion \(\dot W\le0\) from this expression requires an additional quadratic-form condition which does **not** hold for every positive parameter in the published theorem. For example, at \((\alpha,k,b,\beta)=(1,2,1,3)\) and \((x,y,z)=(-2,1/2,1)\), direct substitution yields \(\dot W=1>0\). This is a counterexample to that *particular Lyapunov decrease assertion*, **not** a counterexample to Li's stability theorem. The cross-term-free identity above supplies a valid proof for the published interior region with no such restriction.

The distinct extension of the global-attraction statement is the previously excluded **boundary \(\alpha=k\)**. Li's strict hypothesis does not imply this equality case by continuity alone; the proof uses the invariant-set property \(\dot z=x-bz\). The earlier statement must not be described as having a \(b,\beta\) restriction: such a restriction appears only as a missing condition in its displayed proof.

Other same-system literature includes Hide–Skeldon–Acheson (1996, DOI:10.1098/rspa.1996.0070), Moroz (2007, DOI:10.1098/rspa.2006.1758), Mahdi–Valls (2014, DOI:10.1016/j.bulsci.2013.04.001), and Diz-Pita et al. (2025, DOI:10.14232/ejqtde.2025.1.76). Their inspected local-stability, bifurcation, and integrability conclusions do not establish the equality-boundary statement for all positive parameters.

## Scope and limitations

The theorem is a sufficient closed-half-space result and does **not** say that \(\alpha\le k\) is necessary for global stability. No conclusions about attractors for \(\alpha>k\), quantitative convergence rates, or the full bifurcation diagram are asserted. The strict-interior conclusion is explicitly attributed to Li (2022); the boundary closure and corrected uniform Lyapunov certificate are the specific contributions. A literature comparison cannot rule out all earlier equivalent energy estimates, so historical priority for these particular improvements remains a qualified best-of-knowledge assessment.
