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

# Reproducibility

Execute `python3 verify.py` with a standard Python 3 interpreter. The verifier uses only the Python standard library and exact rational arithmetic for every claimed comparison. A successful run prints:

`VERIFY_OK 84 exact optimal designs; 10752 Walsh-Laplacian equations; 1440 irregular Rayleigh upper bounds`

It covers dimensions \(3\) through \(8\), eight rational prices covering both phases and the threshold, radial all-edge designs, sparse Hamilton paths, critical fractional forests, and nonuniform individual-edge Rayleigh comparisons. For smaller dimensions it explicitly evaluates the weighted Laplacian on every Walsh character. It does not enumerate all feasible networks, prove the continuum of cases, or resolve the historical-priority question; those scientific boundaries are handled by the analytical argument and cited literature comparison.
