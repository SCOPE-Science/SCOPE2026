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

The standalone `checker.py` was executed from the package directory using Python 3. It enumerated every square-zero binary linear map in dimensions one through four and every probe subspace of dimension \(\lfloor n/2\rfloor\), comparing the joint flag counts with the exact formula. This comprised 343 maps and 11,227 map/subspace pairs. Another 141 symbolic normalizations over field orders two, three and four and ambient dimensions through twelve matched the Gaussian-binomial identity.

Successful output:

`SQUARE_ZERO_RANDOM_SUBSPACE_OK 343 11227 141 even 0.337415921240 odd 0.436153157721`

The infinite limiting-distribution argument is supplied in `RESULT.md`. Exhaustive finite checks alone do not prove asymptotic convergence or priority. The stated numerical intervals also have explicit analytic truncation bounds in the proof. Independent verification has not been performed.
