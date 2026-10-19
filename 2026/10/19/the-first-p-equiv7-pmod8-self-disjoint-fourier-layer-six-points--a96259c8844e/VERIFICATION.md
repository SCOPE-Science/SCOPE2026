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

# Exact verification

Execute `python3 artifacts/verify.py`. The checker uses no packages beyond the Python standard library and uses exact integers only. It lists every subset containing the origin of sizes 1 through 6, performs Gaussian elimination over four finite fields containing a primitive seventh root, uses the full 720-term signed determinant to certify all surviving singular sets, then computes the orbit partition under the 96 dot-product similitudes and 49 translations.

Observed normalized set counts: 1, 48, 1128, 17296, 194580, 1712304. The successive six-element modular-survivor counts are 57360, 960, 672, 672, with 672 exact cyclotomic zeros. For cardinalities at most five, no candidate survives all four modular checks. The computed global count is 5488, with orbit sizes 2352, 784, 2352. Successful reruns report `VERIFY_OK`.

The arithmetic proof reduces the full characteristic-zero claim to this complete finite exhaustion. The calculation is not a floating-point approximation. The precise hypothesis is the standard dot product on the 49-point affine plane, not an arbitrary field size or pairing. External independent audit has not been performed.
