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

# Verification of the noncrossing variance theorem

The proof is analytical: every sorted-risk four-point crossing has a non-more-expensive uncrossing, a lexicographic span argument yields a globally noncrossing optimum, and an interval recurrence minimizes over all such pairings. Exact finite calculations support only the individual factorization checks, implementation, and explicit six-person extremum.

To reproduce, place `verify.py` and `verification_certificate.json` in the same directory and execute `python verify.py`. Compare its exact JSON output with the certificate. The verifier uses Python standard-library rational arithmetic and independently enumerates the underlying binary infection statuses for its size-six moment checks. Its result in the completed package was `all_checks_passed`.

The full certificate records 126 four-point rational checks, 219 complete risk profiles over sizes four/six/eight, 1260 exact size-six workload moment enumerations, and 15 full-matching cross-checks for ten-person risk profiles. It separately checks all fifteen matchings of the six-risk witness. Computations are finite; they neither establish literature originality nor replace the universally quantified proof.
