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

# Verification information

The proof in \(\texttt{RESULT.md}\) is analytic. Both Bregman minimization objectives are reduced globally to one negative or one positive rank-one eigenmode by Sherman–Morrison and the extremal Rayleigh quotients. The unrestricted spectral competitor is bounded by rank-one eigenvalue interlacing, with matching explicit candidates. Elementary logarithmic-mean and monotonicity calculations give the thresholds, strict inequalities, and sharp suprema. These steps settle the infinite quantifiers; computation is not the proof.

The bundled \(\texttt{verify.py}\) with \(\texttt{requirements.txt}\) produces the recorded \(\texttt{verification_output.txt}\). Checks include the exact score-difference identities, orientation decisions, both constructed spectral condition numbers, and seeded generic rank-one preconditioners of both signs across seven values of \(K\). This is a finite numerical smoke test; floating-point near-tie behavior and all untested dimensions are covered by the proof rather than sampling. No independent audit has been performed.
