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

For a fixed spot order, when car sigma_j arrives, the smaller-labeled cars occupy exactly their designated spots; the allowed preferences for sigma_j run from one past the nearest larger label on its left up to j. This proves the fiber product by induction over arrivals. For a rise a<b at i,i+1, the two old distances A,B satisfy A+1<=B<=i+1 and the two new distances are B-1,1. A later nearest larger predecessor changes only for a value strictly between a and b with no larger entry in the intervening suffix; then its distance increases from j-i-1 to j-i. Thus the local factor is between 1/(i+1) and i/(i+1), and the later factors lie between 1 and their full telescoping product n-i. The increasing order and the stated (2,...,i,1,n,i+1,...,n-1) order realize the respective extremes, including empty prefix or suffix. For the global maximum, t+(n+1)/t-2 sqrt(n+1)=(t-sqrt(n+1))^2/t gives the rounding error; the endpoint and small-n inequalities follow from the exact envelopes. Independent raw preference enumeration through n=5 confirmed both extrema at each position, checking 1, 6, 36 and 240 rising swaps respectively.

## originality

PASS

The mass identity and global atom extrema are known and are not credited as new. The supported distinct claim is the exact mass-ratio envelope on rising adjacent covers, the positionwise witnesses and the resulting global maximum over covers. None of the closest inspected statements gives this optimization; the affected suffix factors must be located and bounded with simultaneous attainment. This is a best-of-knowledge decision.

## value

PASS

Knowing the increasing outcome is the most likely does not tell whether a single new inversion makes a nearby outcome less likely. The exact positionwise envelope gives the first size allowing an increase, distinguishes the last position from all earlier positions for n>=4, and shows a single local move can amplify mass by order n at positions of order sqrt(n). These are quantitative features of the classical permutation law not supplied by its global mode or an isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
