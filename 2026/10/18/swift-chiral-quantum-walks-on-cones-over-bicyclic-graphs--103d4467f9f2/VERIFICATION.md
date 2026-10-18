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

# Reproduction notes

Use Python 3 (standard library only). From a directory containing `verify.py`, execute `python3 verify.py`. The checker creates many labelled theta, figure-eight, and odd–odd barbell graphs with the explicit complex phases from the theorem and independently checks each row of the Hermitian gain adjacency matrix. It applies the full cone Hamiltonian to the apex vector recursively and verifies moment identities through order twelve. It separately evaluates the even-cycle zero-root-contribution identity for unit-circle phases.

Expected deterministic output:

```
VERIFY_OK constructed_cones= 1145 even_lobe_obstructions= 28 cone_moment_orders=1..12
```

Finite floating-point checks provide corroboration, not an exhaustive graph census or a proof for arbitrarily large graphs. The mathematical proof in `RESULT.md` supplies the exact all-order argument, including the necessity and classification. The auxiliary code is standalone and does not depend on external data, unpublished packages, or another record.
