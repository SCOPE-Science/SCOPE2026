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
# Verification record

The exact-integer implementation `verify.py` is provided alongside the proof. Run `python3 verify.py` with Python 3 and no third-party dependencies. Its recorded output is in `verification_output.txt`. The code checks the computed gcd of the first \(r+1\) windows against the same gcd from \(r+10\) windows for every tested odd exponent \(1\) through \(23\) and odd length \(1\) through \(61\); both equal the closed formula for all \(372\) combinations. It separately checks the Fibonacci mod-\(4\) period and an even-exponent counterboundary mod-\(5\).

The proof's unlimited quantifiers rely on the unimodular symmetric-power recurrence and Cassini identity, not on the finite test grid. The program is a consistency check and does not constitute an independent mathematical audit. No external independent assessment was performed.
