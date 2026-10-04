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

The proof was checked from the defining speed and normalization. At a geodesic sphere, exact differentiation of \(E_j\) gives \(\partial E_j/\partial\kappa_i=(j/n)c^{j-1}\), so the quotient derivative is \(\delta F=\delta H/n\) for every admissible \(k\). Differentiating both normalization integrals shows that their area-variation contributions cancel and that the remaining coefficients differ by exactly two, yielding \(\delta\phi=2c\,\overline{\delta F}\).

The packaged checker `verify.py` independently replays these coefficient identities with exact rational arithmetic for representative dimensions and all admissible quotient indices. It also verifies the scaled harmonic eigenvalues through degree eight, including the neutral degree-one mode and the degree-two spectral gap. Its successful output is `VERIFY_OK`.

The all-dimensional result is analytic. Finite replay is not treated as proof of an infinite statement. No nonlinear asymptotic rate beyond the Fréchet spectrum is claimed.
