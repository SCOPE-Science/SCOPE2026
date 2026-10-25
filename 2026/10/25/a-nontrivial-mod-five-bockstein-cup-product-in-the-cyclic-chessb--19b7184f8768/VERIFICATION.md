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

# Reproducibility

Run `python verify.py` with Python 3 and SymPy. The file builds all 20, 120, 240 and 120 original nonempty faces directly from the four-by-five rook definition; reduces by the fivefold translation action to 4, 24, 48 and 24 orbit cells; constructs integral boundary matrices; asserts both differential compositions are zero; and recomputes all nonzero Smith factors by exact integer arithmetic. It verifies that the signed top cycle is closed, the integer Bockstein is a cocycle, and the Alexander–Whitney product has top-cycle evaluation \(2\) modulo five.

Expected terminal output includes `H0=Z; H1=Z/5; H2=Z^4; H3=Z`, `mod-5 evaluation <u cup beta(u),[Y]> = 2`, and `PASS`.

This finite exhaustive verification proves only the presented cell-complex calculation; it does not prove exhaustive coverage of the mathematical literature or independent review.
