---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Indifference with the other n−1 players gives the claimed interior probability and V_n. In RESULT.md lines 40–54, factoring D_n leaves R_n(z), whose derivative has exactly one interior sign change from positive to negative; the strict maximum exceeds R_n(1)=0, giving exactly one interior root and the asserted signs in lambda. The tent-kernel representation compares adjacent sizes strictly: at the root, the negative-to-positive change of f'' lies inside the tent support (giving both strict brackets); if it lies within the overlap, subtract the two tents scaled to agree at that point. Their difference and f'' have the same sign on both sides, and their product has strictly positive integral. If the point is left of the overlap the later tent already integrates a positive f''. Independently checked the most cancellation-sensitive coefficient using the integral: with h=1/n, x=n−1+t, lambda=2−2h+uh^3, the square bracket in f'' is 2ht−uh^2−uh^3t and the prefactor is 2h^4[1+(1−4t)h+O(h^2)] uniformly for |t|≤1 and bounded u. The tent moments of 1,t,t^2 are 1,0,1/6, giving h^6(−2u−8/3)+O(h^7). Bracket with u=−2 and 0 and substitute the root to recover the stated expansion, including the absence of an n^−2 term. Linear interpolation gives the two convex-order directions; V_n is bounded for fixed lambda. The exact change for the example is −2s²+3s³−s^6 with s=e^(−lambda/6), giving the stated fractions at 5/6 and 4/5. This unrestricted analytic check does not rely on executing the supplied finite checker.

## originality

PASS

The standard equilibrium formula is prior work. The supported distinct claim is the strictly ordered second-difference threshold ladder with its sharp coefficient and implied per-group convex-order regimes. The closest indexed record proves a different ladder for first differences; the closest inspected spread result uses a different information structure and outcome. No covering result was established in inspected material; this is not a priority determination.

## value

PASS

There is a meaningful quantitative distinction between where mean volunteer counts peak and where size diversification raises or lowers mean volunteer counts. The ordered thresholds and one-inflection result answer the latter uniformly in group size and explain why local spreads can have opposite effects. The asymptotic identifies the approach to the fixed-lambda phase boundary; basic equilibrium indifference and generic Jensen reasoning are not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
