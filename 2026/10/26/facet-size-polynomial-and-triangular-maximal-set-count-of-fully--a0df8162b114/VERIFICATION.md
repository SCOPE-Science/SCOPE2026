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
Run `python3 verify.py`. The program uses only the Python standard library. For each positive bundle vector with between two and five spine vertices, pendant bundles of size one or two, and at most fourteen graph edges, it enumerates every edge subset. Each candidate is independently checked against every unique shortest path by a breadth-first search in the tree. The program also constructs the predicted sets from the mathematical classification and identifies inclusion-maximal subsets by direct attempted single-edge extension. Exact equality holds for both complete families and facet families, for 60 configurations and 135,720 tested edge subsets. The expected output is in `verification_output.txt`.

This is a finite consistency test, not a certificate of the infinite theorem. The proof in `RESULT.md` handles arbitrary positive bundle multiplicities and arbitrary spine length. No independent mathematical audit was performed.
