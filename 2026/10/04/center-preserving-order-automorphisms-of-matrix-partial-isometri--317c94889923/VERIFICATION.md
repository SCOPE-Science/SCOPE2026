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

Jia--Ji's full arXiv text gives \(\Psi_A(aI)=(a-1)(I-A-aA^*)^{-1}+I\) and proves the denominator is invertible for every \(a\in\mathbb T\). If two distinct nonidentity values have scalar images, then \(I-A-aA^*\) is scalar for each; subtraction forces \(A^*\), hence \(A\), scalar. Conversely scalar \(A=\alpha I\) makes the whole circle scalar. Substitution gives the stated fractional-linear formulas; the sign of \(1-2\operatorname{Re}\alpha\) puts the disk parameter inside \(\mathbb D\), and solving for \(\alpha\) proves surjectivity and uniqueness onto the Möbius/anti-Möbius stabilizer of 1. The same primary paper explicitly identifies \(A=0\) with identity, \(A=I\) with adjoint/conjugation, and proves these are exactly the orthogonality-preserving cases.

## originality

PASS

Jia--Ji completely classify order automorphisms and provide the scalar-unitary formula, but their paper does not isolate the subfamily preserving the center, prove two-probe rigidity, or identify its boundary action with the full Möbius/anti-Möbius stabilizer of 1. Molnar's older order-and-orthogonality theorem has only the identity/conjugation scalar behavior and does not cover the new non-orthogonality-preserving Jia--Ji family. No Resultary search found an equivalent center-preserving classification.

## value

PASS

The center is a canonical subset of the matrix algebra, and identifying exactly which exotic order automorphisms preserve it gives a clean rigidity test and a complete one-complex-parameter boundary dynamical model. The two-probe criterion is a structural lemma, not a numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
