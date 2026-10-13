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

The proof in `RESULT.md` is the evidence for the infinite statement. The accompanying `verify.py` is an independent finite cross-check that constructs the graph neighborhoods directly and tests the defining strong-odd condition for every coloring in its stated range.

Replay command:

`python verify.py`

Expected output from the packaged artifact:

`ALL CHECKS PASSED; small_part_tuples=48; direct_color_assignments=536386; large_arithmetic_cases=700; small_range=r=2..4, part_sizes=1..4, total_order<=6; palette_q<=5`

Checks performed: the full formula for \(F_G(q)\) at every tested palette size; vanishing below the claimed chromatic number; positivity and exact count at the claimed minimum; and 700 larger arithmetic checks of the minimum and optimal-count formulas.

Limit: exhaustive enumeration is finite and does not certify the theorem for untested orders. No independent audit has been performed.
