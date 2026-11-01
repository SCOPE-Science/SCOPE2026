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

Run `python verify_john.py` from the directory containing this report and the standalone script. Expected output: `PASS: 464 configurations for normalized containment and all contact moments`.

The verifier samples integer dimensions \(2\) through \(30\) and sixteen deterministic/pseudorandom radius parameters per dimension, including the sharp threshold. It checks normalized inequalities, exact target contact-moment equations to numerical tolerance, and nonnegative weights. All-dimensional correctness follows separately from the algebraic argument in `RESULT.md`. The closest primary historical source, Güler–Gürtuna Section 8, was read in its accessible complete-text version; no independent historical-priority certification was performed.
