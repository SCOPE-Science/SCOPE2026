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

In coordinates (u,q)=(x+y,y/(x+y)) the radial coordinate multiplies by alpha and the interior angular coordinate follows doubling, giving every finite binary prefix on admissible nondyadic angles. The displayed q_k lies strictly inside its binary cylinder and retains a factor of seven in its denominator. At the first disagreement of two prefixes of length n−1, identical initial fibers and identical prior symbols give identical current fibers. The two next values differ by at least the smaller endpoint value of phi2−phi1, delta, so the difference is observed by time n−1 even if the images overlap. The branch linear parts have infinity-norm row-sum bound max(2alpha,lambda1,lambda2). Thus points in the same length-n cylinder and initial cube of diameter 1/(floor(1/epsilon)+1) cannot be separated by time n−1. The bounds squeeze the fixed-scale growth rate. At q=1 the update is q'=1, not 0 under the usual mod-1 convention; the interior coding construction excludes this endpoint and the upper bound uses Lipschitz estimates directly. The entropy is on the admissible domain, not the limiting fiber on the singular line.

## originality

PASS

Credit the exact separated-set entropy for the specific Catsigeras et al. family in the touching and overlap regimes, not exact log 2 for contracting maps in general, the synchronous-fiber method, or the earlier disjoint-regime lower bound. Kruglikov–Rypdal's Example 2 already uses uniform separation of images of equal initial fiber values to turn maximal itinerary growth into metric entropy in a related model. The inspected statement and examples do not give the equality across this continuous affine fiber family's overlap transition.

## value

PASS

For the published example the best stated lower bound can be much smaller than the exact entropy when fiber images overlap. Resolving that gap for the whole open parameter region, even at a fixed separation scale, shows that the connected attractor and branchwise contraction do not diminish information production of admissible trajectories. The interest is the qualitative transition test in a natural literature example and its quantitative answer, not the mere existence of another positive-entropy contraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
