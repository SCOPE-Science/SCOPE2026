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

# Reproducibility and limits

The standalone Python checker `checks/jordan_census.py` builds polynomial multiplication modulo \(x^3\) and \(y^3\) from monomial exponents. It computes the ranks of \(m_f\) and \(m_{f^2}\) by finite-field elimination, not by the closed-form classification. It compares the resulting Jordan partitions against each proof stratum.

The \(\mathbb F_3\) test is exhaustive across all \(6561\) radical elements, and also checks generator-pair equivalence and counts all \(3280\) order-three subgroups. The \(\mathbb F_9\) test uses a genuine degree-two extension-field model, with \(1800\) deterministic pseudorandom tuples plus \(2916\) targeted quadratic/cubic checks. Discriminant-zero conics are enumerated independently in both fields. All tests matched the theorem, with marker `MODULAR_C3xC3_MULTIPLICATION_JORDAN_OK`; expected exact output is `checks/output.txt`.

Run `python3 checks/jordan_census.py` from the extracted package directory; only Python standard-library modules are needed. The computation establishes the stated finite cases, not a proof for all fields or extension degrees. The general proof is in `RESULT.md`.
