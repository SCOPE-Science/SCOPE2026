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

# Reproducibility and verified scope

Run `python verify.py` in a directory containing the provided `requirements.txt` dependencies. The executable has been run on the embedded file itself with output in `verification-output.txt`. It reconstructs full symmetric transition matrices directly from graph edges and verifies stochasticity and the computed second-largest eigenvalue modulus for 40 graph sizes. It also checks the symbolic eigenvector and Rayleigh identities, exact constants used in the small-size trigonometric bounds, 800 feasible invariant competitor matrices and the leading asymptotic predictions.

The exact analytical proof in `RESULT.md`, not the finite checks, establishes the claim for every integer \(n\ge5\). No calculation checks every infinite case, all possible noninvariant assignments, or originality across all literature. Independent mathematical verification has not been performed.
