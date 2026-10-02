# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-ada22ea47e72`

## Correctness — PASS

The squared Cayley reductions are exact consequences of the source formula for \(p_n\) and the companion recurrence. Eneström–Kakeya gives the stated \(u\)-annuli; for \(Q_n\), the leading term versus the sum of the lower terms makes the outer unit-circle bound strict. The inverse Cayley identity \(\operatorname{Re}z=(|w|^2-1)/|w-1|^2\) then gives Hurwitz stability and the Apollonius regions. The discriminant derivation checks: differentiating \(R_n=(1-u)Q_n\), evaluating the three elementary root products, applying the squared-variable discriminant identity, and then Möbius covariance produces the displayed closed form. The package verifier independently matches exact symbolic discriminants through degree six. For the limiting law, Erdős–Turán gives angular equidistribution, the root-product identity gives only \(O_\delta(\log n)\) roots away from the unit circle, and Haar measure pushed through the square-root and inverse Cayley maps is the standard Cauchy law on \(i\mathbb R\).

### Correctness sources

- assigned RESULT.md
- artifacts/verify_companion_discriminant.py
- Dilcher–Kim–Stolarsky primary paper
- classical Eneström–Kakeya and Erdős–Turán theorems

### Correctness risks

- The finite symbolic check is corroborative, not a proof for all \(n\).
- The stated zero regions are inclusions, not optimal regions.

## Originality — PASS

The primary Dilcher–Kim–Stolarsky paper gives the Cayley representation for \(p_n\), defines the companion family, and computes \(\operatorname{Disc}(p_n)\). Its discussion after Proposition 5.4 notes that no analogous small-prime-factor identity appears for the companion discriminant. Fresh Resultary and exact-formula searches found no prior closed form matching the audited \(\operatorname{Disc}(q_n)\), nor the combined Hurwitz/Cauchy-law theorem for these two families. The classical zero-location, discrepancy, resultant, and Möbius-covariance results are ingredients rather than prior implication of this family-specific package.

### equivalent_formulations

Searches:
- Resultary semantic search for the Chebyshev-like families, companion discriminant and Cauchy zero law
- exact search for the factor \(((n+2)^n+n^n)/2\) in a companion discriminant

Evidence:
- The audited record was the only exact published-finding match located.

Reasoning:
Equivalent forms in the \(u\)-plane, squared-Cayley \(w\)-plane, and original reciprocal-polynomial \(z\)-plane were compared.

### broader_coverage

Searches:
- Dilcher–Kim–Stolarsky arXiv:2607.16940
- classical Eneström–Kakeya and Erdős–Turán sources
- general discriminant covariance

Evidence:
- The source paper computes the other family's discriminant and provides the reduction ingredients, but does not state the audited companion formula or limit law.

Reasoning:
General resultant identities make the computation possible but do not mechanically tabulate this specialized closed form without carrying out the family-specific products.

### exact_database_or_table

Searches:
- current Resultary polynomial/discriminant findings and exact-formula web search

Evidence:
- No database/table entry containing the audited companion discriminant was located.

Reasoning:
The closed form is derived symbolically rather than read from an existing table.

### claim_vs_prior_implication

Searches:
- claim-versus-source implication comparison

Evidence:
- The primary source's formulas determine \(Q_n\), but the exact discriminant, left-half-plane theorem and Cauchy weak limit require additional derivations.

Reasoning:
Being computable from source definitions does not make these conclusions prior stated or mechanically immediate.

### source_inspections

- **Properties of two Chebyshev-like polynomial sequences** — https://arxiv.org/abs/2607.16940. Trigger: Primary source introducing both polynomial families. Material read: Public full-text material was inspected through the defining Cayley formula, companion recurrence, Section 5 discriminant calculation, and the comment immediately after Proposition 5.4. Method: Primary formula and theorem comparison. Assessment: NOT COVERING the audited companion formula or root-distribution theorem. Evidence: The source computes \(\operatorname{Disc}(p_n)\) and remarks on the lack of an analogous simple companion pattern.
- **Assigned exact discriminant verifier** — artifacts/verify_companion_discriminant.py. Trigger: Critical closed form. Material read: Complete source file. Method: Line-by-line inspection; it constructs the source polynomials and compares exact symbolic discriminants for \(1\le n\le6\). Assessment: Correct corroboration of the algebraic formula. Evidence: All exact checks are equality tests in symbolic arithmetic.

### checked_sources

- Dilcher–Kim–Stolarsky arXiv:2607.16940
- assigned RESULT.md and verifier
- Resultary semantic search
- classical zero-distribution/discriminant sources

### residual_risks

- Older general resultant literature could contain the same specialization under different notation; no such source was found.
- The source family is recent.

## Scientific value — PASS

An exact missing companion discriminant together with finite-degree stability geometry and a limiting zero law gives a coherent structural description of two newly introduced reciprocal polynomial families. The discriminant explains the source's observed arithmetic difference and the Cauchy limit gives a natural global asymptotic invariant.

### Value sources

- Dilcher–Kim–Stolarsky source problem
- assigned exact discriminant and root-geometry derivation

### Value risks

- No optimal finite-degree zero region or post-Cayley discrepancy rate is claimed.

## Limitations

- The Apollonius regions are inclusion bounds.
- The limiting statement is weak convergence only.
- Originality is best-of-knowledge; older general resultant formulas are a residual risk.

## Disposition

**PASSED**
