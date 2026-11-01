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

# Reproducibility and limits

The embedded `checker.py` was executed from the extracted package using standard Python 3. It passed 102 arithmetic, peripheral-phase and sampled-Fourier consistency assertions across nine example measures, with centered, noncentered and lattice-periodic examples. Sampled frequency maxima were compared with the asymptotic constants at `n=6400`; this numerical exercise is not a proof of the continuum maximization or of the limiting theorem.

Analytical verification rests on: (1) unitary Fourier representation of the convolution operator; (2) exact equality cases for a positive convex combination of unit phases and the gcd support identity; (3) nondegenerate Gaussian envelope from positive variance; (4) uniform control away from and outside shrinking neighborhoods of peripheral frequencies; and (5) explicit maximization of the two Gaussian profiles. Boundary one-atom laws are checked independently.

No independent mathematical review or proof certification has occurred. Literature priority cannot be conclusively established by finite searches.
