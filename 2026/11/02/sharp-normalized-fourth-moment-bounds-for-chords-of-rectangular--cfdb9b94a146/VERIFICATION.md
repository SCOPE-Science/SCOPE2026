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

Run `python3 verify.py` in the same directory as the scientific proof. The script is self-contained and uses Python standard-library exact rational arithmetic and an explicit three-variable polynomial engine; no symbolic or numerical packages are needed.

Observed completed run:

`VERIFY_OK upper_monomials=15 lower_ordered_monomials=39 exact_face_pair_cases=5 seeded_pairs=240000`

The exact algebraic checks regenerate \(Q\) and \(W\) and verify the two stated homogeneous certificate identities and sign patterns. The upper difference has 15 positive monomials in positive box half-lengths. The lower difference has 39 positive monomials after imposing the permissible ordering, and its terms contain positive powers of the two shape gaps, proving strictness outside cubes.

Five exact rational dimension triples (including a cube and strongly anisotropic cases) were additionally checked by an **independently conditioned sum over 36 ordered face pairs**, using the second and fourth raw moments of fixed coordinates or uniform interval coordinates as applicable. These cases detect normalization and cross-coordinate mistakes but are not a proof for all dimensions. A seeded 240,000-pair numerical simulation across three dimension triples corroborates the formulas within stated tolerances and is also not an infinite proof.

The complete mathematical proof rests on the face-conditioning identities, symbolic polynomial equalities, coefficient positivity, and continuity/limit arguments in `RESULT.md`. These checks do not establish priority against inaccessible literature, nor do they constitute independent external validation or finite-sample inference guarantees.
