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

The included `verify.py` is a standalone numerical consistency check for the formulas in `RESULT.md`, requiring Python, NumPy and SciPy. Run `python verify.py` from the directory containing this file and `verify.py`.

The deterministic seed checks 900 randomly sampled heterogeneous chains tuned to the same isolated-dimer optical squared frequency. For each sampled chain it checks the eigenvalue, its eigenvalue index, the exact zero-strain displacement mode, arbitrary positive changes to inter-dimer stiffnesses, loss of exact pinning on perturbing one internal spring, and finite-difference confirmation of the eigenvalue sensitivity identity. An additional 100 tests check the explicit geometric mode envelope in uniform mass dimers. All 5,500 test counts pass. Maximum measured eigenvector residual is less than \(10^{-15}\); finite-difference gradient errors are below \(2.6\times10^{-8}\).

Computational sampling does not establish uniqueness or assertions over infinite positive parameter domains. Simplicity, necessity, sufficiency, spectral index and arbitrary-coupling invariance follow from the analytic proof in `RESULT.md`. This numerical verification is not an independent scientific audit.
