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

## Reproducible mathematical checks

Run `python3 verify_mixed_hamming_rank3.py` with Python 3 and no third-party dependencies. The program directly constructs graph vertices and edge relations, forms all third-vertex atomic diagrams relative to a fixed first vertex, and compares their resulting three-round fingerprints to separately coded closed-form extension profiles. Direct enumeration covers 93 product instances of at most 150 vertices. An additional symbolic parameter sweep covers 6,434 factor tuples in dimensions one through eight, with alphabet sizes two through eight. Nine distinct class fingerprints and minimal representative orders 2, 3, 4, 6, 8, 9, 12, 16, and 27 are checked. Recorded standard output is in `verification_output.txt`.

## Logical scope

The infinity of product dimensions and factor sizes is treated by the inequalities in `RESULT.md`, particularly the monotonicity and positivity analysis for \(N-2\Delta\), rather than inferred from finite testing. The verifier independently corroborates the pair-extension formulas; it does not provide an external or independent scientific audit.
