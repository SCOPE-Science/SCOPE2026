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

# Verification and limitations
The finite checker is `verify.py`; run `python verify.py` from the extracted package directory. It enumerates every simplex in the four-vertex vertex-witness Čech complexes for the maximum, taxicab, Euclidean and a cut-square norm. The observed face counts are \((4,0,0,0)\) below one, \((4,6,4,0)\) for each nonmaximum norm on the interval starting at one and ending at its diagonal norm, and \((4,6,4,1)\) after the diagonal threshold. The nontrivial middle-stage complex is therefore the tetrahedron boundary, an integral two-sphere.

The checker does not certify infinitely many norms or arbitrary finite metric spaces. Universal correctness rests on the written inequalities, exact face equivalence, and explicit strong deformation homotopy. The original content is the norm-rigidity boundary, not the previously established general categorical-product Künneth theorem. No independent audit has occurred.
