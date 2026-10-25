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

The symbolic proof bounds a Dyck prefix through a three-state greedy-arch register, the height of its prefix path, and the parity of its completed arch count. Each of the six register/parity cases has a displayed potential; the transitions use increments \(1\), \(3-2h\), or \(-1\), yielding nonnegative slacks on all reachable states. At final height zero, the potential is nonpositive.

To reproduce the finite checks, run `python3 check.py`. It uses the Python standard library and verifies the exact Dyck census through semilength eight against independently enumerated subsequence targets, the height-restricted min-plus recurrence through height 150, all reachable potential transitions through height 150, and constructed extremal families through height 50. Successful output begins with `DYCK_HEIGHT_UNIVERSALITY_PASS`.

No finite computation is treated as a proof for unbounded heights or lengths. The unbounded statement rests on the symbolic invariant and explicit constructions. No independent audit or verification is represented by this document.
