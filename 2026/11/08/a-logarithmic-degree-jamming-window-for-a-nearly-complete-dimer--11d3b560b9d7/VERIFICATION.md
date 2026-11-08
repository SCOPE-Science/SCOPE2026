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

- `python verify.py` completed from the standalone extracted file and reported `ALL CHECKS PASSED: 102`.
- For each even \(N\in\{4,6,8,10,12\}\), every exceptional degree is checked against a labeled-vertex Markov recursion and a separate exact permutation formula, using rational arithmetic.
- Twelve additional finite scaling-window checks use floating-point recursion only as diagnostics, never as a proof of the infinite limit.
- The proof supplies the exact recurrence, exact product representation, exact hazard expectation, a uniform finite-population variance estimate, and a uniform logarithmic correction estimate. These establish the stated limiting law for every degree sequence.
- The finite checks do not independently certify novelty, the absence of equivalent earlier results, or any graph family outside the hypotheses.
