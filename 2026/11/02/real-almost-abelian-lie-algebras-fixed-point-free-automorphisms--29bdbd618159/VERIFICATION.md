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

Run `python verify.py` with SymPy installed. The script tests 19 exact-arithmetic invertible real matrices with Jordan structures spanning paired real eigenvalues, doubled purely imaginary blocks, single purely imaginary blocks, and off-axis complex quartets. Each test checks anticommutation and absence of eigenvalue one; order-four examples additionally check the fourth power. A symbolic two-dimensional calculation verifies the sign obstruction for a single rotation block.

Observed output:

```
VERIFY_OK exact_matrix_constructions=19 parity_obstruction_symbolic=1
```

These are reproducible finite tests. The universal existence and impossibility assertions depend on the Jordan-block proof in `RESULT.md`; no infinite enumeration, formal proof assistant, or independent audit is claimed. The completeness of literature priority has not been independently established.
