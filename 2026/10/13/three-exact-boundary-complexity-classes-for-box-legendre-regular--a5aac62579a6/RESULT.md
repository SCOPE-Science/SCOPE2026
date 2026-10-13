# Three exact boundary-complexity classes for box Legendre-regularized policies
## Finding

Consider the box
\[
S=[0,1]^n
\]
with \(F=I\) and smoothing scale \(\tau>0\). The three canonical box constructions in Lin--Chen--Wang give coordinatewise optimizer maps. For one coordinate, write the latent score as \(z\), and let the target endpoint be \(0\). By symmetry the same formulas hold at endpoint \(1\).

If the latent model is restricted by
\[
|z|\le R,
\]
then the smallest achievable distance to the endpoint is exactly
\[
E_{\log}(R)=
\frac{2}{R/\tau+2+\sqrt{(R/\tau)^2+4}},
\]
for the log-barrier map,
\[
E_{\mathrm{ent}}(R)=\frac{1}{1+e^{R/\tau}},
\]
for the binary-entropy map, and
\[
E_{\mathrm{ptb}}(R)=\overline\Phi(R/\tau)
\]
for Gaussian perturbation, where \(\overline\Phi=1-\Phi\).

These are exact finite-\(R\) formulas. Their boundary asymptotics are
\[
E_{\log}(R)\sim\frac{\tau}{R},
\]
\[
E_{\mathrm{ent}}(R)\sim e^{-R/\tau},
\]
and
\[
E_{\mathrm{ptb}}(R)
\sim
\frac{\tau}{R\sqrt{2\pi}}
e^{-R^2/(2\tau^2)}.
\]

Equivalently, for a requested endpoint error
\[
0<\varepsilon<\frac12,
\]
the exact minimum latent magnitudes are
\[
R_{\log}(\varepsilon)
=
\tau
\frac{1-2\varepsilon}{\varepsilon(1-\varepsilon)},
\]
\[
R_{\mathrm{ent}}(\varepsilon)
=
\tau\log\frac{1-\varepsilon}{\varepsilon},
\]
and
\[
R_{\mathrm{ptb}}(\varepsilon)
=
\tau\Phi^{-1}(1-\varepsilon).
\]

At the score that attains error \(\varepsilon\), the coordinatewise Jacobian magnitudes are exactly
\[
J_{\log}(\varepsilon)
=
\frac{\varepsilon^2(1-\varepsilon)^2}
{\tau(1-2\varepsilon+2\varepsilon^2)},
\]
\[
J_{\mathrm{ent}}(\varepsilon)
=
\frac{\varepsilon(1-\varepsilon)}{\tau},
\]
and
\[
J_{\mathrm{ptb}}(\varepsilon)
=
\frac{\varphi(\Phi^{-1}(1-\varepsilon))}{\tau},
\]
where \(\varphi\) is the standard normal density.

Consequently,
\[
R_{\log}(\varepsilon)=\Theta(\varepsilon^{-1}),
\qquad
R_{\mathrm{ent}}(\varepsilon)=\Theta(\log(1/\varepsilon)),
\qquad
R_{\mathrm{ptb}}(\varepsilon)=\Theta(\sqrt{\log(1/\varepsilon)}),
\]
while
\[
J_{\log}(\varepsilon)=\Theta(\varepsilon^2),
\qquad
J_{\mathrm{ent}}(\varepsilon)=\Theta(\varepsilon),
\qquad
J_{\mathrm{ptb}}(\varepsilon)
=
\Theta(\varepsilon\sqrt{\log(1/\varepsilon)}).
\]

Thus the three smooth, onto-interior box policies have three distinct boundary-complexity classes. Under a finite latent-score budget, Gaussian perturbation reaches a boundary target most rapidly and retains the largest local gradient near that target; entropy is intermediate; the log barrier has only polynomial endpoint approximation and the fastest gradient collapse.

## Assumptions and scope

The statement concerns the separable box examples in arXiv:2607.24007v1, with \(F=I\) and a common scale \(\tau>0\). The source displays the unit-scale formulas; the general-\(\tau\) form follows by the regularizer/noise scaling used in its definitions.

For the log-barrier coordinate the regularizer is
\[
-\tau\log w-\tau\log(1-w),
\qquad 0<w<1.
\]
For the entropic coordinate it is
\[
\tau w\log w+\tau(1-w)\log(1-w).
\]
For the perturbation map the scalar noise is
\[
Z\sim N(0,\tau^2).
\]

The claim is coordinatewise. On \([0,1]^n\) the full optimizer is the Cartesian product of the scalar maps, so every coordinate approaching a box face obeys the corresponding law. No analogous rate is claimed here for an arbitrary nonseparable polytope.

## Proof

