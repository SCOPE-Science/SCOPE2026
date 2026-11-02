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

# Verification record

Run `python3 verify_wireframe.py` in the same folder as this document. The Python 3 program uses only the standard library. It enumerates all disjoint pairs from the complete 12-edge cube and octahedral one-skeleta, constructs the four exact segment-orientation polynomials for each pair, proves each nonzero determinant is linear in the two projection parameters, and checks every connected sign chamber via rational witnesses.

Observed output: cube chamber counts `[2,2,2,2,2,2]`; octahedron chamber counts `[2,2,2,6]`; symbolic nonzero determinant occurrences cube `168`, octahedron `120`. Cube boundaries: `s=1`, `t=1`, `s=t`; octahedron boundaries `s+t=1`, `s=t+1`, `t=s+1` in positive parameters. All assertions passed. The passage from finite chambers to all real parameter values uses the analytic fact that proper intersection predicates depend only on orientation determinant signs. A separate analytic affine-dependence proof handles the tetrahedron; exact spherical excess handles probabilities. No experimental finite sample is presented as an infinite proof.

Excluded directions and historical-priority access limits are stated in the result. Independent validation has not been performed.
