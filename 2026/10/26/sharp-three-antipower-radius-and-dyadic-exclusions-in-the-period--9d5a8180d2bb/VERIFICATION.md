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

# Reproduction and proof boundaries

From a folder containing `verify.py` and `factors.csv`, run `python3 verify.py`. The script requires Python 3.8 or later and only the standard library. Its assertions reconstruct the 23 possible length-fifteen factors from the three overlapping substitution-block pairs; identify the exceptional three length-nine prefixes; check all 115 block-length tests in the embedded CSV; and independently compare 65,536 generated bits against the valuation-parity formula. It also verifies sample dyadic exclusions through exponent 12 and the exact rational density identity from algebraic factor frequencies.

The all-index and all-exponent claims rely on the structural proof in `RESULT.md`: prefix-agreement of the two substitution images; exact source-pair cover of every length-fifteen factor; and the parity recurrence for occurrence frequencies. The finite samples alone are not an infinite certificate. No higher-order antipower claims are made. Mathematical priority and independent scientific review remain unverified.
