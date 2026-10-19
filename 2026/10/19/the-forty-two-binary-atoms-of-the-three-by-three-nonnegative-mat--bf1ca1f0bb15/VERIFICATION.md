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

# Finite verification and scope

`python3 verify.py` uses only the Python 3 standard library. Its assertions exhaustively form the 512 binary matrices, compute all 512 integer determinants, form all 36 row/column permutation actions, and calculate all \(506^2=256036\) ordered products of nonunit binary matrices. The program asserts exactly six units, 42 atoms in the two specified orbits, 464 binary composites, 338 singular matrices, 174 nonsingular matrices and eight nonsingular double orbits. It also checks that every singular binary matrix has a zero or repeated row or column.

The script raises an exception on any disagreement and otherwise emits `VERIFY_OK`. These are exhaustive **finite** checks, not tests of the infinite monoid. Lemma 1 of RESULT.md establishes that *every* nonnegative-integer factorization of a nonsingular binary target has binary factors; the zero-/duplicate-row or column construction gives factorizations for singular targets. Therefore the finite certificate and the algebraic lemmas jointly cover the full target claim.

Independent expert auditing and exhaustive literature certification have not been performed.
