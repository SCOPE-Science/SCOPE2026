---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

After normalizing the equal sides to one and base to x in (0,2), direct median/altitude/inradius formulas reduce the claim to G(x)>=0. On [4/7,(3sqrt(3)-4)/2] the rationalized defect has the correct sign termwise. On the two outer intervals, sign-preserving squaring reduces to S=U-Vsqrt(1+2x^2), with U^2-V^2(1+2x^2)=784(x-1)^2(x-4/7)^2(x+2)^2Q(x). On the left interval Q is strictly increasing by the exact positive Bernstein coefficients of Q'((4/7)u) and Q(4/7)<0, so S<0 with the required original sign. On the right interval the shifted Q has a positive low block and a positive quadratic high block of discriminant -10, while shifted U has all positive coefficients, giving S>=0 and equality only at x=1. The frozen verifier reconstructs these identities exactly in Q(sqrt(3)); it corroborates the symbolic proof rather than replacing it.

## originality

PASS

The 2012 primary source states exactly this inequality as Conjecture 4 for all triangles. The submitted theorem resolves the entire nondegenerate isosceles subclass by a global one-variable sign proof. Liu's later 2023 article gives a pointwise lower bound for individual median-minus-altitude differences, but its summed bound is strictly weaker on an explicit isosceles triangle and therefore does not imply the claim. Resultary returned the audited result as the direct exact match and no covering isosceles proof.

## value

PASS

This proves an explicitly published open triangle inequality on the complete one-parameter isosceles subclass, including uniqueness of equality, with an exact global certificate rather than numerical evidence. A full symmetry-class resolution of an open conjecture is a motivated mathematical advance even though the scalene case remains open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
