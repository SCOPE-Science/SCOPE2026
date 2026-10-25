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
# Reproducibility and scope of checks

Run `python3 verify.py` in the directory containing the bundled verifier. Only Python's standard library is required. Compare its output with `verify_output.txt`.

The checker constructs an explicit undirected simple graph for each ordered tuple of two through four cycle lengths in the range 3–7 whose total edge count is at most 15. For each graph it enumerates all edge subsets, tests the definition of a perfect edge dominating set edge-by-edge, records the number of selected spokes, and separately identifies dominating induced matchings by pairwise edge nonincidence.

The predicted bivariate coefficient table is independently obtained from the binomial closed form, not from the graph enumeration. The checker tests both the exact polynomial and the modular DIM formula. The recorded verification covered 132 graph tuples with 1,679 PED sets and 30 DIMs; the largest tested graph has 15 edges. These tests verify finite cases only. They do not establish the general formula or novelty. All universal assertions instead depend on the explicit proof in `RESULT.md`.

The comparison with the 2026 generalized-series-parallel counting algorithm is a bibliographic assessment, not a machine-certified originality result. Independent audit and external validation are not performed.
