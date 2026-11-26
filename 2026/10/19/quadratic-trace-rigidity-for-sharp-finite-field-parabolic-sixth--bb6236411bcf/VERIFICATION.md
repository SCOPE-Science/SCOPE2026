---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Theorem 1.3 gives constant modulus and sharpness at constants with the stated measures. Orthogonality gives q^(-4) times the sum of squared ordered fiber sums. At constant modulus the triangle inequality bounds each summand by its value at a constant, so equality holds separately on every fiber, in particular the generic ones. The four-point resonance has defect 6h², nonzero for h≠0. Ratios of consecutive ratios on each prime-field line are two-periodic, hence constant on its odd cycle, giving p-th root phases and degree at most two on each line. In equation (3), equating coefficients gives x²yφ=(x²y²φ)/2 and xy²φ=−5(x²y²φ)/2; interchanging x,y forces the common term to vanish because 3 is invertible. The three-direction cube then gives vanishing mixed third differences, so polarization is prime-field bilinear. In the split rotation representation only opposite weights from the same Frobenius index can pair, since q−1>2p^(n−1). In the nonsplit case p^d≡−1 mod q+1 has only d=n modulo 2n: smaller d is excluded by size, larger d by inversion. In both cases the n-dimensional invariant space is exhausted by trace multiples of S, which are independent by polarization on a nonisotropic field line. In the split case invariance extends to isotropic vectors by the parallelogram identity, avoiding at most three values of each coordinate. Evaluation at (t,−t,0), then trace nondegeneracy, gives the asserted quadratic and linear terms. Modulation translates the output and polarization gives q² distinct classes. The frozen verify.py was inspected, not executed: its F_25 fiber sizes and rank-20 test are bounded corroboration, not needed for the uniform proof.

## originality

PASS

Credit the known sharp constant, constant-modulus necessity and the prime-field phase classification. The supported distinct claim is rigidity of the phases over proper extension fields: generic fibers force field-trace quadratics, not just arbitrary prime-field quadratics. None of the inspected prior statements supplies that step.

## value

PASS

The known sharp inequality left all phase information unresolved on extensions. Excluding the extra prime-field quadratics completes a natural equality classification and identifies precisely which modulations give all extremizers up to scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
