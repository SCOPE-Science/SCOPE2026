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
# Verification record

Run the embedded `verify.py` with Python 3, NumPy and SciPy. This program independently constructs the left-regular transposition matrix for three and four particles, exponentiates both coherent and classical generators and verifies equality at the predicted minimum revival times and strict squared-distance improvement away from them. It also enumerates integer partitions and hook-length dimensions for \(2\le n\le18\), confirms the content-difference gcd and Plancherel dimensions, and checks the leading revival curvature numerically. The actual completed output is `PASS 127 finite checks; n=2..18 content gcd + Plancherel; n=3,4 matrix dynamics, exact periods, strictness and curvature`.

Those tests are finite diagnostics, not a proof for arbitrary particle number. The complete proof is the algebraic argument in `RESULT.md`: Lindblad/convolution factorization, central Fourier Plancherel, a point-mass equality argument, the content gcd and the even Taylor expansion. Numerical tolerance in the matrix tests is at most \(10^{-4}\) for the finite-difference curvature and tighter for matrix identities. No independent audit, formal theorem-prover certification or external reproduction is asserted.
