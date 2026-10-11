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

# Verification notes

The proof uses exact spatial Fourier orthogonality, discrete-root temporal orthogonality, a divisor-factorization equivalence, Cauchy--Schwarz and the classical Bertrand--Chebyshev postulate. All Fourier integrals are probability normalized, and the summation \(0\le m\le K-h-r\) is empty unless \(h+r\le K\).

Run `python3 verify.py` from this package. It uses only the Python standard library and exact Gaussian integer arithmetic in the enumerated cases. It checks 888 independently constructed finite fourth moments, 444 modular cutoff cases and the least-prime sample rule for bandwidths \(2\) through \(139\). It also verifies that signed alias defects can be negative. These checks do not stand in for the infinite-parameter proof or certify historical originality.

Scientific limitations: the theorem applies to consecutive frequency bands, integer quadratic dispersion and uniform time grids beginning at zero. The exact norm constant in aliasing cases and analogues for other moments or sampling patterns are unproved here. An equivalent older mathematical statement may exist.
