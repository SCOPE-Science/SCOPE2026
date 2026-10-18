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

Run `python3 checker.py` with Python 3.9 or later; no third-party packages are required. The test prints seven strictly positive exact rational surpluses, followed by `ARCHIMEDES_INEQUALITIES PASS`, `SQUAREFREE_SAMPLES 18242`, and `ALL_CHECKS_PASSED`.

The checker verifies exact rational inequalities for the primes \(5,7,11,13,17,19,23\), checks the rational reductions used to place the interval endpoints, and checks all squarefree integers up to 30,000 against the predicted interval union. Computation does not prove the infinite tail assertion. For primes \(p\ge29\), the proof independently invokes Nagura's 1952 prime-in-short-interval theorem; the no-gap step is proved directly by a residual binary-subsums argument. No assumption of exhaustive numerical testing of infinitely many primes is made.

The review of published literature and the arithmetic verification are distinct. An unindexed equivalent result remains possible. Independent audit has not been performed.
