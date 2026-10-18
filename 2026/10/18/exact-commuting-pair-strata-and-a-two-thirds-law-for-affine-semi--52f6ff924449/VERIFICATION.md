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

# Reproducibility checks

Run `python verify.py` with Python 3 and no external dependencies. The program constructs finite fields of sizes 2, 3, 4, 5, 7, 9, enumerates all matrices of dimensions 1–3 in fourteen configurations, tests the cubic matrix identity, computes ranks by field-aware Gaussian elimination, and compares full weighted strata against the exact three-case formulas in `RESULT.md`.

Seven configurations additionally enumerate every permitted affine translation vector and all ordered input pairs, checking both the semisymmetry equation and each operation's predicted number of commuting pairs without relying on the general proof.

The recorded clean execution printed `VERIFY_OK: 14 exhaustive matrix strata and 7 direct quasigroup-identity checks`. These are finite checks, not a proof of the general rank classification or asymptotic claims. Those claims rely on the centralizer analysis and discrete-Gaussian estimate supplied in `RESULT.md`. No independent audit has been performed.
