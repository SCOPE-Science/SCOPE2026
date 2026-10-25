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

# Reproducible checks and limits

The included `verify.py` is self-contained apart from Python 3 and SymPy. Running `python verify.py` reconstructs the weighted de Bruijn transfer matrix from all three-bit states and the two forbidden alternating four-letter words. It verifies the determinant and characteristic-polynomial factorizations by symbolic subtraction, with both differences exactly zero.

Independently, for each \(3\le n\le14\), it enumerates all \(2^n\) colorings and evaluates every opposite-color swap with the original and the destination utilities. All binary verdicts match cyclic avoidance of \(0101\) and \(1010\), and the complete producer-color count of each degree matches the weighted matrix trace. The totals are \(8,14,22,38,72,134,242,442,816,1502,2758,5070\) and also agree with the tribonacci-Lucas expression.

The infinite assertion rests on the combinatorial proof and exact transfer identity, not on extrapolating finite tests. The program does not independently assess prior-art originality, welfare outcomes, or other neighborhood definitions. Independent audit has not been performed.
