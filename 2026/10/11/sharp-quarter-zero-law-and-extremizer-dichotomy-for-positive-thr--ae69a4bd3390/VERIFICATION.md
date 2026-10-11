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

Run `python3 verify_positive_three_sparse.py` using Python 3 and its standard library. The checker uses the exact quotient \(\mathbb Z[X]/(X^{N/2}+1)\) to evaluate dyadic Fourier sums with rational integer weights and the algebraic weight \(\sqrt2\). The latter is expanded exactly as the sum of two eighth roots of unity. A successful run prints:

`VERIFY_OK rational_trials=35658 strict_geometry_cases=24816 integer_and_quadratic_extremizers=13`

The checker enumerates the displayed finite ranges and exact witness families through order \(256\). The proof for every power-of-two order uses the injective phase map, triangle rigidity, and four-root geometry independently of any finite enumeration. No machine run establishes the originality of a mathematical statement; the separate literature comparison and residual access risks are recorded in `REVIEW.md` and `AUDIT.json`.
