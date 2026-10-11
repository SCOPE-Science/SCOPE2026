---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The two quadrics form a smooth \((2,2)\) complete-intersection curve of degree \(4\) and genus \(1\). The tangent-bundle ideal is the two quadrics plus their two Jacobian tangent equations. Fresh exact elimination for the displayed complementary affine plane reproduced a zero-dimensional reduced section with lex leading monomials \(x,y,z,u,v,w^{12}\) and a squarefree degree-12 eliminant. Independently, homogenizing the tangent-bundle ideal, saturating by the affine homogenizer, and computing the exact leading-monomial Hilbert series gave \((1+t)^2(-t^3+t^2+2t+1)/(1-t)^3\), whose numerator evaluates to \(12\) at \(t=1\); hence the projective closure, and therefore the affine geometric degree, is exactly \(12\). This direct degree computation removes dependence on an externally unread secant-bound theorem.

## originality

PASS

Best-of-knowledge originality passes for the explicit elliptic-quartic equality case. The 2024 primary paper proves the exact general curve formula deg(TC)=deg(C)+omega(C)deg(Tan(C)) but contains no elliptic-quartic example or automatic numerical evaluation of the two additional tangent-direction invariants. The newer Lanciano abstract announces a sharp universal quadratic theorem; its full text could not be independently retrieved in this run, so no whole-document noncoverage claim is made. Resultary returned the assigned finding as the only exact degree-12 elliptic-quartic hit.

## value

PASS

A smooth elliptic quartic is the simplest standard positive-genus nondegenerate complete-intersection curve in projective three-space. Its exact tangent-bundle degree supplies a concrete sharpness benchmark for the new tangent/secant degree theory beyond plane/rational examples, and the degree is independently certified by exact algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
