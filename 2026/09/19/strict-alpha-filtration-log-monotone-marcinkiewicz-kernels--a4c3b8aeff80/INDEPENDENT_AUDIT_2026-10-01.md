# Independent mathematical audit — 2026-10-01

## Final claim assessed

Strict alpha-filtration of logarithmically monotone Marcinkiewicz kernels

## Correctness — PASS

PASS. For fixed \(n\), if \(0<\alpha<\beta\), then \(p_n^{(\alpha)}<p_n^{(\beta)}\), and monotonicity of normalized positive moments gives \(A_n^{(\alpha)}\le A_n^{(\beta)}\), hence \(\Phi_\alpha\le\Phi_\beta\). The compressed-block probe is also valid: its block mass is \(r_n\), its support endpoint satisfies \(\log R_n=L_n-r_n^\gamma\), and previous and next block contributions are asymptotically negligible. The normalized moment therefore has the factor \(\exp(-r_n^{\gamma-\alpha}/p_n+o(1))\), giving exactly \(0\), \(e^{-1}\), or \(1\) according as \(\alpha<\gamma\), \(\alpha=\gamma\), or \(\alpha>\gamma\). Choosing \(\gamma\) strictly between two parameters proves strict kernel inclusion. The Hardy--Littlewood obstruction for every interior parameter follows from Huang's \(f,g\) pair and the corresponding moment estimates.

## Originality — PASS

PASS to the best of current knowledge. Huang's complete 11-page primary paper was inspected. It defines the entire \(\alpha\in(0,1]\) family but specializes to \(\alpha=1\) for a non-strongly-symmetric norm and \(\alpha=1/2\) for a non-Hardy--Littlewood-solid kernel; it does not state monotone nesting, strictness, or the threshold probes. A highly relevant same-day published result on the general critical scale \(L_n(1-p_n)\) was also inspected in full: it proves a different phase diagram, including the \(\alpha>1\) fully symmetric regime and order-theoretic behavior for \(\alpha<1\), but it does not imply strict separation among distinct parameters in \(0<\alpha<1\) or construct \(h_\gamma\) with the \(0/e^{-1}/1\) response. No earlier exact strict-filtration theorem was found.

### equivalent_formulations

Searches: Resultary: Marcinkiewicz Huang logarithmically monotone alpha kernels strict filtration threshold probes; Huang 2609.20270 alpha parameter kernel

Evidence: Huang's full paper contains the family but only two special parameter applications. No earlier record states \(X_\beta\subsetneq X_\alpha\) for every \(0<\alpha<\beta<1\) with threshold probes.

Reasoning: The strict filtration is equivalent to existence of a separator for every parameter pair; the explicit \(h_\gamma\) supplies exactly that information and is absent from the inspected sources.

### broader_coverage

Searches: Complete 2026/9/19 critical-scale phase-transition Resultary result; Kalton Sukochev nonsymmetric singular functionals Marcinkiewicz

Evidence: The same-day phase-transition result classifies regimes according to \(L_n(1-p_n)\) and proves \(\alpha<1\) kernels are not Hardy--Littlewood solid, but does not compare two interior alpha kernels. Classical singular-functional work establishes the broad phenomenon of nonsymmetric behavior, not this parameter geometry.

Reasoning: The broader order-theoretic results do not dominate the strict continuum filtration.

### exact_database_or_table

Searches: Resultary semantic search for strict alpha filtration and \(0/e^{-1}/1\) probe

Evidence: The audited record was the exact matching result; the nearest other record concerns a different critical-scale phase diagram.

Reasoning: No database/table is natural; theorem-level published-record comparison was performed.

### claim_vs_prior_implication

Searches: Huang Propositions 3.1, 3.5, 3.6; Critical-scale phase transition in logarithmically monotone Marcinkiewicz renormings

Evidence: Huang proves \(\alpha=1\) and \(\alpha=1/2\) endpoint examples; the related record proves phase behavior but not pairwise strictness. Pairwise strictness requires a new concentration-scale probe tuned to an intermediate \(\gamma\).

Reasoning: The claimed filtration is not obtained by merely substituting parameters into a prior closed formula.

## Scientific value — PASS

PASS. The result shows that Huang's continuum of parameters is not redundant: it yields a strictly ordered continuum of distinct logarithmically solid kernels inside one fixed Marcinkiewicz space, with explicit probes that measure the concentration exponent separating any two parameters. That is a natural structural refinement of a new counterexample family.

## Source inspections

- **A logarithmically monotone symmetric norm which is not fully symmetric** — https://arxiv.org/abs/2609.20270. Material read: Complete 11-page primary paper, including the general alpha construction and Sections 3.2--3.3. Assessment: PRIMARY_SOURCE_NOT_STRICT_FILTRATION_COVERAGE. Evidence: The paper defines the alpha family but uses only alpha one and one-half for its two main counterexamples; it contains no pairwise nesting or threshold-probe theorem.
- **Critical-scale phase transition in logarithmically monotone Marcinkiewicz renormings** — https://github.com/Resultary/2026/blob/main/2026/9/19/SCOPE-critical-scale-phase-transition-log-monotone-norms--d7fba80be965/RESULT.md. Material read: Complete published result. Assessment: OVERLAPPING_NOT_COVERING_STRICT_FILTRATION. Evidence: It identifies the \(L_n(1-p_n)\) phase boundary and the \(\alpha>1\) regime but does not prove strict inclusion between distinct interior kernels.

## Limitations and residual risks

The strict-filtration theorem concerns Huang's specific Marcinkiewicz scales and \(0<\alpha<1\); it does not assert abstract Banach-lattice nonisomorphism of the kernels or a noncommutative analogue.

- Older singular-functional literature may contain an equivalent family-separation construction under different notation, though no exact match was located.
- The theorem is specific to Huang's scales and does not classify arbitrary logarithmically monotone seminorm families.

## Disposition

**passed**
