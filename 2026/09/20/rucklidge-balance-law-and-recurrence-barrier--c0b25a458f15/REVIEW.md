# Review: exact Rucklidge balance and recurrence barrier

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Direct differentiation of
\[
\mathcal F=\frac12x^2-\frac b2y^2+\frac12y^2z-\frac14z^2
\]
along \(\dot x=-ax+by-yz\), \(\dot y=x\), \(\dot z=y^2-z\) gives
\[
\dot{\mathcal F}=-ax^2+\frac12(y^2-z)^2=-ax^2+\frac12\dot z^2.
\]
The accompanying symbolic artifact verifies this with an identically zero residual.

The bounded-orbit average follows by integrating the exact derivative and dividing by time. The periodic-orbit identity follows because \(\mathcal F\) returns to its initial value. The invariant-measure identity follows from \(\int L\mathcal F\,d\mu=0\) on compact support.

For \(a<0\), the zero set of \(\dot{\mathcal F}\) requires \(x=0\) and \(z=y^2\); its largest invariant subset is exactly the equilibrium set. For \(a=0\), the zero set is \(z=y^2\); differentiating this constraint forces \(xy=0\), and invariance again leaves only equilibria. A bounded forward orbit is precompact, \(\mathcal F\) is monotone and bounded on it, and LaSalle's invariance argument places the omega-limit set in the finite equilibrium set. Connectedness of the omega-limit set then gives convergence to one equilibrium.

The Shimizu–Morioka companion identity was checked independently by exact symbolic differentiation.

## Originality

**PASS, to the best of our knowledge.** The following close literature was checked for equivalent or stronger coverage.

- Rucklidge (1992, 1993) derives and studies the low-order convection equations, homoclinic explosions, Lorenz-like chaos, bifurcations at infinity and unbounded trajectories. The inspected 1993 author manuscript does not state the polynomial balance or the nonpositive-damping recurrence barrier.
- Messias, Gouveia and Pessoa (2012) gives a global Poincare-compactification description of Shimizu–Morioka dynamics, including the \(\alpha=0\) heteroclinic structure and local behavior for negative \(\lambda\). The inspected statements do not imply the exact balance or the global bounded-orbit result for \(\lambda\le0\).
- Zhao et al. (2013) develops general attractive-set criteria for classes of quadratic systems and lists Rucklidge among systems satisfying a structural condition. No Rucklidge-specific balance equivalent to the present identity was found in the inspected article.
- Lima, Llibre and Valls (2014) classifies Darboux and analytic integrability for the same Rucklidge family. Its introduction explicitly lists \((a,b)=(-0.1,-1)\) as a chaotic-attractor parameter example. The present theorem is not an integrability claim and gives a direct obstruction to any bounded recurrent attractor for that example.
- Huang, Shi and Li (2017) studies meromorphic non-integrability. Huang, Shi and Li (2020) establishes the scaling relation between Rucklidge and Shimizu–Morioka and studies integrability. Neither located result states the balance law or damping-sign recurrence barrier.
- Dong et al. (2021) studies unstable periodic orbits, symbolic encodings and bifurcations for positive parameters. Its detailed periodic-orbit calculations do not report the universal integral constraint \(\int\dot z^2=2a\int x^2\).
- Demina and Ilyukhin (2023) classifies invariant algebraic manifolds and explicit solutions lying on them. Only the abstract and bibliographic description were inspected; the full theorem statements were not available in the inspected sources, making this the principal residual prior-coverage risk.
- More recent searches through 2026 for Rucklidge global dynamics, invariant measures, Lyapunov/balance identities, negative damping, and Shimizu–Morioka bounded dynamics did not locate an equivalent theorem.

The direction of improvement is global and exact: the result converts a polynomial differential identity into a sharp sign obstruction for all compact recurrent statistics and all bounded forward trajectories, rather than locating individual bifurcations or numerically classifying attractors.

## Value

**PASS.** The identity provides a parameter-only consistency condition for every periodic orbit and every compact invariant measure in the physically studied positive-damping regime. More importantly, it separates volume contraction from bounded recurrence: nonpositive damping allows no bounded non-equilibrium recurrent dynamics. This resolves a concrete literature inconsistency at \((a,b)=(-0.1,-1)\), where a published integrability paper labels the dynamics a chaotic attractor even though the exact balance forces every bounded forward orbit to approach the sole equilibrium.

## Scientific limitations

Originality remains a literature-search judgment rather than a proof that no equivalent identity has ever appeared. The Rucklidge/Shimizu–Morioka family has a large control, synchronization and numerical-simulation literature, and an equivalent balance could be hidden under a different normalization or in a source not located here. The uninspected full text of Demina and Ilyukhin (2023), DOI 10.1134/S0037446623050075, is the most plausible identified source that could affect originality because it classifies invariant algebraic manifolds of the same system; its accessible abstract does not state the balance or recurrence theorem.

The convergence theorem assumes the forward orbit is bounded and therefore does not prove global existence or ultimate boundedness. This qualification is substantive: the original magnetoconvection analysis already records escape to infinity in parts of the reduced-ODE parameter space. The conclusion applies to the autonomous low-order ODE, not automatically to higher-order corrections or to the parent PDE.

## Checked sources

- https://doi.org/10.1017/S0022112092003392
- https://doi.org/10.1016/0167-2789(93)90291-8
- https://doi.org/10.1007/s11071-011-0288-8
- https://doi.org/10.1155/2013/590421
- https://doi.org/10.1007/s11071-014-1389-y
- https://doi.org/10.3390/e19050211
- https://doi.org/10.1016/j.cnsns.2019.105101
- https://doi.org/10.1155/2021/4465151
- https://doi.org/10.1134/S0037446623050075
