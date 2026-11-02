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

# Mathematical verification

The file `verify.py` is self-contained and uses only the Python standard library. The command `python verify.py` completed with the PASS line reporting 98 exhaustive forbidden-word count checks, exact rational depth-cylinder identification for all \(2\le m\le8\), and direct rational-orbit survival comparisons for \(2\le m\le6\) and \(1\le t\le6\).

The infinite quantifiers for every integer \(m\ge2\) and every integer \(t\ge1\), the generating function, and the exact mean are proved analytically by the invertible difference-word recoding and last-one recurrence. The escape exponent and topological consequences use the elementary Perron eigenvalue of the primitive finite-type recurrence. The small-hole coefficient follows from expansion of the characteristic equation. The finite computational checks do not certify the infinitely many cases; independent audit is not yet performed.
