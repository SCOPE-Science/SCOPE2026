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

The analytic proof in `RESULT.md` gives the defect-partition bijection, weighted-state overlaps, a dimension-free Pauli-moment continuity inequality, the partition-function upper bound, and the explicit entropy error estimate for all real orders above one.

Run `python verify.py` with Python 3 and NumPy. The script verifies the Dyck-area identity and staircase counts through half-chain length six and computes all Pauli moments for half-chain lengths one to four at \(q=1/4\). Its exact four-qubit comparison is \(F_2=1-4q(1-q)^2/(1+q)^4\). The run produced the final line `All finite checks passed; infinite-size statements use the separate analytic proof.`

Finite enumeration checks normalization and local formulas only; it does not prove convergence for unbounded system sizes. That inference is contained in the independent analytic inequalities in the proof. Numerical moment values are not rigorous interval enclosures. No independent audit or external validation has been performed.
