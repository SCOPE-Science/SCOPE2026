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

# Verification of the choice-strength theorem

The proof in `RESULT.md` was reconstructed from the source definitions: (i) inductive soundness of generated certificates, (ii) ZF finite-list selection for depth-zero subterms, (iii) the exact certificate/selector identity for the fixed term, (iv) three-level order construction to recover arbitrary choice functions, and (v) an explicit height-two selector. The source's universal neighborhood-product constructor, not a weaker existential approximation, is essential.

A standalone Python 3 checker in `check_choice_height.py` enumerates all rooted labelled partial orders on carriers of sizes one through five compatible with a topological numbering. Every finite rooted poset admits such a numbering. It independently evaluates semantic truth and compatible generated certificates for `Box Diamond (+)` under every Boolean truth-set valuation. It also checks the explicit height-two construction. Successful output:

```
FINITE_VERIFY_OK rooted_orders=51 valuations=1414 height_two_positive=9
Logical limit: every finite family has a selector; this program cannot certify AC over arbitrary sets.
```

Run directly with `python3 check_choice_height.py`. Only the Python standard library is used. No external packages, stale logs, mechanical ZF proof, proof assistant, or independent auditor are involved. The finite tests are diagnostic only: an infinite family without a global selector cannot be exhibited in ZF without further model-theoretic metatheory. The mathematics rests on the symbolic ZF reductions in `RESULT.md`.
