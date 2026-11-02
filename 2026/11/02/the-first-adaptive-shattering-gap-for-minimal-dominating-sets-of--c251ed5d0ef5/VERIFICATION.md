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
The finite certificate was reconstructed from all vertex subsets of each path on one through eleven vertices. Two independent exact membership predicates, one based on single-vertex deletion and one based on private neighbors, returned identical minimal dominating families. Enumerating every vertex-query support gives the VC dimensions, including all 462 five-element supports on the eleven-vertex path. Memoized exact first-query recurrence supplies Littlestone upper bounds, and all eleven explicit adaptive witness trees were replayed against the concepts. In particular, the eleven-vertex tree has 32 leaf witnesses; its 36-concept cardinality separately rules out depth six.

On the connected two-module graph, every product pair from the two 36-element families, all 1,296 pairs, was independently checked for minimal domination. This finite check supplements rather than replaces the unrestricted support-vertex gluing proof. The arbitrary-size dimension identities use a separate product-additivity proof.

Reproduction: in a folder with `verify_minimal_domination.py`, execute `python3 verify_minimal_domination.py`; compare standard output to `verification_output.txt` and verify regenerated `adaptive_trees.json` and `path_census.json` match the packaged files. No claim of independent scientific certification is made.
