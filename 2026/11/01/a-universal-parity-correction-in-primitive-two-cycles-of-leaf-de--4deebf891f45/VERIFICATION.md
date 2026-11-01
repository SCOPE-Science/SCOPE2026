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

# Reproducibility

Run `python3 verify_sunlet.py`; all calculations use only the Python 3 standard library.

The verifier enumerates configurations at every vertex in the range \(0\le h_v<2d_v\) for six finite graph instances: \((n,r)=(3,1),(4,1),(5,1),(3,2),(4,2),(3,3)\). That is 1,864,640 microscopic candidate states altogether. Each candidate is advanced twice by literal graph-neighbor chip transfers, and a primitive two-cycle is counted only when the two-step return occurs without a one-step return. The observed interface histograms match a separate even-boundary-word count. Integer transfer traces and the closed-form recurrence are independently compared through \(n=30\) and \(1\le r\le15\); direct phase summation is also used through \(n=15\).

The recorded output is in `verify_output.txt`, ending with `SUNLET_PRIMITIVE_TWO_CYCLE_VERIFY_OK`.

The infinite assertions rely on the local-height, parity, and characteristic-polynomial arguments in `RESULT.md`; finite tests alone would not suffice. The restriction to \(h_v<2d_v\) is exhaustive only for the primitive two-cycles being counted, as proved by the local inequalities. No independent external audit or validation is asserted.
