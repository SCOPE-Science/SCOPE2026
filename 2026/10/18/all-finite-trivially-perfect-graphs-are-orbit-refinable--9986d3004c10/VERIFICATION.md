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

The infinite claim is proved by component-size detection and induction on maximal connected-component order; the finite checks serve only as independent consistency tests of small cases.

Run `python check_forest.py` to enumerate canonical rooted forests through eleven vertices and test within-colour graph automorphisms by pointed isomorphism. Run `python check_atlas.py` to independently select all trivially perfect graphs in the graph atlas through seven vertices via the forbidden induced subgraphs and test orbit equality. Run `python check_nonamenable.py` for the six-vertex limitation witness. Compare outputs with the three included `.out` files. NetworkX is the only nonstandard library.

No complete finite-census program can by itself verify the unbounded theorem. The proof's key noncomputational assertions are that two refinement rounds recover a component's order from the maximum degree in the closed neighbourhood, and that stable colour restrictions to unions of cells remain equitable; these assertions were independently reconstructed in the self-review. There has been no independent scientific audit.
