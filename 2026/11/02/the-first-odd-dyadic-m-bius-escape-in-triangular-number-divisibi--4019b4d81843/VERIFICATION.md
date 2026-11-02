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

The accompanying `verify.py` is a standard-library exact-integer verifier. Run `python3 verify.py` from the extracted package directory.

It enumerates all divisors from trial-divided factorization of each target \(T(2^k)\) for odd \(1\le k\le35\), using the perfect-square characterization \(d=T(j)\iff8d+1=(2j+1)^2\). It compares every resulting complete interval with the table in RESULT.md. It recomputes the incidence Möbius function on the eight-point interval below \(2^{35}\), all earlier odd-exponent dyadic Möbius zero values, and 3,822 direct-versus-order-formula divisibility comparisons.

Observed output: `VERIFY_OK: 18 complete dyadic divisor intervals; first odd-power escape at 35;` followed by two lines identifying the eight-element Möbius calculation, the modulus-70 condition, and 3,822 comparisons.

The unlimited order formula and the infinite progression are proved symbolically in RESULT.md. No computation asserts all-exponent testing or a general asymptotic for \(\mu_T\). No independent audit is represented.
