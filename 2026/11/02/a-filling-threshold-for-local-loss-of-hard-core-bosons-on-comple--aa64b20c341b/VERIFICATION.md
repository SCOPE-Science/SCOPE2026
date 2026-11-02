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

The reproducible verifier is `verification/check_capture.py`; its recorded output is `verification/output.txt`.

Run with Python 3 and installed NumPy and SciPy:

```bash
OPENBLAS_NUM_THREADS=1 python verification/check_capture.py
```

The code independently constructs occupation-basis Hamiltonians for both particle statistics, computes spectral projector overlaps for 66 cases covering \(4\le N\le9\), and compares them with the analytic dark dimensions. It then evaluates 48 finite-time no-jump traces at time \(t=600\) for two distinct loss strengths, with maximum residual below \(1.1\times10^{-13}\). Those finite cases are supplementary tests. The full-integer proof is the Boolean-lattice commutator and exterior-power argument in `RESULT.md`.

A no-jump survival probability is not a mean first-jump time; the statement applies to the eventual occurrence of the first event, not a complete counting-process distribution. Independent scientific audit has not been performed.
