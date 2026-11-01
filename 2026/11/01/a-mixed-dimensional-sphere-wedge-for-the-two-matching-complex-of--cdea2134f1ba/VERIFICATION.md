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

# Verification of the finite homotopy classification

Run `python3 verify.py` in the directory containing this file. No nonstandard libraries or external data files are required. The script deterministically examines every mask of twenty potential bipartite edges. Faces are row-major masks with every row and column containing at most two edges. It enumerates all nonempty faces and maximal faces.

It constructs a complete vertex-toggling discrete-Morse matching, verifies every pair, and checks global acyclicity of the entire oriented Hasse diagram by topological sorting. The resulting critical vector is one degree-zero cell, 42 degree-six cells, and three degree-seven cells. It computes the exact signed integer Morse attaching matrix using recursive gradient-path elimination; the full matrix has shape 42 by 3 and all entries are zero. The program also directly computes the original simplicial boundary ranks over the two-element field, independently of the Morse reduction.

Expected terminal output includes `FACES_OK`, `MATCHING_OK`, `ACYCLIC_OK`, `INTEGRAL_MORSE_OK`, `RAW_MOD2_OK`, `HOMOTOPY_OK` and finally `ALL_VERIFY_OK`. An assertion failure aborts verification; printed messages alone are not an independent scientific audit. The code exhausts the specific finite graph and does not establish any uniform formula or equivariant conclusion. The attachment-to-homotopy deduction uses the ordinary Hurewicz theorem for a 5-connected 6-skeleton.
