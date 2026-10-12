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

# Computational verification

Run the complete embedded `verify_nuclei.py` with Python 3, without third-party packages: `python3 verify_nuclei.py`.

The actual successful run reported `VERIFY_OK ordered_pairs_checked 349525 refined_ranks_checked 55 independent_full_map_classifications 5 product_instances 3 independent_full_product_classifications 2`.

The checker independently compares literal compositions and the separator-word condition for every pair of nuclei on each finite chain of cardinality 1 through 10, checks the fixed-intersection composition, the entire rank profile and the linear recurrence, and directly filters all self-maps by the nucleus axioms on chains of cardinality at most 5. Product checks examine coordinatewise nuclei on sizes (2,2), (2,3), and (3,3). A second oracle exhaustively classifies all inflationary meet-preserving idempotent self-maps of products with factor sizes (2,2) and (2,3), independently verifying no off-axis nuclei are missing.

The finite checks confirm these bounded instances only. The all-size statement is derived in the accompanying proof via separator intervals and exact generating functions. Prior mathematical literature includes general composition facts and the same unrefined numeric sequence; neither computational checks nor search establish global historical originality or independent certification.