For the log barrier, the scalar optimizer minimizes
\[
zw-\tau\log w-\tau\log(1-w).
\]
The first-order condition is
\[
z-\frac{\tau}{w}+\frac{\tau}{1-w}=0,
\]
hence
\[
z
=
\tau\frac{1-2w}{w(1-w)}.
\]
The optimizer is strictly decreasing in \(z\), so under \(|z|\le R\) its smallest value is attained at \(z=R\). Solving the quadratic first-order condition gives
\[
w_{\log}(R)
=
\frac{2}{R/\tau+2+\sqrt{(R/\tau)^2+4}},
\]
which proves the exact approximation floor. Setting \(w=\varepsilon\) gives
\[
R_{\log}(\varepsilon)
=
\tau\frac{1-2\varepsilon}{\varepsilon(1-\varepsilon)}.
\]
Differentiating the inverse relation yields
\[
\left|\frac{dw}{dz}\right|
=
\frac{w^2(1-w)^2}
{\tau(1-2w+2w^2)},
\]
and substitution of \(w=\varepsilon\) gives \(J_{\log}\).

For entropy, the first-order condition is
\[
z+\tau\log\frac{w}{1-w}=0.
\]
Therefore
\[
w_{\mathrm{ent}}(z)
=
\frac{1}{1+e^{z/\tau}}.
\]
Monotonicity again makes \(z=R\) optimal for approximating endpoint \(0\), giving the stated \(E_{\mathrm{ent}}\). Inversion and differentiation give
\[
R_{\mathrm{ent}}(\varepsilon)
=
\tau\log\frac{1-\varepsilon}{\varepsilon}
\]
and
\[
\left|\frac{dw}{dz}\right|
=
\frac{w(1-w)}{\tau}.
\]

For Gaussian perturbation, the linear oracle on \([0,1]\) chooses \(1\) exactly when
\[
z+Z<0.
\]
Taking expectations gives
\[
w_{\mathrm{ptb}}(z)
=
\Phi(-z/\tau).
\]
Thus
\[
E_{\mathrm{ptb}}(R)
=
\overline\Phi(R/\tau),
\]
\[
R_{\mathrm{ptb}}(\varepsilon)
=
\tau\Phi^{-1}(1-\varepsilon),
\]
and
\[
\left|\frac{dw}{dz}\right|
=
\frac{\varphi(z/\tau)}{\tau}.
\]

The three large-\(R\) formulas follow from elementary expansion for the log and entropy maps and the Gaussian Mills ratio
\[
\overline\Phi(x)\sim\frac{\varphi(x)}{x}.
\]
The inverse Gaussian quantile satisfies
\[
\Phi^{-1}(1-\varepsilon)
\sim
\sqrt{2\log(1/\varepsilon)}.
\]
Combining this with the Mills ratio yields
\[
\varphi(\Phi^{-1}(1-\varepsilon))
\sim
\varepsilon\sqrt{2\log(1/\varepsilon)}.
\]

## Verification

The standalone script `artifacts/verify_boundary_classes.py` evaluates the three exact maps, their inverse score formulas, and their Jacobian formulas at several scales. It also checks the large-score ordering
\[
E_{\mathrm{ptb}}(R)<E_{\mathrm{ent}}(R)<E_{\log}(R)
\]
for representative sufficiently large \(R/\tau\), and checks the corresponding near-boundary gradient ordering.

The script is supporting evidence only. The exact formulas and asymptotic classifications are proved symbolically above.

## Relationship to prior work

Lin--Chen--Wang introduce the three constructions in a common Legendre-regularized-policy framework. Their box example displays the unit-scale log-barrier, entropy, and Gaussian-perturbation maps. Their main theorem proves smoothness, an explicit Jacobian, Lipschitz continuity, and surjectivity onto the relative interior; their universal-approximation theorem shows that continuous feasible policies can be approximated without imposing a bound on the latent score.

The present result asks the complementary quantitative question created by that universality statement: how much latent score is required when a target policy approaches a hard boundary, and how much local gradient remains there? The exact answer differs by orders of magnitude across the three canonical examples.

Berthet et al. develop differentiable perturbed optimizers and prove smoothness and derivative formulas for stochastic perturbation. Their general framework covers the Gaussian smoothing premise but does not compare its box-boundary score budget with entropy and log-barrier regularization.

Sturmfels et al. compare log-barrier and entropic regularization on polytopes through their central and entropic paths and algebraic geometry. The inspected material does not provide the bounded-score endpoint floors, the Gaussian comparison, or the Jacobian hierarchy stated here.

## Limitations

The result is a sharp box-coordinate classification, not a theorem for every polytope. Coupled constraints can make boundary approach depend on face geometry and on the chosen latent matrix.

The comparison concerns representational score magnitude and local Jacobian size. It does not by itself prove an end-to-end training-time ordering, because the latent network, loss geometry, optimization algorithm, and data distribution also matter.

The formulas are consequences of the canonical maps once those maps are written explicitly. Their contribution is the complete finite-budget comparison and its connection to the boundary case of the source universal-approximation theorem, rather than a new general theory of Legendre maps.

## References

1. Z. Lin, R. Chen, Y. Wang, *Smooth Learning with Hard Constraints via Legendre-Regularized Policies*, arXiv:2607.24007v1, first public 27 July 2026.
2. Q. Berthet, M. Blondel, O. Teboul, M. Cuturi, J.-P. Vert, F. Bach, *Learning with Differentiable Perturbed Optimizers*, arXiv:2002.08676, 2020.
3. B. Sturmfels, S. Telen, F. Vialard, *Toric geometry of entropic regularization*, Journal of Symbolic Computation 120 (2024), 102221. DOI: 10.1016/j.jsc.2023.102221.
