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
The standalone `verify_pal.py` (Python 3, standard library) generates each finite generalized Cantor word by two independent definitions: iterating the substitution and evaluating its base-\(q\) digits. It then directly enumerates all palindrome factors by exhaustive substring comparison and checks the closed indicator formula for \(3\le q\le9\), \(1\le n\le80\), and the length-zero convention. Run `python verify_pal.py` from this directory. A successful run prints `VERIFY_OK independent_base_digit_and_substitution q=3..9 palindromes_n=0..80 cases=560`.

The scan uses sufficiently long but finite substitution iterates; it cannot certify exhaustiveness in the infinite word. The all-length theorem is established instead by the separate valuation proof in RESULT.md. The literature comparison is limited to the inspected sources; no claim of independent scientific validation is made.
