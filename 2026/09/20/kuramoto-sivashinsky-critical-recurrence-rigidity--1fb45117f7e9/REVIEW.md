# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The centered $L^2$ energy identity is exact for every conservative flux $\partial_x f(u)$: the nonlinear contribution is a periodic spatial derivative. At $\nu=1$, the dissipation defect is
\[
D=\|u_{xx}\|_2^2-\|u_x\|_2^2
=2\pi\sum_{|k|\ge2}k^2(k^2-1)|\widehat u_k|^2,
\]
so its kernel is exactly the mean plus the first Fourier harmonic. Recurrence forces the nonincreasing energy to return to its initial value and hence to remain constant, placing the whole recurrent trajectory in that kernel. Substitution of a constant-amplitude first harmonic into the PDE forces $f'$ to be constant on the entire attained value interval; conversely an affine flux on that interval produces the asserted traveling wave. This proves the recurrent-orbit classification without a numerical or perturbative step.

The invariant-measure statement follows by integrating the finite-time energy drop against an invariant measure: nonnegativity forces support in the same zero-dissipation kernel, and invariance of support then invokes the orbit classification. For the classical quadratic flux, no nontrivial affine interval exists. Established compactness of the one-dimensional periodic KS semigroup then permits LaSalle's principle and yields convergence to the conserved mean at the critical parameter. The strict $\nu>1$ estimate follows from Poincare's inequality, while $\nu<1$ has a positive real $k=1$ eigenvalue. The three regimes therefore close to the exact threshold $\nu\ge1$ for global asymptotic stability of the set of constants.

The argument was stress-tested against nonzero conserved means, where the linearization acquires only an imaginary advection shift, and against locally affine fluxes, which indeed generate exact first-harmonic traveling waves at criticality and therefore show that the affine-flux obstruction is necessary as well as sufficient.

## Originality

**PASS, to the best of our knowledge.** Older foundational work by Nicolaenko--Scheurer--Temam, Il'yashenko, Collet--Eckmann--Epstein--Stubbe, and Goodman develops nonlinear stability, absorbing sets, attractors, phase portraits, and stability for the classical KS equation. Tadmor supplies the well-posedness framework. Li--Chen and later papers study bifurcation near critical modes. Cui--Guo treat generalized conservative fluxes under Dirichlet conditions and a strict spectral inequality.

The directly comparable Al Jamal--Morris paper proves global asymptotic stability of the set of constants only for $\nu>1$ and instability for $\nu<1$. Its final draft discusses $\nu=1$ inconsistently: one passage cites the zero equilibrium as a global attractor, while a later passage says the zero equilibrium is Lyapunov stable and not asymptotically stable. Neither passage supplies the critical zero-dissipation invariant-set calculation, distinguishes fixed-mean attraction from attraction to a single zero equilibrium, or gives the affine-flux classification.

No checked accessible source states the theorem that every critical recurrent orbit of the conservative-flux periodic family is a first-harmonic traveling wave whose amplitude interval is exactly an affine interval of the flux; nor was the resulting invariant-measure rigidity found. Exact and synonymous searches covered critical/neutral KS stability, generalized conservative-flux KS equations, first bifurcation, attractors, invariant measures, recurrent dynamics, and traveling waves.

Residual originality risk is scientifically significant. Full theorem-level text was not available for Nicolaenko--Scheurer--Temam (1985), Il'yashenko (1992), Goodman (1994), or Li--Chen (2001). Any of these could contain an equivalent critical-boundary observation for the classical quadratic equation. The strongest originality claim is therefore the generalized affine-flux recurrent-orbit classification and its exact obstruction mechanism; the classical $\nu=1$ closure is presented as a concrete consequence and clarification, with possible older implicit coverage explicitly acknowledged.

## Value

**PASS.** The result closes a nonhyperbolic equality case left outside the usual strict energy estimate and identifies exactly why the equality case is nevertheless dissipative for the classical nonlinear flux: neutral first harmonics cannot remain neutral because the flux generates harmonics outside the energy kernel. The generalized theorem turns that mechanism into a sharp structural criterion—critical recurrence survives exactly on amplitudes over which the flux becomes affine. It constrains all recurrent trajectories and compactly supported invariant measures, not merely a local branch or a numerically observed attractor, and yields an exact global stability threshold for the classical periodic equation.

## Scientific limitations

The general-flux recurrence theorem assumes sufficiently regular solutions; the global-attraction consequence for a general $C^1$ flux additionally requires global well-posedness and precompact positive orbits and is not asserted unconditionally. The unconditional corollary is restricted to the classical one-dimensional periodic KS equation, whose semigroup theory is established. The result does not classify dynamics for $\nu<1$, does not give a quantitative critical decay rate, and does not address higher-dimensional KS equations. Several old, highly relevant full texts remain inaccessible enough that they pose residual originality risk for the classical special case.
