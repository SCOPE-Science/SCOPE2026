# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-bbf7e58277be`

## Correctness — PASS

Mayeli's full primary paper was inspected through the exact trace-defect identity, the three-regime upper theorem, the discretization estimates, and Remark 9.4. The alternating-gap Cantor coloring in the audited proof has boundary-neighborhood size \(O(h^	heta)\) and a matching translation lower bound at every sufficiently small scale. Parseval turns that into a uniform lower bound for Fourier energy on every multiplicative annulus. The cell approximation transfers the spatial translation law to lattice symmetric differences. In the exact nonnegative trace identity, summing disjoint annuli gives \(N^{d-	heta}\log N\) on the fractional critical line; terminal-scale or fixed-mode terms give the two off-critical powers. The tensor-product construction contributes exactly \(N^{d-1}\). These lower bounds match Mayeli's upper powers.

### Correctness sources

- assigned RESULT.md
- Mayeli, arXiv:2609.12226 full text
- same-day off-critical Resultary theorem
- independent parameter checks of the Cantor construction

### Correctness risks

- The theorem gives growth-rate sharpness, not leading constants.
- The examples are disconnected self-similar sets rather than connected smooth domains.

## Originality — PASS

A same-day published theorem already settles both off-critical powers along explicit lacunary scales, so those clauses alone are not originality-bearing. Mayeli's full paper explicitly leaves the fractional critical line \(0<\gamma=\eta<1\) open and treats its Cantor experiments as numerical evidence. Fresh searches found no other theorem proving the critical logarithm for every fractional exponent. The audited result survives because its all-scale alternating-gap construction closes that open critical line and simultaneously yields a unified matching family.

### equivalent_formulations

Searches:
- Resultary searches for fractional critical trace-defect logarithmic sharpness, off-critical power sharpness, Cantor translation moduli, and Fourier shell energy
- full-text comparison with Mayeli Remark 9.4

Evidence:
- A same-day record covers off-critical powers only and explicitly excludes the critical line.
- Mayeli states the fractional critical logarithm as open.

Reasoning:
Equivalent formulations via translation moduli, annular Fourier mass, and the exact trace-defect sum were compared.

### broader_coverage

Searches:
- Mayeli arXiv:2609.12226 full text
- same-day `SCOPE-sharp-off-critical-discrete-fourier-trace-defect--dc7870b56a90`
- Marceca–Romero–Speckbacher 2024 concentration estimates

Evidence:
- The same-day theorem proves off-critical powers but says the fractional critical problem is not addressed.
- The earlier continuous concentration literature uses different regularity hypotheses and does not imply the audited all-fractional critical logarithm.

Reasoning:
The final theorem's critical line is strictly outside the coverage of the identified same-day off-critical result.

### exact_database_or_table

Searches:
- current Resultary trace-defect findings
- Mayeli numerical Section 10

Evidence:
- The source has numerical scaling tables, not a proof; no database/table result supplies the required infinite lower bound.

Reasoning:
Finite numerical scaling cannot establish the critical asymptotic.

### claim_vs_prior_implication

Searches:
- claim comparison with the off-critical sharpness theorem and Mayeli's endpoint box example

Evidence:
- Prior current coverage gives \(\gamma
e\eta\) and Mayeli gives only \(\gamma=\eta=1\); neither implies any fractional \(\gamma=\eta\in(0,1)\) case.

Reasoning:
The audited critical theorem fills the exact missing region in the phase diagram.

### source_inspections

- **Trace-defect bounds for discrete Fourier concentration operators** — https://arxiv.org/abs/2609.12226. Trigger: Direct source of the upper bounds and open sharpness questions. Material read: Full primary paper through Theorems 2.1–2.2, Proposition 4.1, Sections 5–10, Remark 9.4, and numerical fractal tests. Method: Primary full-text theorem/proof comparison. Assessment: NOT COVERING the fractional critical logarithmic lower bound. Evidence: Remark 9.4 explicitly leaves every \(0<\gamma=\eta<1\) critical logarithm and both off-critical powers open.
- **Sharp off-critical powers for discrete Fourier trace defects** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-sharp-off-critical-discrete-fourier-trace-defect--dc7870b56a90. Trigger: Closest current same-day sharpness theorem. Material read: Complete RESULT.md. Method: Full statement and proof comparison. Assessment: PARTIAL COVERAGE only. Evidence: It settles \(\gamma
e\eta\) along lacunary scales and explicitly says the fractional critical line is not addressed.

### checked_sources

- Mayeli arXiv:2609.12226 full text
- same-day off-critical Resultary theorem
- Marceca–Romero–Speckbacher 2024 context
- current Resultary critical-line searches
- assigned RESULT.md

### residual_risks

- Because Mayeli's source is very recent, unindexed concurrent work remains possible.
- No leading constant or plunge-profile sharpness is claimed.

## Scientific value — PASS

The surviving critical-line theorem closes the principal fractional sharpness question explicitly left open by the direct source, and the proof isolates a reusable mechanism converting two-sided translation roughness into annular Fourier energy and discrete trace lower bounds. That is a natural phase-boundary result, not merely another numerical example.

### Value sources

- Mayeli Remark 9.4
- audited fractional critical construction
- same-day off-critical comparison

### Value risks

- The theorem does not determine leading constants or eigenvalue-threshold profiles.

## Limitations

- The off-critical clauses are already covered by a same-day theorem; originality rests primarily on the fractional critical logarithmic line and unified all-scale construction.
- No leading constants are claimed.
- Very recent concurrent work remains a residual risk.

## Disposition

**PASSED**
