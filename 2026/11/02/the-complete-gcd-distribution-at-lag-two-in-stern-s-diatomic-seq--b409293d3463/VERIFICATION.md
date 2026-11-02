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

# Reproducibility and limits

Run `python3 verify_stern.py` in a Python 3.9+ environment; it uses only standard-library modules. It reconstructs the Stern recurrence, checks the exact closed gcd identity at all 262144 initial indices, and checks primitive congruence-pair fractions directly for moduli below 100. It prints the formula and empirical divisor densities for small odd moduli and ends with `VERIFY_OK` if successful.

The infinite density result is proved using the published uniform modular distribution of primitive adjacent Stern pairs (Reznick, Theorem 4.7), the new lag-two identity, and a geometric run-length tail. The code does not and cannot certify the infinite modular equidistribution theorem; no independent external audit has been performed. The numerical approximation of the coprime-frequency constant is an absolutely convergent Möbius series, with a geometric bound on omitted terms.
