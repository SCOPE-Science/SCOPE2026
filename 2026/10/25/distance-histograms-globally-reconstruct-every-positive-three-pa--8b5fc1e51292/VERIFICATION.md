---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For small r, the length measure of metric balls gives P(D<=r)=2r/L+O(r^2), recovering L. Four simple endpoint/other-arm routes bound the diameter by (b+c)/2, attained by midpoints on those two arms, hence a=L-2d*. Set epsilon=d*-r. On b,c arms, variables p=x+y-(b+c)/2 and q=x-y-(b-c)/2 satisfy |p|<epsilon, |q|<a+epsilon plus domain |p+q|<b, |p-q|<c, with Jacobian 1/2. For epsilon<=(b-a)/2 the rectangle is uncut and both orders have tail measure 4epsilon(a+epsilon). At the first onset h=(b-a)/2 the same-long-arm and short-long-arm contributions enter with positive linear 2(a+c)delta (doubled when b=c); old b,c corner-clipping affects only O(delta^2), making the threshold sharp. For a=b<c the distinct-arm and same-arm leading slope is 2c+6a, and for a=b=c it is 12a, both >4a. Thus the slope classifies ties and the first exact-law breakpoint identifies b otherwise, completing inversion for all real triples. Inspected rational polygon-clipping verifier checks finite parameter cases, but proof is analytic.

## originality

PASS

Published distance-distribution inverse geometry includes local injectivity in metric-graph classes, stronger in some other senses but not identified as globally injective for all three-arm positive theta metrics including ties. Forward network-distance formulas and noisy point-cloud graph reconstruction do not imply global injectivity of one scalar unmarked pair-distance histogram. The closest full Mémoli--Needham text could not be read, so priority risk remains substantive.

## value

PASS

A global inverse theorem is mathematically meaningful because distance histograms fail injectivity on arbitrary metric-measure spaces. This exact three-arm classification and constructive inversion, including collisions of arm lengths, is a distinct natural finite-dimensional identifiability result; no downstream theorem is needed to justify the classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
