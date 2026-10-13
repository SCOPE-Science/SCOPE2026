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

The theorem has two logically separate components.

First, `artifacts/verify.py` performs an exhaustive finite table calculation. Each product of two group-like basis vectors is encoded as one of `0`, `g0`, or `g1`, so all \(3^4=81\) labeled tables are checked. The script verifies exactly \(21\) self-distributive compatible tables, \(13\) simultaneous-swap orbits, \(6\) orbits with no zero entry, \(5\) swap-fixed tables, and \(3\) swap-fixed tables with no zero entry. The recorded run ends with `CHECK_OK`.

Second, the arbitrary finite-field statement is symbolic. A two-dimensional finite étale algebra over \(\mathbb F_q\) is either \(\mathbb F_q\times\mathbb F_q\) or \(\mathbb F_{q^2}\). The quadratic extension is separable for every finite field, including characteristic \(2\), so its dual coalgebra splits after scalar extension and the nontrivial Galois automorphism swaps the two group-like factors. Galois-fixed tables are exactly the descended products. The nonsplit coalgebra automorphism group is the same order-two Galois group, which fixes each descended table, so the five fixed tables represent five distinct isomorphism classes.

The checker does not certify general Galois descent or the classification of finite étale algebras; those are used as proved algebraic steps in the written proof. No independent audit has been performed.
