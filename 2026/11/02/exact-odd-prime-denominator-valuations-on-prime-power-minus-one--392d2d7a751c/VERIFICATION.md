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

The companion `verify.py` uses Python standard-library integer binomial coefficients, `fractions.Fraction` and modular inverses. Every checked \(p,m\) pair is tested for the **complete** shift range \(1\le r<p^m\). Independently evaluated rational sums are checked against both the exact valuation and the nonzero normalized residue. The code also verifies reduced denominator divisibility by \(\binom{p^m-1+r}{r}\) and equality of their \(p\)-adic valuations.

Finite execution checks are only corroborative; the infinite theorem rests on the uniquely minimal valuation argument and integer binomial identity in `RESULT.md`. The tested finite ranges do not address primes/indices outside those enumerated, nor other denominator primes. Independent auditing remains unperformed.
