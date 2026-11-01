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

# Verification of the central-section polygon law

The self-contained script `verify_truncated_octahedron.py` runs under Python 3 using only the standard library. It constructs the 24 integer vertices, the 14 supporting hyperplanes, and the 36 edges by independently checking shared active facet normals. It confirms every edge has squared length two, every vertex has degree three, and the incidence table agrees with the five chamber representatives.

The script tests the exact pointwise threshold formula on 2,919 strictly ordered integer normal vectors and the complete signed-coordinate symmetry orbits of five representative vectors, then recomputes the spherical-triangle and quadrilateral formulas. In a fresh execution it reported `PASS 3911 checks` and numerical probabilities `0.498450689917704`, `0.316108855580191`, and `0.185440454502106` for sections with 6, 8, and 10 sides respectively.

Critical mathematical limits: the finite tests cannot establish the theorem for every real orientation; that step is supplied by the proof that the only sign-change walls are three linear planes and the five regions are connected. Floating-point spherical-area calculations are checks of, not proofs of, the analytic solid-angle identity. Normal directions on walls have Haar measure zero and are outside the pointwise assertion. Independent validation has not been performed.
