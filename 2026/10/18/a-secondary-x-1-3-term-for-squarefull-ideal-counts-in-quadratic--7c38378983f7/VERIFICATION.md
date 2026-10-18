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
Run `python3 check.py` from the package directory. It checks exactly five rational-integer cutoffs, counting squarefull ideals of the Gaussian integers by two independent finite formulas. A successful finite check does not establish an asymptotic expansion.

The infinite argument is the proof in RESULT.md: quadratic ideal count; squarefree Möbius convolution; two partial summations; exact square-cube decomposition; and cancellation of the three intermediate hyperbola terms. The classical ideal-counting input is a standard theorem and can also be derived from the quadratic Dirichlet character. Independent external audit has not been performed.
