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

# Reproduction and limitations

Use `python3 artifacts/verify.py` from the extracted package root. Only Python's standard library is needed. The verifier enumerates all invertible matrices of size two over \(\mathbb F_2\) and \(\mathbb F_3\), and then all quadratic generator-substitution coefficients for each square-one linear part, directly composing the algebra maps modulo words of length three. It independently constructs the linear kernel equation, verifies rank/nullity for every square-one linear part of size three over \(\mathbb F_2\) and \(\mathbb F_3\), and separately tests the kernel count over \(\mathbb F_4\). Its expected markers are `VERIFY_OK` and `VERIFY_GF4_OK`.

The direct two-generator totals, including the identity, are \(304\) over \(\mathbb F_2\) and \(7534\) over \(\mathbb F_3\). The three-generator kernel-rank totals are \(134561792\) and \(7626343628152\), respectively. The field-of-four test gives \(69376\) for two generators. The general theorem uses an algebraic module decomposition, not exhaustive finite enumeration; none of these finite checks alone proves its full claim. No independent mathematical audit has been carried out.
