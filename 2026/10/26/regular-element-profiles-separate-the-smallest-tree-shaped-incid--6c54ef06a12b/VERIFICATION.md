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

## Reproducible finite-field tests

`python3 verify.py` constructs the two finite-dimensional incidence-algebra products directly from the three strict comparabilities. It tests the existence of an inner inverse by solving the linear system associated to the map \(b\mapsto aba\), with no use of the proposed diagonal-zero criterion. It separately enumerates all idempotents and all ordered commuting-idempotent pairs. For all elements over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), it matches the exact induced-edge formula and the difference \(q(q-1)^3\). The output marker is `VERIFY_OK_INCIDENCE_REGULARITY_SEPARATION`.

This checks finite instances only. The theorem for every finite height-two poset and every finite field, the subgraph expansion, and the large-field asymptotic are established by the written algebraic and inclusion-exclusion arguments, not by finite enumeration. The comparison of earlier literature does not constitute independent mathematical validation.
