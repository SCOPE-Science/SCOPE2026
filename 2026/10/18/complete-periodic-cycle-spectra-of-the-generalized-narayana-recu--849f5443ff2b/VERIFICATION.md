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

The general proof is given in `RESULT.md` and relies on 2-adic Hensel splitting and matrix lifting; finite tests are not treated as a substitute for this reasoning. Run `python3 verify.py` to reconstruct two exact odd-coefficient lifting checks and exhaustively compare all functional digraphs for twelve coefficients at exponents one through four. The checker prints `VERIFY_OK` when successful. The claimed transient cardinality is checked in these enumerated cases; no finite test asserts a universal upper bound on individual transients.
