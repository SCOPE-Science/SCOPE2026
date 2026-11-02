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

# Verification evidence

The integral dual proof and witness are verified by executing `python3 verify_certificate.py`, which depends only on the Python standard library. Its exact output is embedded as `verification_output.txt`.

The checker reconstructs the full universe of 243 five-words, all 216 nonpalindromic words, all 108 reversal pairs, and all six exceptional palindromic four-vertices; proves their three-in/three-out reversal pairing by explicit enumeration; sums the normalized pair weights to 486; checks the universal inequality for each of 216 edges; and verifies a period-93 word against all cyclic windows and their reversals. These checks are exhaustive for the finite order-five ternary universe, not probabilistic samples. No floating-point arithmetic or package dependencies are used.

The scientific proof of why the inequalities give a universal upper bound—the Eulerian cancellation, nonnegative reversal-pair allowance, and special-vertex degree cap—is written separately in `RESULT.md`. Source comparison and scientific limitations appear in `REVIEW.md` and `AUDIT.json`. No independent mathematical review has been performed.
