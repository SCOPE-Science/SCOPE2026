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

The analytic bounds and the length-fourteen classification are proved by run-center constraints and a shorter-unique-palindrome contradiction in `RESULT.md`. The executable `verify_sups.py` directly constructs a frequency table of all contiguous substrings, finds unique palindromes and tests every query interval in each finite target word. All \(6944\) words with at most five runs and lengths \(1\) through \(14\) were covered. Exactly four distinct words of length \(14\) had a query with three shortest unique palindromes; the unique query interval for each is a singleton. The verifier also checks all three predicted factor positions for \(48\) members of the infinite family and samples \(2400\) additional interval queries on larger low-run words.

Run `python3 verify_sups.py` with a standard Python 3 installation; no third-party package is required. The finite computation cannot prove the unbounded family or general upper bounds and must be read alongside the full mathematical argument. The literature comparison was made against accessible general SUPS results; historical originality beyond that scope remains unverified. No external independent validation has been performed.
