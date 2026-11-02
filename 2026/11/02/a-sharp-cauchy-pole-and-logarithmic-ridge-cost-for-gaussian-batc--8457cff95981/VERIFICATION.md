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

Run the bundled Python-standard-library verifier with `python3 verify.py`. It performs exact-rational regression/Polyak identities at five minibatch sizes, gamma-integral comparisons for 12 parameter settings, exact variance identities for 16 settings, and 570,000 seeded diagnostic Gaussian samples. It is deliberately a finite checker: no numerical simulation certifies the sharp tail, invariant moment class, or logarithmic ridge asymptotic. Those are established by the displayed conditional-density, chi-square and affine-series proofs in `RESULT.md`.

All assumptions for the statement are explicit: positive error variance, deterministic initial point, independent Gaussian covariates and errors, finite \(k\ge2\) for the pole and ridge, and fresh independent minibatches for the stationary-law comparison. The calibrated \(k=1\) Cauchy case is an additional exact boundary check. The `verify.py` file requires no third-party library or network access. Independent mathematical audit is not yet performed.
