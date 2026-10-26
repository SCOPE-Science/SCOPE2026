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

# Verification
Run `python check.py` with Python 3 standard library. It evaluates the exact rational integrals for the second, fourth, and sixth Gaussian-mixture moments and draws 120,000 reproducible Gaussian matrices for sample second/fourth-moment comparisons. The expected exact moments are \(4/\pi\), \(16/\pi\), and \(112/\pi\). The finite simulation checks distributional plausibility only; the infinite moment formula is established by conditional Gaussian integration in RESULT.md. No independent audit has been performed.
