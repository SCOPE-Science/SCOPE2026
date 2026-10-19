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

The proof uses the following exact, finite and general checks.

1. The nine MUB vectors per finite parameter are normalized; nondegenerate character orthogonality gives cross-basis squared overlap \(1/9\). The computational basis has the same mutual-unbiasedness property.
2. The complete-MUB projection decomposition proves \(\sum p_{j,b}^2=2\) for every normalized pure state. Cauchy--Schwarz yields the universal support lower bound \(50\) without finite enumeration.
3. For the explicit state, the finite-field trace map \(b=u+v\iota\mapsto(2u,-2v)\) is invertible. A three-value phase identity proves exactly four zero coefficients for each finite \(a\), with five other coefficients each of probability \(1/5\).
4. Run `python3 verify_mub9.py` from the embedded file; it enumerates all 81 quadratic-phase sums in \(\mathbb Z[\zeta]\) with exact integers, and asserts the full pattern and support total.

This finite checker is corroboration, not a replacement for the universal proof. The analysis is restricted to the displayed standard family and does not certify historical uniqueness, independent validation, or a classification of all optimizers.
