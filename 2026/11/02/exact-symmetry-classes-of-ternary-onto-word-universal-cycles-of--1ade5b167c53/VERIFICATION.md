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

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` in a directory also containing `witness.txt` if inspecting both artifacts. Its complete 36-edge DFS fixes the factor `0120` at the beginning and never identifies a word by an unverified period. The output checks all 36 length-four windows of each of 4,800 cycles; it also checks the Laplacian cofactor and an independent subset enumeration of prism spanning trees, the quotient transposition cofactor and voltage, zero three-cycle quotient voltage, and all 12 symbol/reversal fixed-point actions.

The expected exact counts are 36 edges, 24 active overlap vertices, 75 prism spanning trees, 4,800 labeled rotation classes, 40 transposition-fixed classes per transposition, zero three-cycle-fixed classes, zero classes fixed by any reversal combination, 820 alphabet-relabeling classes, and 410 classes with reversal also identified. The provided witness's windows are independently checked by the program's enumeration.

No computational assertion is extended to larger alphabets or different read lengths. The proof of the complete classification is given separately in `RESULT.md`; computation verifies the finite graph and its group actions, not originality or independent validation.
