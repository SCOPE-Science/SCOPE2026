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
# Verification scope

The proof in `RESULT.md` shows global strict monotonicity of the critical lift, uniqueness of the singular point, a sharp local inverse \(1/3\)-Hölder estimate, a Lyapunov–Schmidt normal form for the bifurcating inverse pair, and a compactness argument eliminating remote branches. The exact finite-path trigonometric identity \(\sum_i v_i^4=3/[2(N+1)]\) fixes the square-root amplitude.

Run `python verify.py` with Python, NumPy and SciPy to reproduce 66 finite spectral, cubic, and near-critical root diagnostics at a selection of matrix sizes. Computational convergence and root finding are not exhaustive proofs. The critical unique-inverse claim applies globally on the compact torus; the Hölder estimate is local; the branch expansion is asymptotic in the positive excess step for fixed finite dimension. No independent audit or validation has been performed.
