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

# Verification of the excluded-area identity

The closed formula follows from the planar mixed-area edge-support identity and a finite coprime residue argument. No asymptotic assertion depends on finite numerical extrapolation. The step that collapses the support sum to one cosine relies on the identity for a centered finite trigonometric progression; the exact phase is retained in the proof.

Run the included `checker.py` with `python3 checker.py`, using only the Python standard library. The checker reconstructs polygon Minkowski sums from their original vertices via an independent convex-hull algorithm and area formula. All 1,376 checks passed in the packaged copy: 1,360 direct finite polygon-hull comparisons, 12 sharp endpoint checks, and four numerical rotation-mean checks.

The finite tests check numerical geometry, not all polygon orders or continuously many angles. The unrestricted theorem, fold periodicity, and scaling limits are justified by the displayed algebraic and analytic proofs. The novelty comparison remains bibliographic rather than an independent priority determination.
