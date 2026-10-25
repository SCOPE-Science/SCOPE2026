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

# Verification and reproducibility

Run `python3 verify_cyclic_histories.py` with Python 3 and no third-party modules.

Actual checks executed:

- Exhaustive scan of all \(n!\) perfect matchings for \(2\le n\le7\), confirming that exactly the cyclic shifts are stable.
- Exhaustive reachability graph search under all single-agent entry/exit events, permitting repeated events, for \(3\le n\le6\) without a temporary participant. The only full terminal outcomes were the two extreme shifts. The visited state counts were 71, 293, 1,195, and 4,827 respectively.
- Full augmented entry/exit state searches for \(3\le n\le5\), containing 140, 585, and 2,401 states respectively; the interior shift was reachable.
- Explicit one-temporary-person construction replayed for every integer \(3\le n\le50\), with stability checked after each event.

The program reported `PASS: 10886 enumerated states, stable-set counts and constructive steps; n=3..50 histories`.

These finite checks independently stress-test implementation and boundary cases; the infinite-size statement is proved analytically in RESULT.md. No independent external audit has been performed.
