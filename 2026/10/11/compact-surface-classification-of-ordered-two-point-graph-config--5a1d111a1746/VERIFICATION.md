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

# Reproducibility and limits

Run `python3 verify.py`. It uses only the Python standard library and exhaustively processes every labeled simple graph with three, four, five and six vertices. The accepted graph counts are respectively 0, 0, 38 and 340. It constructs complete isomorphism orbits of the proposed graph families, verifies equality of the two labeled mask sets at every order, then builds exact ordered two-point cubical boundary incidences and checks orientability, component count, Euler characteristic and boundary cycles for every exceptional family. It also tests three cycle lengths, not an unbounded family. Expected successful final line: `VERIFY_OK`.

The uniform exclusion of noncycle graphs with seven or more vertices, and the annulus assertion for **all** cycles of length at least five, are proved mathematically in `RESULT.md`; no finite enumeration alone establishes those infinite statements. The code computes cubical combinatorial topology, not continuous graph configuration homotopy equivalences. This package does not include externally supplied manuscripts, nor does it attest independent validation.
