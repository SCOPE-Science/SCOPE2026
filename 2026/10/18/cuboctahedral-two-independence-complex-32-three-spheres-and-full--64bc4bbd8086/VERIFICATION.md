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
# Reproducibility and limits

Execute `python3 verify_cube_line_graph.py` and `python3 verify_coordinate_model.py` in a clean Python 3 environment. The scripts use only the Python standard library. Compare stdout byte-for-byte with `verification_output_cube.txt` and `verification_output_coordinates.txt`.

The first script exhausts every nonempty subset of twelve graph vertices, prints all face counts and matching stages, tests acyclicity of the full oriented face-poset graph, computes mod-two boundary ranks, enumerates 48 graph automorphisms, and calculates ten rational character traces via exact signed fixed-simplex sums. The second script independently constructs the Euclidean cuboctahedral graph and computes the component condition via breadth-first search; it checks the Euler characteristic, the identity and antipodal character values, and the full-group invariants.

The finite search is mathematically exhaustive because all \(2^{12}-1\) possible nonempty vertex subsets and all 48 signed coordinate permutations are explicitly traversed, without sampling or timeout. The integer homotopy statement additionally invokes the standard discrete Morse theorem: one zero-cell and 32 three-cells are the only critical cells. No calculation here determines a general family of larger line-graph cubes; no external independent audit has been performed.
