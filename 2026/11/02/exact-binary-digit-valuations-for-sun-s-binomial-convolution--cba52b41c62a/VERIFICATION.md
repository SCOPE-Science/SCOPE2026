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

# Verification and limitations

Run the standalone `verify.py` using `python3 verify.py`. It relies only on Python's standard library and independently recomputes binomial coefficients, direct convolution values, the finite transformed Clausen coefficient sum, the Sun–Guo denominator, the integral quotient, and exact powers of two.

Executed result:

`VERIFY_OK positive_indices=240 clausen_coefficients=241 normalized_quotients=240`

These are finite checks at indices \(0\le n\le240\). The proof in `RESULT.md`, rather than enumeration, establishes all positive indices. The classical Clausen identity and Guo's integer-divisibility theorem are cited external inputs; no independent audit or external formal certification is claimed.
