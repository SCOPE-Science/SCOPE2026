---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"passed"}
---

# Independent mathematical audit

## Final claim

The Cayley graph of SL(3,Z) on E12^±1,E21^±1,E23^±1,E32^±1 has ordinary chromatic number 3, and no proper 7-color rule depending only on the radius-1 Bernoulli pattern exists for the associated free-part shift graph.

## Correctness — PASS

Exact integer matrix multiplication verifies the odd length-9 identity word, so the Cayley graph is not bipartite. Independent closure modulo 2 has 168 elements, and an independently verified proper 3-coloring of that quotient pulls back to the full Cayley graph. For the radius-1 statement, every generator has overlap size 2 and a 64-pattern compatibility clique. The finite compatible cylinders are realized in the free shift because the free part is dense in every nonempty cylinder for an infinite group, completing the local-rule implication.

Checked sources: artifacts/gen_check.py (blob 50a974521bed0bcd30d335227b118f02409d9d5d); artifacts/quotient_exact_chi3.py (blob 2417d4487b5416e5fed05184ac4a5573c0dcc6ec); artifacts/fallback_radius1_clique.py (blob e729961e051a8a35567cfdb7aaa74c5494d9991d); independent mod-2 closure and coloring check

Residual risks: The result is ordinary chromatic number only; it does not establish the measurable or Borel chromatic number.; The local obstruction is only for radius-1 rules.

## Originality — PASS

No inspected source gives this exact elementary-generator Cayley graph value or the radius-1 pattern obstruction. The closest Cayley-coloring literature treats other group classes, while general descriptive-set-theoretic bounds do not calculate this graph.

### Equivalent formulations

Ordinary Cayley coloring and finite local-rule obstruction were both searched under their natural aliases. Evidence: No equivalent exact result for this generating set was located.

### Broader coverage

Neither source implies ordinary chi=3 for this SL(3,Z) generating set or the radius-1 7-color no-go. Evidence: The inspected minimal-Cayley work emphasizes other classes such as nilpotent/generalized-dihedral settings; the Borel degree bound is only a general upper bound.

### Exact database or table

The 168-vertex quotient certificate is not a recomputation of a located published table. Evidence: No exact quotient/coloring table for this graph was found.

### Claim versus prior implication

The package uses graph-specific algebra and a graph-specific quotient coloring. Evidence: General bounds leave the exact ordinary value and local pattern obstruction undetermined.

### Source inspections

- **Coloring minimal Cayley graphs** — https://arxiv.org/abs/2405.19543. Trigger: Closest modern source on exact chromatic behavior of natural Cayley graphs. Material read: Scope and principal group classes/results. Method: Primary full-text inspection. Assessment: NOT_COVERING. Evidence: The inspected results do not state the SL(3,Z) elementary-generator value or this radius-1 local obstruction.

Checked sources: https://arxiv.org/abs/2405.19543; Kechris-Solecki-Todorcevic general Borel coloring bound

Residual risks: A specialized group-theoretic source may contain an equivalent coloring under a different generating-set description.

## Scientific value — PASS

The elementary matrices form a standard natural generating set for SL(3,Z). Its exact ordinary chromatic number is a natural invariant, and the radius-1 no-go is a concrete search boundary for the associated shift graph. Both facts directly calibrate the broader measurable/Borel coloring problem without claiming to solve it.

Checked sources: natural elementary generation of SL(3,Z); descriptive graph coloring context

Residual risks: The local-rule obstruction should not be interpreted as evidence against larger-radius or nonlocal Borel colorings.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and scientific value.
