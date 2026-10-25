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

The analytic verification consists of the exact cell-scaling identity, the expansion \(F(\rho)=(1-\rho)^5/196830+O((1-\rho)^6)\), and convergence of the coefficient series by comparison with \(\sum_i i^{-(r+5)}\). The first-cell integral is \(\int_0^1(t^3-t)^2dt=8/105\). The included `verify.py` checks exact rational cell scaling for the subfamily \(r=3\), meshes \(N=2,\ldots,7\), and reports numerical partial sums for selected \(r\); these finite checks are reproducibility aids, not the proof for all \(r>0\). No independent audit or independent validation is claimed.
