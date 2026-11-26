---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproduction and limits

The unchanged standard-library program `verify.py` (run with `python3 verify.py`) compares graph primitivity with group transitivity for every permutation on 3, 5 and 7 bins. Its recorded output is:

`VERIFY_OK 5166 full fine-graph comparisons; 70 exact recurrence levels; N=3,5,7 counts (4, 80, 3552)`

The program also gives a finite probability spot-check. These diagnostics do not certify the unbounded dynamical criterion, the rooted-map identification or the asymptotic. The proofs use parity of the period classes, the explicit dart-root correspondence and a specialization of the cited factorial-asymptotic theorem.
