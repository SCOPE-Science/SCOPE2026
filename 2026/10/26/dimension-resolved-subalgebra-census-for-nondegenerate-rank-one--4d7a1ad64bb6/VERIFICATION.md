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

# Computational reproduction

Run `python verify.py` in a directory containing this document and the included `verify.py`. Python standard library only; no packages, network connection or external data are required. Expected terminal prefix: `VERIFY_OK cases= 75 subspaces_examined= 81142`.

The verifier represents each subspace by a unique reduced row-echelon basis, evaluates algebra products on all pairs of basis rows and checks membership in that subspace. It independently evaluates the predicted Gaussian-binomial/polar-count formula. It includes prime fields of sizes \(3\), \(5\), \(7\) and the order-nine field with irreducible relation \(\omega^2=-1\). Both isotropic and anisotropic distinguished vectors are tested where available.

These exhaustive finite samples verify the stated instances, not the general theorem. The unrestricted formula and modularity obstruction follow from the arguments in `RESULT.md`. This is not an independent audit.
