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

The checker implements the signed double Italian definition directly. For \(T_4\) and \(T_5\) it enumerates every assignment from \(\{-1,1,2,3\}\) to all vertices and checks every vertex condition from scratch.

A second exact method generates all feasible arm states from the local defining inequalities, then performs dynamic programming over support-label sums and positive support mass. This method checks every \(q\) from \(4\) through \(60\) and compares both the optimum value and the full number of optimum assignments with the closed formulas.

Recorded output:

```text
VERIFY_OK
full_label_bruteforce_q = 4,5
direct_labelings_checked = 4456448
exact_arm_state_DP_q = 4..60
all optimum values matched q+ceil(q/4)+1
all optimum counts matched the residue-class formula
```

The finite computations are corroborative only. The theorem for every \(q\ge4\) follows from the center-case proof.
