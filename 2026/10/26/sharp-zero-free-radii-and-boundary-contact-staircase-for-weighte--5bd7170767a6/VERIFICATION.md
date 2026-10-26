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

# Reproducible checks and limits

The proof is self-contained in `RESULT.md`; no external formal prover or human audit was used. The script `checks/boundary_phase_check.py` uses SciPy bracketing to independently locate boundary zeros and compares them with the analytic integer count for selected weights and 150 deterministic random exponents. It also samples the zero-free circles and evaluates the local splitting coefficient. The required libraries are listed in `requirements.txt`, and its exact recorded stdout is embedded as `checks/boundary_phase_output.txt`.

The root search is finite and floating-point, so it does not independently certify the all-real parameter theorem, nonexistence of infinitely many other roots, or publication originality. At double contacts a small numerical root-splitting artifact may occur; the checker explicitly merges numerical duplicates before comparison. The analytic monotonicity and extremum arguments supply the infinite case.
