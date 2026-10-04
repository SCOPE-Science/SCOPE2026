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

The mathematical verification is analytic. For \(p=2\) and three active eigenvalues, the endpoint evaluations of the published Cauchy--Binet multiplier have only one surviving two-index term at each spectral extreme. Direct cancellation yields the standard-weight ratio recurrence, and the published fixed-weight conjugacy yields the factor \(w_3/w_1\). Taking the logarithm around the positive fixed ratio gives the exact linear recurrence \(z_{k+2}=z_{k+1}-2z_k\), whose characteristic roots have modulus \(\sqrt2\).

A bundled pure-Python checker, `verify_projective.py`, evaluates the determinant-ratio complete-sweep multiplier in high-precision decimal arithmetic for a compatible warm-up trajectory with \(H=\operatorname{diag}(1,2,5)\). It compares every generated extreme-mode ratio against the closed recurrence over multiple delayed sweeps and prints `VERIFY_OK` only when all relative residuals are below the stated tolerance. This finite replay is a consistency check, not the proof of the asymptotic theorem.

Scientific limits: the checker covers one standard-weight instance; the weighted formula is verified algebraically by conjugacy. Finite-precision rank-selection behavior and nonquadratic extensions are not assessed.
