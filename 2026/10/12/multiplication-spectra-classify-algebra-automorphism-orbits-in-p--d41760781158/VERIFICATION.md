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

The proof is symbolic and valid for every prime \(\ell\) and prime power \(q\) with \(\ell\nmid q\). The accompanying `verify.py` is a bounded independent stress check of the finite cases below; it is not used to infer the universal theorem.

It explicitly constructs binary extension fields and the full product of Frobenius actions with coordinate permutations for
\[
(\ell,q,f,m)=(3,2,2,1),\ (5,2,4,1),\ (7,2,3,2).
\]
For every element in those cases it computes the factorization signature of the multiplication characteristic polynomial and checks that the signature is constant on each algebra-automorphism orbit and distinct for distinct orbits. It also checks both element-orbit and unit-orbit formulas. The split case \((\ell,q)=(2,3)\) is exhaustively checked under the full coordinate-permutation action.

A fresh replay of the packaged checker produced:

`non_split l=3 q=2 f=2 m=1 H=3 orbits=6 unit_orbits=2`

`non_split l=5 q=2 f=4 m=1 H=6 orbits=12 unit_orbits=5`

`non_split l=7 q=2 f=3 m=2 H=4 orbits=20 unit_orbits=6`

`split l=2 q=3 orbits=6 unit_orbits=3`

`VERIFY_OK`

Unproved by computation: no finite replay establishes the all-parameter statement. The universal step is instead the exact factorization and automorphism-group argument in `RESULT.md`.
