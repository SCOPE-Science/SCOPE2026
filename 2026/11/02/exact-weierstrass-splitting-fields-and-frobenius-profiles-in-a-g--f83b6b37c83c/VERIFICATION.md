---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For U(t)=t(t²+1)(2t²+1)(t²+2)(t²−1)(t⁴+t²+1) nonzero, the quartic identity Q_t(x)=(4t²x²+1)²+16(t²+1)(t−1)²x² and A²=t²+(t²+1)B² yield quartic roots i(εA+δB√(t²+1))/(2t²). The two other branch roots are ±√(-t)/2. Difference of quartic roots recovers i and i√(t²+1), and hence s; quadratic roots recover √t. The resultant 256(t−1)^4A^4 excludes collisions. Distinct root actions follow directly by applying signs under any Galois automorphism. In Fq, each sign is χ(-1),χ(t²+1),χ(t); q ≡ 3 mod 4 has opposite quadratic-pair fixedness. External Jacobian isomorphism is correctly cited as Abdellatif Theorem 2, not independently proved. Confirmed polynomial identities/resultant with fresh SymPy and direct character-root counts for all admissible t in prime fields 5..31. Full field proof, not finite enumeration, proves universal part.

## originality

PASS

Abdellatif supplies the same curves and unpolarized Jacobian isomorphism, not an explicit family-wide six-root splitting-field equality and opposite branch Frobenius permutation profiles. Howe previously established broader arithmetic disparity for other isomorphic-Jacobian families. Novelty here is the explicit field and full Galois actions, not the construction or general phenomenon.

## value

PASS

The Weierstrass branch divisor and its Frobenius representation are natural genus-two arithmetic invariants that measure precisely what unpolarized Jacobian isomorphism does not preserve. Explicit formula for the entire parameter family is mathematically usable and not a mere sample curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
