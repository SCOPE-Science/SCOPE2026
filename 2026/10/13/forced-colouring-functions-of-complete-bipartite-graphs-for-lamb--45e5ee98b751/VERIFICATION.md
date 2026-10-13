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

The general theorem is proved symbolically in `RESULT.md`. The executable check is deliberately finite and corroborative.

`artifacts/verify.py` directly simulates the forcing rule on every partial assignment for \(\lambda\in\{3,4\}\), \(1\le m,n\le3\), and total order at most six. For each state it checks equality between the direct forcing outcome and the structural classification used in the proof. It then compares the exact probability obtained by summing all forcing states with the closed formula at \(p=1/(2\lambda)\), \(p=1/(3\lambda)\), and \(p=1/\lambda\). Finally it checks the explicit \(\lambda=3\) formulas for \(K_{1,2}\), \(K_{1,3}\), and \(K_{2,2}\).

Replay output:

`ALL CHECKS PASSED; profiles=18; states=31081; rational_probability_evaluations=54; lambda_values=3,4; max_order=6`

The finite check does not establish the unrestricted theorem; it is an independent sanity check on the symbolic argument and counting formula. No computation beyond the stated finite ranges is claimed exhaustive.
