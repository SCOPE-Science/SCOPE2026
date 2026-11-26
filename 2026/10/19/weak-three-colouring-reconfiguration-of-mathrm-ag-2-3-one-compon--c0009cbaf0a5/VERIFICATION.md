---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite strict-endpoint check

Run `python3 verify_strict_distances.py` from the package directory. The program constructs the weak graph without quotienting by any symmetry and computes one strict root's distances to all reachable states. The theorem's symmetry argument establishes transitivity on strict roots. At distances 4 through 10 the strict root counts are 32, 22, 16, 80, 8, 1, 2; the two distance-ten endpoints are cyclic palette permutations of the root. This certifies the bounded strict-endpoint distances together with the transitivity proof; no general affine-plane metric is inferred.
