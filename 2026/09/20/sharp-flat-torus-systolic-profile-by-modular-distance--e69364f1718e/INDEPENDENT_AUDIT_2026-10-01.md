# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-e69364f1718e`

## Correctness — PASS

In the reduced modular half-domain, the normalized systolic ratio is \(q=(\sqrt3/2)/y\) and quotient distance to the hexagonal class is the hyperbolic distance to \(\rho\). A hyperbolic circle about \(\rho\) is an explicit Euclidean circle. Its largest feasible height is on \(x=1/2\), giving the exact lower envelope \(q=e^{-d}\). Its smallest feasible height lies first on the unit-circle boundary and, after the square point, on \(x=0\), giving the two displayed upper branches. The feasible intersection arc is connected, so every intermediate ratio occurs, and algebraic inversion yields the exact distance interval.

### Correctness sources

- assigned RESULT.md
- current modular-distance Loewner-defect theorem
- standard reduced modular-domain geometry

### Correctness risks

- The metric normalization is curvature minus one and the theorem concerns flat similarity classes only.

## Originality — PASS

A same-day published modular-distance Loewner-defect theorem already contains the minimum-height optimization, hence the audited upper \(q\)-envelope and the rhombic-to-rectangular transition are not independently original. It does not supply the opposite maximum-height boundary \(q=e^{-d}\), the complete fixed-distance interval of all systolic ratios, or the full inverse distance interval. Resultary searches targeted at the lower envelope and inverse profile found only the audited record. The surviving two-sided classification is therefore original to the best of current evidence.

### equivalent_formulations

Searches:
- Resultary: flat torus systolic ratio modular hyperbolic distance exact sharp profile hexagonal rhombic rectangular phase transition
- Resultary: flat torus modular distance hexagonal lower envelope e^{-d} systolic ratio exact inverse distance interval

Evidence:
- The same-day Loewner-defect theorem matches the minimum-height/upper-ratio branch exactly.
- No separate current result matched the maximum-height/lower-ratio branch or the complete two-sided interval.

Reasoning:
Equivalent formulations through \(y\)-height, Hermite invariant, Loewner deficit, and modular distance were compared.

### broader_coverage

Searches:
- https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-sharp-modular-distance-loewner-torus-defect--9d33731886f5
- earlier Resultary flat-moduli stability theorem
- Horowitz–Katz–Katz arXiv:0803.0690

Evidence:
- The same-day theorem gives a sharp one-sided modular defect for general Riemannian tori, which is broader in metric class but one-sided in the modular profile.
- The earlier stability theorem is a coarse deficit-distance bound.

Reasoning:
Broader metric scope does not imply the missing lower envelope or the complete interval at fixed distance.

### exact_database_or_table

Searches:
- current Resultary flat-torus records
- geometry-of-numbers/modular-surface terminology

Evidence:
- No exact table or database of the two-sided profile was located.

Reasoning:
This is a continuous moduli-space optimization rather than a tabulated invariant.

### claim_vs_prior_implication

Searches:
- formula-by-formula comparison with the same-day Loewner-defect record

Evidence:
- Its piecewise \(\Phi(d)\) is algebraically the same minimum-\(y\) branch that determines the audited \(M(d)\).
- It does not determine maximum \(y\) at fixed \(d\), which yields \(e^{-d}\), nor the resulting complete inverse interval.

Reasoning:
Partial one-sided coverage does not imply the final two-sided classification.

### source_inspections

- **Sharp modular-distance defect for Loewner's torus inequality** — https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-sharp-modular-distance-loewner-torus-defect--9d33731886f5. Trigger: Highly relevant same-day published result. Material read: Complete published RESULT.md. Method: Full formula and proof comparison. Assessment: PARTIAL COVERAGE. Evidence: It proves the same minimum-height piecewise branch and square-torus transition but not the opposite height extreme or full two-sided interval.
- **Loewner's torus inequality with isosystolic defect** — https://arxiv.org/abs/0803.0690. Trigger: Primary source for the conformal-factor defect underlying the same-day comparison. Material read: Bibliographic/theorem scope as cited in the fully inspected current theorem; no whole-document exclusion is inferred from this run. Method: Context comparison only. Assessment: Residual primary-source access risk, not decisive for the surviving lower-envelope claim. Evidence: The current theorem identifies its established input as a conformal-class inequality, distinct from the two-sided flat-moduli profile.

### checked_sources

- https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-sharp-modular-distance-loewner-torus-defect--9d33731886f5
- https://arxiv.org/abs/0803.0690
- earlier Resultary flat-moduli stability finding
- current Resultary two-sided search
- assigned RESULT.md

### residual_risks

- The surviving formulas are elementary consequences of classical reduction theory, so equivalent older geometry-of-numbers folklore may exist.

## Scientific value — PASS

Completing a one-sided sharp stability result to the exact set of all possible systolic ratios at every modular distance, with an explicit inverse distance interval, is a natural global classification of flat-torus shape stability. The lower envelope and full interval are mathematically useful even though the upper envelope is independently covered.

### Value sources

- same-day one-sided modular defect theorem
- assigned two-sided profile

### Value risks

- The theorem controls only systolic ratio, not diameter or covering radius.

## Limitations

- Flat two-tori up to similarity only.
- The upper envelope and square-torus transition are currently covered elsewhere and are not counted as novel.
- Originality of the surviving lower envelope/full interval is best-of-knowledge with classical-folklore risk.

## Disposition

**PASSED**
