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
# Reproducibility of finite supporting checks

Run `python3 verify.py` with Python 3.9 or later. It uses only the standard library and makes no network requests. The recorded output in `verification_output.txt` is the single-line assertion count. Tests are deterministic.

For 180 finite-dimensional eigenvalue profiles with dimensions two through seven, the checker independently evaluates exact moments of spherical quadratic forms via Dirichlet coordinate squares with concentration parameters \(1/2\). It compares centered moments of orders two through four against the proposed spectral power-sum formulas. These computations are exact rational arithmetic and include zero eigenvalues. The code separately checks nonnegativity of the fourth moment and its uniform variance-moment bound.

For dimension two, the verifier evaluates the defining mean by a 16,384-point periodic midpoint rule for 17 spectra, including two rank-one endpoints and the isotropic case. It checks that the measured deficit is inside the analytically predicted interval with a stated numerical tolerance of \(3\times10^{-7}\). It also checks matching spectral purity and opposite cubic moment for explicit perturbations. Its 1,478 passed assertions supplement but do not replace the infinite-family analytical proof.

The proof depends critically on the all-domain scalar factorization in `RESULT.md`, the independence of the Gaussian radius and direction, and elementary Gaussian quadratic-form moments. No finite experiment, code output, or third-party software is treated as a proof of universal asymptotics or historical novelty.
