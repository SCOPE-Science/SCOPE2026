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

Run `python3 artifacts/verify_book.py` using Python 3.10+ standard library. The result must match the embedded `artifacts/verification_output.txt` including `VERIFY_OK`.

The program builds each graph from its edge list, tests the original no-exactly-one-neighbor fort definition, independently enumerates all claimed minimal forts, and tests every vertex subset of cardinality at most the claimed minimum against the original zero-forcing rule for page counts 2 through 7. It tests the exact rational fractional assignment for page counts 2 through 30; the matching LP lower bounds are proved symbolically in the article.

The output records 87,354 exhaustive nonempty fort-subset checks and 34,896 subsets at or below the minimum zero-forcing size. Finite enumeration is not a proof for arbitrarily many pages. The all-size result relies on the full structural proof.
