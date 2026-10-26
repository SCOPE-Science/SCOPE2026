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
# Computational verification

The companion `verify.py` uses Python and `mpmath` (100+ decimal-digit arbitrary precision, configured at 155 decimal digits). Running `python verify.py` evaluates parity-separated finite-domain Dirichlet eigenvalue roots through the exact confluent hypergeometric determinants. It checks that each exact bandwidth is positive and closer to the two-term asymptotic than to the leading approximation for indices \(0\) through \(4\) at \(a=6,8,10\). It checks the exact Dirichlet-to-Robin spectral shift at these test points, as well as 16 duplication-formula identities for the even/odd prefactors. All 61 assertions passed in the delivered copy.

Representative exact-width-to-leading-factor ratios at \(a=10\) are \(0.99494870140686\), \(0.97986973070234\), \(0.95506491576808\), \(0.92113170932083\), and \(0.87894069224794\) for \(n=0,1,2,3,4\), respectively. These are consistent with the predicted correction \(-(n+1)^2/(2a^2)\) and a bounded fixed-index residual after multiplication by \(a^4\).

The infinite-index and infinite-separation assertions are proved analytically in `RESULT.md` through the Wronskian, exact edge factorization, and endpoint Laplace expansion; no finite numerical test certifies them. The numerical program requires the third-party Python package `mpmath` but no non-embedded data files. Independent scientific audit has not been performed.
