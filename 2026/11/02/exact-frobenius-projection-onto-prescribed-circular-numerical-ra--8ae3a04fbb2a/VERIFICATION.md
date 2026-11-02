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

# Reproducibility and proof checks

The standalone `verify.py` uses Python 3.9+ standard library only. Run `python3 verify.py` from the directory holding this file and `RESULT.md`. On the reviewed package, it reported 1,386 exact rational tests of the trace-free matrix identities and 32,810 deterministic complex-input and candidate-comparison checks, all passing.

The proof covers every complex \(2\times2\) input, every complex disk center, and every positive disk radius. The computation checks a finite subset of cases and does not establish the universal theorem by itself. The essential mathematical steps are the full support-function characterization of circular numerical ranges in dimension two, orthogonality of a top singular pair for traceless matrices, attainment of the global Frobenius bound, and equality-case classification.

This is a mathematical proof with reproducibility checks, not an external certification. No independent audit has been performed, and historical priority is not conclusively established.
