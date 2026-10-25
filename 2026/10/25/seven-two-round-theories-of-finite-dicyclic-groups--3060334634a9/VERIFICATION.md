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

## Verification protocol

Run `python3 verify.py` with the standard Python library. The program constructs every group by its defining multiplication and obtains complete two-variable atomic diagrams including the named identity. It independently compares direct full-vertex and orbit-reduced two-round signatures, the reduced four-bit case analysis, and the proposed complete index classification. The console output is captured in `verification_output.txt`.

## Observed results

- Full-vertex and automorphism-orbit atomic signatures agree for all indices from 2 through 18.
- The eight pointed-pattern templates reproduce all actual local signatures for indices from 2 through 40.
- All seven representative theories are distinct and all indices from 2 through 100 map to the predicted theory.
- The largest least representative order is 48 elements.

## Limits

These are finite checks, not a proof for every index. The all-index conclusion follows from the group presentation, the equations for two-variable atomic diagrams, and the eight-row pointed-type table in `RESULT.md`. Independent scientific audit has not been performed.
