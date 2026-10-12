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

# Reproducibility

Using Python with NumPy and SciPy, run `python verify.py`. The checker constructs the adjacency tensor Hamiltonian and determines each detector-visible eigenspace using singular-value decompositions, not using the stated formula as a computational shortcut. It compares its independently computed spectral dimensions and all localized capture projectors against the theorem for \(3\le L\le7\), including generic positive hopping ratios, equality, and the potentially overlapping \(1:2\) and \(2:1\) energy ratios. It separately evolves four non-Hermitian models with nonuniform positive reaction rates and compares twelve long-time norms with spectral survival.

Expected replay line: `VERIFY_OK spectral_cases=25 sitewise_probabilities=950 projector_idempotence=25 loss_dynamics=12`.

Critical noncomputational checks: the physical no-reaction generator is contractive; the nondecaying subspace consists exactly of loss-free eigenvectors; the leaf-difference product Gram matrix is positive definite when \(L\ge3\); and all coincident-energy detector images have the ranks used in the proof. Long finite-time evolutions and finite sizes do not prove general capture, publication priority, or robustness to altered hypotheses.
