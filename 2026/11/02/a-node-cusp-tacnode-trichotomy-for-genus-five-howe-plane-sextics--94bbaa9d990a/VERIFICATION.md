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

# Exact verification and scope

The accompanying executable `verify_howe_types.py` uses the Python standard library only. Executed with `python3 verify_howe_types.py`, it returned:

`HOWE_SEXTIC_NODE_CUSP_TACNODE_WRONSKIAN_AND_CUSP_WITNESS_EXACT_PASS`

The code checks the rational cusp-witness branch-polynomial coprimalities and discriminants, the exact common Wronskian root at \(T=2\), the identity \(H(Q_1,Q_2,\phi)=0\), the quadratic and tangent cubic terms at \([-1:1:1]\), and the central-node linear terms. It also verifies distinct published examples over \(\mathbb F_{31}\) with a nodal quotient and an axis-node tangent-cone discriminant. The complete proof for all admissible parameters is geometric and is given in RESULT.md; the finite tests are not substituted for that proof. No external audit, certification, or independent validation has been performed.
