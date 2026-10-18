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

# Verification scope

Run `python VERIFY.py` in a directory containing the accompanying standalone program. It uses only Python's standard library. Its exact-coefficient multiplication verifies the published rational-function definition against the displayed polynomial factorizations for 48 cases with \(1\le n,k\le8\) that fall in the polynomial branches. An independently coded cyclotomic-exponent formula tests the polynomiality decision for 1,800 parameter pairs with \(1\le n\le60\) and \(1\le k\le30\). It also checks the predicted \(q=-1\) residue in the complementary small cases.

The program returns `VERIFY_OK exact_polynomial_identities= 48 cyclotomic_cases= 1800` if all assertions succeed. Finite validation is not a proof for all parameters. The complete proof uses a telescoping identity, explicit nonnegative-factor expansions, and a nonremovable pole. The boundary \(n=1\) is handled separately, and the nonpolynomial case begins at even \(n\ge2\) with odd \(k\).

Independent external scientific validation has not been performed.
