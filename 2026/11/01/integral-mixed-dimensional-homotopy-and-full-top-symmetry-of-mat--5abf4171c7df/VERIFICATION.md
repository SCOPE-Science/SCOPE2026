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

# Exact reproduction
Run `python3 verify.py` in the directory containing the embedded verification source. It uses only standard Python 3 modules and performs deterministic integer operations. Compare its exact stdout to `verification_output.txt`.

The verifier exhaustively constructs all 18,494 nonempty simplices by taking all nonempty subsets of every open neighborhood. It constructs 9,120 matched pairs, orients the full Hasse diagram (98,805 incidences) and topologically sorts it to certify acyclicity; no sample or randomized graph test substitutes for this check. The critical-cell counts are 1 in dimension zero, 246 in dimension three and 7 in dimension four.

The only possible nonzero Morse differential is checked over the integers, with all 1,722 entries exactly zero. Seven integral simplicial four-cycles are constructed and independently checked by their full oriented boundaries. The integral module calculation projects the cycles through unit-pivot elimination, forms a unimodular signed-permutation basis, verifies six adjacent transposition matrices on all seven basis vectors, and computes the traces for all 15 conjugacy classes.

The wedge-of-spheres proof additionally uses the standard simplicial discrete-Morse theorem and the elementary fact that the Hurewicz map from the third homotopy group of a wedge of 3-spheres to its third homology is an isomorphism. This finite computation does not address the integral symmetry structure of degree-three homology, nor does it exhaustively search all mathematical literature.
