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

Run `python3 artifacts/verify_crowns.py` from the extracted package root. The program requires only the Python standard library and independently enumerates actual functions between the reflexive crown posets, testing `f(up(x))=up(f(x))` for every source point and testing global surjectivity. These checks do not assume the walk normal form. In addition, direct lazy-walk enumeration is compared with subset inclusion–exclusion traces for 27 pairs, the target-two formula is checked in four exhaustive function instances and 11 binomial identities, and the short-length coefficient and first zero-winding formulas are checked.

The command succeeds on all checks; its actual stdout is preserved verbatim in `artifacts/verify_output.txt`. Exhaustive direct-function enumeration covers source n=1–4 and target m=2–4 in selected pairs; broader finite checks range through target m=5, source n=9. No finite enumeration proves an unbounded claim. The accompanying symbolic proof in RESULT.md establishes the theorem for every integer n,m at least two. Any external audit remains unperformed.
