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

Parametrized the central plane with normal coordinate c=|u_z|, tangent parameter xi=kc/sqrt(1-c^2). Direct Cartesian integration yields S=4sqrt(k^2+xi^2) F(xi) with F=int_xi^infty sqrt(t^2-xi^2)/(1+t)^3 dt; endpoints S(0)=2k, S(1)=pi. Differentiation gives F_prime=-xi I, I=int_0^infty(1+xi cosh v)^-3 dv>0, hence stationary equation k^2=F/I-xi^2. The explicit F expansion and I=log(2/xi)-3/2+O(xi^2 log(1/xi)) prove S decreases immediately to the right of xi=0 for every k>0. As k tends to zero, all global minimizers must tend to xi=0 by positivity of xi F; the stationary map Q has Q_prime~1/[2xi log(2/xi)^2]>0 near zero, establishing uniqueness for thin cones. The next constant term in I implies xi_k~2exp(-3/2)exp(-1/(2k^2)) and area benefit~4k exp(-3)exp(-1/k^2). Independently integrated three central sections directly in plane coordinates against F to better than 1e-45, and solved the stationary equation at k=.30,.20; x/asympt ratios 1.00033745 and ~1, deficit/asympt ratios 1.00034791 and ~1. These finite checks do not establish global uniqueness; analytic compactness/monotonicity do.

## originality

PASS

PASS best-of-knowledge for this particular global minimum central *area* and its essential-singularity tilt/deficit constants, not the classical section formulas or other cone optimization problems.

## value

PASS

Minimizing an area of a central plane section is a natural convex-geometric extremal problem. The apparently optimal axial-containing plane fails at every positive height; the truly optimal latitude is exponentially close and the gain beyond all algebraic orders, so standard power-series perturbation would miss it. Exact constants quantify geometric sensitivity in a canonical shape.

The dated certificate retains the supplied scientific assessment, sources and limitations.
