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

The proof is self-contained after the contract/obstruction definitions stated in `RESULT.md`. Its critical nonstandard steps are the private-pivot identity minor, the exact-guard singleton explanation table, and the XOR-cycle obstruction for the witness-tree condition. The all-contexts difference subspace has dimension no more than the number of contexts minus one. No general external certificate is claimed.

Run `python checker.py` with standard Python 3. Recorded result: `ALL_CHECKS_OK antichains=193 semantic_tables=52670 tree_models=3103`. The checker performs finite Horn-closure checks on all nonempty antichains over at most four source coordinates, private-rank lower bound tests across 52,670 three-coordinate semantic tables with up to two choices, and 3,103 disjoint-label tree-code tests. Enumerated examples do not replace the algebraic proof.

Source access: full open-access HTML for arXiv:2610.32805v1 was read. Full text for the closed 1992 discernibility chapter was not obtained; priority claims are limited accordingly. Independent audit: not performed.
