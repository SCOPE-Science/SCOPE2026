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

# Verification and reproducibility

`RESULT.md` gives analytic arguments for the global intrinsic-distance identity, extremal center, tail coefficients, inverse formulas and exact second moment. `check.py` performs independent high-order numerical integrations across 24 parameter combinations and checks 50,000 random sector configurations. It passed when executed with Python 3 and NumPy. These finite tests are corroboration and not substitutes for analytic statements covering all integers \(n\ge3\), all \(a>0\), and all \(h>0\).

The leading tail coefficient must be interpreted in original distance units, and the inverse problem uses the exact law; no sampled-data statistical performance is certified. Bibliographic noncoverage is only a best-knowledge self-review, not proof of absolute historical novelty.
