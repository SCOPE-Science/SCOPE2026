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

# Verification of the stated theorem

The accompanying `CHECK.py` was executed using Python 3 and the standard library from its included path. It returned `CHECK_OK assertions=4424 degrees=0..14 exact_rational=True`. The checker forms exact rational Legendre polynomials and their supported self-convolutions on \(0\le x\le2\), calculates \(\pi M_{k\ell}\) as an exact integral of their convolution derivatives, checks \(M_{0k}=1/[\pi(2k+1)]\) for degrees through 14, and verifies \(M_{00}=1/\pi\), \(M_{01}=1/(3\pi)\), \(M_{11}=7/(15\pi)\). It also checks many rational finite mass vectors against the sharp profile, and direct equality for distributions supported in degrees zero and one.

The infinite-dimensional argument is analytic and invokes the published Theorem 1.2 of arXiv:2610.19648 for the strict ordering of diagonal Bessel fourth moments for all nonnegative integer degrees in dimension three; the finite checker is explicitly not an independent proof of that premise. Every other necessary constant-to-mode comparison and equality implication is derived in RESULT.md. The exact integration uses no floating-point approximations, and the checker needs no other files or nonstandard dependencies.

No independent audit has been performed.
