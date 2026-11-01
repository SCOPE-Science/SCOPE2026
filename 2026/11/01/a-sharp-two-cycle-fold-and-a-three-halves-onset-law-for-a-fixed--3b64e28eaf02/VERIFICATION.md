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

# Reproducibility and evidence

Run `python verify.py` using Python 3 and SymPy, with no data files. The program verifies the two-cycle elimination identity symbolically, the exact second derivative of the scalar fold curve, the positive degree-eight polynomial and its nine rational Bernstein coefficients, the leading three-halves onset constant, and six independently forward-iterated sample period-two points. It prints two distinct roots at each of three parameters: `(alpha,beta)=(0.1,1.35),(0.1,1.7),(0.1,1.85)`.

The symbolic polynomial certificate plus the analytical bounds in `RESULT.md` constitute the infinite proof. The finite forward-orbit checks are sanity tests and do not establish completeness or general stability. The code uses its own scalar root finder and checks the original two-dimensional map on each reconstructed point. The public-source date of March 9, 2023, and the defining equation were confirmed from the original open-access journal article. Publication-priority review does not constitute independent mathematical validation.
