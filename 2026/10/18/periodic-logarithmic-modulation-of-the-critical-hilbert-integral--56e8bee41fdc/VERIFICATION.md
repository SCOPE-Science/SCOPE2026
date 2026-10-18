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
# Verification details

The theorem is verified analytically in `RESULT.md`: a Hilbert–Schmidt kernel comparison, two explicit unitaries, periodic weakly-null translation lower bounds for the essential norm, Bloch-fiber positivity, and isolated simple-eigenvalue perturbation.

Run `python check.py` with NumPy installed as specified in `requirements.txt`. This checked the finite-section Fourier representation at three fixed frequencies and six signed nonzero amplitudes per frequency, the exact unperturbed constant \(2\), amplitude sign symmetry, the rigorous lower bound and agreement with the computed quadratic coefficient within the stated finite-amplitude tolerances. It does **not** verify the infinite-dimensional compactness, Bloch identity, or asymptotic remainder independently.

No independent audit has been performed. Priority remains subject to the related classical periodic/weighted Hardy literature. No claims beyond the stated fixed-frequency continuous Hilbert-integral model have been checked.
