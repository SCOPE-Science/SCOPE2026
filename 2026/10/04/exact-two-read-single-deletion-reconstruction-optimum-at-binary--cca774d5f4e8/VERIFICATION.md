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

`certificate.json` contains two finite certificates for the same length-\(7\) compatibility graph: an explicit compatible set of size \(70\), and a color assignment using exactly \(70\) colors.

Run `python3 verify.py`. The verifier constructs all \(128\) binary words and their distinct single-deletion descendants directly from the definition. It checks every pair in the witness code, every compatibility edge against the coloring, and the equivalent confusability-graph clique-cover condition. Successful replay ends with `VERIFY_OK`.

Run `python3 search.py` independently. This program reconstructs the graph independently and executes a complete maximum-clique branch-and-bound search with valid greedy-color upper bounds. Successful replay prints `MAX=70` and `SEARCH_OK`.

The verification proves only the stated finite length-\(7\) claim. It does not extrapolate to any larger length, count all optimum codes, or establish a general closed formula.
