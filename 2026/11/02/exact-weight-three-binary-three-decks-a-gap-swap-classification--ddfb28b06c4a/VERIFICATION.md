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

# Reproducibility and verification

Run `python3 verify.py` with a standard Python 3 interpreter. The verifier uses no nonstandard dependencies and must print `VERIFY_OK` after enumerating all weight-three words for each length from 3 to 22 inclusive. The program compares actual deck equivalence classes with the invariant-fiber partition; checks every fiber has size at most two and the exact alternative-mate formula; independently evaluates the pair-count summation and coefficient extraction; and compares literal index-triple enumeration with an independent subsequence dynamic program for each length through 15.

These are finite corroborations. The all-length theorem is established by the algebraic identity of the deck and \((L,T,Q)\), quadratic root classification and exact combinatorial bijection stated in `RESULT.md`, not by the test range. The self-review passed; independent audit or human validation was not performed. The historical-priority limitations are listed in `REVIEW.md` and `AUDIT.json`.
