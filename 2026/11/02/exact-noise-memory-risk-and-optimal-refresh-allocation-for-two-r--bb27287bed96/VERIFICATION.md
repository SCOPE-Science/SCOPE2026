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

# Verification of the mathematical result

Run `python verify.py` with Python 3 and no external packages. It outputs `VERIFICATION_OK 8100 exact rational assertions`. The verifier constructs and independently propagates the seven monomials of degree at most two in the scalar orthogonal error and two cached observation errors, using all sixteen conditional refresh/sign combinations and rational probabilities. It compares the resulting stationary moment identities to the closed-form solution for five rational angle choices (including the orthogonal limiting boundary), twenty-five refresh probability pairs, and three innovation-scale choices. It also compares the clipped exact allocation with sixty-five evenly spaced feasible rational allocations over a grid of budgets, row angles and variances; direct common-rate formula identities are checked separately.

The finite test grid is not a proof of validity for every real parameter, nor is a stationary linear identity by itself sufficient for convergence. The analytic geometric recursion has scalar contraction factor \(0<u<1\), which independently proves convergence to the unique second-order stationary response. The exhaustive stationary moment tests are exact for the checked cases only. The result assumes independent centered rowwise innovation streams and the other hypotheses in `RESULT.md`; no independent audit or empirical deployment test has occurred.
