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
# Finite proof verification

The included `verify_graph.py` computes all 65,536 four-mer subsets through exact integer masks and the eight-vertex three-mer overlap graph, using topological sorting and longest-path DP. It checks the optimality/count profile for all integer windows from 4 through 11, all six cyclic rotation classes, all 128 transversals, and the exact 98/10/4/16 transversal breakdown.

The included `verify_words.cpp` instead computes the four-mer presence set directly for every binary word of each length from 4 to 11 and tests each proposed hitting set against all those words. It asserts the same exact optimum/count table. Build/run with `c++ -O2 -std=c++17 verify_words.cpp -o verify_words && ./verify_words`; separately run `python3 verify_graph.py`. Both were executed successfully. The infinite range follows from the independently justified necklace obstruction and the heredity of hitting under extension.

The finite package supplies an exhaustive computational proof, not a formal theorem prover certificate. Originality beyond the named inspected articles is uncertain because a 2021 supplementary document and unindexed computations were not completely inspected.
