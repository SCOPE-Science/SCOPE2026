---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The integer displacement f(i)-i decreases by 0 or 1 and brackets zero, so the fixed points form an interval. Below and above it each orbit moves strictly inward without overshooting the nearest fixed endpoint; monotonicity makes the two chain endpoints slowest. Equality T=n-1 forces one orbit through all n sites in order, which fixes the entire map to one of the two clipped unit shifts (including n=2). Given the exact fixed interval, the adjoining steps are forced flat and the remaining steps on each side are independent fair bits, giving the same nested prefix count H(d) at every iteration, not a resampled binomial. The side-length weights sum to (n-r+3)2^(n-r-2) for fixed interval length r<n, with the identity at r=n, giving the asserted uniform geometric bound. Except on an exponentially small event one side has length at least n/4. A union of prefix Hoeffding bounds gives an exponentially tailed cutoff K; above it the distances contract between factors 1/2-epsilon and 1/2+epsilon, and the remaining time is at most K. Taking a cutoff of sufficiently small positive multiple of log_2 n gives the polynomial relative-deviation bound. The bound using random K with one fixed epsilon, rather than that polynomial probability alone, gives uniform integrability in every positive power and hence the claimed moment limits. The supplied script was inspected, not executed. A separate direct-composition enumeration for n=2 through 11 reproduces map counts, clipping, and the extremizers (6,144 maps at n=11, exactly two at T=10) and the n=4,6,10 histograms; it is not evidence for the asymptotic step.

## originality

PASS

Credit the existing monoid identifications, finite counts, and idempotent/fixed-point structure. The supported distinction is the stabilization index as a dynamical observable, especially the sharp leading log_2 n law with polynomial relative-deviation control and all positive normalized moments for the uniform full-map law. The closest distinct catalogue theorem shares the in-probability law and strengthens the conditioning scope in another direction, but is dated later than the frozen record and does not establish earlier coverage; the inspected statement does not give the two quantitative conclusions above.

## value

PASS

The least time to reach the idempotent power is a natural invariant which rank and eventual image do not determine. Its uniform-law behavior differs parametrically from its extremal value (logarithmic with an exact leading constant versus linear), and tail and moment control describe typical and mean behavior rather than just bounding an orbit. The existing counts and clipping formula alone are not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
