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

# Reproduction

Run `python3 verify.py` from the directory containing this document. Python's standard library is sufficient.

The program constructs all \(3^n\) maps from vertices to \(\{0,1,2\}\) for each checked graph, directly checks every uncoloured vertex's two neighbours (or available path neighbours), and bins valid maps by the number of positive labels. It compares that independently obtained coefficient dictionary with the theorem for path orders \(1\)–\(11\) and cycle orders \(3\)–\(11\), examining 531426 maps in total.

A separate arithmetic check independently iterates the second-order characteristic recurrence and the path recurrence through order 100 and compares with the explicit coefficient formula, including the cyclic parity correction.

Expected terminal line: `VERIFY_OK direct_assignments=531426 paths=1..11 cycles=3..11 recurrence_lengths=3..100`.

These are finite regression and consistency checks, not proofs of the universal quantifiers. The proof for all orders is the independent-zero and inequality-forest classification in RESULT.md. No external independent audit or formal proof assistant validation has been performed.
