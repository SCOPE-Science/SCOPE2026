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

# Reproducible computation

The full state space contains exactly \(2^{20}=1{,}048{,}576\) binary assignments. `dodeca_majority.cpp` constructs the successor of every assignment, removes noncycle states by indegree peeling, then classifies cycles and their complete basins. The archived transition table `transition_u32le.bin` contains all 1,048,576 little-endian 32-bit successor words; its SHA-256 is `231454f9198ec28f2950bcf9004b75978c9275ac53635cbe93ba6a5fcc741fc6`.

`verify_dodeca.cpp` independently recomputes each successor by three Boolean majority terms and compares every record in the archive, then performs direct trajectory tests on every starting state. It verifies the 16 exact entrance-time/attractor cells. The output file `verify_dodeca_output.txt` records the successful whole-space checks. `verify_automorphism_group.cpp` independently enumerates all graph automorphisms using full adjacency-preservation backtracking and confirms that all 120 appear in `automorphisms.csv`. `symmetry_classes.cpp` enumerates the orbits of recurrent temporal cycles under these exact permutations, and its class-size frequencies sum to all 118 fixed points and 9,679 primitive two-cycles. `verify_matching_cuts.cpp` checks the fixed-state characterization for each configuration. `verify_graph_identity.cpp` checks the vertex bijection from `gp10_2_isomorphism.tsv` against the complete GP(10,2) edge list.

All five sources are independently compilable with a C++17 compiler. Run them from the directory containing the extracted files using the commands provided in `RESULT.md`. Outputs corresponding to each checker are embedded. The C++ source, actual certificate, and exact enumeration provide a finite proof, but no formal theorem is claimed for larger graphs. This is a self-review, not an independent third-party audit.
