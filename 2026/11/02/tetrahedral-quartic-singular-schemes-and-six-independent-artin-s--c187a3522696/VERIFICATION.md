---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Verification and reproducibility

The exact universal proof is in `RESULT.md`. It identifies the six relative edge divisors from the Jacobian ideal, proves the completed edge-preserving equation over the completed coefficient base, and determines fibre types from that equation and the simple-root case.

The standalone `python3 verify_tetrahedral.py` reproduces the support test for all 64 binary mixed-coefficient patterns at \(b_i=1\) over \(\mathbf P^3(\mathbb F_4)\). It also runs supplementary trace tests over \(\mathbb F_4,\mathbb F_8,\mathbb F_{16}\) retained for reproducibility of the arithmetic context. The success marker is `TETRAHEDRAL_CHAR2_64_SURFACES_4028_TRACE_CASES_PASS`. These finite tests do not establish the formal local or universal flatness statements.
