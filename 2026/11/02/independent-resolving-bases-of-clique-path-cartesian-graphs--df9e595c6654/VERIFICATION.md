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

# Reproduction and limits

Run `python3 verify_independent_clique_path.py` with Python 3. The code derives graph adjacency directly from the Cartesian-product definition, computes distances by BFS, checks independence against those edges and distinguishes all vertices by full distance vectors. For each tested graph it exhausts independent sets of every smaller size and every set at the first feasible size; it also checks all possible sizes for cases with no independent resolving set. Expected counts are calculated from the closed formulas.

The executed script returned `ALL PASS: 28 graphs; 72202 independently constructed landmark sets tested.` Cases include \(q=2,3,4,5,6\), both impossible short-length instances and feasible instances, and path lengths through eight in the two-color case. The analytic argument in RESULT.md proves the infinite parameter ranges. The verifier is a finite regression check only, not an exhaustive certificate for infinitely many graphs.
