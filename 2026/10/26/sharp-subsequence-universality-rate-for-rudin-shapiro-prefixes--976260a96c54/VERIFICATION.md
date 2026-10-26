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

Run `python3 verify.py` from the directory containing this file. The script uses only the Python standard library. It reconstructs the four-letter substitution transducer, checks its precise even/odd transformation tables at 44 successive levels, compares the fixed-point coding against the independent parity-of-`11` arithmetic definition for 32768 symbols, and verifies subsequence universality directly on every binary word of lengths 0 through 12. It also checks the theorem's exact dyadic formula and all-prefix digit-sum discrepancy through 131071 symbols.

Expected final status: `VERIFY_OK`. The script's bounded tests confirm definitions and calculations. For arbitrary prefix length, correctness relies on the symbolic weighted-scanner induction and aligned dyadic-prefix decomposition in `RESULT.md`. No external mathematical audit or infinite exhaustive computation has been carried out.
