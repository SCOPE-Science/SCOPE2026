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

Run `python3 verify.py` in the directory containing this file and `verify.py` using Python 3 with standard libraries only. Successful replay from the embedded package returned:

```
VERIFY_OK rational_dp_cases=3186 rational_h_values=177 memo_states=700209 independently_enumerated_cases=48 terminal_prefix_cases=66
```

The checker uses exact scaled integer states for all rational tested exceptional values, explicitly tries every remaining good type and both possible recipients, and separately uses a full order/recipient brute force over small instances. It also enumerates signed unit paths and verifies the proof's odd-prefix bound for odd step counts up to \(21\). The tested rational exceptional values have denominators at most \(8\), positive numerators up to nine times the denominator, and every positive unit count from \(1\) to \(18\) in the dynamic program. The exhaustive brute-force check covers unit counts from \(1\) to \(6\) at eight exceptional values. Finite checks are not a proof for arbitrary real \(H\) or arbitrary positive integer \(r\). These are established by the edge-pairing and terminal-gap argument in `RESULT.md`.

There is no external code, dataset, solver, precomputed table, or fixed absolute path required to replay the check. No externally independent audit is claimed.
