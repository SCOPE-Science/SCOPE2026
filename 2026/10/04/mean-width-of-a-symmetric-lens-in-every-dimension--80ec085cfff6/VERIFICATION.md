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

The lens K=B(ce1,1) intersect B(-ce1,1) has sections |x1|<=1-c, |x_perp|<=sqrt(1-(|x1|+c)^2). Maximizing t(y-c)+sqrt(1-t^2)sqrt(1-y^2) over c<=y<=1 gives y=max(c,t) and stated support split. Spherical |U1| density Cn(1-t^2)^((n-3)/2) integrates to the three incomplete-beta terms; boundary derivatives cancel, leaving strictly negative derivative for 0<c<1. n=3 reduces exactly to the Finch formula; n=2 endpoint singularity is integrable. Finite scripts only supplement analytic proof.

## originality

PASS

The motivating 2013 primary source explicitly did not attempt higher-dimensional lens mean width; a 2025 general lens extremal theorem proves inequalities, not this beta-function evaluation in statements inspected. Best-of-knowledge novelty keeps a specific historical quermassintegral risk.

## value

PASS

Fills an explicit quantitative gap in the motivating lens geometry source: universal support function and mean-width evaluation across n>=2, with scaling and strict decrease in separation. This exact geometric integral is useful when later sharp intrinsic-volume comparisons invoke the lens.

The dated certificate retains the supplied scientific assessment, sources and limitations.
