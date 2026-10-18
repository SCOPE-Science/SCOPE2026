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

# Reproducible checks and limits

Run `python3 verify.py` in a directory containing the attached `verify.py`. The script uses only the Python standard library and defines the clique–path adjacency exactly. It enumerates all selected separated-gap, row-labeled square-pair cycles, checks their sixteen signed tetrahedra belong to the dual complex, checks zero simplicial boundary, verifies distinguished tetrahedra are maximal, and checks the complete signed evaluation is unimodular diagonal. It independently enumerates all faces of the robust-clique dual for six small graphs and obtains complete third-homology dimensions over the field of two elements.

The actual successful execution output is supplied in `verification_output.txt`; in particular, all seven structural samples passed. The proof of the unrestricted integer-parameter theorem is symbolic (RESULT.md); finite checks alone do not prove it. Results about the uncomputed full homology, torsion outside the guaranteed summand and complete wedge homotopy are explicitly **not** certified. An independent mathematical audit has not been performed.
