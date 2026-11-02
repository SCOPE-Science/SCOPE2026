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

# Reproducible checks

With Python 3 and the version of `mpmath` pinned in `requirements.txt`, execute `python verify_tempering.py`. Recorded output is in `verification_output.txt`. The script ran successfully, reporting 187 checks passed.

The computations compare the closed hypergeometric and integral representations of a power-potential specialization for multiple exponents and positive tempering values, check the Gaussian arctanh identity, verify positivity/monotonicity and asymptotic scales, and print representative constants. Exact proof of the all-potential regular-variation theorem is in `RESULT.md`; finite checks neither cover all \(\eta\), all \(\ell\), nor every smooth potential. No independent audit has been performed.
