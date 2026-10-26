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

The accompanying `check_weak_ratchet.py` is a standalone Python 3 script requiring NumPy and SymPy. Run `python check_weak_ratchet.py` from the directory containing the extracted file.

Symbolic computations: direct Taylor expansion of the resolvent \(H_q(k)\) at \(k=0\) reproduces the rational \(K(q^2)\) exactly; differentiation reproduces \(K'(t)\). The checker verifies both endpoint limits and the passive limit \(v=0\) as exact SymPy identities.

Independent numerical computations: for each of four choices of thermal diffusivity, flip rate, propulsion and real periodic potential, construct the entire two-spin truncated Fourier–Bloch operator with modes \(-5\) through \(5\). Extract its principal eigenvalue at three small tilt parameters and compare the centered second derivative with the exact asymptotic prediction for amplitudes \(0.08\) and \(0.04\). All programmed assertions passed at the reported tolerances.

These finite-dimensional spectral calculations are consistency checks, **not** a proof of the untruncated or infinite-time statements. The analytical eigenvalue-resolvent argument supplies the proof. An independent mathematical audit has not been performed.
