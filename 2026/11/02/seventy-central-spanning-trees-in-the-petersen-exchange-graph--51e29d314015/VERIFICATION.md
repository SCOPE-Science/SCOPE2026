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
# Exact finite checks

Run `python verify_direct.py` and `python verify_contraction.py` with standard Python 3. The first directly constructs the Petersen graph as a disjointness graph on pairs, lists all 2000 spanning trees, calculates their 1,999,000 pairwise distances, and classifies their complements and all length-5 and length-6 cycles. The second independently sums the squared number of tree extensions of every possible forest, using exact integer reduced-Laplacian determinants after contraction; binomial inversion recovers the same distance histogram. The checks were executed successfully against these exact delivered source files. Their conclusions are finite and exhaustive, not probabilistic; independent expert review has not been performed.
