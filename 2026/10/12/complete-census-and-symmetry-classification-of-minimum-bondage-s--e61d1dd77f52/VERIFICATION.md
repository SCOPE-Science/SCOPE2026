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

# Reproducible verification

The proof is a complete **finite** exhaustive enumeration for one 24-vertex graph; it is not an inferred general infinite-family statement. The file `verify_bondage.cpp` implements direct domination checks using exact 24-bit neighborhood unions, tests all six- through eight-vertex possible small dominating sets, all four- and five-edge deletion subsets, all automorphisms, the star census, the eight orbits, and nine-vertex witnesses. Exact expected counts are displayed in `verification_output.txt`, which records an actual replay.

The independent `census.cpp` implements the different exact bundle-coverage criterion: a dominating set survives an edge deletion unless for some undominated vertex all its edges to the set are deleted. It reproduces all 276 winning five-edge subsets, written to `bondage_sets.txt`, using the same fixed graph but a distinct domination-survival algorithm. Both programs are standalone C++17 sources.

The original source (Srivastava, arXiv:2609.02477v1) already establishes that the graph has domination number eight and bondage number five; the independently checked refinement concerns the **full** 276-minimizer census, compulsory complete vertex star, and eight symmetry classes. Potential undiscovered equivalent enumerations remain a literature risk. This documentation reports self-review only, not external audit.
