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

Execute `python verification/check.py` with SymPy >=1.14. The verifier uses exact rational and radical expressions for seven integer dimensions, \(N=2\) through \(N=8\). For every dimension it verifies that the nilpotent matrix has exactly the indicated index, that the fixed covariance satisfies the continuous Lyapunov equation, that site diffusivities are positive, that the exact current quadratic trace equals its bond-by-bond entropy production formula, and that four rational-time matrix exponential norms equal the symmetric-tensor closed form. Expected terminal output: `VERIFY_OK`.

The all-dimensional proof is analytic: the symmetric tensor power of a rank-one 2x2 nilpotent matrix has nilpotency index exactly \(N\); the Lyapunov equation has a unique solution because the drift eigenvalue is strictly negative; the current integral is a Gaussian second moment; and the exact propagated-norm identity follows from tensor factorization. Finite verification does not establish the all-dimensional statements without these proofs. No perturbation robustness, external review, independent audit or numerical experimental confirmation is claimed.
