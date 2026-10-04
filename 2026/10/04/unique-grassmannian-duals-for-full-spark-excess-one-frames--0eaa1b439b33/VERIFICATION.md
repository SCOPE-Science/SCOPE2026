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

The theorem is verified analytically by the following chain.

1. A dual frame has an idempotent cross-Gramian whose range is the analysis range, and every projection onto that range arises from a unique dual.
2. In excess one, that range is the hyperplane \(z^\perp\), so every such projection is \(I-qz^*\) with \(z^*q=1\).
3. The off-diagonal maximum is exactly \(\max_i b_i|q_i|\).
4. The weighted triangle inequality gives \(1\le\mu\sum_i a_i/b_i\). Equality forces every row constraint to be active and every summand \(\overline{z_i}q_i\) to have the same nonnegative phase, proving uniqueness.
5. Comparing the resulting \(q\) with the orthogonal-projection vector \(z/\|z\|^2\) proves the canonical-dual criterion.

The accompanying exact checker verifies the displayed rational \((3,2)\) counterexample using fraction arithmetic. It checks the dual identities, cross-Gramians, idempotence, and the strict inequality \(2/5<3/7\). This finite replay verifies only the example; the general theorem rests on the proof above.
