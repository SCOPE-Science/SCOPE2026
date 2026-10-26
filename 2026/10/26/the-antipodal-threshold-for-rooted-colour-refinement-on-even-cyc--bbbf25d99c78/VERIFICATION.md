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

# Reproducibility of the even-cycle refinement theorem

The standard-library Python file `verify_even_cycles.py` builds Cartesian-cycle graph adjacency lists independently of its weighted histogram quotient. It compares each actual synchronous colour-refinement partition with the claimed roundwise profile, tests the hypercube boundary, and checks predecessor-multiset injectivity by direct finite enumeration. Execute `python verify_even_cycles.py`; its recorded output is in `verification_output.txt`.

Completed checks: 21 direct full-graph parameter configurations, 43 separate weighted-quotient configurations, 58 predecessor-injectivity configurations. All completed tests passed. The program tests only finite parameter ranges; the all-parameter theorem rests on the written induction, triangular reconstruction, and exceptional-case argument, not on exhaustive finite computation.

No independent mathematical audit has been performed. Equivalent results in specialized or unindexed literature remain a possible originality limitation.
