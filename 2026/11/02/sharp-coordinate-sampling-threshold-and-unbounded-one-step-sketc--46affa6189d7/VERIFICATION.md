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

# Reproducible mathematical checks

The standalone program `check.py`, with the dependency specified in `requirements.txt`, constructs the matrices from the stated formulas and executes assertions for: symmetric reflection identities; eigenvalues and condition numbers; exact sampled action \(SA_\eta b=\eta Sb\); the sketched least-squares coefficient; exact Euclidean residual formulas; the ordinary one-step GMRES minimum residual; and the selected-versus-alternative row cases. It also samples independent SPD matrices with condition numbers below the sharp threshold to test the spectral lower bound.

Command: `python check.py`.

Observed output: `PASS: 62206 assertions. Analytic universal and critical-limit proofs are given separately.`

The construction and threshold are proved for every permitted \(n,s,q,\eta\) in `RESULT.md`; these finite, floating-point checks do not independently certify a continuum, a limit, or novelty. No independent mathematical validation is asserted.
