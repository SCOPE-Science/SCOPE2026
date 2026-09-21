# Exact stationary moment parabola and critical rigidity in the Rössler system

Consider the classical Rössler system
\[
\dot x=-y-z,\qquad \dot y=x+ay,\qquad \dot z=b+z(x-c),
\tag{1}
\]
with \(a,b,c>0\). Let \(\mu\) be any compactly supported invariant probability measure for the flow and write
\[
m:=\int z\,d\mu,\qquad \Delta:=c^2-4ab.
\]
When \(\Delta\ge0\), set
\[
z_\pm:=\frac{c\pm\sqrt\Delta}{2a}.
\]

## Theorem

Every such invariant measure satisfies the exact first- and second-moment balances
\[
\langle y\rangle=-m,\qquad \langle x\rangle=am,
\tag{2}
\]
\[
\langle xz\rangle=cm-b=a\langle y^2\rangle,
\qquad
\langle xy\rangle=b-cm.
\tag{3}
\]
Consequently,
\[
\boxed{\operatorname{Var}_\mu(y)=\frac{cm-b-am^2}{a}}.
\tag{4}
\]
Equivalently, whenever an invariant probability measure exists,
\[
\boxed{\operatorname{Var}_\mu(y)=(m-z_-)(z_+-m)}.
\tag{5}
\]
The associated covariances obey
\[
\boxed{\operatorname{Cov}_\mu(x,z)=a\operatorname{Var}_\mu(y),\qquad
\operatorname{Cov}_\mu(x,y)=-a\operatorname{Var}_\mu(y)}.
\tag{6}
\]

