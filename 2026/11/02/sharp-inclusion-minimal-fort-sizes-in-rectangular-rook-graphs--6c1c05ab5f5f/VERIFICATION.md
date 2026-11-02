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

Run `python3 verify.py`. It independently builds the original rook-graph adjacency, computes whether every unselected vertex has zero or at least two neighbors inside the candidate, and computes inclusion-minimality against *all* proper subsets via an exact subset dynamic program. The test cases are \((2,2)\), \((2,3)\), \((2,4)\), \((2,5)\), \((3,3)\), \((3,4)\), \((3,5)\), \((3,6)\), \((4,4)\), and \((4,5)\). Its finite exhaustive run visited 1,414,992 subset masks including the empty mask and confirmed the maximum sizes predicted by the theorem. The code depends only on the Python 3 standard library.

The theorem itself has an infinite proof via the incidence-graph criterion, cyclic versus acyclic upper bounds, a minimal two-arm cross construction, and a minimal simple-cycle construction for consecutive dimensions. The verifier provides a finite cross-check; it is not an independent mathematical audit of that infinite proof. It does not test nor claim the complete enumeration of minimal forts for untested dimensions.
