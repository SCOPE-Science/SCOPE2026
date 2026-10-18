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

# Reproducibility and verification

Execute `python3 verify_direct.py` and `python3 verify_transfer.py` in the directory containing these standalone files. They require Python 3 standard library only. `direct_output.txt` and `transfer_output.txt` are the recorded outputs. The degree-histogram JSON objects on their first lines are byte-for-byte identical for all lengths from one through eight.

The direct program enumerates every perfect matching recursively on the Cartesian cube grid and tests each elementary four-cube square. At length eight it examines all 23,409 tilings. The transfer program independently enumerates sixteen possible adjacent-layer transition types with exactly weighted cap and side flips, checking the formulas through length fifteen and producing the full histograms through eight. The two finite algorithms are structurally different. The finite tests are consistency checks; the infinite result follows from the block proof in `RESULT.md`.

Exact boundary tests cover the two exceptional maximum-multiplicity cases at lengths one and two, the equality class count at lengths divisible by three, and all residue classes modulo three. The comparison does not verify unpublished literature exhaustively, mixing rates, or boxes outside the stated family. An independent external audit has not been performed.
