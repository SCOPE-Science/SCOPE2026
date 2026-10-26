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
# Verification of the Lipschitz contraction theorem

The self-contained proof in `RESULT.md` consists of: (1) a sharp duality between periodic mean-zero derivatives and \(L^1\)-distance of the Fejér kernel to constants, with sign-derivative attainment; (2) a sine-product sign identity proving the exact median for odd degrees; (3) a joint Fourier-character equidistribution argument; and (4) uniform boundedness of capped kernels and an explicitly evaluated triangular integral. This establishes the exact finite-degree invariant and its large-degree first-order asymptotic for all integers in scope.

`verify_fejer.py` was executed with Python 3 and numpy/scipy against both the sine-quotient and Fourier-cosine kernel representations. Tests for \(n=2,3,4,5,7,20,50,100,200\) agreed with the exact first cases, odd sign symmetry, and the predicted leading limit. The sampled values include \(L_4\approx0.890451200\) and \(200(1-L_{200})\approx0.40529258\) versus \(4/\pi^2\approx0.40528473\). Numerical quadrature cannot certify the infinite limit or originality.

Prior-work comparisons are stated specifically in `REVIEW.md` and `AUDIT.json`. The public proof and checker contain no dependencies on unpublished records. Independent audit and independent validation have not been performed.
