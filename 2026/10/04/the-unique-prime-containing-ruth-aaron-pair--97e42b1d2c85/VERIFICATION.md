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

The unrestricted proof is symbolic and appears in `RESULT.md`.

The packaged checker performs two independent finite corroborations through \(2{,}000{,}000\):

1. for every composite \(m\) in the range, it computes \(S(m)\) from a smallest-prime-factor sieve and verifies that
   \[
   S(m)=m-1
   \]
   occurs exactly at \(m=6\);
2. for every consecutive pair \((n,n+1)\) in the range, it checks the Ruth–Aaron equality and records those for which at least one member is prime, verifying that only \((5,6)\) occurs.

These finite checks are not used to infer the infinite theorem. The proof instead uses complete additivity and the exact inequality
\[
(a-1)(b-1)\le2
\]
forced by a hypothetical composite solution of \(S(m)=m-1\).
