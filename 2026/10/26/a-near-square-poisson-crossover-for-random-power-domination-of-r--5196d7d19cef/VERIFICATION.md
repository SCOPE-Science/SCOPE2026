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

Run `python3 verify.py` with Python 3.8 or later and the standard library only. The script enumerates all \(2^{mn}\) initial sensor subsets for \((m,n)\in\{(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3),(4,4)\}\). Each selected subset is simulated directly using rook-graph adjacency and ordinary power-domination propagation, then compared with the independent empty-row/empty-column test. Each coefficient of the finite power-domination polynomial is computed independently by inclusion-exclusion and compared with the exhaustive counts.

The verifier also checks exact mixed factorial moments for the \(3\times4\) board under independent cell inclusion at probability \(1/3\), and under uniformly selecting exactly four cells. These checks are finite and exact. They do not empirically certify the asymptotic Poisson convergence, which is established mathematically by the displayed moment arguments and concentration estimate. The expected terminal message is `ALL_VERIFY_OK`.
