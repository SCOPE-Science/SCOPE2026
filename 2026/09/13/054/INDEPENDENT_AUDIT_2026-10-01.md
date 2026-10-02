---
record_id: SCOPE-20260913-054
audit_date: 2026-10-01
disposition: passed
---

# Independent scientific audit

## Final claim

For the full log-unit lattices of the maximal real subfields \(K_16^+\) and \(K_32^+\), \(mu(Lambda_32)/sqrt(7)>mu(Lambda_16)/sqrt(3)\), with \(mu(Lambda_16)<=1.25675225\) and \(mu(Lambda_32)>=2.20\).

## Correctness — PASS

The interval certificate was inspected. Rank three exhausts relevant vectors and Voronoi triples; an independent reconstruction found 22 relevant vectors, 24 feasible vertices, and maximum \(q\) about \(1.5794261923\). Rank seven uses a hole of squared distance \(5.1669025993\) and a fail-closed interval-LDL decoder excluding every point within radius \(2.20\). The normalized bounds \(0.72558625\) and \(0.83152184\) are strictly separated.

## Originality — PASS

Closest literature gives general upper bounds for full cyclotomic log lattices, not this maximal-real-subfield upper/lower comparison.

### Equivalent formulations

**Searches.** maximal real cyclotomic log-unit covering radius

**Evidence.** Same invariant, different lattice objects.

**Reasoning.** No equivalent prior statement found.
### Broader coverage

**Searches.** de Araujo 2024; Punch 2026

**Evidence.** Both are upper-bound results for full cyclotomic fields.

**Reasoning.** They do not imply the rank-seven lower bound.
### Exact database or table

**Searches.** Punch 2026 Table 1 n=16; number-field labels; published Q16+ Q32+ search

**Evidence.** Punch's n=16 value concerns the full cyclotomic lattice.

**Reasoning.** No exact table covers this pair.
### Claim versus prior implication

**Searches.** general bounds versus audited lower/upper pair

**Evidence.** Upper bounds cannot imply the lower bound; the circular-unit index theorem identifies the lattice but not its covering radius.

**Reasoning.** No prior implication yields the strict inequality.

### Source inspections

- **An improved upper bound on the covering radius of the logarithmic lattice of Q(zeta_n)** (https://doi.org/10.1016/j.disc.2025.114909): Trigger — Closest current paper. Material read — Full accessible introduction, definitions, theorem comparison and Table 1. Method — Primary full-text inspection. Assessment — NOT_COVERING. Evidence — It treats full cyclotomic fields and general upper bounds.
- **An upper bound on the covering radius of the logarithmic lattice for cyclotomic number fields** (https://doi.org/10.1016/j.disc.2023.113665): Trigger — Immediate predecessor. Material read — The theorem as reproduced and corrected in the 2026 paper. Method — Cross-source theorem inspection. Assessment — NOT_COVERING. Evidence — No matching lower bound or exact real-subfield comparison.

### Checked sources

- https://doi.org/10.1016/j.disc.2025.114909
- https://doi.org/10.1016/j.disc.2023.113665
- https://arxiv.org/abs/2507.20544
- Sinnott circular-unit index theorem
- artifacts/cert_final.py
- artifacts/cert_summary.json
- artifacts/highprec_reference.py

### Residual risks

- Full-unit identification relies on cited class-number/index facts.
- RESULT.md has a stale `output/artifacts/` prefix; actual files are under `artifacts/`, corrected in METADATA.json.

## Scientific value — PASS

Covering radius is a natural active invariant of log-unit lattices; the consecutive power-of-two comparison is motivated and the strict normalized separation is reusable.

## Limitations

- The rank-seven lower bound is not claimed sharp.
- The stated Euclidean normalization is essential.

## Disposition

**PASSED**. Acceptance requires PASS on correctness, originality, and scientific value.
