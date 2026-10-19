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

The analytic proof diagonalizes the magnetic cycle using Fourier characters and counts exactly the characters paired by their energies that lie in the kernel of the two-site evaluation map. Dissipativity and a reducing-subspace argument establish that the resulting count is the full nondecaying dimension and determines long-time averaged survival. The source model uses a fixed positive loss coefficient; no limit of weak trapping is taken.

`checker.py` was executed from its local content with `python checker.py` and reported 5,473 passing assertions. Tests include all separations for cycle sizes 3 through 45 at three flux classes, direct nullities of sampled energy eigenspaces, independently constructed dissipative spectra, and finite-time survival comparisons. It requires NumPy and SciPy and provides finite-size numerical checks rather than an infinite proof.

The primary 2009 trapped-ring result contains an even-cycle, zero-flux, perturbative-width expression and special configurations whose zero-width modes overlap this result. This is recognized as prior coverage. No claim of independent replication or external mathematical certification is made; independent audit remains unperformed.
