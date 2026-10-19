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

The formula and boundary cases were checked analytically using the local energy increment. An independent reference implementation, `check_absorbing.py`, calculates each configuration's full periodic Hamiltonian, evaluates the Hamiltonian after individually flipping every spin, and counts strict absorbers by down-spin number. It verifies the exact phase diagram for \(N=5,6,\ldots,14\), four independent pairs of positive couplings satisfying \(0<K<J/2\), and several fields including zero, weak fields, both threshold equalities, intermediate fields, and strong fields: 330 finite-state parameter comparisons passed.

A separate symbolic characteristic-polynomial calculation checked \(\det(\lambda I-T)=\lambda^4-\lambda^3-z^2\) and \(\det(I-tT)=1-t-z^2t^4\). The finite checker and algebraic calculations are reproducibility checks; the proof of the universal result and entropy limit is in RESULT.md. No independent audit or third-party validation has been conducted.
