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

The universal statement is proved by Segre factorization, uniqueness of rank-one tensors and the automorphism classification of the smooth split quadric. The rank-one condition is equivalent to tangency of each coordinate plane. The proof shows exhaustiveness, disjointness and freeness of the two reciprocal-diagonal torus orbits without depending on a finite experiment.

The standalone standard-library-only `verify.py` and its actual output `verification_output.txt` check one exact integer-coefficient witness: the Segre coordinate-change determinant is \(1\), each coordinate bilinear form has rank one, the dual quadratic matrix has zero diagonal and nonzero determinant, and the equation vanishes by an explicit inverse linear transformation. Running `python3 verify.py` prints `VERIFY_OK`. Finite sample checks do not establish the universal claim, and no claim about the scheme structure of the incidence fiber or real-field descent is made.
