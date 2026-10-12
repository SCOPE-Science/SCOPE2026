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

# Reproducibility and verification

Run `python3 verify.py` with a Python interpreter supporting `int.bit_count`. No third-party dependencies are required.

The verifier builds the Fano point-line graph and Boolean rank-two/rank-three inclusion graph directly, confirms expected vertex/edge counts and regularity, constructs edge compatibility by testing all pairs of edges, runs an exhaustive pivoted maximal-clique enumerator, and independently counts cliques of the established optimum sizes by non-pivot recursion. It validates each enumerated optimum's induced star profile and verifies the full optimum family is one orbit under explicit finite graph automorphisms.

`verification_output.txt` is a complete captured successful execution of exactly the included `verify.py`. In the Heawood graph the maximum is 6 with 14 packings, all profile (2,2,2); in the Desargues graph the maximum is 9 with 20 packings, all profile (2,2,2,3). The captured run reports 336 and 240 automorphisms respectively and ends in `ALL_CHECKS_PASSED`.

The finite calculations check only these two named graphs. They cannot establish novelty, characterize other graphs, or replace the structural upper-bound and classification proof supplied in `RESULT.md`. Independent audit has not been performed.
