---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"passed"}
---

# Independent mathematical audit

## Final claim

Every rank-5 paving matroid on n>=12 points whose nonbases are Johnson-stable has a U_{2,5} minor.

## Correctness — PASS

The proof is self-contained. Contracting any 3-set C gives a loopless rank-2 matroid. Two remaining points are parallel exactly when C together with them is a nonbasis. Johnson stability makes this pair graph a matching; on n-3>=9 vertices such a matching has an independent 5-set, whose restriction is U_{2,5}. No finite experiment is needed for the theorem.

Checked sources: RESULT.md proof; artifacts/verify_disproof.py (blob 9a33a80633875051a40c63dd4b62c66f8bc46a01) as illustration only

Residual risks: The bound n>=12 is sharp for this matching-independence argument, not asserted to classify all n<=11 cases.

## Originality — PASS

The inspected sparse-paving literature identifies Johnson-graph stable sets with sparse paving matroids and proves broad asymptotic uniform-minor phenomena, but it does not state this exact rank-5 all-n>=12 matching-contraction obstruction.

### Equivalent formulations

That encoding matches the hypothesis but does not itself contain the contraction lemma. Evidence: Published sparse-paving work uses stable sets of Johnson graphs as the standard encoding.

### Broader coverage

An asymptotic almost-all statement does not imply the exact theorem for every Johnson-stable rank-5 paving matroid on n>=12. Evidence: The inspected work gives asymptotic statements about fixed uniform minors in sparse paving matroids.

### Exact database or table

The proof is theorem-level and not a recomputation of a known finite table. Evidence: No exact census/table covering all n>=12 was found.

### Claim versus prior implication

The inspected prior results do not mechanically imply the all-n>=12 conclusion. Evidence: The stable-set correspondence supplies terminology; the exact forced-minor implication requires the new matching argument.

### Source inspections

- **On the number of matroids compared to the number of sparse paving matroids** — https://arxiv.org/abs/1411.0935. Trigger: Primary sparse-paving source using Johnson graph stable sets and uniform-minor context. Material read: Stable-set correspondence and the relevant uniform-minor discussion. Method: Primary full-text inspection. Assessment: NOT_COVERING. Evidence: The source gives the Johnson-stable encoding and asymptotic context, not the exact rank-5 n>=12 theorem.

Checked sources: https://arxiv.org/abs/1411.0935

Residual risks: An older specialized excluded-minor lemma under different language could overlap; no such result was located.

## Scientific value — PASS

The matching-contraction lemma is a concise structural obstruction that rules out an entire proposed infinite sparse-paving construction regime and directly links a natural Johnson-stability condition to a fixed excluded uniform minor. This is a motivated reusable structural fact rather than an arbitrary finite computation.

Checked sources: excluded-uniform-minor context; sparse-paving/Johnson stable-set literature

Residual risks: The theorem deliberately says nothing about non-Johnson-stable or n<=11 cases.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and scientific value.
