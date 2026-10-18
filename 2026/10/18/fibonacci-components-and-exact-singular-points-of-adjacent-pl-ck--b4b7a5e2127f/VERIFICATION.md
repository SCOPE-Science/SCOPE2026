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

# Reproducible checks and limits

The companion standalone script `verify.py` requires only Python 3 and executes with `python verify.py`. It directly enumerates each rank-two row space using unique reduced row-echelon representatives, checks the adjacent Plücker equations, computes the full Jacobian over the stated finite fields, and compares its rank to the claimed intrinsic smoothness test. It also checks independent-interior-subset counts. The verified configurations include the complete \(\mathbb F_2\)-Grassmannians for \(n=4,5,6,7\) and \(\mathbb F_3\)-Grassmannians for \(n=4,5\).

The proof of the all-characteristic result depends instead on the block-stratum dimension formula, the complete-intersection height criterion, generic reducedness, the local Jacobian linear-independence calculation, and adjunction. Finite experiments do not establish the theorem for untested fields or unbounded sizes. The specific generic ordinary-crossing statement concerns only the stated open subset of adjacent-zero strata. Independent audit has not been performed.
