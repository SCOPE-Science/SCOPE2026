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

# Reproducibility

Run `python3 verify_tree_purity.py` in the directory containing the script. The program uses no nonstandard dependencies. It enumerates every Prüfer code for orders three to six, plus thirty additional codes for orders seven to nine. For each tree it constructs all strong matchings by induction over vertex-order prefixes, constructs the rooted spanning orientations, and checks that the greatest possible cardinality is one less than the tree order, the maximum faces are exactly the rooted facets, and every strong face is root-extendable precisely at diameter at most three. It also checks the leaf-removal condition for pure-facet complexes and a diameter-four path witness.

The packaged script was executed, returning `VERIFY_OK 1470 labeled-tree test instances; diameter_counts= [(2, 42), (3, 285), (4, 780), (5, 360), (6, 1), (7, 1), (8, 1)]`. These tests do not exhaust arbitrary tree orders and do not constitute the universal proof. The universal proof appears in `RESULT.md` and relies on the source definitions and a constructive obstruction. No independent audit has been performed.
