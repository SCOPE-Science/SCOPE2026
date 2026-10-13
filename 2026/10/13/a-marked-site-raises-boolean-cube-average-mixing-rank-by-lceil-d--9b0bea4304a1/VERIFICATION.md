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
# Computational verification and scope

Run `python3 VERIFY.py` with NumPy and SymPy installed. It reconstructs the Boolean-cube adjacency matrix by bit flips and independently builds the eigenspace-projector Schur-square average. Repeated eigenvalues are grouped before projector formation. Five exact symbolic Fourier-weight dark-projector profiles verify ranks and the explicit antipodal kernel vector. Fifty-four odd diagonal-moment entries are checked with exact rational arithmetic, including all prescribed zeros and the leading \(\tau(r!)^2\) coefficients. Thirty floating-point spectral profiles span dimensions \(1\)–\(6\), both signs and zero potential, and check average-mixing ranks and stochastic row sums. A representative clean execution yields:

```
VERIFY_OK exact_dark_profiles=5 moment_identities=54 spectral_profiles=30 matrix_entries=28664 cube_orders=1..6
```

The mathematical statement for all dimensions, all real nonzero potentials, and the exact kernel is established by the analytical Fourier/projector and moment proof in `RESULT.md`. Exact finite calculations are checks of specific inputs; floating-point rank classification uses a numerical threshold and is not an infinite-dimensional or arbitrary-parameter certificate. These checks are not independent scientific validation.
