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

Run `python verify.py` with Python 3 and no external packages. It performs exact integer arithmetic for the Fibonacci powers, inversion identities, the sharp Fourier-mode lattice minimum on a bounded integer square, and the explicitly claimed maximizers for times \(0\le n\le12\). The program completes without relying on floating-point tolerance. It is a check of worked formulas, not a substitute for the universal lattice lower bound proven in `RESULT.md`.

The measure-theoretic assertions follow analytically from the invariant-fibration identification and Fourier density: no numerical sampling of quaternions or ergodic orbits is used. The conjugation-invariant disintegration is with respect to normalized spherical area and torus Haar on the commuting locus, not the six-dimensional ambient Haar probability. Equality in each finite-time Hilbert-norm inequality is witnessed by the real cosine functions written in the proof.
