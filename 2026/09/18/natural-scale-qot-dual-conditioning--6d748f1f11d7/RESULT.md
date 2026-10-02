# Natural-scale strong concavity for quadratically regularized optimal transport

## Statement

Consider quadratically regularized optimal transport with quadratic cost
\[
c(x,y)=\tfrac12|x-y|^2
\]
under the smooth uniformly convex positive-density hypotheses of González-Sanz and Nutz, *Geometry and Convergence of Quadratically Regularized Optimal Transport I*. Let \((f_\varepsilon,g_\varepsilon)\) be an optimal dual pair,
\[
q_\varepsilon(x,y)=f_\varepsilon(x)+g_\varepsilon(y)-c(x,y),
\qquad
\ell=\varepsilon^{1/(d+2)}.
\]
Write \(\mathcal H=\{u\oplus v\}\) for the direct-sum subspace of \(L^2(\mu\otimes\nu)\), modulo the usual gauge through the direct-sum representation.

There are constants \(\theta,m,M,\rho,\varepsilon_0>0\), depending only on the fixed marginal data and dimension, such that for every \(0<\varepsilon<\varepsilon_0\):

1. The positive-slack core
\[
E_\varepsilon=\{(x,y):q_\varepsilon(x,y)\ge\theta\ell^2\}
\]
satisfies
\[
\int_{E_\varepsilon}(u(x)+v(y))^2\,d\mu(x)d\nu(y)
\ge m\varepsilon\|u\oplus v\|_2^2
\]
for every \(u\oplus v\in\mathcal H\).

2. On
\[
\mathcal B_\varepsilon
=
\{h\in\mathcal H\cap L^\infty:
\|h-h_\varepsilon\|_\infty\le\rho\ell^2\},
\]
the dual functional is \(m\)-strongly concave in the \(L^2(\mu\otimes\nu)\) norm.

3. The local gradient Lipschitz constant satisfies
\[
L_\varepsilon\le M\ell^{-2}
=
M\varepsilon^{-2/(d+2)}.
\]

4. Consequently, for every \(h\in\mathcal B_\varepsilon\),
\[
\|D\Phi_\varepsilon(h)\|_2^2
\ge
2m\bigl(\Phi_\varepsilon(h_\varepsilon)-\Phi_\varepsilon(h)\bigr)
\]
and
\[
\Phi_\varepsilon(h_\varepsilon)-\Phi_\varepsilon(h)
\ge
\frac m2\|h-h_\varepsilon\|_2^2.
\]

Thus the sharp support geometry yields an \(\varepsilon\)-uniform local curvature modulus on the natural potential scale
\[
\Theta(\ell^2)=\Theta\!\left(\varepsilon^{2/(d+2)}\right).
\]

This corrected statement does not claim a new optimizer Hessian condition-number asymptotic. The optimizer spectral scales are already established in an earlier public result and are treated here only as prior context.

## Proof

The geometry theorem gives inner positive-slack balls of radius comparable to \(\ell\), row and column section masses comparable to \(\ell^d\), and uniform overlap for rows whose base points are within a fixed multiple of \(\ell\). After decreasing \(\theta\), these properties hold on the fixed positive-slack core \(E_\varepsilon\).

For
\[
I(u,v)
=
\int_{E_\varepsilon}(u(x)+v(y))^2\,d\mu(x)d\nu(y),
\]
minimizing over one endpoint value at a time gives a variance form. The row-overlap estimate therefore implies
\[
I(u,v)
\ge
c\iint_{|x-x'|\le a\ell}(u(x)-u(x'))^2\,d\mu(x)d\mu(x').
\]
A finite-range Poincaré estimate on the bounded uniformly convex support gives
\[
I(u,v)\ge c\ell^{d+2}\operatorname{Var}_\mu(u).
\]
The symmetric column argument gives the same estimate for \(\operatorname{Var}_\nu(v)\).

The normalized core measure has both marginals with densities bounded above and below by constants relative to the original marginals. Cauchy--Schwarz on the core therefore controls
\[
\left(\int u\,d\mu+\int v\,d\nu\right)^2
\]
by \(C\ell^{-(d+2)}I(u,v)\). Combining the variance and mean estimates yields
\[
I(u,v)\ge c\ell^{d+2}\|u\oplus v\|_2^2
=
c\varepsilon\|u\oplus v\|_2^2.
\]

Choose \(\rho<\theta/2\). Every \(h\in\mathcal B_\varepsilon\) leaves the whole core active. Along a line segment \(h_t\) in the ball, the one-dimensional second derivative exists almost everywhere and equals the active-set quadratic form divided by \(\varepsilon\). The fixed-core coercivity makes it at least \(m\|h_1-h_0\|_2^2\). Integrating in \(t\) gives strong concavity.

For the upper curvature bound, the transformed optimal potentials have uniform Hessian control and slack height \(O(\ell^2)\). Hence every active row and column throughout \(\mathcal B_\varepsilon\) has measure \(O(\ell^d)\). The active-set quadratic form is then at most \(C\ell^d\|u\oplus v\|_2^2\); division by \(\varepsilon=\ell^{d+2}\) gives \(L_\varepsilon=O(\ell^{-2})\).

The PL inequality and quadratic growth are the standard consequences of strong concavity on this convex neighborhood.

## Relation to prior work

The geometry paper supplies the sharp support thickness, slack height, inner core, overlap, and localization estimates used above. The earlier PL paper proves a local PL inequality in a broader setting with different quantitative constants. The earlier gradient-convergence paper studies the optimizer linearization and local convergence.

A separate earlier public result already establishes the sharp small-\(\varepsilon\) spectral conditioning of the optimizer linearization. For that reason, the present corrected result claims only the robust positive-core coercivity and natural-scale nonlinear strong-concavity neighborhood, together with their PL and smoothness consequences.

## Limitations

The theorem is local, assumes smooth positive marginal densities and uniformly convex supports, and does not prove that a nonlinear algorithm initialized outside \(\mathcal B_\varepsilon\) enters or remains in it. Semi-discrete transport, rough marginals, general costs, discretization, and finite-precision effects are outside scope. A contemporaneous working paper titled *Geometry and Convergence of Quadratically Regularized Optimal Transport II* was cited by the primary geometry source but no public full text was located, so some overlap risk remains.

## References

1. A. González-Sanz and M. Nutz, *Geometry and Convergence of Quadratically Regularized Optimal Transport I*, arXiv:2609.20400.
2. A. González-Sanz, M. Nutz, and A. Riveros Valdevenito, *Polyak--Łojasiewicz Inequality for Quadratically Regularized Optimal Transport*, arXiv:2605.27175.
3. A. González-Sanz, M. Nutz, and A. Riveros Valdevenito, *Linear Convergence of Gradient Descent for Quadratically Regularized Optimal Transport*, arXiv:2509.08547.
