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

The mathematical proof is in `RESULT.md`; the following finite checks corroborate, but do not replace, the proof.

Run `python verification/check.py` with NumPy installed as specified in `verification/requirements.txt`. The packaged checker passed **2028 assertions** with its deterministic seeded random test cases, covering bath dimensions one through eight, exact covariance spectral bounds, rank-one pure-state counterexamples beyond the sharp boundary, the fixed-input Schur-complement criterion, the one-bath-mode Choi matrix, and thermal-band formula evaluations.

For arbitrary (including infinite-dimensional) baths, the universal assertion follows by applying the two operator Schur complements and approximate spectral-edge unit vectors, not by testing a finite number of matrices. The complete-positivity claim is limited to a one-bath-mode local qubit map, and no broader implementability certificate is asserted.

The numerical example uses \(\beta J=3\), \(\mu=0\), and the infinite tight-binding band \([-2J,2J]\); a finite open chain has different band edges. The input-independent cone-preservation criterion must not be confused with positivity along a particular dynamical trajectory. No independent audit was performed.
