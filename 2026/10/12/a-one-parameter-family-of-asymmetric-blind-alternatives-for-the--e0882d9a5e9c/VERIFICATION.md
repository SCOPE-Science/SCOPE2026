---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Define z=2u−1, h=z³−(15/28)z, d_epsilon=1+epsilon h, |epsilon|<28/13. Exact calculus gives |h|<=13/28, so quantile Q(u)=int_0^u dv/d(v) is increasing and finite with inverse F, density f(Q(u))=d(u)>0 analytic on interior. h is odd about u=1/2, hence d(1−u)≠d(u) for epsilon≠0, impossible for a symmetric absolutely continuous distribution. Substituting rho3=4u−3u² and reflected counterpart gives W3=(5z−3z³)/2; direct exact symbolic integration against h gives zero. For rho4=6u²−4u³, W4=6z−2z³, and int_0^1 W4h du=2/35, thus X_(1,4)=epsilon/35. Independent sympy integration reproduced W3/W4, 0 and 2/35; no finite experiment substitutes for the polynomial proof.

## originality

PASS

No directly equivalent consecutive-system fixed-(1,3) asymmetric null family found in literature/result-corpus searches. All-system-size theorems do not imply the individual contrast separates asymmetry; the construction specifically demonstrates their scope difference. Generic functional-analytic nullspace intuition makes other blind families unsurprising; originality is the explicit smooth polynomial witness for the implemented statistic, with uninspected paper-section and earlier test primary risks.

## value

PASS

A proposed symmetry test can conflate a vanishing SINGLE population contrast with symmetry even when a full collection of contrasts characterizes symmetry. The explicit smooth bounded-support family makes that failure mechanism precise and separately exhibits a detecting X_(1,4) contrast, directly motivating multi-contrast testing rather than a hollow general linear-kernel observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
