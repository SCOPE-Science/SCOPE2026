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

# Reproduction and limits

Run `python verify.py` with Python 3.9 or later; only the standard library is required. The script constructs connected labeled graphs whose simple cycles are pairwise vertex-disjoint. It enumerates all base-edge orientations and computes the in/out-degree cost directly. Separately it constructs the signed line graph from oriented incidence signs, enumerates vertex switchings with one variable fixed to remove global duplication, and compares the exact minimizing sign assignment count. It compares both calculations against the theorem and the full optimal-orientation count.

The run recorded in `VERIFY_OUTPUT.txt` returned all checks passed: 5,428 exhaustively listed small graphs on three through six vertices, 169 generated cactus instances of up to 15 edges, and specified odd-cycle sun cases. For small graphs the script compares the sign count using a separate switching enumeration in every case. For generated cases it performs direct switching checks on a bounded subcollection as recorded by the script. Orientation counts are compared on all checked generated instances.

These tests are finite and do not establish an all-order claim by themselves. The proof in `RESULT.md` establishes the all-order result by an odd-cycle local lower bound, a constructive block-tree orientation, classification of equality, and the two-to-one orientation/signature correspondence for connected signed-line graphs. The relevant mathematical references are those named in `RESULT.md`; no independent external audit is implied by this reproduction record.
