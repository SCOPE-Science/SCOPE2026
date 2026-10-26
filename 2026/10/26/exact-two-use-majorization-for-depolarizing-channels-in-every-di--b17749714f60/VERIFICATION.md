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

The theorem is verified analytically in `RESULT.md` by the exact bipartite depolarizing expansion, Schmidt-basis block diagonalization, a sum-of-rank-one-vectors Gram identity, and the Ky Fan eigenvalue inequalities, including physical negative depolarization coefficients. These implications are dimension-uniform and apply to all bipartite states. The finite tests below cannot prove the theorem's universal quantifiers.

The standalone file `verify.py` requires NumPy and runs `python3 verify.py`. Its execution passed exact rational Gram identity checks in dimensions 2, 3 and 4, and 1050 randomly sampled input/parameter numerical majorization examples for dimensions 2, 3, 4, 5 and 7 (including the extreme physical parameter). The maximal observed numerical Lorenz-defect residual was approximately \(1.78\times10^{-15}\), consistent with floating-point rounding. Such experiments do not certify arbitrary dimension, all inputs, or exact identities; the written proof supplies those assertions.

Limitations: two identical finite-dimensional depolarizing channels, not unequal channels or three and more uses. No independent audit or independent numerical validation is represented as performed.
