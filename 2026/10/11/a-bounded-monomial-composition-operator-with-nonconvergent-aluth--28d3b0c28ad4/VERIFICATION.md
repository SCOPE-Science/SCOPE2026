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

# Reproducible finite checks and mathematical limits

Run `python verification/check_aluthge.py` using a standard Python 3 interpreter. Expected success marker: `MONOMIAL_COMPOSITION_ALUTHGE_BINOMIAL_IDENTITIES_OK`.

The program verifies exact integer interpolation values, the first three binomial exponent identities, and exact rational binomial expectations for \(N=3\cdot2^\ell\) with \(4\le\ell\le9\). It separately evaluates the stated finite-index exponential Hoeffding bound. No numerical sample certifies a limit. The infinite claim follows from the Lipschitz estimates for \(F\), the reducing-orbit polar decomposition, binomial convolution for every \(N\), and an analytic binomial concentration inequality for every \(\ell\ge4\), all supplied in `RESULT.md`.

The construction applies to a specified coefficient-weight Hilbert space, not to every weighted Hardy space. The preexisting nonconvergence result for abstract weighted shifts is credited. No external independent audit has been performed.
