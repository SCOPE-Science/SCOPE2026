---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytic certificate is the basis calculation in RESULT.md, which proves the exact torsion identity for every field of characteristic different from two; scalar extension yields the general form case. The finite-field count is obtained by the direct count of nonzero vectors on the smooth quadratic cone and the uniqueness of rank-one tensor factorizations up to nonzero scaling.

`verify.py` uses only the Python 3 standard library. It tests every nonzero pair of vectors \((u,f)\) over the prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7\). For each pair, it computes the torsion both directly and through the claimed rank-one expansion on the three basis pairs; it verifies the admissible-covector count for each fixed \(u\), and checks the total and trace-stratified counts. The output terminates with `SL2_RANKONE_NIJENHUIS_OK` on success.

The experiments do not check all prime powers, prove the descent argument, or establish novelty. Those assertions rely respectively on the proof and the bounded literature comparison. No independent audit has been performed.
