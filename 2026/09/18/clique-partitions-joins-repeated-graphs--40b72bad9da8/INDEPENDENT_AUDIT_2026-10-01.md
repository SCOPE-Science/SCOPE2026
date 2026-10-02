---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

If each side contains at least the edge-chromatic number of a finite graph H, then the Erdős–Faudree–Ordman cut lower bound is attained exactly for the clique partition number of the join of a disjoint copies of H with b disjoint copies of H; for complete H this yields the stated asymmetric parity-free partition, covering, and spread formulas.

## Correctness — PASS

The cut lower bound specializes to \(abv^2-(a+b+\min\{a,b\})m\). Assuming \(a\le b\), a proper edge-colouring of H partitions its edges into at most a matchings. Pairing equal-colour edges across the first a copy pairs produces edge-disjoint 4-cliques that cover each internal edge once; for each excess copy, triangles anchored in distinct A-copies cover its internal edges without cross-edge collisions. Remaining cross edges are singleton 2-cliques, and the count equals the lower bound. The inspected construction verifier independently checks representative paths, cycles, and complete graphs.

**Checked sources.** Assigned RESULT.md at tree a838136e8f910e9fdf0f54256f51319778a60974; artifacts/verify_construction.py blob 162a2b45df96499a1f31607cd6eeb2ea106bac9b; Erdős–Faudree–Ordman 1988; Rohatgi–Urschel–Wellens 2021; Ning 2026

**Residual risks.** The theorem makes no necessity claim outside the chromatic-index regime.

## Originality — PASS

The classical cut inequality supplies only the lower bound, the 2021 result supplies a one-sided join mechanism, and Ning's recent construction treats a more special balanced complete-cluster family. Searches found no prior two-sided repeated-arbitrary-H equality theorem or the asymmetric parity-free complete-cluster corollary.

### Equivalent formulations

These are the natural equivalent formulations; none inspected states the arbitrary repeated-H equality.

### Broader coverage

None of the broader results alone implies the two-sided arbitrary-H construction because simultaneous packing of both sides' internal edges requires the new coordinated matching layer.

### Exact database or table

Database/table comparison is inapplicable to an all-graphs symbolic theorem, except as small-instance checking.

### Claim versus prior implication

The prior implications stop short of the exact equality for arbitrary H; the construction is the additional theorem.

**Checked sources.** https://www.renyi.hu/~p_erdos/1988-04.pdf; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i4p53/pdf/; https://arxiv.org/abs/2609.20305; semantic published-results search

**Residual risks.** Very recent or poorly indexed equivalent formulations remain possible. The exact relevant theorem text in Ning was not fully extracted by the web interface in this run; the assigned package states the specialization and the public abstract confirms the paper's scope.

## Value — PASS

The theorem identifies chromatic index as a general mechanism for equality in a classical cut bound and extends a current extremal construction from complete clusters to arbitrary repeated graphs. The complete-graph corollary yields a natural asymmetric parity-free exact family, so the contribution is structurally motivated.

**Residual risks.** The global extremal deficit order is not improved and the threshold may not be necessary.

## Limitations

- The chromatic-index threshold is sufficient, not claimed necessary.
- For arbitrary H the theorem determines the clique partition number only; the covering and spread formulas are additionally proved for complete H.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
