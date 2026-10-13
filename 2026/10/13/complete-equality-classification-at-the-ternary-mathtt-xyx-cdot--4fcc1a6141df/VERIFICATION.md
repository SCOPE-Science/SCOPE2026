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

Run `python3 verify.py` beside `certificate.json`.

The first engine scans every factor \(F\) for a nonempty border \(X\), writes \(F=XYX\), and checks whether \(Y^R\) is also a factor. The second independently enumerates nonempty factors \(X,Y\) and checks whether both \(XYX\) and \(Y^R\) occur.

Both engines regenerate identical complete ternary prefix levels through length \(15\). The verified counts are
\[
1,3,9,18,30,42,54,54,54,48,42,36,24,12,6,0.
\]
The verifier checks the exact six length-\(14\) words, the empty length-\(15\) level, the full six-element alphabet-permutation orbit, and reversal closure.

The verification establishes only the finite equality classification stated here. Independent audit has not been performed.
