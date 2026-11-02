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

# Reproducible verification
Execute `python3 check.py` in any Python 3 interpreter. The checker uses only the standard library. It constructs finite-field arithmetic for \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\) with explicit irreducible binary polynomials and exhaustively enumerates each coefficient tuple in the declared test ranges.

It checks the square-zero derivation condition by direct coefficient multiplication of \(f f'\) modulo \(t^N\), separately constructs the linear-component zero sets, confirms agreement for every tuple, checks all component dimensions and nested intersections, and verifies the formula \(c q^m-(c-1)q^{m-1}\).

The observed final marker is `SQUARE_ZERO_TRUNCATED_DERIVATION_COMPONENT_CENSUS_OK 22`. The mathematics is established by the independent valuation/coordinate proof in RESULT.md. Finite checks establish no claim of exhaustive coverage for all \(N\) or all finite fields. The checker does not compute the full nonreduced scheme structure; the universal nilpotent \(f_1\) is established algebraically in the proof. Independent validation is not performed.
