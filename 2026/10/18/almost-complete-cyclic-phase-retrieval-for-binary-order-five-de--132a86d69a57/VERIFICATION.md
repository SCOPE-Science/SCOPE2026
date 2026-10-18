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

# Verification instructions and limits

Place `verify.py`, `cycles.csv`, and `ambiguities.csv` in one directory. Run `python3 verify.py` with Python \(3.10\) or newer. There are no external dependencies.

The program constructs all Eulerian circuits anchored at the uniquely occurring all-zero five-bit edge. Independently it checks every one of the \(65536\) local edge-pairing assignments. Both methods produce the same \(2048\) canonical de Bruijn cycles. For each of those cycles, it computes the \(16\) independent periodic autocorrelation values three ways: direct signed products, pair-difference intersections, and integer bitmask popcounts. All methods agree pointwise.

The program then verifies the \(526\) full autocorrelation signatures and their \((2,4,8)\)-size multiplicities, the \(528\) reversal/complement symmetry orbits, exactly two nontrivial homometric fibers, and \(521\) versus \(526\) distinct lag signatures at cutoffs \(12\) and \(13\). Every row of both CSV files is checked against the independently regenerated objects. The expected successful output is reproduced in `RESULT.md`.

This constitutes finite exhaustive verification, not an infinite-order proof, an assertion about arbitrary binary strings, or an independent scientific audit. Bibliographic searches and checked primary sources are documented separately in the accompanying review.
