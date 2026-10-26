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

# Reproducibility

Run `python3 verify_knockout_spectrum.py` from the directory containing this file and `RESULT.md`. No external Python packages are required. The program independently enumerates every fair internal-node coin assignment for \(n=2,4,8,16\), computes score first and second moments exactly, compares every covariance entry against the displayed closed forms, and verifies dyadic eigenvectors/eigenvalues and Rayleigh-quotient extrema using exact rational arithmetic. The reported run passed **1,085 exact rational assertions**. The further diagnostics for \(5\le\ell\le20\) check exact eigenvalue trace/bounds, together with floating-point convergence toward the determinant limit.

# Evidence limits

The first four sizes are finite exhaustive checks of bracket-outcome assignments; they do **not** establish the unrestricted covariance theorem. The infinite family follows from independent-node survival probabilities, exact orthogonal Haar diagonalization, and dominated convergence as written in `RESULT.md`. Floating-point diagnostics neither replace a proof nor certify exact asymptotic constants. No external audit or independent validation has been performed.
