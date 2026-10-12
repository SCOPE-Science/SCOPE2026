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

# Finite corroboration and proof boundaries

Run the included `verify.py` with Python 3.9 or later:

`python3 verify.py`

The recorded executable output was:

`VERIFY_OK digit_positions=131072 substitution_levels=17 dyadic_window_cases=2097153 full_parikh_levels=13 last_maximum=2584`

The script directly computes the binary-digit definition and separately generates the four-state substitution; their first 131072 positions agree. It checks the coordinatewise domination identity and Fibonacci count for levels 0 through 16, and every shifted dyadic window lying in this same finite prefix. It also verifies all Parikh weights for levels 0 through 12. The finite prefix does not exhaust the infinite word.

For the infinite statements, inspect the proof in `RESULT.md`. The essential checked-on-paper identities are \(D_k=0^{2^k}\), \(A_k=B_k+C_k\) coordinatewise, and the overlap decomposition into two consecutive aligned blocks. The sum of the cyclic rotation of \(A_k\) is constant, giving an upper bound for arbitrary shifted factors; the prefix itself attains it. The Fibonacci weight recurrence then determines the exact dyadic maximum. Arbitrarily long \(D\)-blocks guarantee zero-weight factors, and sliding windows traverse all intermediate weights. Monotonicity of maximal weight bounds nondyadic lengths between powers of two. No external audit or unbounded computation is represented as completed.
