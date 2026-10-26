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

The accompanying `VERIFY.py` reconstructs the half-normal centered fourth moment and the rational lower-bound certificate, computes the leading constant using both a tail formula and an independently integrated absolute expectation, tests strict increase of 81 sampled profile values, integrates the exact pole kernel row in six finite dimensions up to 4096, and checks the exact reproducing-kernel identities against 180000 pseudorandom hemisphere samples in each of dimensions 4, 8 and 25. The script prints `all checks passed` when complete.

Execution: `python VERIFY.py`, requiring Python 3, NumPy, and SciPy. A successful run was observed against the packaged candidate. Exact symbolic rational checks supplement but do not replace the analytic monotonicity proof; numerical/Monte Carlo tests are not infinite-dimensional certificates. All steps needed for the theorem itself are explicitly proved in `RESULT.md`.

Scientific limitations: fixed polynomial degree one, normalized surface area, hemisphere opening angle exactly a half-sphere, and limit of increasing ambient dimension. Finite-dimensional exact pole optimality is not asserted. No external independent scientific audit or verification has been performed.
