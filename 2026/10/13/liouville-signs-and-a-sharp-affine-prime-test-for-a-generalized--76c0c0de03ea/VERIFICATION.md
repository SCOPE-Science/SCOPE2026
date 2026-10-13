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

# Reproducible checks
Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier calculates the original floor recurrence, a separate proper-divisor recurrence, and inclusion-exclusion counts for ordered nontrivial squarefree factorizations. It performs exact equality comparisons for the declared index and slope ranges and checks both transition counterexamples, coefficient positivity, and the leading and trailing coefficients. Output is recorded in `verify_output.txt` and is reproducible by executing the packaged source.

The program is a finite consistency test; the theorem for all indices is established algebraically by the argument in `RESULT.md`. No independent audit has been performed.
