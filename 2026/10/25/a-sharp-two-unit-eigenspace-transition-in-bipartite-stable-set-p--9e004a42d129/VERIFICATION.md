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

The exact rational checker `verify.py` is supplied with this result. Running `python verify.py` produces a success line only after:

- integrating every first- and second-moment entry independently over all explicit sorted simplex chambers for \(2\le p,q\le4\);
- comparing each entry with the displayed closed covariance formula;
- checking the exact \(\det B\) and \(\det(B-t_{\min}I)\) factor identities and the strict imbalance threshold for \(2\le p,q\le50\);
- checking the exact balanced eigenvalue identities.

Observed output: `VERIFY_OK chamber_parameter_pairs=9 independent_chambers=1024 exact_matrix_entries=336 rational_phase_cases=2401 balanced_lambda_max=1/12`.

The derivation of the Dirichlet moments, the two exact determinant factorizations, and the uniform Stirling estimate are the infinite proofs; no finite test is being presented as a certificate for all parameters. No independent audit has been performed.
