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

# Reproducibility and proof limits

The standalone `verify.py` uses SymPy and mpmath and requires only an ordinary Python installation with those packages. Run `python verify.py` from the directory containing this file and the script. It successfully verified the exact rational-parameter cumulative-ratio derivative, the algebraic quartic threshold and its positive root, both rank-reversal threshold inequalities, the analytic witness sign at \(t=2\), and four positive crossover times to high precision. It also completed 160 reproducible seeded strictly admissible parameter cases checking the strict ordering of thresholds and local monotonicity at both minima. The script uses no external network or private data.

The universal classification is proved analytically in `RESULT.md`. The sample is not an exhaustive numerical census and cannot establish infinitely many parameter cases; arbitrary-precision root finding is used as a consistency check, not an independent certification. The quartic root count is justified symbolically through the sign-change argument in the proof. External mathematical audit has not been performed.
