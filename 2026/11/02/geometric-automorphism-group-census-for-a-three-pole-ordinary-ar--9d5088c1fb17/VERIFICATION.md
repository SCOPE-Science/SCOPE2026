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

## Reproducible checks
Run `python3 verify.py` with the Python 3 standard library. The script computes complete permutation orbits on the two-dimensional nonzero coefficient torus for the first twenty-three primes \(p\ge5\), through \(p=97\). It asserts the three transposition fixed-set count, the three-cycle fixed sets, their intersection, the four orbit counts and the explicit formulas, and concludes with `VERIFY_OK`.

## Scope of verification
The finite checker verifies only finitely many primes. The proof of the result for every prime \(p\ge5\) rests on the rational-function identities, the Valentini--Madan uniqueness theorem, the elementary orbit and fixed-point count, and Schur--Zassenhaus. No computer program certifies the quoted external structural theorems. The arithmetic forms and their twists are outside the theorem.
