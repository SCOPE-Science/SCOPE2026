---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS. Checked one-to-one almost-everywhere change from ordered triple (x1,x2,x3) to circumcenter c, radius r and three circle angles, with absolute Jacobian r^3|det(u2-u1,u3-u1)|; normalized sampling density pi^-3. For each c, feasible angles form a single arc with half-length alpha=pi for r+s<=1, arccos((r²+s²-1)/(2rs)) in the intersecting regime, or zero outside. Sorting three labeled angles supplies 6 permutations; the gap variables and sine area produce Phi(alpha)=24[alpha²+alpha sin(2alpha)/2+cos(2alpha)-1], Phi(pi)=24pi². Center polar integration gives j(r,s)=(2r³s/pi²)Phi(alpha) and f_R(r) with contained-circle 24r³(1-r)_+² plus crossing integral on |1-r|<s<1+r. The map covers all noncollinear triples and gives total probability1. Contained probability integral is exactly2/5; known P(R<1)=4-32/pi² matches crossing mass. Finite source quadrature and quasi-Monte Carlo checks are supplementary; analytic Jacobian and angular integral prove all r,s.

## originality

PASS

PASS best of knowledge. Bakó-Szabó–Besau–Fodor arXiv:2608.29975 explicitly calculates the unit disk circumradius CDF for R>=1, and its public abstract says so, not a joint (R,S) density across R<1. Le Caër arXiv:1803.08484 states condition that circumsphere be fully contained, which excludes the new crossing population. Published general smooth-convex-body small-radius expansion gives only the first two coefficients of marginal near zero; its full text has no evaluated restricted-arc joint density. Highly relevant 2026 arXiv paper full text was inaccessible; authorized Oxford route returned vpn_disconnected, so priority claims have this residual risk and no unearned NOT_COVERING label for unread entire document.

## value

PASS

PASS. Resolves a natural explicitly identified geometric-probability gap: the full joint law of circumradius and circumcenter including boundary-crossing circumcircles. Exact restricted-arc determinant integration supplies a usable one-dimensional marginal and separates physically distinct events; not a mere known-contained-case re-expression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
