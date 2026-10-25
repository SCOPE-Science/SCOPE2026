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

# Verification and reproducibility

The exact-arithmetic program `verify.py` uses only SymPy, with the supported version range in `requirements.txt`. Run `python verify.py` from the package directory. The expected output is `VERIFY_OK 222 independent exact wheel damages, Green entries, pair identities, sign cases; bound`.

It constructs wheel Laplacians and direct zero-sum inverses on \(3\le n\le13\); verifies the single-spoke trace increment and two-spoke rank-two identity at every allowed distance, the closed cyclic Green and squared-Green entries, the exact five boundary signs, and the explicit geometric-series bound at \(m=4\). All equalities use exact rational or algebraic operations. No external data or randomized sampling is required.

These finite tests do **not** establish an infinite assertion. The universal claims rely on the written Green-kernel derivation, the algebraic Woodbury update, strict discrete convexity of the periodized kernels, the global geometric-series inequality, and the uniform asymptotic bound for distances proportional to \(\log n\). No independent audit has been performed.
