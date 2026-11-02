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

# Verification

Run `python3 verify.py` using only Python 3 standard-library modules. This program independently checks the direct antisquare predicate up to order \(n+1\), the eight-factor predicate, the run-grammar predicate and the weight-resolved rational generating function on all binary strings of length 1 through 14 (32,766 source words); checks primitive necklace multiplicities by direct rotation orbits to length 12; and confirms the full-count recurrence and weight support through length 80. Successful output begins `VERIFY_OK` and includes `SOURCE_WORDS_CHECKED 32766`.

The direct antisquare tester is explicitly bounded to orders up to \(n+1\); it is a finite cross-check, not a test of arbitrarily long factors. The certificate is finite. The published complete minimal-antisquare classification and its periodicity obstruction are needed for the unbounded equivalence in the proof. The word count at length 80 verifies a recurrence only numerically; formal generating-function manipulation proves the recurrence for all lengths. No independent expert or external formal certification has occurred.
