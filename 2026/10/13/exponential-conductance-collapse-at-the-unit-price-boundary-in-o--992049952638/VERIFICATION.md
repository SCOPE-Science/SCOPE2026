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

# Verification

Run `python3 verify_hypercube.py` using a standard Python 3 installation; it requires no external packages. Observed output:

`VERIFY_OK 27 exact Kirchhoff inverse-spectrum identities; 225 exact Walsh eigenpairs; 180 bracketed scalar stationary points; finite tests do not prove the asymptotic theorem`

The exact tests construct every edge weight of 27 small priced hypercubes, invert the augmented Laplacian over rational numbers, and compare the resulting Kirchhoff indices to the binomial spectral formula. All nonconstant Walsh characters are tested as exact eigenvectors in these cases. Separate numerical root brackets and asymptotic diagnostics are finite reproducibility checks, not infinite-domain proofs.

The mathematical proof in RESULT.md establishes strict global uniqueness, the unique positive scalar solution, all three fixed-price limiting regimes, and the limiting index formula. It requires standard binomial concentration and the explicitly supplied moment arguments. It does not establish uniform behavior in a price window shrinking to one, and it has not been independently audited.
