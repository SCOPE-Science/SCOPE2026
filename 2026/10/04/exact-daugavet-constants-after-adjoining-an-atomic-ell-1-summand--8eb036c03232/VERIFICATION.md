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

The proof was checked algebraically from the slice definition. The critical lower-bound dichotomy uses the fact that a norm-one functional on an \(\ell_1\)-sum has at least one dual block of norm one. The two matching upper bounds use, respectively, a refined slice from the \(X\)-component and a coordinate slice from the atomic \(\ell_1\)-component.

The included `verify_formula.py` checks the finite-dimensional specialization in exact rational arithmetic. For \(X=\ell_1^k\), the proposed identity simplifies to the known formula \(\operatorname{dc}(z)=2(1-\|z\|_\infty)\). Exhaustive signed integer vectors of total dimensions two through six, across every nontrivial split, produce `VERIFY_OK 92760`.

The computation does not certify the infinite-dimensional theorem; the theorem is established by the written proof. Literature comparison remains limited by indexing and terminology differences.
