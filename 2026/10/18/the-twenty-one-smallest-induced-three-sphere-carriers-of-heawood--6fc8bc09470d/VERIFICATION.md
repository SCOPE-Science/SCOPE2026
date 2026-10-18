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

# Reproducibility
Run `python3 verify.py` in the directory containing this file. The program uses only the Python 3 standard library, contains all input incidence data as a seven-point binary inner-product rule, and independently rebuilds every simplex and boundary; it needs no external files.

The program verifies the complete degree-three induced homology census on all 2002 nine-vertex and 1001 ten-vertex supports; the geometric complement classification of all 21 hits; the finite acyclic Morse matched Hasse digraph for every hit and for the ambient complex; 21 actual mod-two kernel cycles not contained in the ambient four-boundaries; and six-dimensional quotient generation by the 21 cycles.

Expected final line:

`VERIFY_OK 2002_NINE_ZERO 21_TEN_SPHERES 21_NONZERO_MAPS SPAN_6`

The exact finite computation proves statements only about these finite simplicial complexes. The integral homotopy inference uses the standard acyclic discrete-Morse matching theorem. The conversion between mod-two bounds and rational inclusion maps uses free homology in degree three for the sphere sources and their ambient wedge. No independent scientific assessment is claimed.
