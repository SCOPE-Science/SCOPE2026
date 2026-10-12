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

# Verification and limits

Run `python3 verify.py` in the extracted directory. The checker uses only Python standard-library exact fractions and floating arithmetic. It tests equality of the first-moment integral expansion and the known alternating subset identity on 176 parameter pairs, as well as the exact conditional covariance/correlation identity on 45 numerical cases: total **221 successful assertions**. The first-moment checks are independent finite identities, useful for identifying an incorrect conditioning factor or last-coupon contribution.

The proof of the asymptotic Gaussian law itself is analytical: exact conditional truncated-Poisson structure, uniform conditional multivariate triangular-array CLT, exponential maximum law, and optional martingale isometry for replacing the Poisson time by the observed coupon count. The checker does not certify an infinite-dimensional limit, independent review, general nonuniform frequencies, or any growing-album-index theorem. The source papers establish first-order comparison results, not an independent audit of this new result.
