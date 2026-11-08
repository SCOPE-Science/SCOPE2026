---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Affine reduce to the standard tetrahedron with x1<=1-s and x2<=1-t. For s,t>=0, s+t<=1, c=s^3+t^3<1, the disjoint cap-volume calculation is vol=(1-c)/6. The coordinate facets have areas (1-t^2)/2, (1-s^2)/2 and (1-s^2-t^2)/2. By the mixed-area formula with support h_{-K}, the other outward facets have zero support and 6V(K,K,-K) equals their weighted sum N. Independent symbolic expansion verifies rho-5/3=(1-u)((1-u)(5u+4)+12st)/[3(1-c)], u=s+t, so equality requires u=1. Fixing c, st=(u^3-c)/(3u), u ranges c^(1/3)..min((4c)^(1/3),1); differentiation gives dN/du<=u^2-1<0 for 0<u<1, strict also at u=1 when c<1. Endpoints then give one-cap maximum, balanced minimum for c<=1/4, edge-contact minimum thereafter and the explicit quadratic discriminant solutions. The universal proof uses geometry/algebra; finite exact difference-body checks are supplementary.

## originality

PASS

The anti-blocking mixed-volume projection identity is prior work, as are the general Godbersen inequality and one-corner simplex truncation profile. The precise two-cut fixed-c reallocation extremum, threshold 1/4 and 5/3 plateau are not logical corollaries of those general bounds or one-cap formulas without fresh two-variable optimization. Best-of-knowledge PASS with older truncation literature risk.

## value

PASS

The removed volume c is a natural geometric constraint for loss of tetrahedral vertices; the exact optimal placement of two cuts is a nontrivial finite-parameter mixed-volume problem. A rigorous phase boundary c=1/4, unique equal-cut minimizer below it, a continuous edge-contact minimizing family above, and a sharp explicit maximum provide geometric information not present in the global Godbersen inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
