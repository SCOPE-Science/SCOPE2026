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

# Reproducible mathematical checks

The analytic proof in RESULT.md establishes the formulas for every finite admissible parameter and is the primary correctness evidence. To supplement it, run `python3 verify.py` with standard Python 3. It directly computes the iterated interpolation closure and minimizes over every feasible candidate discovery set without using the proposed closed forms inside either independent computation. The program then compares both results with the formulas for all n=1,...,7, all 1<=r<=k<=n, and all S; expected stdout includes `PASS: 5630 individual subset comparisons`. All arithmetic is integer-valued. This finite test does not replace an infinite proof. No independent scientific audit has yet been performed.
