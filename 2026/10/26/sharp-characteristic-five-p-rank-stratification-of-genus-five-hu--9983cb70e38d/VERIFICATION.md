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

# Reproducibility

From this bundle run `python3 checker.py` using Python 3 without external dependencies. The checker implements arithmetic in \(\mathbb F_{25}\) and prints `CHECK_OK` when the finite verification succeeds. The checker was run with all checks passing. It verifies the two roots of \(t^2-t+1\), three rank witnesses, and every ordered pair in the finite field; it does **not** establish the theorem for all algebraically closed extensions. That conclusion follows from the complete symbolic five-Hasse-numerator argument and the algebraic isogeny proof in `RESULT.md`.

The claimed \(5\)-rank classification is a self-reviewed mathematical result. Independent audit has not been performed. Previously published five-factor decompositions are credited and are not claimed as new.
