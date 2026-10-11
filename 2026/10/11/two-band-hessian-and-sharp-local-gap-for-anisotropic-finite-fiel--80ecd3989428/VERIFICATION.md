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

# Verification of the two-band local curvature formula

Run `python3 verify.py` with the Python 3 standard library. The program constructs the fields of orders \(3\), \(7\), \(11\), and \(27\), using an explicit irreducible cubic for the extension field. It enumerates quadratic-norm shells, all centers, and tests the exact integer identities for the real and imaginary second-order coefficients. The observed outputs were:

```
PASS q=3, 2 mean-zero patterns, 9 centers, exact real/imag coefficients
PASS q=7, 2 mean-zero patterns, 49 centers, exact real/imag coefficients
PASS q=11, 2 mean-zero patterns, 121 centers, exact real/imag coefficients
PASS q=27, 1 mean-zero patterns, 729 centers, exact real/imag coefficients
```

The direct character-sum definition was separately tested over \(\mathbb F_3\) and \(\mathbb F_7\) at small real perturbation sizes; its deficit divided by the squared perturbation norm approached the two theoretically predicted eigenvalues.

Finite tests validate the implemented polynomial coefficients and normalization at these field orders only. The unrestricted formula follows from the exact orthogonality, shell and affine-incidence proof in the main result. No third-party or independent audit was performed.
