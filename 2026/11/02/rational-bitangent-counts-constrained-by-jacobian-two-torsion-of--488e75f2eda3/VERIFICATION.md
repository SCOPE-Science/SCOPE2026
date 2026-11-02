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

# Computational verification

Both independent enumerators run from the embedded sources, without relying on outputs from prior executions. The first enumerates all symplectic bases, the second generates the group with transvections; the two tables and the eighteen witnesses are embedded. The standalone Python replay checks every witness against all sixty-four vectors and all 4096 ordered symplectic pair tests, then recompiles and reruns both enumerators. It requires `python3` and a standard C compiler providing `cc`.

The complete group order is 1,451,520, there are 28 odd refinements, the table has eighteen nonzero entries, and its multiplicities sum to the group order. All code checks are finite and exhaustive over the abstract group, not over the family of all plane quartics. The general geometric reduction is supplied in RESULT.md; finite-field realizability of abstract matrix classes is not established.
