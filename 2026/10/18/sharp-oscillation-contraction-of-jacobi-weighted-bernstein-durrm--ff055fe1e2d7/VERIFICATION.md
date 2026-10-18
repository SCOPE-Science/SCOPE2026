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

# Verification of the sharp Jacobi Durrmeyer oscillation law

The explicit operator definition, exact beta-law crossing, fixed-parameter asymptotic and spectral comparison appear in `RESULT.md`. The reproducible file `check_durrmeyer.py` uses NumPy and SciPy; execute `python check_durrmeyer.py`. On examination it completed 527 finite assertions, including quadrature-versus-regularized-beta identities, endpoint-dominance samples, total-positivity minors, and large-degree asymptotic ratios. All tested assertions passed.

The analytical proof uses monotone likelihood-ratio composition, stochastic ordering, one-crossing integration and endpoint Laplace asymptotics. Finite consistency testing cannot establish those statements universally, certify historical originality, or replace an independent scientific audit. The leading asymptotic assumes fixed strictly positive beta parameters; convergence uniform in parameters approaching zero is not established. The 1995 related operator article was not inspected in full and remains a priority-risk source.
