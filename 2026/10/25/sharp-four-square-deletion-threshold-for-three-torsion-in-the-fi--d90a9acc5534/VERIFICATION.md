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

# Exact verification

The attached `verify.py` uses only the Python standard library (Python 3.10+) and exhaustively generates all orbits with at most four forbidden squares. The output file records, for every representative, its independent labeled orbit size; the second-boundary rank; integral unit pivots, residual exact rank and residual gcd of the third boundary; the resulting second-homology free rank; and its deletion pattern category. Every integer operation is exact. The script includes `assert` checks for the rank-one 2-by-2 minor identities (including zero entries), the torsion classification, and the sum of orbit sizes to the full binomial counts. Run `python3 verify.py` to reproduce. The saved `verify_output.txt` records the successful execution, ending in `VERIFY_OK_CHESSBOARD_FOUR_DELETION_TORSION_THRESHOLD`.

The computational certificate covers the finite claimed domain fully, not just random or low-prime tests. It is not an independent external audit. Literature coverage and absence of unpublished equivalent results cannot be mechanically certified.
