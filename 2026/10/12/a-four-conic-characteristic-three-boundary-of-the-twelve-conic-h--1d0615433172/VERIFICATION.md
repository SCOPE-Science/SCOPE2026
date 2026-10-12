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
# Verification notes

Execute `python verify.py` with Python 3.11+ and SymPy 1.13+. The program checks all twelve original quadrics by coefficient reduction in the polynomial ring of characteristic three, confirms the determinant identities, verifies the six displayed points and pairwise component memberships, the coordinate-permutation action and the local uniformizer restrictions. It independently enumerates every rational projective point over the fields of orders three and nine and every admissible parameter to confirm the six-point incidence census. The universal conclusion relies on exact polynomial identities and Bézout's theorem, not finite sampling. The conics in the original twelve-factor product coalesce, so conclusions about the reduced support do not describe the embedded structure of the nonreduced original.
