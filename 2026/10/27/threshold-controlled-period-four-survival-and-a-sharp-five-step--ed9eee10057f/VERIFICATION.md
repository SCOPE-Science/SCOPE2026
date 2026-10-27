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

# Finite computational verification
Execute the embedded `gh_bipartite_threshold_checker.py` with Python 3. It generates every labelled state for each of the ten parameter triples listed in `gh_bipartite_threshold_checks.txt`. It computes the deterministic update directly vertex by vertex, checks \(F^{17}(x)=F^5(x)\), checks that every trajectory enters a cycle by time five, and counts the fixed points and exact three- and four-periodic labelled states against the independent multinomial and binomial formulas. The run contains graphs of up to ten vertices, including a threshold-two example with sharp entrance time five. Its lines are execution evidence, not a substitute for the symbolic proof for arbitrary \(a,b,k\). The founding historical article and one later lattice paper were not inspected in full, so literature originality remains a bounded judgment; independent audit is not performed.
