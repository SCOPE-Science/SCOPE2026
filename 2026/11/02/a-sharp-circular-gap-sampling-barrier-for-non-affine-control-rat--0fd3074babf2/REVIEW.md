# Self-review

## Correctness

**PASS.** The strictly monotone map has derivative \(\rho=(T/2)(1-a\cos(2\pi(\sigma-c)))\), so every affine pseudotime control has physical derivative \(K/\rho\). The exact nodal admissibility radius is \(R\min_j\rho_j\), attained by a choice of \(K\); global maximum equals this divided by \(\min\rho=(T/2)(1-a)\). Circular nearest-neighbor geometry then proves the sharp worst-phase formula, and the unit sum of the gaps proves the unique minimax mesh. The two-node Radau calculation can be checked directly by exact fractions. The attached checker reproduced 11,313 finite supplementary assertions. No finite test is treated as proof of infinite quantifiers.

## Originality

**PASS, with historical-priority limitations.** The motivating full primary manuscript gives the differential constraints as nodewise inequalities and separately specifies sinusoidal dilation. Its paper sections and numerical cases do not give a continuous rate guarantee or the exact circular-gap/minimax phase factor. The inspected relevant 2016 collocation convergence paper and 2022 parametric-mapping paper pursue asymptotic numerical convergence rather than this sharp fixed-degree/fixed-mesh physical-time slew-rate safety factor. Related sampled trigonometric extrema and circular covering facts exist, but the claimed contribution is their exact consequence for nodally enforced physical time derivative constraints under this particular prescribed map. A 2021 direct rate-constraint implementation paper was cited in the motivating source but its full text was inaccessible for review; older specialized equivalent formulas therefore remain a risk. Published material comparison and searches do not constitute independent priority certification.

## Mathematical value

**PASS.** This is not solely an arbitrary pointwise counterexample: it gives the exact operator norm from nodal rate constraints to whole-interval affine-control feasibility, the worst-case map-center law for any mesh, the unique minimax N-node placement, a sharp mesh-count/tightening rule, and a concrete low-order Radau case. Physical actuator slew limits must hold between nodes; the factor can diverge as map concentration \(a\uparrow1\), notwithstanding exact derivative interpolation. These quantitative boundaries can guide sampling and constraint margins in numerical trajectory optimization without claiming a higher-order method-wide error theorem.

## Source comparison and limitations

Minnozzi–Sagliano, arXiv:2610.17842, Sections 2.2, 3, 4.2, 5.1.1–5.1.2 (especially Eqs. (38), (42), (74)–(75)); Hager et al., arXiv:1607.02798, introduction and formulation; Elgindy–Refat, arXiv:2207.05467, introduction and mapping/convergence discussion. The older Nie–Kerrigan article, DOI:10.1109/TAC.2020.2976051, is an unresolved full-text comparison; no statement about its entire content is inferred from abstracts or citations. The result is limited to affine pseudotime controls and a particular sinusoidal finite-interval map. The finite checker is supplemental, not a formal proof.

Self-review: passed. Independent audit: not yet performed.
