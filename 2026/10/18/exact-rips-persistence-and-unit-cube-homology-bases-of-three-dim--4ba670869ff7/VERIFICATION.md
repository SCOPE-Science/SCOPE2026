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
# Reproducibility and checks

Run `python3 VERIFY.py` from the directory containing both `VERIFY.py` and `VERIFY_OUTPUT.txt`. The script uses only the Python standard library, reports local signed-span contributions, checks 27 width vectors and 117 anchored simplices, checks distinct unit-cube retraction behavior, and computes all mod-two simplicial boundary ranks for eight finite boxes, including a 64-vertex box. The expected exact output is `VERIFY_OUTPUT.txt`.

The output concludes with `ALL_FINITE_CHECKS_PASSED`. Its eight box cases have reduced mod-two third Betti numbers respectively 0, 0, 1, 3, 6, 8, 18, 27, agreeing with the three-dimensional unit-cube counts.

The proof of the infinite family does not depend on extrapolation from the finite cases. It relies on the published equal-cube sphere-wedge and contractibility results, a uniformly defined simplicial coordinate-clamping retraction, a complete sign-reversing involution for all width-two simplices, an exact local Euler calculation, and integral retractions producing a splitting map for unit-cube homology classes. The claims are scoped to the integer Manhattan metric and inclusive integer threshold transitions.

Independent audit has not been performed.
