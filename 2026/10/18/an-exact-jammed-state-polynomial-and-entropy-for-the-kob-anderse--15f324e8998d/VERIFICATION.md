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

The attached `verify.py` rebuilds the local rule and a 64-state transfer graph, checks the unique recurrent 29-state primitive component, verifies the full weighted characteristic-polynomial identity with exact symbolic arithmetic, and compares physical-graph brute-force enumerations for all 4 through 8 rungs against occupancy-graded transfer coefficients. Execution passed in the supplied package. SymPy is needed for the exact polynomial arithmetic. The finite checks are not used as a proof of the all-size transfer identity: that identity follows from the closed-walk bijection and exact finite matrix reduction. Root isolation and Perron–Frobenius, plus analytic perturbation, prove the asymptotics. Independent scientific validation has not occurred.
