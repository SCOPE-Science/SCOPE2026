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

# Reproducibility

Execute `python3 verify.py` from the directory containing that file using Python 3 standard library only. Successful completion prints `VERIFY_OK: generator rigidity, embedded census, refined EGF n<=5`.

The program independently generates partial bijections for \(0\le n\le5\), constructs inverse submonoids by closure, checks distinct generator fibers, computes chain and cycle profiles, compares every positive-chain profile to rational formal-power-series coefficients, independently counts cyclic subgroups of each symmetric group by permutation orders, and checks total embedded counts.

The checked totals for \(n=0,1,2,3,4,5\) are \(1,2,6,24,126,838\), respectively. Proof of the universal rigidity lemma and of the formal generating series is mathematical and does not rely on numerical extrapolation. No independent external validation or machine-formal proof is asserted.
