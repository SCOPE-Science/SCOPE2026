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

# Verification scope

`python3 check.py` uses exact integer truth-table masks. For each of the \(2^{2^{m+1}}\) pairs of valuations for \(m=1,2,3\), it enumerates all allocations, evaluates the two envy inequalities directly, and separately applies the definition of Pareto dominance to every realized pair of utilities. It compares both resulting feasibility bits to the complementary-support theorem and checks the exact EF, EF-and-PO, and conditional-by-normalization counts.

Expected checked totals: \(16,256,65536\) profiles. Observed no-EF-and-PO totals: \(2,8,80\); no-EF totals: \(2,4,16\); EF-but-not-EF-and-PO totals: \(0,4,64\). Expected and observed normalized counts agree. The program terminates with `PASS` after all exact comparisons.

The general proof is the structural argument in `RESULT.md`. Exhaustive finite checks alone cannot establish the result for unbounded \(m\). The results do not assert a distributional law beyond the explicit independent fair Boolean truth-table model. Independent audit has not been performed.
