---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed stationary age mixture U=exp(-κT) with U density q u^(q-1) and conditional X|U=u∼N(mu,v+du²), where q=r/κ>0, v=D/κ>0 and d=σ²−v>−v. Independently expanded all raw moments up to degree 4, formed the fourth cumulant and symbolically verified exactly the given rational A,B,C and positive quadratic discriminant 288q²(q²−2q+3)/[(q+1)^4(q+2)^2(q+3)^2(q+4)^2]. A changes sign at positive roots of q³−q²−6q+2, approximately 0.321637 and 2.855773; B changes sign at (√13−1)/2, between those roots. For d≠0, t=m²/|d| yields quadratic A t²+6sgn(d)B t+3C, with positive constant and discriminant. Vieta signs prove exactly two positive simple roots only in the two stated open regimes, one when A<0, and the asserted endpoint linear cases; d=0 is separate. Verified exact q=4 witness polynomial (13t²−850t+4375)/26250. No mistaken inference of Gaussianity from κ4=0.

## originality

PASS

Qualified PASS limited to the complete quantitative fourth-cumulant sign/root diagram: Olsen (2023) gives every stationary OU resetting moment, including Gaussian resetting, so the underlying renewal law and raw cumulant are covered and not new. The two disjoint rate–width regimes, two positive roots and boundary classification require an additional discriminant and sign analysis not stated in Olsen §III or the comparison literature; their exact historical priority remains uncertain.

## value

PASS

PASS: the exact +/−/+ fourth-cumulant reentrance determines where two physical reset scales produce qualitative changes in shape of a natural stationary non-Gaussian process. It is a complete sharp parameter-space classification, not just substitution of Gaussian moments or a trivial two-point example, and it distinguishes fourth-cumulant zeros from Gaussianity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
