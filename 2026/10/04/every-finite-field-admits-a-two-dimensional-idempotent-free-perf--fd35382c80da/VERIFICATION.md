---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Direct reconstruction of the six actual assigned source files proves the displayed statement with no characteristic restriction. The natural-basis structure matrix [[0,1],[1,d]] has determinant -1, so E_d^2=E_d and every derived term remains E_d. For x=a e1+b e2, x^2=b^2 e1+(a^2+d b^2)e2. Thus x^2=x implies a=b^2 and either a=b=0 or b != 0 and d=b^{-1}-b^2. Since |F_q^×|=q-1<q, at least one d avoids the image and all nonzero idempotents. Every one-dimensional algebra has e^2=lambda e; lambda=0 is solvable, lambda!=0 gives nonzero idempotent lambda^{-1}e. This proves minimum dimension 2 also for characteristic 2. Independent from the package verifier, exhaustive finite-field arithmetic checked all d and all (a,b) over q=2,3,4,5,7,8,9,11, including proper extension-field arithmetic; results agree. No infinite conclusion is inferred from these finite checks.

## originality

PASS

Best-of-knowledge PASS for the sharp all-finite-fields existence/minimum theorem, qualified by its very elementary proof. González Nevado (2019/2025, Example 44) and Hu–Wen (2026, Remark 2) give only a two-dimensional F3 case. The 2023 full classification includes precisely the structural E_d family but its inspected statements do not determine which finite-field parameters are idempotent-free or give the universal all-q omission argument. García-Martínez–Pérez-Rodríguez Theorem 3.5 applies to C, not to finite fields. Fresh Resultary and primary-literature alias/parameter/implication searches did not locate a covering earlier all-q theorem; this is not conclusive novelty proof, and all identified priority risks are recorded.

## value

PASS

The exact minimum-dimensional obstruction across every finite field is a natural and mathematically motivated field-boundary question arising from the recent complex solvability–idempotent conjecture and the previously isolated F3 exception. It sharpens the field-dependent behavior by including characteristic two and every prime-power extension and gives a uniform parameter-exclusion witness mechanism. The proof is elementary but the universal sharp field boundary is not a textbook restatement, arbitrary slice, or mere recomputation of the known F3 instance. It does not count isomorphism classes or parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
