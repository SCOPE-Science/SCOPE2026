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

# Verification details

Run `python3 verify.py` with the Python standard library. In this package's working directory it returned `VERIFY_OK 1490 alpha 1.79328213290076 bound 1.298425607525639 mu200 1.296345920324350`.

The code performs exact rational comparisons between a polynomial antiderivative for polar volume and the independent closed integral for dimensions 2 through 18, compares two normalized-product expressions, and numerically examines maximizers for dimensions 2 through 200 and dimensional scaling for multiple parameters. Floating-point tests permit machine-epsilon ties where values saturate. The all-dimensional derivative argument, strict inequalities, and limiting maximization are analytical claims, not consequences of those tests.

Historical-priority uncertainty remains, particularly possible older equivalent unconditional-body or shadow-system formulations. The public mathematical sources listed in RESULT.md were compared; independent scientific review has not occurred.
