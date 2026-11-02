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

# Reproducibility and limits

`verify.py` uses Python, NumPy, SciPy and SymPy; run `python verify.py`. The attached `verification_run.txt` is the actual output from the completed run. The symbolic stage compares 81 rational grounded pseudoinverse traces against the analytic four-eigenspace formula and checks at least the stated positive spectral multiplicities. Numerical tests run 30 unrestricted per-edge SLSQP optimizations and 3,000 individually randomized budget-feasible asymmetric allocations, and check 48 ratios at or near the support transition. The algorithm verifies the objective only on finite instances and numerically selected test points; numerical optimization or random sampling cannot prove infinite-family optimality. The closed-form proof and strict convexity argument in `RESULT.md` establish the theorem. No independent mathematical audit has been performed.
