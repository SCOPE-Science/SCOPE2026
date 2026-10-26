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

# Reproducibility and verification

Run the accompanying standalone `checker.py` with `python3 checker.py` (Python 3 standard library, no external modules) from this directory. Its deterministic input generator computes 2,000 sets of linear uniform-vorticity gravity–capillary upstream and downstream dispersion speeds and independently verifies difference/product identities and inversion of all four coefficients. It additionally rejects deliberately inconsistent measured-data pairs, tests monotonic depth-ratio derivatives, and compares finite-depth expansions to asymptotic formulas. The recorded successful output is `PASS; independent dispersion identities, inversions, compatibility, and asymptotic checks: 12028`.

The analytical proof does not depend on the random tests. Global uniqueness relies on strict monotonicity of \(k/\sinh(2kh)\) in \(k>0\), invertibility of the restoring-force two-by-two system, and positivity-based recovery of individual speeds from difference and product. The depth sensitivity follows from ordinary Taylor and exponential expansions for \(\tanh\). The source model itself is the established constant-vorticity linear dispersion [Ellingsen–Brevik, arXiv:1311.1073, Eqs. (33)–(34)]; this work verifies the inverse consequences, not that the physical idealizations hold experimentally.

The finite floating-point checker is not an exhaustive proof and is not suitable for arbitrarily singular near-zero/infinite depth ratios where double precision collapses. Noise, velocity calibration error, nonlinear hydrodynamics, unknown density and independent external validation remain outside scope.
