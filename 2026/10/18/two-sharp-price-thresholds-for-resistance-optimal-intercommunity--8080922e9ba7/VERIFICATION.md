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

# Verification and scope

Run `python verify.py` with Python 3 and SymPy installed. It must print `Total exact assertions: 752` and exit with status zero. The code reconstructs the complete weighted network Laplacian from individual edges, computes \(N(\operatorname{tr}(L+\mathbf1\mathbf1^{\mathsf T}/N)^{-1}-1)\) exactly, and compares this with the independently derived group-spectrum objective. It also verifies budgets, full-matrix edgewise KKT inequalities and equalities, optimal objective formulas, exact upper and lower price boundaries and the fixed-smaller-group asymptotics. Assertions use exact symbolic/rational arithmetic at selected parameter values; the three-regime theorem for all integer group sizes rests on the proof in `RESULT.md`, not on finite enumeration.

Independent audit and independent validation have not been performed. The archival literature comparison is not a guarantee of novelty, and no claim is made beyond the two-group linear-cost model.
