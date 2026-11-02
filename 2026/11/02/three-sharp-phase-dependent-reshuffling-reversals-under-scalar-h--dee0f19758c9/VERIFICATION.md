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

For the scalar recursion the two-by-two deterministic companion matrix has strict Schur stability in the stated parameter interval. The iid and reshuffled stationary covariances are unique solutions of explicit 2-by-2 discrete Lyapunov equations. The supplied SymPy script obtains those solutions by independent symbolic linear-system solving, verifies every final variance and factored difference, confirms phase indexing and the exact rational witness, and checks additional admissible rational points. The executable's observed output is `VERIFY_OK symbolic=7 rational_and_boundary=111; exact stationary covariance identities and two-phase reversals`.

A finite list of symbolic expressions is sufficient here only because the algebra and analytic sign arguments have been explicitly derived for arbitrary real admissible parameters. The code does not constitute external independent validation, does not prove a broader multi-component result, and is not a novelty certificate. The literature comparison remains subject to independent priority review.
