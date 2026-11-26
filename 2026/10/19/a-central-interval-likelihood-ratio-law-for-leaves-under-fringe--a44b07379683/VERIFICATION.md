---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Contracting a marked complete occurrence gives an ordered m-vertex tree with a marked leaf, with inverse given by expansion. Hence the leaf count shifts by ell-1 from the size-biased Narayana law; this is occurrence bias, not conditioning on presence. Vandermonde identifies the ordinary m-vertex leaf count as hypergeometric with population 2m-2, m-1 successes and m draws, giving mean m/2 and variance m(m-2)/(4(2m-3)). After cancellation, the shifted Palm-to-ordinary adjacent ratio at j is [(m-j-1)/(m-j+k-ell-1)][(m-j)/(m-j+k-ell)] times [1+(2ell-1)/j+ell(ell-1)/j^2]. Both factors are positive and strictly decreasing over the indices compared, since k-ell is at least one. The support is contiguous, with upper endpoint n-1-(k-ell), and lower endpoint ell. The above-one interval is nonempty by normalization and the missing positive ordinary mass; ell at least two excludes both endpoints. Contiguous rejection sets follow by thresholding, with boundary ties available for exact-size randomization. The normalized covariance is the difference of the Palm and ordinary means, hence ell-(k+1)/2+(m-2)/(2(2m-3)); the correction is zero at m=2 and in (0,1/4) otherwise. The strict-ratio comparisons are vacuous for m=2,3 where appropriate. At n=k Palm is deterministic, as separately stated.

## originality

PASS

To the best of current knowledge the distinct result is the uniform-in-size strict relative log-concavity of the occurrence-Palm versus ordinary leaf laws and the resulting central-interval testing statement, with the finite sign boundaries as a companion. Basic marked-tree enumeration, Narayana counts, the general likelihood-ratio test principle and the leading asymptotic covariance are not credited as new.

## value

PASS

A leaf-only test for occurrence enrichment is a natural statistical question in this model. The exact all-size shape theorem says enrichment is detected by an interval, not necessarily by a one-sided tail, and for a fringe with multiple leaves the ratio-above-one region excludes both extremes. The normalized covariance sign identifies when a mean comparison obscures or reverses the impression of enrichment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
