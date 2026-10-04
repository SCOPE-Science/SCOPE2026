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

`verify_partial_basis_teleportation.py` reconstructs the source's partially entangled orthonormal basis and the three-qubit input-resource state directly.

It checks the corrected four-branch decomposition for deterministic complex input amplitudes and several interior values of \(x\). It verifies that every branch map has singular values \(x/\sqrt2\) and \(y/\sqrt2\).

The script verifies the corrected Kraus completeness relation and that the success map returns the unknown qubit with joint probability \(y^2/2\) per branch, so the four-outcome total is \(2y^2\).

It also checks that the two matrices printed in the source's Eq. (9), if interpreted as Kraus operators, fail completeness for interior \(y/x\).

The replay is supplementary. Branchwise optimality follows analytically from the contraction inequality for a reversing Kraus operator.

No independent audit has been performed.
