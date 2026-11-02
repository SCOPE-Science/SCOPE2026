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

# Verification record

The proof in `RESULT.md` establishes the arbitrary-length theorem. The decisive nonstandard steps are: (i) the exact equality criterion for rotated \(2\)-binomial profiles, derived by counting the cross-boundary ordered subsequences; (ii) the coprime-content divisibility of any balanced interval length; (iii) the observation that a circular interval has two boundary runs and cannot intersect three or more monochromatic runs partially; and (iv) the one-vertex change of the centered-prefix-vector multiset under an adjacent exchange.

Run `python3 checker.py` in a directory containing the supplied files. The checker requires only the Python standard library. It enumerates all 18,666 labeled words for eight fixed content vectors, independently compares complete pair-subsequence signatures with centered-prefix coordinates, checks both equality cases and every attainable value, and produces swap-path witnesses. Expected final line: `total fixed-content words inspected: 18666`.

Finite enumeration does not prove the claim for unbounded lengths; all general quantifiers follow from the written proof. The checker does not enumerate all possible content vectors, certify historical novelty, or perform an independent mathematical review.
