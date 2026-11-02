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

The precise mathematical claim and its proof are in `RESULT.md`; the executable `verify_sparse_cmi.py` contains only finite consistency and asymptotic checks and is not an infinite proof. Run with `python verify_sparse_cmi.py` after installing NumPy and SciPy. On the tested environment, the script completed successfully with 90 deterministic assertions. Tests comprise direct configuration-space three-time joint probabilities on cycles of sizes four and six (for grand-canonical and exactly half-filled canonical stationary ensembles), uniformly connected versus perturbed hub generators, finite-cycle Fourier/theta comparisons, and large-time Bessel comparisons.

The graph iff statement is proved by the spectral measure of the one-particle Laplacian, including strict positivity and the zero-eigenspace normalization. The hydrodynamic and infinite-chain limits are proved analytically by Fourier dominated convergence, small-correlation expansion, and the Bessel heat kernel. The numerical tolerances in the script are used only for finite approximations, not to certify uniqueness, infinite asymptotics, or the originality assessment.

Independent mathematical and publication-priority review: not performed.
