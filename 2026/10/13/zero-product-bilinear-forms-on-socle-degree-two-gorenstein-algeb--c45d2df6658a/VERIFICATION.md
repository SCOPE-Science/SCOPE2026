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

In the graded split algebra any element outside m=V⊕kz is a unit by nilpotence, so a nontrivial zero product has both arguments in m and is equivalent to β(u,v)=0. Products with z force the z-row and z-column to vanish on m. For each u≠0, b(u,−) on V is proportional to β(u,−); independence for two independent vectors and comparison at their sum make the proportionality constant, and nonzero multiples have the same constant by bilinearity. This proves necessity and sufficiency over every listed field, including when β is alternating. The free unit row and column yield dimension 2d+4. Evaluation at the unit makes the multiplication pullback injective; its equalities are ℓ=r and c=e=λ, whereas symmetry only requires ℓ=r and c=e. The symmetric and unrestricted quotient dimensions are thus 1 and d+2. Direct row/column expansion gives −ceλ^d det(B); counting the free and nonzero parameters yields all four stated counts, including precisely zero nonsingular symmetric nonfactorable forms at q=2. Surjectivity of multiplication also gives the stated tensor dimensions. Inspected RESULT.md, VERIFICATION.md and verify.py without running the supplied script. A fresh constraint-nullspace enumeration in d=2 gave constraint rank 8 in each case: over F₂ with either the alternating Gram matrix or I₂ the nonsingular total/symmetric/factorable counts were 32/8/8; over F₃ with I₂ they were 1944/108/54. These are bounded checks; the determinant and orthogonality proofs are general.

## originality

PASS

The general zero-product tensor formalism and qualitative local failure are prior coverage, and a distinct indexed theorem overlaps exactly in the split hyperbolic d=2 case. The supported distinct result is the normal form, symmetric defect and nonsingularity census uniformly across d and multiplication forms, in ordinary zero-product characteristic two as well as odd characteristic.

## value

PASS

The result quantifies rather than just detects failure of zero-product determination in a standard local Gorenstein family. It isolates a one-dimensional symmetric defect despite a much larger full defect, and shows exactly when symmetry and nonsingularity still permit nonfactorization. The sharp F₂ distinction and uniformity across multiplication form types give the census a use beyond restating qualitative non-ZPD.

The dated certificate retains the supplied scientific assessment, sources and limitations.
