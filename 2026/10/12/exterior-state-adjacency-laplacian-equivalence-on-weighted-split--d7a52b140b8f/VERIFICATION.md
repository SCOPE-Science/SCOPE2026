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
# Verification record

The mathematical proof is a symbolic two-class decomposition, explicit matrix exponentiation, and a two-branch amplitude comparison. This document records supplementary finite tests, not an infinite certificate.

Execute `python verify.py` with Python 3 and NumPy. The script constructs the actual symmetric adjacency and signed weighted Laplacian matrices from their edge definitions. It compares all exterior-start probabilities at six nonzero times and across 151 matching class-size and weight profiles (121,212 scalar entries); the largest floating-point absolute discrepancy in the recorded run was \(1.665\times10^{-14}\). Nonmatching cases exhibit positive differences. It separately verifies the key fourth-order polynomial identity exactly over rational arithmetic for 1,980 choices, including vanishing clique weights and singleton boundaries. Nine unit-weight nonregular examples also confirm a center-start exclusion that is outside the theorem's assertion.

The unconditional, unrestricted statement relies on the proof in `RESULT.md`. Numerical agreement may reflect numerical error; finite samples alone cannot establish all-time equivalence or impossibility outside sampled profiles. The code is an independently constructible computational cross-check, not an independent scientific audit.