There is also a heightwise stationary-flux identity. If \(\nu=z_\#\mu\) is the \(z\)-marginal, then
\[
\nu(\{0\})=0,
\qquad
\boxed{\mathbb E_\mu[x\mid z]=c-\frac b z\quad \nu\text{-a.e.}}
\tag{7}
\]
Thus the conditional mean of \(x\) is fixed exactly at every recurrent height seen by a compact stationary state.

The moment parabola has the following sharp consequences.

1. **No-equilibrium regime.** If \(\Delta<0\), there is no compactly supported invariant probability measure. Hence the flow has no nonempty compact invariant set and no bounded forward-global trajectory.

2. **Critical saddle-node.** If \(\Delta=0\), the unique compactly supported invariant probability measure is
\[
\delta_{E_*},\qquad
E_*=(az_*,-z_*,z_*),\quad z_*={c\over2a}=\sqrt{b/a}.
\tag{8}
\]
Every nonempty compact invariant set must therefore contain \(E_*\). Moreover, if a forward-global trajectory is bounded, then its empirical measures converge weakly to \(\delta_{E_*}\); equivalently, every continuous observable has time average equal to its value at \(E_*\). This is a statistical statement and does not assert pointwise convergence of every bounded trajectory.

3. **Two-equilibrium regime.** If \(\Delta>0\), every compact stationary state satisfies
\[
\boxed{z_-\le m\le z_+},
\tag{9}
\]
and
\[
\boxed{0\le \operatorname{Var}_\mu(y)\le {\Delta\over4a^2}},
\qquad
\boxed{0\le \operatorname{Cov}_\mu(x,z)\le {\Delta\over4a}}.
\tag{10}
\]
Equality \(m=z_\pm\) holds if and only if \(\mu=\delta_{E_\pm}\), where
\[
E_\pm=(az_\pm,-z_\pm,z_\pm).
\tag{11}
\]
The variance and covariance upper bounds are sharp: they are attained by the equal mixture \((\delta_{E_-}+\delta_{E_+})/2\). More generally, every point of the parabola (5) is realized by a convex mixture of the two equilibrium measures. Hence (5) gives the exact projection of the full compact stationary-measure simplex onto the pair \((\langle z\rangle,\operatorname{Var}(y))\).

## Proof

For every \(C^1\) observable on a neighborhood of the compact support, invariance gives \(\int L\phi\,d\mu=0\), with \(L\) the Lie derivative along (1). Taking \(\phi=x\) and \(\phi=y\) gives
\[
0=-\langle y\rangle-\langle z\rangle,
\qquad
0=\langle x\rangle+a\langle y\rangle,
\]
which proves (2).

Next,
\[
Lz=b+xz-cz,
\]
so
\[
\langle xz\rangle=cm-b.
\tag{12}
\]
For \(H=(x^2+y^2)/2\),
\[
LH=x(-y-z)+y(x+ay)=ay^2-xz.
\]
Thus \(\langle xz\rangle=a\langle y^2\rangle\). Finally, from
\[
L(x^2/2)=-xy-xz
\]
we obtain \(\langle xy\rangle=-\langle xz\rangle=b-cm\). Equations (3) follow.

Since \(\langle y\rangle=-m\),
\[
\operatorname{Var}(y)
=\langle y^2\rangle-m^2
={cm-b-am^2\over a},
\]
proving (4). Factoring the numerator gives (5). Using (2)--(3),
\[
\operatorname{Cov}(x,z)
=cm-b-am^2=a\operatorname{Var}(y),
\]
and
\[
\operatorname{Cov}(x,y)
=b-cm+am^2=-a\operatorname{Var}(y),
\]
which proves (6).

For (7), let \(\nu=z_\#\mu\) and let \(q(z)\) be a version of \(\mathbb E[x\mid z]\). For every smooth compactly supported \(\psi\), invariance applied to \(\psi(z)\) gives
\[
0=\int \psi'(z)\,[b+z(x-c)]\,d\mu
 =\int \psi'(z)\,[b+z(q(z)-c)]\,d\nu(z).
\tag{13}
\]
Thus the compactly supported signed measure
\[
d\eta=[b+z(q(z)-c)]\,d\nu
\]
has zero distributional derivative. A distribution on \(\mathbb R\) with zero derivative is constant; compact support forces that constant to be zero. Therefore
\[
[b+z(q(z)-c)]\,\nu(dz)=0.
\]
At \(z=0\) the multiplier equals \(b>0\), so \(\nu(\{0\})=0\), and (7) follows.

Because a variance is nonnegative, (4) requires
\[
am^2-cm+b\le0.
\tag{14}
\]
If \(\Delta<0\), this quadratic is strictly positive for all real \(m\), contradiction. Any nonempty compact invariant set supports an invariant probability measure by time averaging, proving the compact-set obstruction. A bounded forward-global orbit has a nonempty compact omega-limit set, so it is also impossible.

If \(\Delta\ge0\), (5) implies (9). At an endpoint, \(\operatorname{Var}(y)=0\), so \(y=-m\) on the support of \(\mu\). The support of an invariant measure is invariant. Therefore \(\dot y=0\) there, forcing \(x=am\); then \(\dot x=0\) forces \(z=m\). Hence the support is the singleton \(E_\pm\). Conversely each equilibrium delta measure attains its endpoint. When \(\Delta=0\) the two endpoints coincide, so \(\delta_{E_*}\) is the unique compactly supported invariant probability measure. Standard time-averaging then gives the stated empirical-measure rigidity for bounded forward-global trajectories.

Finally, the concave parabola in (5) has maximum \((z_+-z_-)^2/4=\Delta/(4a^2)\), yielding (10) together with (6). A convex mixture \(p\delta_{E_-}+(1-p)\delta_{E_+}\) has mean \(m=pz_-+(1-p)z_+\) and variance exactly \((m-z_-)(z_+-m)\), proving sharpness and realization of the full moment parabola.

## Relation to prior literature

Rössler introduced (1) as a minimal continuous-time chaotic system in 1976. Starkov and Starkov (2007) developed rigorous localization criteria for compact invariant sets and proved that \(c^2-4ab<0\), equivalently absence of equilibria, rules out periodic orbits. Their Theorem 2 uses logarithmic localizing functions to exclude compact invariant sets wholly contained in either open half-space \(z>0\) or \(z<0\), and their Corollary 3 states the no-periodic-orbit consequence. Those results are prior art and are not claimed here.

Kontorovich et al. (2009) explicitly studied statistical moments of the Rössler attractor using degenerated cumulant equations. Their equation (15) gives an approximate variance relation used to predict \(\operatorname{Var}(y)\) with a reported 5.8% discrepancy in the standard parameter example, and the paper later emphasizes that exact variance evaluation was not obtained by their approximation. The exact invariant-measure balance (4) contains the additional \(-b/a\) term and is valid for every compact stationary measure, including equilibrium measures and mixtures, rather than only an approximately modeled physical chaotic measure.

Sprott and Li (2017) reported that a broad computer search found no chaotic or periodic solutions when \(c^2-4ab<0\), and described the absence of hidden attractors there as probable. The present stationary-measure obstruction gives a rigorous exclusion of all compact invariant dynamics in that regime, although this consequence is conceptually close to the earlier localization results of Starkov and Starkov.

Bramburger and Fantuzzi (2024) treated the Rössler attractor as a modern invariant-measure test case: they reconstructed an approximate physical measure from data and reported agreement of degree-two moments with long-time averages to within 13%. Their general framework uses invariant-measure moment constraints, but the Rössler example is computational and does not state the closed analytic parabola (5) or the critical uniqueness result above.

To the best of our knowledge, we did not find a prior statement of the exact compact-invariant-measure parabola (4)--(5), the covariance identities (6), the heightwise conditional law (7), or the critical uniqueness/statistical-rigidity conclusion. The closest priority risk is the older localization literature around the Rössler system; the 2007 paper was inspected in full and does not state these stationary-measure formulas. Some later model-specific literature, including Malasoma and Malasoma (2020), was checked at abstract level but not exhaustively theorem by theorem, so priority uncertainty is not zero.

## Limitations

The invariant-measure theorem assumes \(a,b,c>0\) and compact support. It does not classify noncompact invariant objects or finite-time blow-up. The critical result gives uniqueness of the compact stationary probability measure and convergence of empirical measures for bounded forward-global trajectories; it does not rule out a nontrivial compact invariant set carrying only the equilibrium measure, nor does it prove pointwise convergence of every bounded trajectory. The no-compact-invariant-set statement for \(\Delta<0\) is included as a consequence of the moment obstruction, not as the principal originality claim because it is closely adjacent to Starkov and Starkov's earlier localization theorem.

## References

1. O. E. Rössler, “An equation for continuous chaos,” *Physics Letters A* **57** (1976), 397–398. https://doi.org/10.1016/0375-9601(76)90101-8
2. K. E. Starkov and K. K. Starkov Jr., “Localization of periodic orbits of the Rössler system under variation of its parameters,” *Chaos, Solitons & Fractals* **33** (2007), 1445–1449. https://doi.org/10.1016/j.chaos.2006.02.011
3. V. Kontorovich, L. A. Beltrán, J. Aguilar, Z. Lovtchikova, and K. R. Tinsley, “Cumulant Analysis of Rössler Attractor and its Applications,” *The Open Cybernetics & Systemics Journal* **3** (2009), 29–39. https://doi.org/10.2174/1874110X00903020029
4. J. C. Sprott and C. Li, “Asymmetric Bistability in the Rössler System,” *Acta Physica Polonica B* **48** (2017), 97–107. https://doi.org/10.5506/APhysPolB.48.97
5. J. J. Bramburger and G. Fantuzzi, “Data-driven discovery of invariant measures,” *Proceedings of the Royal Society A* **480** (2024), 20230627. https://doi.org/10.1098/rspa.2023.0627
6. J.-M. Malasoma and N. Malasoma, “Bistability and hidden attractors in the paradigmatic Rössler'76 system,” *Chaos* **30** (2020), 123144. https://doi.org/10.1063/5.0030023
