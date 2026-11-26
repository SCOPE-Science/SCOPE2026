---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Put m=(q−1)/3. The cyclic subgroup H has order 4m, with intersection with F^× of order gcd(4m,3m)=m, exactly its cubic subgroup C. The Frobenius ratio h^(q−1) has order four because the kernel of this power map on H is C. Consequently its sum with its inverse is zero, and T²/N=2 for trace T and norm N∈C. In the order-three group F^×/C, squaring is invertible, so T lies in C exactly when 2 does. Modulo the subfield, h² projects to Tu by its quadratic equation, and h³=h⁴(T−h)/N projects to −(h⁴/N)u, a scalar in C times u since −1 is a cube. Projection is a bijection on each nonzero coset onto its corresponding cubic coset. For each x, a given h' in its projection fiber contributes exactly one representation, with a=x−h'. This yields the stated zero-fiber count, the nonzero counts 3 or 2 and 1, and the cardinalities and complements after multiplying by q. This argument works in every permitted characteristic and for nonprime base fields. Independent exact check: python3 /workspace/branches/independent_checks.py 2, output /workspace/branches/independent-2.txt; it covers every additive quotient fiber for q=7,31,343, both branches, and a nonprime base (q=343 gives 39,445 covered elements). These examples are corroboration, not an exhaustive proof. The frozen verifier was inspected, not executed.

## originality

PASS

The supported distinct result is the exact quartic-quotient cubic-class fiber law, not the projection method or the general necessary covering bound. The nearest explicit example classifies a different subgroup and does not supply this distribution. No checked source covers the claim; this is a bounded comparison, not a priority certificate.

## value

PASS

This is the next natural projective quotient size after the cited order-three covering example, and a family at the boundary of the prior necessary covering bound. The result resolves not only failure of that bound to be sufficient but the size, location and ordered representation counts of the deficient fibers, distinguishing two persistent arithmetic regimes. These are useful precise data for the subfield-translate problem; no classification at other indices is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
