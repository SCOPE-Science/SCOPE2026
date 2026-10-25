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
# Verification notes

The standalone `verify.py` requires Python 3 with only standard-library modules (`decimal`, `math`). Run it from a directory containing the embedded file:

`python3 verify.py`

The test constructs the lower Wythoff sequence with exact integer square roots, the upper Wythoff sequence by its exact offset formula, and the entire pair-sum convolution through \(n=4500\). It independently reconstructs counts from membership in the complementary sequence and from the orbit/floor representation with 85-decimal-place arithmetic. It confirms the OEIS initial values, Beatty complementarity, the three-piece profile, uniform finite errors, and total mass of the mixture. One actual execution returned:

`VERIFY_OK exact_convolution_n=4500 rotation_n=4500 Beatty_partition=PASS profile=PASS max_error=1.821120@3025 law_mass=PASS`

These finite checks do not prove an infinite discrepancy estimate, the weak limit, or the Wasserstein bound. Those statements are proved by the Fibonacci-denominator block argument and equidistribution in `RESULT.md`. The high-precision test is supplementary and does not constitute external verification.
