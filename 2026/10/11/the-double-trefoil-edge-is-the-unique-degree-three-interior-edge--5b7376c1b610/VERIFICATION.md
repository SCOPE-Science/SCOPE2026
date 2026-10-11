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
# Verification

Run `python3 verify.py` using a standard Python 3 interpreter. The script reconstructs the published sphere and ball from the compact Table 6 tetrahedron notation, checks the exact boundary triangle list, computes all edge incidences, and verifies the claimed unique degree-three interior edge and full degree histogram.

The computation is exhaustive over all edges of the fixed finite complex. It does not infer a universal theorem about other triangulations or other knotted spanning edges. The statement that degree three is the minimum possible for an interior edge uses the standard manifold-link fact that the link is a simplicial circle.
