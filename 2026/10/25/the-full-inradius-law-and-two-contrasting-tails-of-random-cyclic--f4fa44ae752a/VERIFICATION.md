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

Cyclic arc spacings are Dirichlet(1,1,1), so ordered triangle half-angles X,Y,Z have constant coordinate density 8/pi^2 on X+Y+Z=pi/2 and R=4sin Xsin Ysin Z. At fixed X=x the difference coordinate has unit Jacobian and the admissible interval yields the arccos integral with exact roots. Three corner neighborhoods give each area t/4 log(1/t) plus O(t); other edge bands are O(t). The equilateral maximum Hessian is 2(u^2+uv+v^2), and the ellipse area gives the upper-tail coefficient. Independent quadrature at 5 thresholds agrees with a two-dimensional grid survival at t=1/4 (0.406006 vs 0.405971), and near-maximum ratio 1.470259 vs exact 1.470210. These numerical checks do not replace asymptotic proofs.

## originality

PASS

Kórus computes the first two moments for precisely this random cyclic triangle but those do not entail its distribution; Labelle uses fixed-perimeter uniform side lengths, a different probability model, and Finch gives sampling context not the full inradius CDF. Equivalence to incenter-circumcenter distance via Euler formula considered.

## value

PASS

A complete exact distribution with logarithmic near-degeneracy and linear equilateral-endpoint tails is a natural stochastic-geometry invariant and identifies distinct local geometric mechanisms; known first two moments cannot supply either tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
