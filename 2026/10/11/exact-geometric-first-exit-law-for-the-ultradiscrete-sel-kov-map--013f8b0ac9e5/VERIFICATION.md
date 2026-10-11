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

# Reproducible verification

Use Python 3 with only the standard library. From the directory containing `RESULT.md`, run `python verification/check.py`. The script's expected final line is `EXACT_SELVKOV_SURVIVOR_CERTIFICATE_OK`.

This checks the exact matrix identity, branch-condition row vectors, bounded seven-vertex polygon, all seven rational vertices, rational shoelace area, and the inverse-image identities and area law through thirteen consecutive n values starting at n=6. It also checks three positive rational parameter scalings and the first-coordinate half-plane test against direct piecewise-map iteration at several rational initial conditions.

**Scope of verification:** Finite checked cases do not prove the theorem for all time. The proof for arbitrary \(n\ge6\), the exact probability distribution and the unique infinite survivor follow from the symbolic matrix identity, half-plane redundancy and determinant-induction arguments given in `RESULT.md`. Independent audit has not been performed.
