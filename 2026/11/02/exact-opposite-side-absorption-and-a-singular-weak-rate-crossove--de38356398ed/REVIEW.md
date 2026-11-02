# Self-review

## Correctness — PASS

The claim specifies the whole-line Brownian diffusion normalization, the two-state gate, reset protocol, incoming-side event, and the strictly positive parameter domain. The no-reset Brownian first-zero Laplace transform and two-state gate semigroup yield the displayed \(g_A,g_I\) and \(\ell_A,\ell_I\). The inactive-origin transform follows from an explicit bounded coupled ODE with active absorption and inactive derivative-continuity boundary conditions. The reset equation is a two-by-two renewal equation preserving the gate state, and its solution yields the complete conditional and stationary formulas. Strict monotonicity and singular limits are proved analytically, with numerical cross-checks by independent backward equations and a Brownian-bridge event simulator. No finite simulation is used as proof of a universal assertion.

## Originality — PASS, subject to the stated residual risk

The closest same-model paper, Żbik et al. (arXiv:2512.09739, full text including Section III.3 and Appendix B), studies the opposite-side directional observable *numerically* and derives the *unmarked* hitting-time transform. The present explicit directional probability, exact conditional gate-state splitting, strict monotonicities and joint weak-rate crossover are not supplied in that material. The reflecting-inactive model of Mercado-Vásquez and Boyer (arXiv:2107.02148, inspected PDF) has no opposite-side incoming flux, and its target state is redrawn after resets. Bressloff (arXiv:2009.02739, inspected PDF) studies mean passage at reflecting/absorbing gated boundaries rather than a two-sided incoming-direction law. Semantic searches of mathematical result summaries and searches for equivalent Brownian side-flux or splitting formulas did not identify a result implying the full claim. A broader specialized flux-splitting theorem remains a genuine residual priority risk; absence of a search result is not proof of uniqueness.

## Value — PASS

The exact probability concerns the capture-side mark explicitly motivated and sampled in the source's Figure 5; it cannot be reconstructed from the total passage-time law alone. The distinction between resetting position and resetting the gate is structural, and the noncommuting weak-rate limits expose an observable that behaves differently from the unmarked absorption time. The exact sign of the gate-switching dependence, its upper bound, and the universal ratio-dependent crossover provide testable diagnostics for reactive transport and search models; no assertion of a general-dimensional theorem is necessary for this value.

## Closest literature, qualifications and boundaries

The methodological inputs are Brownian hitting-time transforms, finite-state Markov resolvents, two-sided reflection symmetry, and renewal decomposition. The model, basic first-passage equations, and simulation of direction already appear in Żbik et al. The proof is for symmetric switching and a fixed positive reset point; it does not cover asymmetric or coupled gates. Full independence of review is not claimed, and a further manual priority check against more specialized directional-flux literature is warranted.

Self-review: passed. Independent audit: not yet performed.
