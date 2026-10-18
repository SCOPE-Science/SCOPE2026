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

The claimed eigenspectrum follows by polar integration of the normalized Gaussian-window Hermite spectrogram. Its finite differences have an exact boundary expression; this gives all maximizing-mode indices and ties for all positive annular areas and all radii. The one-sided derivative jump at every crossing follows by differentiating that same boundary expression. Stirling expansion uniformly in the bounded offset between the maximizing Hermite index and the annular central area produces the periodic Bernoulli correction and an error of relative order \(O_w(c^{-2})\).

Run `python3 checker.py` (dependency: `mpmath`) to compare the incomplete-gamma integrals, adjacent-mode signs, exact switching/tie radii, derivative jumps, and large-radius coefficients. The numerical program tests finitely many parameters only. It is not an infinite-case certificate. Verification is same-model only; independent audit has not been performed.
