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

# Verification record

The finite experiments were rerun using the accompanying standalone `verify.py`, with the result:

`VERIFY_OK exact_real_spectra=60 exact_row_checks=744 exact_quadratic=65 exact_bias_monotonicity=60 CLT_ratio_n10000=0.483895011 target=0.483941449`

The script uses exact fractions for nonhomogeneous spectral-kernel row sums, signed rational coefficient masks, quadratic binomial identities, and coordinatewise rare-probability comparisons. Its last Gaussian-limit diagnostic uses finite-precision arithmetic and is not evidence of an infinite proof. The general convex-order inequality, \(L^1\)/\(L^\infty\) endpoint identities and Gaussian limit are justified in `RESULT.md` by analytic arguments. The checker was executed from this package's actual `verify.py` path before serialization. No independent audit has been performed.
