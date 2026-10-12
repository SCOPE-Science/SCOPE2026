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

# Verification of bounded-run binary bigram-profile enumeration

Run `python3 verify_profile.py` and `python3 verify_identity.py` from the directory containing these files. Both programs use only the Python standard library. The first builds all admissible binary strings with \(1\leq n\leq17\) and \(1\leq h\leq5\); it reconstructs each exact bigram-profile fiber, independently verifies its binomial/bounded-composition count, and constructs a valid representative. It checks the rational generating-function coefficients for \(1\leq h\leq20\), \(1\leq n\leq500\). At \(h=2\) it also compares the twelve-residue formula and counts singleton fibers. The second compares the cleared-denominator rational generating function and quasipolynomial series by exact polynomial arithmetic, establishing an identity rather than only sampling coefficients.

Observed terminal outputs:

`VERIFY_OK brute_h_1_to_5_n_1_to_17; exact_fibers; canonical_representatives; rational_h_1_to_20_n_1_to_500; h2_quasipolynomial_singletons`

`IDENTITY_OK rational_GF_h2_equals_exact_period12_quasipolynomial`

The proof for all lengths and run caps is the exhaustive run-count case distinction and formal power-series summation in `RESULT.md`. Finite exhaustive tests do not independently establish infinite statements; the exact polynomial identity and algebraic proof cover them. No noisy-spectrum, incomplete-coverage or error-correction guarantee was tested or asserted.
