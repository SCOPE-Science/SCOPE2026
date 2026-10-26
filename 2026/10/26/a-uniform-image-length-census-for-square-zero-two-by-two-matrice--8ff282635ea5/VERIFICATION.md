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

# Reproducibility

Run `python3 verify.py` with Python 3 and no third-party packages. The program computes every entry of the square of every matrix in each finite ring, then calculates the image length using determinant valuation after factoring out the common entry valuation.

The polynomial-ring backend exhaustively checked ten cases: residue cardinalities 2 at lengths 1–5, 3 at lengths 1–3, and 4 at lengths 1–2. The residue-4 arithmetic is implemented as extension-field arithmetic. The modular-integer backend independently checked nine cases: primes 2 at lengths 1–4, 3 at lengths 1–3, and 5 at lengths 1–2. All nineteen sets of rank multiplicities agree with the theorem, including both equal-characteristic polynomial rings and mixed-characteristic integer rings. A sample 16-element residue ring of length four has 640 square-zero two-by-two matrices, with rank multiplicities 1, 9, 78, 168 and 384.

These are exhaustive enumerations only within the listed finite rings. The infinite theorem is established by the separate valuation-shell and trace–determinant argument in RESULT.md. No external audit has been performed.
