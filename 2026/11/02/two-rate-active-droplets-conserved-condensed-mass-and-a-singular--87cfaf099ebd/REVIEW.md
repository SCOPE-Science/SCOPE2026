# Scientific review of the two-tumbling-rate stationary branch

## Correctness — PASS

The stationary equations reduce phasewise to two flux equations. The positive decaying gas branch has zero first-integral constant and fixes both interface fluxes. In the liquid, interface matching fixes a hyperbolic two-mode profile, rather than a single exponential. Integrating the flux and density gives an exact strictly increasing mass equation with a positive-width solution precisely above the gas-controlled threshold. The proof checks nonnegative component populations, the origin reset source, exact total mass, strict monotonicity in liquid tumbling and the singular layer measure limit. The supplied verifier passes 594 finite checks, which corroborate algebra but are not the proof.

## Originality — PASS (best-knowledge)

The closest source is Grange, arXiv:2610.26149 (2026), whose complete online manuscript sections 2–6 and relevant appendices were examined. It treats one common tumbling rate, derives the gas/droplet profiles and phase masses, and extends to finite return velocity; those fixed-rate results are credited. Evans–Majumdar 2018 studies resetting of a *single noninteracting* RTP at homogeneous flip rate. Cates–Tailleur 2012 treats general density-dependent motility/MIPS, not the local-reset matched interface. An accessible earlier general-flux classification with homogeneous tumbling also yields a gas-mass invariant but not the two-rate liquid transfer solution, its strict width law, or the fast-liquid-tumble singular profile. Specific semantic mathematical-database searches for alternate formulations were performed; the returned closest records did not state the paired phase-dependent tumbling theorem. The search is not a uniqueness or priority proof. Residual risk: broader piecewise-constant kinetic transfer-matrix formulae could entail some identities even if not presented in this physical formulation.

## Value — PASS

The addition of a separate dense-phase tumble rate is physically motivated because dense clusters can modify particle reorientation as well as speed. The theorem isolates which observables a dense-phase reorientation control changes (droplet width and center density) and which remain pinned to dilute transport (phase mass and nucleation threshold). It establishes the unexpected singular limit of a shrinking droplet with finite mass and an explicit inner-layer law, providing a sharp mathematical boundary for modeling very rapid dense-phase reorientation. Neither an arbitrary parameter substitution nor a new name for a known stationary expression yields this full result.

## Scientific limitations and closest coverage

The contribution is restricted to a symmetric one-droplet steady branch of a discontinuous mean-field kinetic model with two positive constant tumbling rates. No broad dynamical stability, global stationary uniqueness, particle-level limit or independent priority certification is claimed. The closest exact source already establishes the homogeneous-tumbling limit and the gas-side mass mechanism, which are not asserted as new. An unrestricted linear-system transfer theorem remains a residual overlap risk.

Self-review: passed. Independent audit: not yet performed.
