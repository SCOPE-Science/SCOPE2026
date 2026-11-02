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

The analytic proof is in RESULT.md. Run the standalone `CHECK.py` using Python 3. It uses no external data or packages. Replayed checks include all increasing recursive tree parent assignments through eight labels, independent global maximum-independent-set enumeration, exact coefficient comparison against the marked exponential generating function, the unmarked recurrence, and rational factorial-moment identities. The checker passed 11,887 exact assertions. A separate float recurrence at 1,000 labels tests numerical agreement at the expected order, not an infinite theorem.

The logarithmic singularity transfer and its complex-uniform derivative step are analytic, not established by the finite checker. The parameters and boundary cases are specified in the result; the exact conditional event is undefined for two labels and positive for three or more. No independent audit or external certification is asserted.
