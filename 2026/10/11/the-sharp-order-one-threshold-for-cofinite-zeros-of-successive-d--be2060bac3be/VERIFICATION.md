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

# Reproducibility and verification

All assertions are verified by the mathematical derivation in `RESULT.md`; no stand-alone numerical certificate is needed. For fixed \(R\), splitting the derivative series at \(m=n\) gives the uniform upper bound. The coefficient \(m=\lfloor |z|L_n\rfloor\), when \(|z|\) stays away from zero, gives the lower bound by Stirling. Planar uniform anti-concentration proves the exact logarithmic tail estimate with exponent \(2\). Integration of the nonnegative deficit's tail and Jensen's inequality justify the circle expectation bound without assuming independence between derivatives. On a zero-free disk, the mean-value identity converts the strictly positive circular average of \(|z|\) into a nonzero logarithmic deficit, giving a convergent sum of hole probabilities. The countable-disk Borel--Cantelli argument establishes the claimed simultaneous property.

The reverse direction is verified for an arbitrary transcendental entire function satisfying \(|g(z)|\le C e^{\tau|z|}\): Cauchy--Stirling gives \(|g^{(n)}(0)|=O(\sqrt n\,\tau^n)\), and the largest normalized coefficient forces infinitely many derivatives to be zero-free in one fixed small disk. Thus the order/type restriction is not an extrapolation from finite data.

No deterministic sample, numerical order-threshold value \(N(U)\), formal certificate, or independent audit is asserted. The primary published comparison proves order two; possible unindexed equivalents remain an originality limitation.
