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

# Verification of the conjugacy-class census

The proof reduces equality of products of two automorphisms to the three necessary and sufficient residue-field equations in RESULT.md. Its cases distinguish a nonzero diagonal residue difference, a zero difference with nonzero off-diagonal vector, and a zero difference with a zero vector. Direct calculation gives centralizers of orders \((p-1)^2p^{b-1}\), \((p-1)p^b\), and \((p-1)^2p^{b+1}\), respectively; dividing the group order by these numbers gives the class sizes. Counting every element in each case yields the displayed complete distribution.

Run `python3 check_aut_classes.py` with Python 3 and no third-party packages. The checker enumerates all automorphism matrices and all their centralizers under genuine modular multiplication in seven parameter pairs, checks the distribution of **elements** across class sizes, and verifies the resulting class counts. The final marker is `AUT_CYCLIC_MIXED_CLASS_EQUATION_OK`. It does not certify untested parameters; those follow from the written proof. No independent mathematical audit has been performed.
