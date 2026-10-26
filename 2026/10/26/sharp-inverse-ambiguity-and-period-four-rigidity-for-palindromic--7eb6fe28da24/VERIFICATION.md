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

# Verification

Run `python3 verify.py` with standard Python 3. The verifier independently reconstructs forward duplication from every detected inverse candidate. It exhaustively checks binary instances for duplication lengths up to six and short source lengths, ternary examples (including full odd-count rigidity at lengths three, four and five), and quaternary boundary cases. It checks witness cardinalities for all \(3\le k\le80\) with \(4\nmid k\) at multiple large source lengths. The expected successful final line is `VERIFY_OK`.

The proof is symbolic: finite enumeration is a cross-check only. The reviewer compared the exact source/received length indices, the collapse of consecutive palindrome starts, the period-four implication for shifts by two, the modular difference between distinct parents, and the necessity of the stated equality pattern. No claims about longer cases when \(4\mid k\) or even-start-count maximizer classification are tested or made.
