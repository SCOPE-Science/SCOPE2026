---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The change of variables gives a monic squarefree degree-eight hyperelliptic model at i=2 modulo 5, so the reduction is good of genus three with two points at infinity. Independent finite-field enumeration gave 7, 43, 133 points and power sums -1, -17, -7, giving the stated numerator by Newton identities and reciprocity. For h(X)=X^3g(X+5/X), g is irreducible by the rational-root test and has discriminant 761. The product of the three quadratic discriminants is -49*71. At an unramified prime over 71, precisely one discriminant has valuation one (g and U^2-20 have only U=34 in common modulo 71); conjugation isolates each of the other discriminants as well. This proves square-class independence and the full wreath group. If a root satisfied alpha^2/5 equal to a root of unity, all its conjugates would have 5-adic valuation 1/2, impossible because the middle coefficient 11 is a unit. The independent pair swaps then exclude root-of-unity quotients between different pairs as well. Powers of the roots thus remain distinct and transitive, giving irreducibility over every finite extension in the sense of the Frobenius polynomial over Q. This excludes a proper abelian subvariety. A complex splitting would give a nontrivial rational endomorphism idempotent defined over a finite number-field extension (endomorphisms are unchanged under algebraically closed base extension); good-reduction specialization injects rational endomorphisms, contradicting geometric simplicity of the reduction. A map to genus one or two would yield a positive-dimensional proper Jacobian quotient by push-pull. The finite checks are arithmetic certificates, not a replacement for the group and specialization arguments.

## originality

PASS

The explicit curve and its geometric and amoeba analysis are prior work. The supported distinct result is the geometric simplicity of its Jacobian and the explicit finite-field certificate establishing it. The strongest same-object text does not assert or imply this invariant, and the closest indexed arithmetic examples concern other curves. This is a best-of-current-evidence judgment, not a priority certificate.

## value

PASS

This computes a substantive intrinsic invariant of a previously singled-out genus-three example, not an arbitrary coefficient choice or a point-count table entry. It rules out splitting and all lower-positive-genus quotient morphisms for that curve via a small exact arithmetic certificate. No generality beyond the specified curve and reduction is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
