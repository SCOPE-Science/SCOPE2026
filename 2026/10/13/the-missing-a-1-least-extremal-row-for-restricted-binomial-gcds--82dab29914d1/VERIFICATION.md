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

The universal proof uses Kummer's theorem in carry form.

For \(2\le q<p\) and every \(1\le d<q\),
\[
(p+1)d=dp+d,\qquad (p+1)(q-d)=(q-d)p+(q-d).
\]
Both base-\(p\) columns sum to \(q<p\), so there are no carries and the selected coefficient has valuation \(0\).

For \(q=p\) and every \(1\le d<p\), the corresponding two low columns each have digit sum \(p\). The units column produces one carry; the next column receives that carry and totals \(p+1\), producing exactly one further carry. The carry then terminates in the \(p^2\)-column, so the valuation is exactly \(2\).

`verify.py` replays these statements for every prime through \(97\) and also compares against exact integer binomial valuations for every prime through \(43\). The observed output is:

`VERIFY_OK primes=25 max_prime=97 smaller_multipliers_zero=1 target_multiplier_two_carries=1 direct_binomial_checks_through=43`

The finite checks are not used as an infinite proof. No independent audit has been performed.
