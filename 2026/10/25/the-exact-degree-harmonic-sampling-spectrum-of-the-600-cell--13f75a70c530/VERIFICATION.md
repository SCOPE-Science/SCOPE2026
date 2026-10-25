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

# Reproduction and verification

Execute `python3 verify.py` from the directory containing the extracted files. The script has no nonstandard dependencies. It generates the 120 golden-ratio coordinates exactly modulo 101, checks norm and dot-product distribution, computes the Chebyshev Gram ranks in the field for all degrees 0–60, and compares them with independently computed affine-\(E_8\) multiplicity ranks. It also verifies that the recurrence has the indicated representation dimensions and its 60-degree shift. Expected terminal markers are `EXACT_FINITE_FIELD_GRAM_RANKS_PASS`, `MCKAY_MULTIPLICITIES_PASS`, `RANKS_0_59`, and `FULL_ODD_FROM_29_AND_FULL_BOTH_FROM_60_PASS`.

Mathematical proof of the infinite complex-field claims is given in `RESULT.md` and uses the group decomposition and exact trigonometric shift, rather than the finite-field experiment. The code does not constitute an independent external audit.
