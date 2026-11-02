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

# Verification of the credit-fairness incentive obstruction

Run `python3 verify_credit_gadget.py` with the standard Python library. The code constructs both true-demand matrices, both forced truthful allocations, and the two altered report histories. It calculates credits by the analytically justified formula \(\Delta c_{i,t}=1-a_{i,t}\), tests CF1–CF5 directly for all five rounds, checks PE, compares the common round-2 reports and allocations, and computes exactly the two deviator payoffs. It samples the 101 rational split values \(x=1+k/100\), \(0\le k\le100\). A second local lattice check enumerates critical round choices at resolution \(1/10\).

Expected result: `VERIFY_OK rational_split_points=101 truthful_round_feasible=[1, 1] altered_round_feasible=11 max_min_gain=1/2`.

**What the checker does not prove:** no finite grid proves the five-round theorem for all real allocations. The complete symbolic proof is supplied in RESULT.md. In particular, the credit identity comes from PE plus CF1–CF3, the two truthful paths from PE and CF4–CF5, and the opposite incentive inequalities from the common observable prefix. No external or independent mathematical audit has been performed.
