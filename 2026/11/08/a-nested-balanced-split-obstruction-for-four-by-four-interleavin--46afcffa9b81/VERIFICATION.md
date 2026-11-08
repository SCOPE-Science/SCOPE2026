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

# Finite verification and limitations

Run `python verify.py` with Python 3.9 or later and no nonstandard packages. The program exhaustively constructs all 70 two-chain interleavings of size four plus four, evaluates every one of the 16 comparisons on every word, verifies the precise 32/16/8/4-sized nested-split obstruction, and separately computes the complete Littlestone recursion for the square profiles of sizes one through four. The expected ending line begins with `FOUR_BY_FOUR_INTERLEAVING_CERTIFICATE_PASS`.

The depth-five lower bound is justified by a self-contained inductive construction in `RESULT.md`; the verifier additionally checks the exact result. Verification concerns a finite family, not an infinite extrapolation. The novelty assessment is limited to the cited comparisons; independent external review has not been performed.
