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

The theorem concerns complete rank-four first-order types of relational prime-order cyclic groups. `verify_rank4_cyclic.py` is a standalone Python 3.9+ standard-library checker. It computes orbit-normalized exact types at ranks zero through four; finite arithmetic covers every prime at most 193 (and separately 197 and 211). Its rational-form generator constructs 19 fourth-move candidate forms, 60 hyperplane normals, 46 special third-coordinate functions, and 93 exceptional normalized two-coordinate ratios, and factors their exact cross-determinants. The exceptional-prime set is all primes through 131 together with 157 and 191. These are precisely the primes requiring individual finite checks; none exceeds 191.

An orbit-free implementation, using every ordered tuple rather than scaling orbits, confirms the low-prime results for primes 2, 3, 5, 7, 11 and 13. The numerical boundary computation was carried out in bounded batches, and the rational arrangement and representative cases 137, 157, 191, 193 were replayed from the included verifier. The full one-command run may exceed restricted tool timeouts; it is intended to be run in an unrestricted local shell. Distinct type codes are mathematical distinguishing certificates through the recursive type theorem; the package does not explicitly print a first-order separating sentence for every pair.

The infinite result does not follow from sampling: for primes at least 193, the 93 normalized exceptional ratios remain distinct and each relevant generic extension exists. This gives a direct Duplicator strategy for four rounds. The novelty comparison is qualified because the conclusion conflicts with a published lower-bound claim whose argument reduces all winning strategies to a closed binder. Independent assessment of that conflict is outstanding.
