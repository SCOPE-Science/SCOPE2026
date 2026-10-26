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

Run `python verify.py` with Python 3 standard library; compare its stdout with `verification_output.txt`.

The verifier constructs each ladder directly from its rungs and rails, exhaustively tests the open-neighborhood odd-occurrence rule and, independently, the adjacency constraints of the graph square. For nineteen finite graph/palette pairs it checks every one of \(1{,}647{,}568\) assignments. A second recurrence checks odd-neighborhood validity directly on a column-by-column construction, without assuming the theorem's square-coloring classification. It agrees with the polynomial for \(105\) pairs with \(2\le n\le16\) and \(2\le k\le8\).

Expected output:

`VERIFICATION_OK brute_cases=19 raw_assignments=1647568 transfer_cases=105 test_lengths=2..16 palettes=2..8`

No random seeds, network calls or nonstandard modules are needed. Finite checks do not establish correctness for all lengths and palette sizes; the formal induction and combinatorial transition proof in `RESULT.md` supply that conclusion.
