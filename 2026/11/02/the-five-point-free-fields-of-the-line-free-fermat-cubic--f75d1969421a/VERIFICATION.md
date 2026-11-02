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

The standalone `verify.py` uses only Python 3's standard library and contains no downloaded data or external executables. Run `python3 verify.py` and compare its stdout byte-for-byte against `verify_output.txt`. A completed reproduction from the actual packaged paths produced identical output ending with `VERIFY_OK`.

Exact integer cyclotomic arithmetic computes all 351 pairwise line determinants and all 2,925 triple-line maximal-minor norm gcds. Histograms are `pairs={0:135,3:162,9:54}` and `triples={0:18,1:702,3:1944,4:27,9:234}`. Nonzero values have no prime divisors outside two and three. These are the critical universal incidence tests.

Independent finite-field point enumerations include fields of sizes 2, 4, 8, 16, 5, 7, 11, 13, 19, 25, 31, 37, and 49, checking the whole surface and geometric-line union. Additional quadratic-field checks for ground fields of sizes 2, 5 and 11 verify the nonsplit geometric-line descent statement. Zeta functions are checked against the polynomial formulas in each of twelve extension degrees for each test field.

The code's exact finite-field enumerations test particular fields, not all finite fields. The general proof relies additionally on the algebraic determinant-norm certificate, the classical complete list of geometric lines, the nonsplit Frobenius argument, and the standard surface-cardinality formula. No external independent audit was performed.
