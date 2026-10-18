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

The standard-library script `verify.py` enumerates connected complete multipartite graphs of all unordered positive part-size compositions on 2 through 8 vertices. For each graph it builds all cycle hulls with the induced-component criterion; independently evaluates Helly, Radon and convex independence on each subset; and compares resulting faces and counts to the proposed classification. It computes simplicial boundary ranks over \(\mathbb F_2\) to verify reduced Betti numbers of the predicted complexes. Result: `PASS 58 multipartite instances on 2..8 vertices; 2414 independent subsets; all three predicates and mod-2 homology verified`.

The script uses no external software or remote dependencies. Finite checking and mod-two homology do not prove the unrestricted integral homotopy statement; the general hull analysis and CW argument in RESULT.md supply that proof. Scientific bibliographic priority is subject to the stated unresolved comparison.
