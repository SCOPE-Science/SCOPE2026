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

The source file `verification/lieb5_flux_checker.py` reconstructs the Hermitian open-boundary graph Hamiltonian directly from three links per original grid edge. Running `python verification/lieb5_flux_checker.py` with NumPy prints ten flat-eigenstate residual/support tests at fluxes zero, half flux, two nontrivial rational fractions, and an irrational test value. The ten observed supports are 8, 12, and 14 as appropriate, for each energy sign, and the residuals are below 1e-12. Exhaustive enumeration within a 4 by 4 hub grid checks candidate support graphs with up to six original edges and minimum degree at least two.

This program is not an exhaustive proof for the infinite graph or for every real flux: the analytic matrix decomposition, cycle geometry and explicit theta amplitudes in `RESULT.md` supply that proof. The full Hamiltonian uses unit hopping; multiplying it by any positive t scales the energies without changing supports. No external or independent audit is asserted.
