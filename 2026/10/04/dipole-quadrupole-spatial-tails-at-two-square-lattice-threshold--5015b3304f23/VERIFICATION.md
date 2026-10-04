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

The analytic verification has three independent pieces.

1. The primary spectral source gives the two-dimensional odd threshold functions as scalar multiples of \(\sin p_j/E(p)\) and the even threshold function as a scalar multiple of \((\cos p_1-\cos p_2)/E(p)\), with \(E(p)=2-\cos p_1-\cos p_2\).
2. Fourier shift identities convert those normalized kernels exactly into first and anisotropic second finite differences of the square-lattice potential kernel. This step uses only algebra and cancellation of the divergent Green constant.
3. The published potential-kernel expansion \(a(x)=2\pi^{-1}\log|x|_2+\kappa+O(|x|_2^{-2})\), with the explicit smooth order-
\(|x|_2^{-2}\) angular correction and an \(O(|x|_2^{-4})\) remainder, yields the leading dipole and quadrupole coefficients by Taylor expansion.

The bundled standard-library checker replays the finite-difference coefficient calculation for the logarithmic leading term along several non-nodal rays and checks the exact algebraic prefactors. It is not a proof of the potential-kernel asymptotic theorem and does not attempt to certify literature originality.

Limits: only the nearest-neighbor square-lattice dispersion and the normalized zero-energy profiles are checked; no off-threshold spectral expansion is asserted.
