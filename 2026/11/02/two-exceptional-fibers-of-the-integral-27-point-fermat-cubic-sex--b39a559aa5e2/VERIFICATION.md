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

The accompanying exact verifier checks the integral polynomial degrees, the characteristic-two equality on the cubic, the characteristic-three local ideal by a Gröbner remainder, and the complete nine-point rational support over the four-element field. It checks three rational points over the prime field and six further points. The polynomial proof in `RESULT.md` establishes all-prime reducedness, finite flatness, and the relative group-scheme interpretation; computational tests do not certify unbounded prime quantifiers. The verifier requires Python 3 and SymPy and prints `FERMAT_CUBIC_27_SEXTACTIC_BAD_FIBERS_2_3_EXACT_OK` on success.

Independent mathematical audit: not performed.
