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

# Reproducibility and scope
The mathematical argument is self-contained modulo elementary regular-simplex geometry and the explicitly proved unsigned incidence identities. With an ordinary Python 3 interpreter, run `python3 checker.py` from the directory containing the embedded files. The observed outcome was `PASS: 262333 exact-integer assertions, m=4,...,18`.

The checker uses only Python's standard library; all Gram entries are multiplied by the integer \(m^2-1\), so no floating-point tolerance, random search, or external package is involved. It verifies the Gram-incidence identity, spectral first and second moments, an annihilating polynomial in the smaller dimensions, and nonnegative directions attaining the asserted stability coefficient. Inspect `RESULT.md` for the general proof. These finite checks are not a proof for unbounded dimension, nor a certificate of historical originality.

The valid domain is real integer \(m\ge4\), fixed regular-simplex midpoint Parseval frame and nonnegative Euclidean unit weights; no result for varied frame geometry, arbitrary projections, or the exceptional dimension three is asserted. No independent audit has been performed.
