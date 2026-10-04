---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The focal source was checked at the exact formula
\[
U_a=(a-1)(I-A-aA^*)^{-1}+I
\]
and at the lemma proving the denominator invertible on \(\mathbb T\). For \(a\ne1\), this also makes \(U_a-I\) invertible.

The two-point argument was replayed symbolically: two scalar values give two equations \(A+aA^*=\gamma_a I\) and \(A+bA^*=\gamma_b I\); subtraction forces \(A\) to be scalar.

For \(A=\alpha I\), the two sign branches were algebraically factorized into standard disk-automorphism forms. The inverse parameterizations were substituted back and give respectively positive and negative values of \(1-2\operatorname{Re}\alpha\). The cases \(\alpha=0\) and \(\alpha=1\) reduce to identity and conjugation and agree with the focal source's orthogonality-preserving classification.

No finite computation is used as proof. The finding does not address non-normalized outer factors.
