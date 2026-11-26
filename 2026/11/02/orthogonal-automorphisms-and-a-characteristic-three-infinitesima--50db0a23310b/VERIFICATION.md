---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and scope

The scheme-level proof is in `RESULT.md`. It uses mixed products to determine the block-diagonal open over arbitrary coefficient algebras and shows that this open, together with its exchange translate in the balanced case, covers the scheme. The finite factor \(\mu_3\) accounts exactly for the characteristic-three tangent defect.

`verify.py` is a standard-library Python diagnostic that can be run with `python3 verify.py`. It counts automorphisms in small rational-point examples and assembles the Leibniz equations in seven small prime-field cases, including characteristic three. The rational-point counts illustrate the distinction between field-valued points and the scheme; these calculations are not a proof of its structure over general coefficient rings. No results in characteristic two or with a noninvertible part size are asserted.
