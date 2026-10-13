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

The universal proof is symbolic. Its critical steps are the exact reduction to \(a s(a)+b s(b)=2ab\), the divisibility \(b\mid p\) when one coordinate is prime, the modulo-prime contradiction for same-base prime powers of unequal exponent, and the mutually contradictory inequalities forced by distinct prime-power bases.

The bundled `verify.py` recomputes divisor sums and distinct-prime supports through \(3000\), scans every unordered pair in that range, checks all five source-table \(WPM(1)\) examples, and independently tests all prime-power pairs through the bound. Its recorded output is:

`VERIFY_OK bound=3000 pairs=9 source_examples=5 prime_power_pair_checks=108811`

The finite scan is a regression test only and is not used to infer the universal theorem.
