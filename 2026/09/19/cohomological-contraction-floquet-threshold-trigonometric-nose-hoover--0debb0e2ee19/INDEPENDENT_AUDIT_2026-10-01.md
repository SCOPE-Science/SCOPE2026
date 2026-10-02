# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-0debb0e2ee19`

## Correctness — PASS

The exact cohomology identity follows immediately from \(\dot z=b(1-2\cos y)\): substituting \(\cos y=(1-\dot z/b)/2\) into the divergence gives the displayed bounded coboundary plus \(-(a/2)\sin z\). Integrating yields the finite-time Jacobian formula and, for invariant measures, the contraction/Lyapunov-sum identity. The periodic Liouville gauge removes the first derivative in the central normal variational equation and gives the stated two-harmonic Hill coefficient; Abel's identity gives determinant one. The inspected verifier symbolically reduces both exact identities to zero. Its high-accuracy integration gives trace \(-2\) near \(a=1.590316803014779\) for \(b=1/2\), with determinant numerically one and traces on opposite sides of \(-2\) at 1.58 and 1.60. The record correctly labels this edge value as floating-point evidence rather than an interval-certified theorem.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_floquet_contraction.py and verification.txt
- earlier reversible-Floquet SCOPE theorem
- Szumiński–Llibre source model

### Correctness risks

- The numerical band edge is not a rigorous enclosure and does not prove a global chaotic transition.

## Originality — PASS

An earlier published SCOPE theorem already gives reciprocal multipliers for reversing-symmetric periodic orbits, non-attraction of the explicit family, the central Hill reduction, determinant one, and the elliptic/hyperbolic/parabolic trichotomy. Those components are prior coverage and are not originality-bearing here. The surviving contribution is the source-specific cohomological contraction identity and its invariant-measure/Lyapunov-sum consequence, together with the computed \(b=1/2\) local \(-1\) edge at \(a\approx1.590316803\). Fresh Resultary search found the audited record as the exact match; a later semifinite-gap result uses the already-known Hill equation for a different spectral classification and does not state the contraction cohomology or this computed edge.

### equivalent_formulations

Searches:
- Resultary semantic search for trigonometric Nosé–Hoover cohomological contraction and Floquet edge
- comparison with SCOPE-reversible-floquet-obstruction-trigonometric-nose-hoover--87f8866a2ffc

Evidence:
- The earlier theorem contains the reversible multiplier/Hill structure but not the coboundary formula or invariant-measure contraction identity.

Reasoning:
Equivalent formulations via divergence cohomology, invariant-measure averages, Lyapunov sums, and Floquet discriminants were separated.

### broader_coverage

Searches:
- earlier reversible-Floquet theorem
- SCOPE-semifinite-gap-floquet-trigonometric-nose-hoover--87ff381e2668

Evidence:
- The earlier theorem is broader for symmetry consequences; the later theorem is broader for certain Whittaker–Hill gap closures. Neither dominates the cohomological identity plus the specific computed edge.

Reasoning:
Substantial components are covered, but not the final surviving package.

### exact_database_or_table

Searches:
- current Resultary trigonometric Nosé–Hoover findings

Evidence:
- No database/table source for the contraction identity or the numerical local edge was located.

Reasoning:
The exact identity is algebraic and the edge is computed from monodromy, not copied from a table.

### claim_vs_prior_implication

Searches:
- implication comparison from reversible Floquet theory

Evidence:
- Reciprocal multipliers do not imply the pointwise divergence coboundary or the invariant-measure formula; the latter uses the special thermostat equation.

Reasoning:
The source-specific cohomology is independent mathematical content beyond generic reversibility.

### source_inspections

- **Reversible Floquet obstruction in the trigonometric Nosé–Hoover oscillator** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-reversible-floquet-obstruction-trigonometric-nose-hoover--87f8866a2ffc. Trigger: Earlier source-specific Floquet theorem. Material read: Complete published RESULT.md. Method: Full statement comparison. Assessment: PARTIAL COVERAGE. Evidence: It already contains reciprocal multipliers and the same Hill reduction, but not the contraction cohomology or \(a\approx1.590316803\) edge.
- **Assigned contraction/Floquet verifier** — artifacts/verify_floquet_contraction.py. Trigger: Exact identities and numerical edge. Material read: Complete source and saved output. Method: Symbolic-line inspection and numerical-method audit. Assessment: The exact symbolic identities are verified; the edge remains numerical evidence as stated. Evidence: Symbolic residuals are zero; direct and transformed monodromy traces agree to numerical precision.
- **Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability** — https://arxiv.org/abs/2609.19958. Trigger: Primary source defining the flow and reporting the transition scale. Material read: Accessible abstract/scope material; full arXiv text was unavailable through the attempted route. Method: Background-scope comparison with access limitation recorded. Assessment: No whole-document originality exclusion is based on this inaccessible full text. Evidence: The assigned package derives the cohomology directly from the source ODE.

### checked_sources

- assigned RESULT.md and verifier
- SCOPE-reversible-floquet-obstruction-trigonometric-nose-hoover--87f8866a2ffc
- SCOPE-semifinite-gap-floquet-trigonometric-nose-hoover--87ff381e2668
- arXiv:2609.19958
- Resultary search

### residual_risks

- The source paper's full text was not available in this run; source-specific parallel observations remain possible.
- The numeric edge is not a certified exact invariant.

## Scientific value — PASS

The cohomological reduction collapses a two-variable contraction observable to a one-variable phase average for every invariant measure, giving a reusable diagnostic for this thermostat model. The computed local Floquet edge is motivated by the source's abrupt transition near the same parameter and distinguishes an exact local mechanism from broader numerical chaos claims.

### Value sources

- source transition problem
- assigned cohomological identity
- central-orbit Floquet computation

### Value risks

- The numerical edge is evidence for a local threshold only, not a proof of global bifurcation.

## Limitations

- The exact identities require \(b
e0\).
- The Hill/reversible multiplier structure is prior covered and is not counted as novel here.
- The \(b=1/2\) edge is high-accuracy floating-point evidence, not interval certification.
- No global route-to-chaos theorem is claimed.

## Disposition

**PASSED**
