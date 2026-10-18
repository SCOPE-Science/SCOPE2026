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
# Reproducibility and verification

Run `python3 verify.py` from a directory containing `verify.py`. It requires only the Python standard library.

The checker performs 1,400 independent random local projected-polygon hull calculations (with deterministic seed) and compares their areas against the exact Gram-determinant formula; 198 exact-formula beta-product moment checks; 105 explicit gamma-ratio, complementary-dimension, and correction-factor identities; and a seeded 130,000-sample numerical beta-product check of the special four-dimensional two-plane case. Expected final output begins with `VERIFY_OK`.

The all-dimensional proof depends on the analytical graph and QR arguments in `RESULT.md` and the sharp global equality theorem of Ivanov (arXiv:2607.12072). The seeded Monte Carlo check is statistical evidence for one finite-dimensional identity, not an exhaustive or rigorous substitute for proof. Endpoint remainder bounds are justified by uniform Taylor expansions on compact spheres and the isolated maximizers, not extrapolated from test samples. No independent audit was performed.
