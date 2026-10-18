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
# Reproducibility and limits

Run `python3 verify.py` with Python 3.9 or later. The program uses exact integer factorial valuations via Legendre's formula, independently of the symbolic cyclic-digit-sum proof. It checks all indices of all rows \((p^r-1)q\) in 13 exact prime/exponent cases, from \(q=2\) through \(q=p^r+1\), and asserts valuation \(r\) throughout the plateau and zero at the first failure. The final summary reports 83,211 selected binomial coefficient checks. Output is deterministic and has no external dependencies.

The universal theorem is proved in `RESULT.md`: the finite tests corroborate the result and are not claimed to exhaust arbitrary primes or exponents. The complete integer GCD and multipliers beyond the first failure remain unspecified. Independent external audit has not been performed.
