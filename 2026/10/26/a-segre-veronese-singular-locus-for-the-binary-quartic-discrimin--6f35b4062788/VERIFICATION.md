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

For k algebraically closed of characteristic 3, the verified RESULT.md gives Δ=U³+C²U²−C³(AD²+B²E)+AEC⁴, U=AE−BD. Direct symbolic differentiation verifies Jacobian vanishing on Q=(C,U) and the quadratic-square image V. The root-partition argument shows every discriminant quartic outside Q∪V has one ordinary double root with two distinct simple roots and is étale-locally a unit times the quadratic discriminant; since 4 is invertible, the hypersurface is smooth there. Q is the rank-one 2×2 Segre quadric image L³M, with degree-three Frobenius on the first P¹. The quadratic square map is a degree-four Veronese surface. Pullback of (C,U) to V is the single smooth conic (t²−su), yielding a scheme-theoretically reduced rational quartic L⁴ and the Frobenius graph. An independently implemented exact F3 check enumerated all 121 P⁴(F3) points and found 25 singular =16 Q +13 V−4 intersection. Finite points only cross-check the geometric proof.

## originality

PASS

Targeted source and implication comparisons did not identify prior coverage of the precisely scoped final theorem; best-of-knowledge PASS with named residual risks, not a priority certificate.

## value

PASS

The modular inseparability changes the classical triple-root image from a characteristic-zero root-partition surface into a smooth Segre quadric, and its intersection with the square Veronese is a Frobenius graph. Identifying both components, degrees and scheme-theoretic intersection is a natural complete classification of the reduced singular support for a central discriminant, beyond routine normal-form substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
