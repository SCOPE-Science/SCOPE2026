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
# Verification procedure and limits

The proof is the all-parameter argument in RESULT.md. The following two programs are independent finite sanity checks and their outputs were regenerated from the exact embedded program files:

```
python3 direct_refinement.py
python3 arithmetic_profiles.py
```

`direct_refinement.py` constructs every tested graph and iteratively refines the colouring from two distinct singleton anchors. It compares the complete stable colour partition with the predicted orbit partition, for 62 parameter triples with \(6\le n\le12\) and \(20{,}098\) total vertex instances. The expected console output is in `direct_output.txt`.

`arithmetic_profiles.py` enumerates feasible four-zone signatures and verifies the simultaneous distance-change formulas, separation modulo balanced complementation, Burnside cell counts and total binomial mass for 2,008 parameter configurations with \(6\le n\le36\) and 268,128 feasible signatures. The expected console output is in `arithmetic_output.txt`.

Computational bounds are finite. They cannot establish anything about parameters beyond the enumerated domain. No independent audit or priority determination has been performed.
