---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The reciprocal change z=1/x converts unforced updates to f(z)=(z+1)/R and pulse to f(z)+(s/R)z(z+1). The exact final reciprocal f^n(z0)+(s/R^n)H_t, H_t=R^t z_t(z_t+1), decouples dose. For R≠1, H_t=R/(R-1)^2 R^t+(2/(R-1)+1)(z0-1/(R-1))+(z0-1/(R-1))² R^(-t), strictly convex in real t; for R=1, H_t=(z0+t)(z0+t+1) is strictly convex. For R≤1 discrete differences >0 imply last unique. For R>1 exact H_(n-1)-H_0 factors with one attainable positive threshold xcrit=(R-1)/(1+R^(n/2)); first below, last above, endpoint tie at equality, interior strictly excluded. Independent exact Fraction test of terminal vs formula and both sides of switch passed; it does not prove all real cases.

## originality

PASS

The exact global terminal scheduling rule under a single product-form sterile mating pulse is not an immediate consequence of inspected multiple-release, stage-structured and proportional-harvesting studies. Closely titled optimal timing work remains a meaningful full-text priority risk.

## value

PASS

A biologically motivated scheduling problem is solved for all finite horizons and parameters: no intermediate optimum, exact switch from early to late intervention and dose-independent threshold, with a closed dose-to-target corollary. These are natural exact mathematical decisions that are not merely a tabulation of a few release dates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
