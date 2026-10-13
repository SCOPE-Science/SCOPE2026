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

The unrestricted theorem follows from exact Fourier and cyclotomic identities, an explicit torus phase-correlation law, continuous-time Kronecker density, and an exact relative-interior convex-density argument; it does not rely on testing an unbounded range of prime orders or time points.

Place `verify.py` and `examples.json` in the same directory. Execute `python3 verify.py`; it runs with Python's standard library only. The checker verifies 592 exact rational scalar identities for odd primes through 101; explicitly enumerates 752 root-permutation phase configurations at prime orders 3, 5, 7 and 11; and evaluates 20 independent Fourier-distance probabilities for approximate weighted observations at prime orders 5, 7, 11 and 13. The expected output is:

`VERIFY_OK exact_barycentric_identities=592 permutation_configs=752 numerical_fourier_distances=20 nonnegative_time_witness_orders=5,7,11,13`

The observation times and weights in `examples.json` are decimal floating-point approximations and hence are **not** exact equality certificates. Exact real times and weights exist by the analytic proof. No experiment resolves the optimal support size or bounds the required times.

Self-review was conducted on the stated finding. Independent audit was not performed.
