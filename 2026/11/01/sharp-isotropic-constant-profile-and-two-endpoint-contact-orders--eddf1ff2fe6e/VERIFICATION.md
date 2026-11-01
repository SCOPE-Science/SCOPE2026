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

# Reproduction and verification limits

The standalone `verify.py` requires only Python 3.10 or later's standard library. Run `python3 verify.py` in the directory containing the extracted program. Successful output is `VERIFY_OK 558 exact checks`.

The tests build the two scalar moment polynomials and covariance matrices from scratch using exact rational arithmetic. They compute full covariance determinants for dimensions two through eight at five rational truncation depths; compare exact integer polynomial coefficients of the derivative and positive-sum factorization for dimensions two through fifty; check strict decrease at ten ordered depths for dimensions two through twenty; and verify simplex and limiting algebraic normalizations. The implementation has no third-party dependencies and does not need internet access.

These finite computations do not certify an all-dimensional theorem. The universal result is supported by the Dirichlet disintegration, the explicit algebraic certificate with coefficient-by-coefficient proof, and the endpoint asymptotic argument in `RESULT.md`. Arithmetic checks use actual rational/integer values, not floating-point signs. The historical-priority comparison is provisional; external independent mathematical auditing has not been performed.
