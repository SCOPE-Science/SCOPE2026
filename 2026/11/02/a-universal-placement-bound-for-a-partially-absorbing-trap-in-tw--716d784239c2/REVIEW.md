# Review: optimal point trapping in two-layer diffusion

## Correctness

**PASS.** The closed positive quadratic form defines the claimed eigenvalue, and the interface and absorber flux jumps match the transfer-matrix implementation. The derivative identity for two one-sided Neumann–Dirichlet logarithmic derivatives proves strict global minimization of the strength required to attain a trial eigenvalue, not merely local stationarity. Analytic phase matching yields the unique optimizer for every positive reactivity and diffusivity ratio. Strict phase monotonicity and the limiting root of \(\tan t=-t\) prove the universal bound; the transfer-matrix checker separately passed 2578 diagnostic assertions.

## Originality

**PASS on inspected sources, subject to historical priority risk.** Kazakevičius–Ruseckas (2016, arXiv:1608.07335v1) analyze heterogeneous diffusion in a different stochastic convention with external potentials. Tung–Lawley (2026, arXiv:2601.08740v1) derive weak-reactivity/target-size asymptotics for escape statistics; their full text does not state an all-reactivity, two-layer one-point placement law or sharp universal location bound. Grebenkov–Kolokolnikov (2026, arXiv:2609.39990v1) treats many-trap mean capture time, not the single point-sink principal eigenvalue maximization. Kolokolnikov–Titcombe–Ward (2005) optimizes small absorbing holes in a planar region; its two-dimensional small-hole limit does not dominate the present statement. An older Cheviakov–Ward (2011) sphere interior-trap paper was only partially accessible, so equivalent historical formulations outside the inspected texts remain a risk. Database comparisons were performed against published semantically related mathematical results and accessible prior claims; absence of a matching search result alone was not treated as novelty proof.

## Value

**PASS.** This resolves a motivated spectral design problem with material contrast rather than a homogeneous rescaling: the exact optimum for every partial absorption strength is offset toward slower diffusivity and has a surprisingly contrast-independent sharp lower-location bound. Its weak- and strong-absorption laws quantify practical placement tradeoffs. This is a finite-parameter exact theorem; no broader theorem or empirical performance claim is required for its utility.

## Limits and comparison risk

The bound assumes equal layer lengths, piecewise-constant Fickian diffusion, one delta absorber, and two reflecting endpoints. Mean-first-passage minimizers and Ito/Stratonovich formulations are different observables/operators. Some older full papers could not be inspected, so independent historical priority and external auditing remain open.

Self-review: passed. Independent audit: not yet performed.
