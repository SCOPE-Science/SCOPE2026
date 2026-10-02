# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-fb793a108374`

## Correctness — PASS

The lifting lemma is exact: moving from cycle layer zero to path layer \(i\) adds the same integer to all three landmark distances, so code collisions require equal gap codes; a height separation of at least \(q\) cannot be cancelled by path-coordinate differences at most \(m-1\) when \(m\le q\). For each parity/residue family, landmarks and antipodes partition the cycle into at most six affine pieces; solving equality of the two affine gap coordinates gives the listed repeated pairs and their height separations, establishing q-separation for all q, not merely the finite tested range. The four boundary families are analogous. The exact-integer verifier was read completely and correctly corroborates all twelve tail cases through q=500 and direct cylinder codes through m=30. The standard lower bound three applies because the cylinders are connected nonpaths and multiset dimension two is impossible.

### Correctness sources

- assigned RESULT.md
- artifacts/verify.py and verification.txt
- Marcelo–Tolentino–Garciano–Buot 2025 cylindrical theorem
- earlier 2026-09-18 mod-four SCOPE theorem

### Correctness risks

- The twelve affine interval calculations are elementary but lengthy; finite verification is only corroboration.
- The theorem is sufficient-range, not a complete classification below the boundary.

## Originality — PASS

The 2025 primary cylindrical paper proves the uniform three-landmark region only for \(n\ge8m+1\) and explicitly leaves remaining cases open. An earlier 2026-09-18 SCOPE theorem reaches the \(6m\) scale only on the congruence class \(n\equiv2\pmod4\) using an antipodal triple. It does not imply the present all-residue tail \(n\ge6m+3\) or the parity-dependent boundary families. Fresh Resultary searches found no broader theorem covering those ranges.

### equivalent_formulations

Searches:
- Resultary search for cylindrical multiset dimension at the 6m scale
- direct comparison with the earlier mod-four theorem
- primary 2025 cylindrical paper

Evidence:
- The earlier SCOPE theorem is confined to one congruence class.
- The primary paper's Theorem 3.5 uses the 8m+1 range and its conclusion leaves the rest open.

Reasoning:
The present q-separated criterion permits repeated gap codes with large translation separation, a strictly more flexible construction than global strong separation.

### broader_coverage

Searches:
- 2025 cylindrical theorem
- 2025 prism classification
- 2026 mod-four SCOPE theorem

Evidence:
- The prism slice and one mod-four family are prior coverage, but the general six-residue construction is not.

Reasoning:
Prior special cases are credited and do not dominate the full final theorem.

### exact_database_or_table

Searches:
- current Resultary multiset-dimension records and exact prism literature

Evidence:
- No table/database contains the general all-q residue families.

Reasoning:
The infinite theorem is proved by affine collision classification rather than table lookup.

### claim_vs_prior_implication

Searches:
- claim-versus-earlier-mod-four implication comparison

Evidence:
- The older theorem proves \(n\equiv2\pmod4\), \(n\ge6m\); many values in the current \(n\ge6m+3\) tail lie outside that congruence class.

Reasoning:
Neither statement implies the other wholesale; the current theorem has genuinely broader circumference coverage while crediting the overlap.

### source_inspections

- **On multiset dimension of cylindrical graphs** — https://doi.org/10.61091/jcmcc126-15. Trigger: Primary predecessor for cylindrical grids. Material read: Full accessible article text, including the Cartesian-product lifting setup, Theorem 3.5 with the \(8m+1\) range, and the concluding open cases. Method: Primary full-text theorem comparison. Assessment: NOT COVERING the 6m-scale all-residue theorem. Evidence: The paper proves the older sufficient range and explicitly leaves remaining cylindrical cases open.
- **Multiset dimension three for a mod-four family of cylindrical graphs** — 2026/09/18/SCOPE-multiset-dimension-three-cylinders-mod-four--18703d594a7d. Trigger: Closest earlier SCOPE theorem. Material read: Complete RESULT.md. Method: Full statement and construction comparison. Assessment: PARTIAL COVERAGE only. Evidence: It gives an antipodal construction for \(n\equiv2\pmod4\), not the six-residue tail or four new boundary families.
- **Assigned cylinder verifier** — artifacts/verify.py. Trigger: Exact repeated-gap and resolving-code checks. Material read: Complete source and saved output. Method: Line-by-line inspection. Assessment: Correct supporting computation. Evidence: It checks 2994 tail constructions, 998 boundary constructions, and 406 direct cylinder instances.

### checked_sources

- 2025 cylindrical primary paper
- earlier 2026-09-18 mod-four SCOPE theorem
- 2025 prism result
- assigned RESULT.md and verifier
- fresh Resultary search

### residual_risks

- Differently phrased older ID-coloring work remains a residual risk, but no plausible covering source was identified.

## Scientific value — PASS

Lowering the general sufficient circumference coefficient from eight to six and covering every residue class is a substantive structural improvement. The q-separated lifting criterion is reusable: it explains exactly how finite path height can absorb repeated cycle gap codes and yields explicit parity-dependent boundary families.

### Value sources

- published 8m+1 theorem
- earlier 6m mod-four special case
- audited q-separated six-residue construction

### Value risks

- The exact transition for all smaller \((m,n)\) remains open.

## Limitations

- The theorem is a sufficient-region result, not a full classification.
- The m=2 prism cases are prior work.
- Finite verification supports but does not replace the all-q affine collision proof.

## Disposition

**PASSED**
