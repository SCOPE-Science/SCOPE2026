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
# Reproducibility and limitations

Run `python3 check.py` in this directory. The standard-library checker evaluates exact two-step matrix multiplication and four scalar spectral identities using rational arithmetic for 80 parameter triples. It also tests the predicted stability frontiers, root coalescence, strict optimality against sampled alternative steps, and the closed-form equal-curvature value for 25 numerical curvature pairs. The successful execution prints `CHECK_OK`.

The universal quantifiers are established analytically by quadratic Schur/Jury inequalities, the sign of the largest positive root derivative, the determinant lower bound after critical damping, and simultaneous diagonalization. The tests are finite consistency evidence only. No claim is made for arbitrary noncommuting Hessians, stochastic refreshes, or finite-precision implementations. No independent validation has been performed.
