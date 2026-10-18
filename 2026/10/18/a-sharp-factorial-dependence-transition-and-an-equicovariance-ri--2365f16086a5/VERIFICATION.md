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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 standard-library modules only. The local verification completed with the output `PASS 1165 exact assertions; complete enumeration n=2,...,7 for five rational Ewens parameters.` It checks all permutations at the selected small orders and rational parameters, computes Ewens weights and factorial moments independently, tests the finite sign rules and the exact \(\theta=2\) equicovariance identity, and verifies the rigidity rational expression at further parameter values.

These are finite, exact checks. The general statements require the proof in `RESULT.md`: the marked-cycle identity, strict comparison of consecutive factors, an order-\(n^{-2}\) expansion for fixed lengths, and the all-parameter covariance-difference factorization. No external or independent proof audit is asserted. Uninspected older mathematical literature may contain an equivalent statement.
