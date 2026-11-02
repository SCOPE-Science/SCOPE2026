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

Compile the packaged source using `g++ -std=c++17 -O3 verify.cpp -o verify`, then execute `./verify` in the same directory. It constructs every product as an edge-labeled adjacency graph, computes shortest paths by breadth-first search and enumerates the forbidden triples, then performs an exhaustive exact-size backtracking search. It separately checks that each predicted optimum is admissible and cannot be enlarged. Finding precisely the predicted \(L-1\) admissible sets of optimal size and proving that all are inclusion-maximal also rules out larger admissible sets for each tested finite graph by downward closure.

The exhaustive parameter pairs are \(m\in\{2,3\}\), \(2\le L\le5\), and \(m=4\), \(L\in\{2,3\}\). The output for these ten instances ends in `VERIFY_OK`. In the largest case (\(m=3,L=5\)), the backtracker visits 716383 internal nodes; in the \(m=4,L=3\) case it visits 46628 internal nodes. The proof in `RESULT.md` supplies the full infinite argument, including the exceptional \(m=t=2\) boundary, and the finite computation is an additional check only.

Independent auditing is not performed; no claim of formal mechanized proof is made. The reachable literature record includes a 2026 graph-products paper whose full text was not accessible for comparison.
