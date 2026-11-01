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

For every integer n>=3, 0<r<1 and p,q>0 the origin is inside all unit disks for 0<=c<1. In each of n regular angular cells the radial function is rho(c,t)=sqrt(1-c^2 sin^2(t))-c cos(t) for 0<=t<=h=pi/n. Implicit differentiation of rho^2+2c rho cos(t)+c^2=1 gives rho_c<0, rho_t>0, and the exact primitive -rho rho_c=d_t(rho sin t). Outside (c0,c1) the two weighted difference terms are nested and the objective is strictly monotone toward that interval; inside it the unique crossing alpha(c) rises from 0 to h. Direct Leibniz differentiation (zero endpoint integrands at the crossing) yields E_n'(c)=2n((p+q)r sin(alpha(c))-q rho(c,h)sin h). The ratio r sin(alpha(c))/(rho(c,h)sin h) is strictly increasing onto (0,1), so there is exactly one global minimizer for each s=q/(p+q). A uniform Taylor expansion rho=r-delta+[r(1-r)/2]t^2+O(h^4), delta=O(h^2), derives the n^-2 center correction and E_n coefficient pi^3 r^2(1-r)(p+q)s(1-s^2)/3 with O(n^-4) remainder at fixed r,p,q; the expansion does not cover degenerate endpoints r=0,1 or p/q=0. Independent SciPy quadrature/root checks for 18 parameter/n cases corroborate derivative stationarity and scaling, not the infinite proof.

## originality

PASS

Best-of-knowledge and restricted to regular-center one-parameter optimization. Primary literature establishes weighted disk-polygon approximation as a natural problem and separately establishes one-sided or fixed-center-radius results, but none inspected gives the precise mixed-sign weighted objective, unique balancing radius for all finite n and fixed positive weights, or sharp O(n^-4) expansion. This is a genuinely narrower theorem than unrestricted disk-polygon approximation, not an assertion of that open problem. Unindexed equivalent calculations remain possible.

## value

PASS

Weighted inside/outside area deviation is a mathematically motivated problem raised by primary disk-polygon approximation work. In the canonical rotationally symmetric one-parameter family, a strict global optimum for every finite n and arbitrary positive weights, a weight-interpolating crossing law and an explicit n^-2 curvature/radius coefficient form a reusable comparison benchmark for unrestricted approximation. This is neither a textbook nesting calculation nor an unsupported claim to solve the unrestricted open problem; the nontrivial part is balancing positive area excess and deficit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
