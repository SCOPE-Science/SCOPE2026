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

Execute `python verify.py` with Python 3. Its enumerator computes the intercalates directly by the defining equality of opposite corners and computes the ascent score directly for all \((n!)^2\) row/symbol permutations. Each computed expectation and second moment is reduced to a `Fraction`; equality with the displayed formula is asserted exactly. The generator separately enumerates all normalized order-five Latin squares, so no external table is required.

Actual successful checks: cyclic tables of orders 2, 3, 4, 5, 6 have respectively intercalates 1, 0, 4, 0, 9 and variances 0, 1, 10/9, 5/2, 14/5; elementary-abelian table of order 4 has 12 intercalates and variance zero. All 56 reduced order-five Latin squares passed: 6 with intercalate count 0 and variance 5/2, and 50 with count 4 and variance 21/10. Program output concludes with `EXACT_ORBIT_MOMENTS_VERIFIED`.

The source proof is infinite and symbolic. Exhausting small orders does not by itself prove arbitrary order, rule out all other invariants, or certify novelty. The rigidity classification follows the proof and a known maximal-intercalate result. The code does not constitute an independent audit.
