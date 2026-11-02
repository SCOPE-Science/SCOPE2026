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

The body is normalized affinely to the simplex (0,0),(1,0),(0,1). For normals (1,t), the centroid of a triangular cap yields C1(r)=(1-(r+q/r)/3,r/3) for sqrt(q)<=r<=1, and the complement triangle yields C2(r)=((1-p²/r)/(3q),(1-pr)/(3q)) for r decreasing 1 to sqrt(p). Cap switch t=p and all six ordered-normal sectors cover the circle. The first arc obeys lambda0*lambda2=q/9 and the second (1-3qx)(1-3qy)=p^3; Green integration gives J1=(p+q log q)/9 and J2=p²(q+p log p)/(9q²), hence F=6(J1+J2). Independent direct quadrature of both arc integrands agreed at six levels, including tiny q and q=1/2; series expansion gave F(q)=1+(2/3)q log q-(11/9)q+q²/6+O(q³). The complement scaling follows the general first moment identity q(Cq-G)+p(Cp(-u)-G)=0, already known. The algorithmic cap-clipping verifier checks other numerical levels but does not replace exact integration.

## originality

PASS

General Ulam body support and moment complement are prior theorems of Huang–Slomka–Werner. Their complete accessible paper does not give the all-level triangle area or conic-sector parametrization. Exact published square Ulam and classical convex floating triangle formulas were read in full and are nonimplicative, because the first body has a different polygon and the second uses a different construction.

## value

PASS

An all-cap-level shape-independent area formula and complete conic-arc boundary for the elementary yet geometrically important simplex under the Ulam floating operation; it is not merely the known classical halfspace-depth floating-body calculation. Natural benchmark for metronoids/trimmed regions and cap-centroid geometry, including half-level and endpoint asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
