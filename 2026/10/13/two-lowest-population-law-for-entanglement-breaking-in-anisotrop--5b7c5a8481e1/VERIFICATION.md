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

# Reproducibility and verification

Run `python verify_reset.py` after installing the dependency in `requirements.txt` with Python 3. The script uses deterministic spectra of dimensions \(3\), \(4\) and \(5\), reconstructs \(J\) from the stated channel, verifies all partial-transpose block eigenvalue signs around the predicted exact transition, evaluates the \(3^d\)-term cubic-phase product-projector sum, and compares the diagonal remainder entry by entry against the analytically predicted coefficients. It also checks three time points straddling the semigroup transition, including the boundary.

Expected and observed output:

`VERIFY_OK fullrank_PPT_and_phase_decomposition=16 Lindblad_thresholds=3`

The principal mathematical certificate is the fully spelled-out proof in `RESULT.md`, especially the exact phase-average identity and its diagonal residual inequalities. These checks do not independently certify originality or extend a finite computation to the infinite family. The theorem assumes positive stationary populations and at least three distinct eigenvalues in dimensions at least three. No independent audit has been performed.
