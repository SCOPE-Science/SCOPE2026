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

The embedded `verify_voter_reset.py` constructs full Markov generators for 20 even-ring stationary instances and compares site means and two-site functions to the analytic formula to tolerance \(3\times10^{-10}\). The runs cover \(N\in\{4,6,8,10\}\) and reset rates \(0.07,0.4,1,3,13\). It also checks 1,500 substituted second-order recurrence equations, 80 opposite-side sign predictions for 40 distinct odd distances, and three large-distance Lambert-function asymptotic comparisons. Execution completed with all assertions satisfied.

The mathematical proof is analytic. Numerical checks cannot prove the infinite-lattice theorem, exclude every conceivable bibliographic overlap, or establish results for model variants. The finite Markov generator is independently assembled from transition rules; it does not call the analytic recurrence solver.

Run: `python verify_voter_reset.py` with Python 3, NumPy and SciPy.
