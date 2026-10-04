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

The proof was checked from the exact three-block ADMM first-order conditions after the scaled-dual change \(u=-\lambda/\rho\). The included `verify.py` is self-contained and uses only the Python standard library. It checks the reduced iteration matrix at multiple exact rational values, the exact discriminant factorization, the stationary-point elimination identity, the Sturm sign-variation count, and a high-precision numerical isolation of the unique root of the quartic.

The infinite-parameter conclusion is analytic: the Sturm argument gives a single real-to-complex transition in \((0,1)\); the real dominant eigenvalue has no stationary point except the horizontal point \(t=1/2\) and has negative derivative on both adjacent intervals; the conjugate-pair modulus is exactly \(t^{3/2}\). Numerical bisection is used only to report decimal values.

A closest later paper on general three-block separable quadratic programs was only partially accessible. Its abstract and introduction were inspected, and bounded open-access plus authorized institutional retrieval attempts did not produce the later pages. That is an originality limitation, not a correctness limitation of the algebra proved here.
