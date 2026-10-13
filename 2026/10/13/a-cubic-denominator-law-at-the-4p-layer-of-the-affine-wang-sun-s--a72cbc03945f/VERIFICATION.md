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

The proof for every prime \(p\ge11\) is symbolic and appears in `RESULT.md`. The accompanying `verify.py` uses Python's exact `Fraction` arithmetic to replay the elementary-symmetric coefficients, Newton recurrence, and the cotangent block
\[
C_{4p}=2P_{4p}(2p)-P_{4p}(4p).
\]
It checks the exact \(p=7\) value and denominator, checks the modular leading coefficient \(14/45\) for several primes \(p\ge11\), and checks a source-listed small denominator as a regression datum.

The finite prime checks are diagnostic only. They do not establish the universal \(p\ge11\) theorem, which rests on the valuation argument isolating the fourth power of the degree-\(p-1\) exceptional coefficient. Independent audit has not been performed.
