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

The symbolic checker verifies three exact algebraic steps used in the proof:

1. the reciprocal expansion around \(\bar v\);
2. the weighted-balance elimination that produces the formula for \(\bar v-v_*\);
3. in the equal-fear case, cancellation of the common fear term from the sign of \(q_1-q_2\).

The strict implication \(\mu\ne\delta_{E_*}\Rightarrow J_i>0\) is not delegated to symbolic computation. It is proved analytically from invariance of the support and rigidity of complete compact positive solutions of the scalar logistic equation.

No finite enumeration, trajectory simulation, or numerical tolerance is used to establish the theorem. The checker output expected from the supplied source is `VERIFY_OK`.
