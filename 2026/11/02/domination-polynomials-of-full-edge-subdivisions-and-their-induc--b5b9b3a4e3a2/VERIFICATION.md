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

# Reproducible checks

Run `python3 verify.py` in the directory containing this file and the bundled `verify.py` file. It uses only the Python standard library and a fixed random seed. It constructs each full subdivision from the original graph's edge list and independently tests domination by closed-neighborhood coverage. The implementation compares every coefficient of the direct enumeration with the vertex-subset formula, brute-forces maximum induced matchings, and checks the forest component constraints for all actual minimum dominating sets. It separately evaluates the complete and complete-bipartite specializations.

Observed output:

`VERIFY_OK 56 graphs; 104426 direct vertex subsets tested; arbitrary-graph polynomial, induced-matching minimum, minimum-set formula, complete and bipartite specializations`

The 56 graph instances include disconnected and edgeless roots, paths, cycles, complete graphs, complete bipartite graphs, and fixed-seed generated simple graphs. Larger complete-root cases are restricted by exhaustive search. These finite computations do not prove the all-graph statements; the mathematical proof is the combinatorial partition and induced-matching argument in `RESULT.md`.

The full 2025 subdivision-paper text was not available for exhaustive publication-priority comparison. Scientific status is self-reviewed, not independently audited or certified.
