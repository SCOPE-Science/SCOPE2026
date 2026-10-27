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

The result follows from two resolvent Gram integrals and the elementary linear independence of rational functions with different simple poles, as stated explicitly in RESULT.md. The nonstandard equality of kernel and Krylov orthogonal complement is proved using these integral and interpolation identities, without numerical extrapolation.

Reproduce the exact two-dimensional certificate by expanding the principal square root of the stated matrix and checking that its correction has positive trace and determinant, with strict determinant inequality equivalent to \(325>324\).

Run `python check.py` after installing NumPy, SciPy and SymPy. The program contains deterministic finite checks for both correction signs, several exponents, positive update strengths, repeated eigenvalues, omitted eigenspaces, and transformed-resolvent integral normalization. The reported checks were run from the package's exact `check.py` bytes before delivery. They are not an exhaustive test of all dimensions or a substitute for the proof.

No independent review, external certification, or formal proof checking has been performed. The statement does not imply that exact full rank prevents high-quality low-rank approximation.
