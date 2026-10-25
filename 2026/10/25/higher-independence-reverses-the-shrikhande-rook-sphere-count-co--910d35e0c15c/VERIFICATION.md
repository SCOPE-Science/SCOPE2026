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

# Reproducibility and evidence

Run `python3 verify_higher_independence.py` from a directory containing the two attached files `verify_higher_independence.py` and `verification_output.txt`. No external modules, downloads, or inputs are required. A standard Python 3.10+ interpreter is recommended because the program uses `int.bit_count`.

The script verifies every vertex subset of both 16-vertex graphs, both face predicates, strongly regular parameters, all four complete face vectors, maximal-face dimensions, a deterministic Morse matching with a common vertex-pivot order, all oriented codimension-one incidences, directed acyclicity by full topological sort, and the number and dimensions of the critical cells. It explicitly asserts all expected counts and ends with `VERIFY_OK` only if they hold. Its actual output, reproduced in `verification_output.txt`, reports **4,960** and **4,224** directed incidences for the two new degree-two complexes and respectively **57** and **105** critical three-cells after each single critical vertex.

The mathematical deduction from these checks uses the standard discrete-Morse CW theorem: one critical vertex and critical cells only in dimension three force a wedge of three-spheres. Unlike homology-only computations, no unresolved attaching map remains in this CW model. This finite certificate proves exactly the two displayed finite homotopy statements. It does not constitute an independent audit, a symbolic general-family proof, or an assertion of unique publication priority.
