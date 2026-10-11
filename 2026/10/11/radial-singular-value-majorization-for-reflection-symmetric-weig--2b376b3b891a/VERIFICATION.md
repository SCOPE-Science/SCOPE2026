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
# Reproducibility and verification limits

Install dependencies from `requirements.txt` and execute `python verify_weighted.py`. This checks the exactly simplified transfer determinant using symbolic arithmetic; the exact first-moment asymmetry for the specified nonsymmetric weight; numerical equality of transfer diagonal entries and compressed singular spectra for representative symmetric weights and complex parameters; and a finite-dimensional failure for a nonsymmetric weight. The recorded execution returned `WEIGHTED_VOLTERRA_TRANSFER_OK`.

These checks do not prove the infinite-family theorem. Its proof consists of the inverse-domain identification, self-adjoint boundary form, transfer-matrix reduction, reflection argument, radial convexity of Ky Fan sums, and strict convexity of Schatten norms. The numerical finite-rank compressions only test representative consequences. No independent audit has been performed. Bibliographic equivalence outside inspected sources remains unresolved.
