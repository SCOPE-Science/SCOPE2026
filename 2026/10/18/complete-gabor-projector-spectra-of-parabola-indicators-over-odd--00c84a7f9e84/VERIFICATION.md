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

From the directory containing `RESULT.md`, run `python3 checks/verify.py`; dependencies are Python 3 and NumPy. The immutable input is the explicit curve \(t\mapsto(t,t^2)\) modulo odd prime powers. The checker generates a unit \(\ell^2\)-norm indicator on the two-coordinate ring grid, calculates every translated self-overlap and its two-dimensional Fourier transform, then uses a separate four-dimensional FFT to obtain the full projector Gram spectrum. Spectral multiplicities, including the zero eigenvalue, match the closed formulas at five finite parameter pairs, from dimensions \(9\) through \(729\).

The same program separately checks squared Fourier magnitudes of the translated intersections over all Weyl coordinates at \((p,k)=(3,2)\) and \((5,2)\): \(6561+390625=397186\) coefficients. Integer multiplicity, dimension and trace identities are checked for \(p\in\{3,5,7\}\) and depths through seven. The recorded exact stdout is in `checks/output.txt`. Direct FFT comparisons use an absolute numerical tolerance \(10^{-6}\), with much smaller actual reported imaginary artifacts. The general theorem relies on congruence counting and primitive Gauss-sum evaluation; finite FFT runs are corroborative and do not establish the theorem for all primes and depths.

There has been no independent mathematical audit or external certified verification of the result. Historical equivalence to an unindexed older Gabor or association-scheme theorem remains possible. Only the complete-orbit linear Hilbert--Schmidt projector spectrum is classified; zero modes need not imply pure-state phase-retrieval ambiguity.
