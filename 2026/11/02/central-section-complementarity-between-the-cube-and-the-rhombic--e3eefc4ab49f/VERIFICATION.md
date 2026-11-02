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

Run `python rd_cube_checker.py` with Python 3 and NumPy. The checker exhaustively enumerates all fourteen rhombic-dodecahedral vertices from intersections of twelve integer halfspace facets in exact rational arithmetic; it recovers exactly twenty-four edges, confirming the axial-to-cubic incidence description and independently constructs twelve cube edges. Signed permutations of both chamber representatives are checked exhaustively against direct endpoint-sign counts, establishing the pointwise complementarity in each open chamber. The exact spherical excess is verified algebraically up to floating-point evaluation, and 150000 independent seeded Gaussian directions provide a supplementary sampling diagnostic. The proof in RESULT.md supplies the universal geometric derivation; no finite test is used to certify all directions by itself.

No independent mathematical audit has been performed. The literature comparison confirms the cube marginal is classical; historical priority of the new pairing remains provisional.
