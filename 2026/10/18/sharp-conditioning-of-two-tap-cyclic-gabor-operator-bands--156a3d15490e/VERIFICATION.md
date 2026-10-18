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

# Verification and reproducibility

The full theorem is deduced from the three-character Parseval identity, the Fourier eigenvalues of the cyclic shift, and an exact single-variable minimax argument. Its quantifiers include all integers \(N\ge3\), all nonzero separations of order \(L\ge3\), and all complex nonzero tap parameters. The even-order balanced-tap rank drop is handled explicitly; the excluded order-two case has colliding characters and is not covered.

Run `python verify_two_tap_band.py` with Python 3 and NumPy to reconstruct the \(N^2\) rank-one projectors, compute singular values of the original lifted map directly by numerical SVD, and compare against the predicted Fourier-band spectrum. The enclosed `VERIFIER_OUTPUT.txt` is the recorded output from this code. The run compared 200 matrices across 50 cyclic separation geometries and detected 14 expected balanced-tap rank defects, with maximum absolute spectral error \(1.22\times10^{-14}\). It also checked the global arithmetic step optimum for dimensions 3 through 16.

These finite computations are corroboration, not a proof of an infinite statement. No external or independent scientific validation has been performed. Known general Gabor spectral formulae underlie the calculation; the asserted new content is its globally sharp weighting and separation design classification.
