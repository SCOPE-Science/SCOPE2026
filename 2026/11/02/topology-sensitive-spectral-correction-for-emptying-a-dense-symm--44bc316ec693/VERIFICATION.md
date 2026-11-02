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

Run `python verify.py` with Python 3, NumPy and SciPy. The script constructs the full occupation-state Markov generator independently, computes its killed restriction, verifies product detailed balance, solves the exact hitting-time linear system, compares the principal eigenvalue with \(q^N(1-q)(1-qT_G)\), checks path Fibonacci and star Schur values, and tests scaled survival against an exponential distribution. Test tolerances are specified in the script. The saved local execution reported **PASS: 221 deterministic graph, Green, stationary, mean, spectral and survival checks**.

The theorem for arbitrary finite connected graphs and all positive moments is proved analytically in `RESULT.md`; matrix checks at finite sizes neither establish nor replace that proof. The comparison to published literature identifies a possible implicit-coverage risk from the known restricted generator. Independent review has not been performed.
