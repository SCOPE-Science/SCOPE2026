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

Running `python3 verify.py` with a Python 3 standard-library installation yields exact depth comparisons for all Boolean cycle valuations through maximum permitted length \(7\), all nonempty period sets drawn from lengths \(1\) through \(6\), and the consecutive sets through length \(7\). The script independently evaluates the formula for every valuation, checks ordered-prefix separation at the asserted optimal positive depth and failure one level below, checks Boolean prefix separation and failure one level below, and checks the explicit lower-bound valuations.

Observed terminal line:

```
VERIFY_OK sets=127 valuations=5828
```

No computation is used to infer an infinite statement from finitely many cases. The general proof rests on the structural induction for locality and positive monotonicity, the least-common-multiple congruences, the classical Fine–Wilf theorem, and explicit sharp witnesses. Formula-size minimality is not checked or claimed. The mathematical review is not an independent audit.
