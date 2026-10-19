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

# Verification and reproducibility

The accompanying `verify.py` is self-contained apart from NumPy. Invoke `python verify.py` in its directory. It checks exact characteristic-coefficient expansions and quadratic discriminants using Python rational arithmetic, deterministic companion-matrix eigenvalues across full-interval sample grids, and the normalized Joukowski identity for the constructed minimax controller.

The mathematical proof itself uses exact algebra, the Joukowski inverse map, and the Schwarz lemma with equality characterization. The finite checks do **not** establish uniqueness or an inequality for infinitely many controllers or interval values; those assertions follow from the proof in `RESULT.md`. The tests do not cover perturbations in input gain, time-varying switching, or arbitrary dynamic compensators.

The motivating 2026 manuscript was inspected in its accessible full HTML text, including its scalar counterexample, FIR policy definition, and main convergence theorem. The closely related 1990 interval-Schur-stability article could be examined only through accessible abstracts; this limits the originality comparison. No independent audit has been performed.
