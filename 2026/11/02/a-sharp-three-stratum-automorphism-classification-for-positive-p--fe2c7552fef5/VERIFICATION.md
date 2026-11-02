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

The symbolic proof reduces the full automorphism group to the real special-orthogonal commutant of the explicitly displayed matrix H. Its determinant is nonzero for all strictly positive parameters. The symmetric/skew-axis argument establishes the full three-case classification for every allowed parameter; the diagonal symmetrizer and simple-spectrum discriminant are the critical nonstandard steps. The isomorphism between different fourth parameters is checked directly against all displayed products.

Run `python3 verify.py` with SymPy to replay ten exact-radical representative cases and 240 signed-orthogonal candidate tests. Observed result: `VERIFY_OK exact_parameter_cases= 10 signed_orthogonal_tests= 240`. These finite checks do not prove exhaustiveness for continuous rotations; that follows from the proof in RESULT.md. Independent verification has not been performed.
