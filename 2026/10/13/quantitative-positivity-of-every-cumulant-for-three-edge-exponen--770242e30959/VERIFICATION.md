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

Run `python3 matching_cumulants_verify.py` using the included standalone script. The exact-rational checker reports `PASS 11500 exact rational and polynomial checks`. It checks the original three-by-three transform by cross multiplication, the coefficient identity for the numerator, the standard exact mean over \(3\leq m,n\leq16\), and the sharp majorant computations for \(3\leq m,n\leq12\) to order 25, along with 300 universal-majorant coefficients.

The exact all-parameter/all-order bound is proved by coefficientwise domination, a recurrence and pole-zero pairing in `RESULT.md`. The finite checker is a regression test, not an exhaustive proof. The lower bound is not asserted optimal. Independently performed scientific review, formal verification and outside priority confirmation have not occurred.
