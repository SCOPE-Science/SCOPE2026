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

# Reproduction and limits

Execute `python3 verify.py` using Python 3 (arbitrary-precision integers). Success prints `CERT_OK` after checking every strict inequality; the program's optional rounded printed margins do not enter any assertion. The coefficient matrices are represented as literal exact integers. Exponential Taylor truncation is controlled by a separately checked factorial tail bound, not by heuristics. Componentwise comparison with a positive integer vector gives spectral bounds by Perron–Frobenius/Collatz–Wielandt.

The program verifies the specific three-patch witness. The general lower bound on patch number is a mathematical reduction to the published symmetric-migration monotonicity theorem; it is not a finite-enumeration inference. The work establishes neither global optimization of the period nor a classification of all three-patch interactions. No independent audit has been performed.
