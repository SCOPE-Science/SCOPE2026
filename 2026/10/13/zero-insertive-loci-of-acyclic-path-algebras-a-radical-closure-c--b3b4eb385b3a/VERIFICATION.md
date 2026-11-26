---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The commutative semisimple quotient kills each sandwich with ab=0; every positive-length path is a sandwich between distinct vertex idempotents, so the locus spans J. If J²=0, all arrows run from a source set to a disjoint target set, so the two summed vertex idempotents realize any radical element in one sandwich. If two arrows compose, keep the three vertices and those two labeled arrows and kill all others. This is a path-algebra quotient onto T₃, valid also with parallel or shortcut arrows. In M₃, UV=0 forces rank(U)+rank(V)≤3 and hence rank(URV)≤1. Thus every radical element with both chosen arrow coefficients nonzero is excluded. This proves nonadditivity and the count of (q−1)²q^(d−2) excluded coefficient choices. In T₃, if either simple-arrow coordinate is zero, the element is supported in the single corner E₁₁ X(E₂₂+E₃₃) or (E₁₁+E₂₂) X E₃₃, respectively as appropriate, proving sufficiency and equality q(2q−1). The zero or arrowless case is included. Read RESULT.md, VERIFICATION.md and verify.py without executing the supplied script. Fresh binary enumeration, taking the image of r↦arb for each zero-product pair via its values on path basis vectors, gave 6/8 for the line, 4/4 for the fork, and 20/32 for the line with the first arrow doubled; these are checks, not the universal proof.

## originality

PASS

Credit the known zero-insertiveness of individual paths and the prior full-matrix rank criterion. The supported distinct result is the radical-wide additive-closure classification for acyclic ordinary path algebras, with the universal sharp finite-field loss and the internal T₃ witnesses. The closest comparisons do not establish that combined statement.

## value

PASS

This determines when a natural ring-theoretic locus already equals its linear span rather than merely generating it. The classification singles out a minimal branching-in-time obstruction, a composable pair, and turns that obstruction into a sharp loss of finite-field elements. The value is in the uniform classification plus quantitative gap, not in the known rank inequality or a standalone small matrix count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
