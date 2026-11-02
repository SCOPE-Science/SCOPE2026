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

# Reproducibility and limits

The proof is in `RESULT.md`. Run `python check_two_hub.py` in an environment with `numpy` and `scipy`. It reconstructs the actual dot-product Hamiltonian, checks conical witnesses over multiple odd sizes and exchange constants, verifies many random full-spin lower bounds, tests scalar minimization independently, evaluates the critical coexistence interval and the chirality formula, and performs direct nonconvex full-spin minimization at five sample parameters.

Observed result in the supplied environment: 3,901 assertions passed; maximum witness-energy absolute discrepancy approximately \(1.43\times10^{-14}\). Computational search is finite and cannot certify absence of exceptional configurations at larger \(n\). Global completeness and boundary cases follow from the analytic Fourier inequality and exact constrained minimization in `RESULT.md`.

No data external to the files in this package are needed for the numerical checker, aside from the stated libraries. The outcome is not an independent scientific audit. Source comparisons are qualified by the material actually inspected and historical priority may require further expert evaluation.
