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

# Verification of the prime-square denominator law

Run `python3 check_denominator.py` with Python 3 standard library. The program computes exact rational Newton sums of the roots \((1+\zeta_m^r)/(1-\zeta_m^r)\), separates even and odd residue classes, and applies the two-block affine reduction for \(n=2p^2\). It confirms that the positive reduced denominator is \(p^{2p}\) for \(p=5,7,11,13,17,19\). It also checks three smaller published alternating-block values. The tests use integer arithmetic and exact `fractions.Fraction`, with no floating-point approximations in the mathematical certificates.

The infinite-parameter proof is given in `RESULT.md`: the coefficient of lowest \(p\)-adic valuation is the unique Newton-expansion term with \(k_d=2p+2\). Competing terms are bounded above by explicit integral or factorial-divisibility estimates; this is the decisive proof step that finite tests cannot supply. No independent audit has been performed.
