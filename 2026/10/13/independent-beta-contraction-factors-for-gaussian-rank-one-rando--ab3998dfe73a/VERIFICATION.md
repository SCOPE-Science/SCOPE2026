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

Execute `python verify.py` with Python 3.9 or newer, standard library only. The expected output begins `VERIFY_OK`. The script enumerates exact rational RCGLS projection identities in dimensions two through five (including nonoptimal two-dimensional finite termination), then executes reproducible pseudorandom Gaussian path simulations in dimensions three, five, and nine. It compares the empirical first- and later-step means and second moments, and the product of two consecutive later factors, against the analytically derived independent-beta expectations. The finite tolerance is statistical, not an exact certificate of infinite-sample laws.

The proof independently establishes the distribution by conditioning on the past, projecting an isotropic Gaussian vector into the preceding-direction orthogonal complement, and using the chi-square decomposition of a spherical squared cosine. The same conditional law at all later times proves factor independence. A strong law for the logarithms of strictly positive beta factors proves the almost-sure exponent. The proof explicitly treats dimensions one and two separately. No proof relies on a simulated run.

Unproved by this package: any similar factor independence for a nonidentity matrix, any finite-precision stability conclusion, practical speedups, or exhaustive uniqueness in previous literature. The scientific status is self-reviewed only.
