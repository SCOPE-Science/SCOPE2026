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

# Finite reproducibility checks

Execute `python verify_directional_crown.py` using Python 3.10 or later without any nonstandard packages. The program builds the exact shortest-path response relation, enumerates all feedback vectors, and solves the finite adversarial belief-set reachability game for \(n=3,4,5,6\), checking the minimum cop numbers \(2,3,4,5\). This is an exhaustive **finite** test for those cases, not an exhaustive proof for all \(n\).

The same program separately verifies the upper-policy responses and invariant evasion witness for \(n=5,6,7\). The general proof in `RESULT.md` is an elementary argument applying to every integer \(n\ge5\). The tested code path and its resulting messages must be verified by executing the bundled program; no external certificate is claimed.

The bibliographic comparison uses arXiv:2609.01745v1 (first public date 2026-09-01), the published cube record, and targeted searches of aliases and related invariants. Not every later section of the original 2026 article was available in full, leaving residual originality risk. Independent audit remains unperformed.
