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

Compile `enumerate_candidate_graphs.cpp` with `g++ -std=c++17 -O3`. Run the binary with `(9,candidates9.txt,all_graphs9.txt)` and `(10,candidates10.txt,all_graphs10.txt)` positional arguments; both runs are exhaustively finite. Check the generated text against the included candidate and complete-census records. Install `requirements.txt` into a Python environment and execute `python verify_candidates.py` and `python check_census.py` in the directory containing all embedded files. Executed outputs, included as `verification_output_final.txt`, `census_output.txt`, `enumeration9.txt` and `enumeration10.txt`, provide numerical counts and a final PASS.

The C++ candidate filter discards a graph only when each stable cell is entirely composed of open twins within one bipartition side, which guarantees that cell is an automorphism orbit. The Python checker independently reconstructs the incidence graphs, computes refinement using counted neighbour colours, enumerates full automorphisms, and tests all the canonical candidates (including possible full side-swapping isomorphisms). Separately it exhaustively checks every connected row-mask representation through nine vertices, with no candidate prefilter. The census checker verifies side swapping in the balanced ten-vertex class and the two external counts 730 and 4032.

Finite enumeration establishes only a finite cutoff, not a claim about all graph orders. An independent scientific audit has not been performed.
