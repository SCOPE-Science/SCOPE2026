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

# Mathematical verification

The standalone program `verify.py` enumerates partial maps on whole blocks and checks that actual squares are empty precisely in the predicted rank strata. It checks 17 finite configurations, including the order-preserving unblocked boundary, and verifies total monoid size without using the square-zero formula. It also computes four factorial-critical samples at both parities (eight cases) and fixed-size mean/variance diagnostics. The direct maps are enumerated by their underlying point maps rather than by the theorem's disjoint-support combinatorial formula.

Run `python3 verify.py` in a directory containing this file. Success prints `DIRECT_ENUMERATION_OK 17` and ends with `VERIFY_OK`. The proof in RESULT.md supplies the unbounded argument: a conditional ternary multinomial local central limit theorem and a dominated-convergence argument from exact factorial ratios. The numerical tests are finite and cannot establish infinite convergence or publication priority.
