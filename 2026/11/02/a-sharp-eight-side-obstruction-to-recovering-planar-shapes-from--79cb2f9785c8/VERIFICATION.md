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

# Verification of the angular width-correlation theorem

Execute `python verify.py` with Python 3 standard library. To additionally replay exact radical algebra for the two cubic width moments, execute `python verify.py --symbolic` with SymPy installed. The verified run with the symbolic option returned `VERIFY_OK 3908 checks`.

The checker performs exact integer multiset comparisons of all six interval classes for each four-direction set, checks every shift/reflection in the twelve-direction grid for inequivalence, and verifies the area radical identity. It independently evaluates the trigonometric primitive on the exact sign-switch partitions, checks the closed-form third-moment difference and the Fourier bispectral coefficient, and numerically compares pair correlations over 17 angular lags. Optional SymPy checks simplify the entire trigonometric cubic integrals to their claimed exact radical expressions.

A finite enumeration of three-point subsets over several finite cyclic grids checks small examples of the reconstruction principle but is not exhaustive in the continuous circle. The continuous uniqueness follows instead from the three-positive-gap proof. Likewise numerical quadrature is not the proof of all-lag correlation equality; Fourier uniqueness of the exactly coincident finite difference measures proves that claim.

Poisson smoothing and the induced strictly positive curvature are proved analytically from convolution with the positive curvature measure. Their correlation identity follows from nonvanishing common Fourier multipliers; no high-dimensional or general noise stability claim is made. External independent audit has not been performed.
